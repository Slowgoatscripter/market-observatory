"""Keyless public crypto collector (observation only; it never places orders).

All decimal observations are stored as integers.  Prices and asset quantities
use six decimal places, probabilities use one millionths, and funding rates
use twelve decimal places.  The deliberately short column names keep the
append-only gzip archive comfortably inside the repository budget.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from collections.abc import Callable, Iterable, Mapping, Sequence
import csv
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
import gzip
import io
import json
import math
import os
from pathlib import Path
import tempfile
import time
from typing import Any
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from observatory.kalshi.client import KalshiClient


UTC = timezone.utc
PRICE_SCALE = 1_000_000
RATE_SCALE = 1_000_000_000_000
TIME_SCALE = 1_000
NOTIONALS = (Decimal("100"), Decimal("1000"))
WARNING_BYTES = 250_000_000
MAX_ANNUAL_BYTES = 300_000_000
KALSHI_MARGIN_BASE_URL = "https://external-api.kalshi.com/trade-api/v2/margin"
COINBASE_BASE_URL = "https://api.exchange.coinbase.com"
KRAKEN_BASE_URL = "https://api.kraken.com/0/public"
BRACKET_SERIES = ("KXBTC", "KXBTCD", "KXETH", "KXETHD")
# Open-bracket snapshots are the bulk of the data (about 1,200 strikes per sample,
# most of them far out with no bid): every 15 minutes came to ~365 MB a year on
# its own (live pilot, 2026-09-29). Every 30 minutes keeps the total near budget;
# settlement capture still runs every sample.
BRACKET_INTERVAL_MS = 30 * 60 * 1000
BRACKET_SLACK_MS = 5 * 60 * 1000  # sample timing jitters; don't skip a due snapshot


def _decimal(value: Any) -> Decimal | None:
    if value is None or value == "":
        return None
    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError):
        return None


def _scaled(value: Any, scale: int = PRICE_SCALE) -> int | None:
    number = _decimal(value)
    if number is None:
        return None
    return int((number * scale).to_integral_value(rounding=ROUND_HALF_UP))


def _milliseconds(value: Any) -> int | None:
    if value is None or value == "":
        return None
    if isinstance(value, (int, float, Decimal)):
        number = Decimal(str(value))
        return int(number if abs(number) >= 10_000_000_000 else number * 1000)
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=UTC)
    return int(parsed.timestamp() * 1000)


def _first(mapping: Mapping[str, Any], *names: str) -> Any:
    for name in names:
        if mapping.get(name) is not None:
            return mapping[name]
    return None


def _base(source: str, collected_at_ms: int, *, rt: str) -> dict[str, Any]:
    return {"s": source, "t": int(collected_at_ms), "rt": rt}


def _compact(row: Mapping[str, Any]) -> dict[str, str | int | None]:
    return {str(k): v for k, v in row.items() if v is not None and v != ""}


def _records(source: str, payload: Any) -> list[Any]:
    if isinstance(payload, list):
        return payload
    if not isinstance(payload, Mapping):
        return [payload]
    for key in ("events", "markets", "funding_rates", "candlesticks", "trades"):
        if isinstance(payload.get(key), list):
            return list(payload[key])
    return [payload]


def parse_fixture(source: str, payload: Any, *, collected_at_ms: int) -> list[dict[str, Any]]:
    """Normalize every captured response shape to compact integer rows."""
    records = _records(source, payload)
    result: list[dict[str, Any]] = []
    for item in records:
        record = item if isinstance(item, Mapping) else {"v": item}
        row = _parse_record(source, record, payload, collected_at_ms)
        result.append(_compact(row))
    return result


def _parse_record(source: str, r: Mapping[str, Any], payload: Any, t: int) -> dict[str, Any]:
    if "bracket_events" in source or source.endswith("_events"):
        meta = r.get("product_metadata") or {}
        return {**_base(source, t, rt="be"), "et": r.get("event_ticker"),
                "st": r.get("series_ticker"), "sd": _milliseconds(r.get("strike_date")),
                "mx": int(bool(r.get("mutually_exclusive"))), "ca": str(meta.get("cadence", ""))}
    if "bracket_markets" in source or source.endswith("_markets") and "perps" not in source:
        return {**_base(source, t, rt="bm"), "tk": r.get("ticker"), "et": r.get("event_ticker"),
                "yb": _scaled(_first(r, "yes_bid_dollars", "yes_bid")),
                "ya": _scaled(_first(r, "yes_ask_dollars", "yes_ask")),
                "lp": _scaled(_first(r, "last_price_dollars", "last_price")),
                "fl": _scaled(r.get("floor_strike")), "cp": _scaled(r.get("cap_strike")),
                "ct": _milliseconds(r.get("close_time")), "rs": r.get("result"),
                "ty": r.get("strike_type")}
    if "funding_estimate" in source:
        return {**_base(source, t, rt="fe"), "tk": r.get("market_ticker"),
                "fr": _scaled(r.get("funding_rate"), RATE_SCALE), "mp": _scaled(r.get("mark_price")),
                "ft": _milliseconds(r.get("next_funding_time")), "kt": _milliseconds(r.get("computed_time"))}
    if "funding_historical" in source:
        return {**_base(source, t, rt="fs"), "tk": r.get("market_ticker"),
                "fr": _scaled(r.get("funding_rate"), RATE_SCALE), "mp": _scaled(r.get("mark_price")),
                "ft": _milliseconds(r.get("funding_time"))}
    if "perps_candles" in source:
        price = r.get("price") or {}
        return {**_base(source, t, rt="pc"), "tk": (payload.get("ticker") if isinstance(payload, Mapping) else None),
                "ep": _milliseconds(r.get("end_period_ts")), "op": _scaled(price.get("open")),
                "hi": _scaled(price.get("high")), "lo": _scaled(price.get("low")),
                "cl": _scaled(price.get("close")), "oi": _scaled(r.get("open_interest")),
                "vo": _scaled(r.get("volume"))}
    if "perps_trades" in source:
        return {**_base(source, t, rt="pt"), "tk": r.get("ticker"), "id": r.get("trade_id"),
                "pr": _scaled(r.get("price")), "qt": _scaled(r.get("count")),
                "ct": _milliseconds(r.get("created_time")), "sd": r.get("taker_side")}
    if "perps_orderbook" in source:
        book = r.get("orderbook", r)
        bids = _levels(book.get("bids", []), reverse=True)
        asks = _levels(book.get("asks", []), reverse=False)
        row = _book_row(source, t, book, rt="po")
        row.update(bq=_scaled(bids[0][1]) if bids else None,
                   aq=_scaled(asks[0][1]) if asks else None, nl=len(bids) + len(asks))
        return row
    if "perps_market" in source:
        m = r.get("market", r)
        return _perp_row(source, t, m)
    if "coinbase_candles" in source:
        values = list(r.get("v", [])) if isinstance(r.get("v"), list) else []
        return {**_base(source, t, rt="cc"), "ep": _milliseconds(values[0] if values else None),
                "lo": _scaled(values[1] if len(values) > 1 else None), "hi": _scaled(values[2] if len(values) > 2 else None),
                "op": _scaled(values[3] if len(values) > 3 else None), "cl": _scaled(values[4] if len(values) > 4 else None),
                "vo": _scaled(values[5] if len(values) > 5 else None)}
    if "coinbase_ticker" in source:
        return {**_base(source, t, rt="st"), "id": r.get("trade_id"), "bb": _scaled(r.get("bid")),
                "aa": _scaled(r.get("ask")), "lp": _scaled(r.get("price")), "qt": _scaled(r.get("size")),
                "et": _milliseconds(r.get("time"))}
    if "coinbase_book" in source:
        return _book_row(source, t, r, rt="sb")
    if "kraken_ticker" in source:
        pair, quote = _kraken_result(r)
        return {**_base(source, t, rt="st"), "pa": pair,
                "aa": _scaled(_array_value(quote.get("a"), 0)), "bb": _scaled(_array_value(quote.get("b"), 0)),
                "lp": _scaled(_array_value(quote.get("c"), 0))}
    if "kraken_depth" in source:
        pair, book = _kraken_result(r)
        return {**_book_row(source, t, book, rt="sb"), "pa": pair}
    # A lossless-enough fallback for future additive fields: preserve identities
    # plus the first numeric observation without ever emitting decimal strings.
    row = _base(source, t, rt="uk")
    aliases = {"ticker": "tk", "event_ticker": "et", "market_ticker": "mt", "trade_id": "id"}
    for key, alias in aliases.items():
        if key in r:
            row[alias] = str(r[key])
    for value in r.values():
        if isinstance(value, (int, float, Decimal)) and not isinstance(value, bool):
            row["v"] = _scaled(value)
            break
    return row


def _perp_row(source: str, t: int, m: Mapping[str, Any]) -> dict[str, Any]:
    reference = m.get("reference_price") or {}
    mark = m.get("settlement_mark_price") or m.get("liquidation_mark_price") or {}
    return {**_base(source, t, rt="kp"), "tk": m.get("ticker"), "as": _underlying(m),
            "bb": _scaled(m.get("bid")), "aa": _scaled(m.get("ask")), "lp": _scaled(m.get("price")),
            "mp": _scaled(mark.get("price")), "rp": _scaled(reference.get("price")),
            "oi": _scaled(m.get("open_interest")), "cs": _scaled(m.get("contract_size"))}


def _levels(values: Iterable[Any], *, reverse: bool) -> list[tuple[Decimal, Decimal]]:
    result = []
    for value in values:
        if not isinstance(value, Sequence) or isinstance(value, (str, bytes)) or len(value) < 2:
            continue
        price, quantity = _decimal(value[0]), _decimal(value[1])
        if price is not None and quantity is not None and price > 0 and quantity > 0:
            result.append((price, quantity))
    return sorted(result, key=lambda item: item[0], reverse=reverse)


def _array_value(value: Any, index: int) -> Any:
    return value[index] if isinstance(value, list) and len(value) > index else None


def _kraken_result(payload: Mapping[str, Any]) -> tuple[str | None, Mapping[str, Any]]:
    result = payload.get("result")
    if not isinstance(result, Mapping) or not result:
        return None, {}
    pair = next(iter(result))
    value = result[pair]
    return str(pair), value if isinstance(value, Mapping) else {}


def executable_bid_ask(
    bids: Iterable[tuple[Decimal, Decimal]], asks: Iterable[tuple[Decimal, Decimal]],
    *, notionals: Iterable[Decimal] = NOTIONALS,
) -> dict[Decimal, dict[str, Decimal]]:
    """VWAP obtained by selling into bids and buying from asks by USD notional."""
    bid_levels = sorted(bids, key=lambda level: level[0], reverse=True)
    ask_levels = sorted(asks, key=lambda level: level[0])
    return {n: {"bid": _sweep(bid_levels, n), "ask": _sweep(ask_levels, n)} for n in notionals}


def _sweep(levels: Iterable[tuple[Decimal, Decimal]], notional: Decimal) -> Decimal:
    remaining, base = Decimal(notional), Decimal(0)
    for price, available in levels:
        taken = min(remaining, price * available)
        base += taken / price
        remaining -= taken
        if remaining == 0:
            return Decimal(notional) / base
    raise ValueError(f"insufficient book depth for ${notional}")


def _book_row(source: str, t: int, book: Mapping[str, Any], *, rt: str, asset: str | None = None) -> dict[str, Any]:
    bids, asks = _levels(book.get("bids", []), reverse=True), _levels(book.get("asks", []), reverse=False)
    row: dict[str, Any] = {**_base(source, t, rt=rt), "as": asset,
                           "bb": _scaled(bids[0][0]) if bids else None, "aa": _scaled(asks[0][0]) if asks else None}
    for notional, suffix in ((Decimal("100"), "1"), (Decimal("1000"), "2")):
        try:
            prices = executable_bid_ask(bids, asks, notionals=(notional,))[notional]
        except ValueError:
            continue
        row[f"b{suffix}"] = _scaled(prices["bid"])
        row[f"a{suffix}"] = _scaled(prices["ask"])
    return row


def _underlying(market: Mapping[str, Any]) -> str:
    title = str(market.get("title") or "").strip().upper()
    if title:
        token = title.split()[-1]
        if token.isalnum():
            return token
    ticker = str(market.get("ticker") or "").upper()
    return ticker.removeprefix("KX").removesuffix("PERP")


class PublicJSONClient:
    """Minimal rate-limited GET-only JSON client for public venue endpoints."""
    def __init__(self, base_url: str, *, requests_per_second: float = 10, timeout: float = 30,
                 sleeper: Callable[[float], None] = time.sleep, clock: Callable[[], float] = time.monotonic) -> None:
        self.base_url, self.interval, self.timeout = base_url.rstrip("/"), 1 / requests_per_second, timeout
        self.sleeper, self.clock, self.last = sleeper, clock, None

    def get(self, path: str, *, params: Mapping[str, Any] | None = None) -> Any:
        now = self.clock()
        if self.last is not None and now - self.last < self.interval:
            self.sleeper(self.interval - (now - self.last))
        self.last = self.clock()
        query = urlencode({k: v for k, v in (params or {}).items() if v is not None})
        url = f"{self.base_url}/{path.lstrip('/')}" + (f"?{query}" if query else "")
        request = Request(url, method="GET", headers={"Accept": "application/json", "User-Agent": "market-observatory/phase-2"})
        with urlopen(request, timeout=self.timeout) as response:  # noqa: S310 - fixed venue bases
            return json.loads(response.read().decode("utf-8"))


class FundingEventState:
    """Small durable set used to archive each settled funding event once."""
    def __init__(self, path: str | Path, *, shared: dict[str, Any] | None = None) -> None:
        self.path = Path(path)
        self.shared = shared
        try:
            raw = shared if shared is not None else json.loads(self.path.read_text(encoding="utf-8"))
            if isinstance(raw, list):
                values = raw
            else:
                values = raw.get("funding_events", raw.get("claimed", []))
            self.claimed = set(values)
        except (FileNotFoundError, json.JSONDecodeError):
            self.claimed: set[str] = set()

    def claim(self, event_id: str) -> bool:
        if event_id in self.claimed:
            return False
        self.claimed.add(event_id)
        if self.shared is None:
            _atomic_json(self.path, {"funding_events": sorted(self.claimed)})
        else:
            self.shared["funding_events"] = sorted(self.claimed)
            _atomic_json(self.path, self.shared)
        return True


def _atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(value, handle, separators=(",", ":"), sort_keys=True)
            handle.flush(); os.fsync(handle.fileno())
        os.replace(name, path)
    finally:
        try: os.unlink(name)
        except FileNotFoundError: pass


def write_hourly_chunk(root: str | Path, *, source: str, hour: datetime,
                       rows: Iterable[Mapping[str, Any]]) -> Path:
    """Atomically publish an immutable source/hour CSV.GZ chunk."""
    hour = hour.astimezone(UTC).replace(minute=0, second=0, microsecond=0)
    safe_source = "".join(c if c.isalnum() or c in "-_" else "_" for c in source)
    directory = Path(root) / safe_source / hour.strftime("%Y/%m/%d")
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{hour:%Y%m%dT%H}0000Z.csv.gz"
    values = [dict(row) for row in rows]
    if not values:
        raise ValueError("a chunk must contain at least one row")
    columns = sorted({key for row in values for key in row}, key=lambda key: (key not in ("s", "t", "rt"), key))
    if any(not 1 <= len(column) <= 4 for column in columns):
        raise ValueError("chunk columns must be compact (one to four characters)")
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=directory)
    os.close(fd)
    try:
        with open(temporary, "wb") as raw:
            with gzip.GzipFile(fileobj=raw, mode="wb", compresslevel=9, mtime=0) as compressed:
                with io.TextIOWrapper(compressed, encoding="utf-8", newline="") as handle:
                    writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
                    writer.writeheader(); writer.writerows(values)
        try:
            os.link(temporary, path)
        except FileExistsError:
            raise FileExistsError(f"immutable chunk already exists: {path}") from None
    finally:
        try: os.unlink(temporary)
        except FileNotFoundError: pass
    return path


def estimate_annual_bytes(chunks: Iterable[str | Path], *, pilot_hours: float) -> int:
    if pilot_hours <= 0: raise ValueError("pilot_hours must be positive")
    return math.ceil(sum(Path(path).stat().st_size for path in chunks) * 24 * 365 / pilot_hours)


def needs_storage_warning(annual_bytes: int) -> bool:
    return int(annual_bytes) > WARNING_BYTES


def load_chunk(path: str | Path) -> list[dict[str, str]]:
    with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


class HourlyChunkStore:
    def __init__(self, root: str | Path) -> None:
        self.root = Path(root); self.pending: dict[tuple[str, datetime], list[dict[str, Any]]] = defaultdict(list)

    def add(self, source: str, rows: Iterable[Mapping[str, Any]], sampled_at: datetime) -> bool:
        hour = sampled_at.astimezone(UTC).replace(minute=0, second=0, microsecond=0)
        safe_source = "".join(c if c.isalnum() or c in "-_" else "_" for c in source)
        existing = self.root / safe_source / hour.strftime("%Y/%m/%d") / f"{hour:%Y%m%dT%H}0000Z.csv.gz"
        if existing.exists():
            # A restarted/queued job can begin in the tail of an hour already
            # finalized by its predecessor.  Immutability wins: resume cleanly
            # at the next hour instead of overwriting or creating duplicates.
            return False
        self.pending[(source, hour)].extend(dict(row) for row in rows)
        return True

    def flush(self, *, before: datetime | None = None) -> list[Path]:
        keys = sorted(self.pending, key=lambda item: (item[1], item[0]))
        if before is not None:
            cutoff = before.astimezone(UTC).replace(minute=0, second=0, microsecond=0)
            keys = [key for key in keys if key[1] < cutoff]
        written = []
        for key in keys:
            source, hour = key
            try:
                written.append(write_hourly_chunk(self.root, source=source, hour=hour, rows=self.pending[key]))
            except FileExistsError:
                # Safe recovery if another process atomically won publication.
                pass
            del self.pending[key]
        return written


def select_bracket_events(events: Iterable[Mapping[str, Any]], *, now: datetime) -> list[dict[str, Any]]:
    """Nearest still-open event, plus the next distinct daily-close event."""
    now_ms = int(now.astimezone(UTC).timestamp() * 1000)
    future = [dict(event) for event in events if (_milliseconds(event.get("strike_date")) or 0) >= now_ms]
    future.sort(key=lambda event: _milliseconds(event.get("strike_date")) or 2**63)
    if not future: return []
    chosen = [future[0]]
    next_daily = next((event for event in future[1:] if (event.get("product_metadata") or {}).get("cadence") == "daily"), None)
    if next_daily is not None: chosen.append(next_daily)
    return chosen


class CryptoCollector:
    """Coordinate public venue reads and produce source-grouped normalized rows."""
    def __init__(self, data_dir: str | Path = "data/crypto", *, kalshi: Any | None = None,
                 kalshi_core: Any | None = None, coinbase: Any | None = None,
                 kraken: Any | None = None, enable_hyperliquid: bool = False) -> None:
        if enable_hyperliquid:
            raise NotImplementedError("Hyperliquid is policy-optional and intentionally disabled by default")
        self.data_dir = Path(data_dir)
        injected_kalshi = kalshi
        self.kalshi = injected_kalshi or KalshiClient(base_url=KALSHI_MARGIN_BASE_URL)
        # Brackets live on the regular Trade API, not under /margin.  Reuse an
        # injected fake for deterministic tests unless a separate fake is given.
        self.kalshi_core = kalshi_core or (injected_kalshi if injected_kalshi is not None else KalshiClient())
        self.coinbase = coinbase or PublicJSONClient(COINBASE_BASE_URL, requests_per_second=10)
        self.kraken = kraken or PublicJSONClient(KRAKEN_BASE_URL, requests_per_second=5)
        self.state_path = self.data_dir / "crypto-state.json"
        try: self.state = json.loads(self.state_path.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError): self.state = {"pairs": {}, "pending_events": {}, "metrics": {}}
        self.funding = FundingEventState(self.state_path, shared=self.state)

    def sample(self, *, now: datetime | None = None) -> dict[str, list[dict[str, Any]]]:
        now = (now or datetime.now(UTC)).astimezone(UTC); t = int(now.timestamp() * 1000)
        output: dict[str, list[dict[str, Any]]] = defaultdict(list)
        markets_payload = self.kalshi.get("/markets", params={"status": "active"})
        markets = list(markets_payload.get("markets", []))
        for market in markets:
            ticker, asset = str(market["ticker"]), _underlying(market)
            detail = self.kalshi.get(f"/markets/{ticker}")
            detail_rows = parse_fixture("kalshi_perps_market", detail, collected_at_ms=t)
            for row in detail_rows: row["s"] = "kalshi"
            output["kalshi_perps"].extend(detail_rows)
            book = self.kalshi.get(f"/markets/{ticker}/orderbook", params={"depth": 20})
            contract_size = _decimal(market.get("contract_size")) or Decimal(1)
            nested_book = book.get("orderbook", book)
            book_row = _book_row("kalshi", t, nested_book, rt="po", asset=asset)
            # Kalshi quotes dollars per contract.  Store executable and top
            # prices in underlying USD so they align directly with spot; retain
            # contract size to make the conversion auditable.
            for key in ("bb", "aa", "b1", "a1", "b2", "a2"):
                if book_row.get(key) is not None:
                    book_row[key] = int((Decimal(book_row[key]) / contract_size).to_integral_value(rounding=ROUND_HALF_UP))
            levels = nested_book if isinstance(nested_book, Mapping) else {}
            bids = _levels(levels.get("bids", []), reverse=True)
            asks = _levels(levels.get("asks", []), reverse=False)
            book_row.update(s="kalshi", tk=ticker, cs=_scaled(contract_size),
                            bq=_scaled(bids[0][1]) if bids else None,
                            aq=_scaled(asks[0][1]) if asks else None)
            output["kalshi_perps"].append(book_row)
            estimate = self.kalshi.get("/funding_rates/estimate", params={"ticker": ticker})
            estimate_rows = parse_fixture("kalshi_funding_estimate", estimate, collected_at_ms=t)
            for row in estimate_rows: row["s"] = "kalshi"
            output["kalshi_funding_estimates"].extend(estimate_rows)
            funding_next = self.state.setdefault("funding_next_fetch", {})
            if t >= int(funding_next.get(ticker, 0)):
                historical = self.kalshi.get("/funding_rates/historical", params={"ticker": ticker})
                funding_last = self.state.setdefault("funding_last", {})
                last_time = int(funding_last.get(ticker, 0))
                newest = last_time
                for row in parse_fixture("kalshi_funding_historical", historical, collected_at_ms=t):
                    event_time = int(row.get("ft") or 0)
                    if event_time > last_time:
                        row["s"] = "kalshi"; output["kalshi_funding_settled"].append(row)
                        newest = max(newest, event_time)
                if newest:
                    funding_last[ticker] = newest
                next_event = estimate_rows[0].get("ft") if estimate_rows else None
                funding_next[ticker] = int(next_event) if next_event and int(next_event) > t else t + 8 * 3600 * 1000
            self._collect_spot(output, asset, t)
        self._collect_brackets(output, now, t)
        # The runner checkpoints this state only after the corresponding
        # immutable chunks are durable, keeping cursors behind (never ahead of)
        # archived observations after a crash.
        self.state["last_sample_ms"] = t
        return dict(output)

    def _collect_spot(self, output: dict[str, list[dict[str, Any]]], asset: str, t: int) -> None:
        pairs = self.state.setdefault("pairs", {})
        cb_pair = pairs.get(asset, {}).get("coinbase") or f"{asset}-USD"
        try:
            ticker = self.coinbase.get(f"/products/{cb_pair}/ticker")
            book = self.coinbase.get(f"/products/{cb_pair}/book", params={"level": 2})
            tr = parse_fixture("coinbase_ticker", ticker, collected_at_ms=t)[0]; tr.update(s="coinbase", pa=cb_pair, **{"as": asset})
            br = _book_row("coinbase", t, book, rt="sb", asset=asset); br["pa"] = cb_pair
            output["coinbase"].extend((tr, br)); pairs.setdefault(asset, {})["coinbase"] = cb_pair
            cursors = self.state.setdefault("coinbase_candle_cursor", {})
            start = int(cursors.get(cb_pair, t // 1000 - 24 * 3600))
            end = t // 1000
            if start <= end:
                candles = self.coinbase.get(f"/products/{cb_pair}/candles", params={
                    "granularity": 900,
                    "start": datetime.fromtimestamp(start, UTC).isoformat(),
                    "end": datetime.fromtimestamp(end, UTC).isoformat(),
                })
                candle_rows = parse_fixture("coinbase_candles", candles, collected_at_ms=t)
                for row in candle_rows: row.update(s="coinbase", pa=cb_pair, **{"as": asset})
                output["coinbase"].extend(candle_rows)
                if candle_rows:
                    cursors[cb_pair] = max(int(row.get("ep", 0)) // 1000 for row in candle_rows) + 900
        except (HTTPError, OSError, ValueError, KeyError):
            pass
        kr_pair = pairs.get(asset, {}).get("kraken") or ("XBTUSD" if asset == "BTC" else f"{asset}USD")
        try:
            ticker = self.kraken.get("/Ticker", params={"pair": kr_pair})
            depth = self.kraken.get("/Depth", params={"pair": kr_pair, "count": 50})
            tr = parse_fixture("kraken_ticker", ticker, collected_at_ms=t)[0]; tr.update(s="kraken", **{"as": asset})
            pair, book = _kraken_result(depth); br = _book_row("kraken", t, book, rt="sb", asset=asset); br["pa"] = pair or kr_pair
            output["kraken"].extend((tr, br)); pairs.setdefault(asset, {})["kraken"] = kr_pair
        except (HTTPError, OSError, ValueError, KeyError):
            pass

    def _collect_brackets(self, output: dict[str, list[dict[str, Any]]], now: datetime, t: int) -> None:
        pending = self.state.setdefault("pending_events", {})
        due = t - int(self.state.get("last_bracket_ms") or 0) >= BRACKET_INTERVAL_MS - BRACKET_SLACK_MS
        for series in BRACKET_SERIES if due else ():
            payload = self.kalshi_core.get("/events", params={"series_ticker": series, "status": "open"})
            for event in select_bracket_events(payload.get("events", []), now=now):
                et = str(event["event_ticker"])
                markets = self.kalshi_core.get("/markets", params={"event_ticker": et})
                market_rows = parse_fixture("kalshi_bracket_markets", markets, collected_at_ms=t)
                for row in market_rows: row.update(s="kalshi", st=series)
                output["kalshi_brackets"].extend(market_rows)
                pending[et] = {"ct": _milliseconds(event.get("strike_date")), "st": series}
        if due:
            self.state["last_bracket_ms"] = t
        # Settlement capture remains pending until Kalshi returns non-active rows.
        for et, meta in list(pending.items()):
            if int(meta.get("ct") or 0) > t: continue
            payload = self.kalshi_core.get("/markets", params={"event_ticker": et})
            rows = payload.get("markets", [])
            if rows and all(str(row.get("status", "")).lower() not in {"active", "open"} for row in rows):
                settled_rows = parse_fixture("kalshi_bracket_markets", payload, collected_at_ms=t)
                for row in settled_rows: row.update(s="kalshi", st=meta.get("st"))
                output["kalshi_bracket_settled"].extend(settled_rows)
                del pending[et]


def run_collection_loop(collect: Callable[[], Any], *, interval_seconds: float = 900,
                        time_budget_seconds: float = 20_400, clock: Callable[[], float] = time.monotonic,
                        sleeper: Callable[[float], None] = time.sleep) -> int:
    if interval_seconds <= 0 or time_budget_seconds < 0: raise ValueError("invalid collection timing")
    started = clock(); deadline = started + time_budget_seconds; next_sample = started; completed = 0
    while clock() < deadline:
        now = clock()
        if now >= next_sample:
            collect(); completed += 1; next_sample = started + completed * interval_seconds
        sleeper(min(max(0.0, next_sample - clock()), max(0.0, deadline - clock())))
    return completed


def run_collector(*, data_dir: str | Path = "data/crypto", interval_minutes: float = 15,
                  duration_minutes: float = 340, commit_interval_minutes: float = 60) -> int:
    del commit_interval_minutes  # Git workflow owns commits; retained as an explicit operational contract.
    data_dir = Path(data_dir); store = HourlyChunkStore(data_dir / "chunks"); collector = CryptoCollector(data_dir)
    paths: list[Path] = []
    def sample() -> None:
        now = datetime.now(UTC)
        # First make the previous hour durable and checkpoint exactly the
        # state that produced it.  Sampling the new hour before this point
        # would advance funding/candle cursors beyond the archived chunks.
        flushed = store.flush(before=now)
        paths.extend(flushed)
        if flushed:
            _atomic_json(collector.state_path, collector.state)
        hour_file = f"{now:%Y%m%dT%H}0000Z.csv.gz"
        hour_directory = now.strftime("%Y/%m/%d")
        if any((data_dir / "chunks").glob(f"*/{hour_directory}/{hour_file}")):
            # A predecessor already finalized this hour.  Do not advance any
            # source cursor for observations that immutable chunks would reject.
            return
        for source, rows in collector.sample(now=now).items():
            if rows: store.add(source, rows, now)
    try:
        count = run_collection_loop(sample, interval_seconds=interval_minutes * 60, time_budget_seconds=duration_minutes * 60)
    finally:
        paths.extend(store.flush())
        _atomic_json(collector.state_path, collector.state)
    total = sum(path.stat().st_size for path in (data_dir / "chunks").rglob("*.csv.gz"))
    metrics = collector.state.setdefault("metrics", {}); metrics.update(samples=count, last_chunk_bytes=sum(p.stat().st_size for p in paths), cumulative_chunk_bytes=total)
    _atomic_json(collector.state_path, collector.state)
    print(f"crypto collector: samples={count} chunks={len(paths)} chunk_bytes={metrics['last_chunk_bytes']} cumulative_chunk_bytes={total}")
    if total > WARNING_BYTES: print("WARNING: crypto chunks exceed 250 MB; review the under-300 MB annual budget.")
    return count


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Collect public crypto observations; never trades")
    parser.add_argument("--data-dir", default="data/crypto")
    parser.add_argument("--interval-minutes", "--sample-interval-minutes", type=float, default=15)
    parser.add_argument("--duration", "--max-minutes", type=float, default=340)
    parser.add_argument("--commit-interval-minutes", type=float, default=60)
    args = parser.parse_args(argv)
    run_collector(data_dir=args.data_dir, interval_minutes=args.interval_minutes,
                  duration_minutes=args.duration, commit_interval_minutes=args.commit_interval_minutes)


if __name__ == "__main__": main()


__all__ = ["CryptoCollector", "FundingEventState", "HourlyChunkStore", "PublicJSONClient",
           "estimate_annual_bytes", "executable_bid_ask", "load_chunk", "main", "needs_storage_warning",
           "parse_fixture", "run_collection_loop", "run_collector", "select_bracket_events", "write_hourly_chunk"]
