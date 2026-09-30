"""Resumable, sampled archive of settled Kalshi markets.

Fast series are sampled at the *event* level: every market in an included event
is retained.  The default is deterministic Bernoulli sampling at 1%, giving
each retained row an inverse-probability weight of 100.  Slow series are kept
in full with weight one.
"""

from __future__ import annotations

import argparse
from collections.abc import Iterable, Iterator, Mapping
from concurrent.futures import ThreadPoolExecutor
import csv
from datetime import datetime, timedelta, timezone
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import time
from typing import Any

from .client import KalshiClient, KalshiHTTPError


DEFAULT_FAST_SAMPLE_RATE = 0.01
FAST_SAMPLE_SEED = "kalshi-fast-events-v1"
FIRST_ARCHIVE_MONTH = "2021-01"
PRE_CLOSE_HORIZONS = {"1h": timedelta(hours=1), "1d": timedelta(days=1), "7d": timedelta(days=7)}
POST_OPEN_HORIZONS = {"1h": timedelta(hours=1), "24h": timedelta(hours=24)}
HORIZON_LABELS = (
    "close_minus_1h",
    "close_minus_1d",
    "close_minus_7d",
    "open_plus_1h",
    "open_plus_24h",
)
PRICE_MEASURES = ("last_trade", "yes_bid", "yes_ask", "spread")
CHUNK_COLUMNS = (
    "ticker",
    "event_ticker",
    "series_ticker",
    "category",
    "frequency",
    "is_mention",
    "open_time",
    "close_time",
    "settlement_time",
    "result",
    "volume",
    "sampling_weight",
    *(
        f"{horizon}_{measure}"
        for horizon in HORIZON_LABELS
        for measure in (*PRICE_MEASURES, "source_timestamp")
    ),
)
SIZE_WARNING_BYTES = 250 * 1024 * 1024
SERIES_CACHE_TTL_SECONDS = 60 * 60
MENTION_CACHE_TTL_SECONDS = 24 * 60 * 60


def _utc(value: datetime | str) -> datetime:
    if isinstance(value, str):
        value = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


def deterministic_sample(
    rows: Iterable[Mapping[str, Any]], *, sample_size: int, seed: str
) -> list[dict[str, Any]]:
    """Select an order-independent fixed-size hash sample.

    This helper is useful when a complete bounded population is already in
    memory.  Production collection uses :func:`event_is_selected`, which can
    stream a large monthly population without retaining excluded rows.
    """

    population = [dict(row) for row in rows]
    if sample_size < 0 or sample_size > len(population):
        raise ValueError("sample_size must be between zero and population size")
    if not population:
        return []
    ranked = sorted(
        population,
        key=lambda row: (
            hashlib.sha256(f"{seed}\0{_row_identity(row)}".encode()).digest(),
            _row_identity(row),
        ),
    )[:sample_size]
    probability = sample_size / len(population)
    weight = 1.0 / probability if probability else math.inf
    for row in ranked:
        row["selection_probability"] = probability
        row["sampling_weight"] = weight
        row["weight"] = weight
    return ranked


def _row_identity(row: Mapping[str, Any]) -> str:
    for field in ("event_ticker", "ticker", "id"):
        if row.get(field) is not None:
            return str(row[field])
    return json.dumps(dict(row), sort_keys=True, separators=(",", ":"), default=str)


def event_is_selected(event_ticker: str, *, seed: str, sample_rate: float = DEFAULT_FAST_SAMPLE_RATE) -> bool:
    """Return the stable Bernoulli sampling decision for one event."""

    if not 0 < sample_rate <= 1:
        raise ValueError("sample_rate must be in (0, 1]")
    digest = hashlib.sha256(f"{seed}\0{event_ticker}".encode()).digest()
    value = int.from_bytes(digest[:8], "big") / 2**64
    return value < sample_rate


def is_fast_series(
    frequency: str | None,
    *,
    open_time: datetime | str | None = None,
    close_time: datetime | str | None = None,
) -> bool:
    """Identify hourly-or-faster series, including short-lived custom markets."""

    normalized = (frequency or "").lower().replace("-", "_").replace(" ", "_")
    if "hour" in normalized or "minute" in normalized or normalized in {
        "15m",
        "30m",
        "intraday",
    }:
        return True
    if open_time is not None and close_time is not None:
        try:
            return timedelta(0) <= _utc(close_time) - _utc(open_time) < timedelta(days=1)
        except (TypeError, ValueError):
            pass
    return False


def apply_sampling(
    markets: Iterable[Mapping[str, Any]],
    *,
    series_by_ticker: Mapping[str, Mapping[str, Any]],
    seed: str,
    sample_rate: float = DEFAULT_FAST_SAMPLE_RATE,
) -> list[dict[str, Any]]:
    """Keep all slow markets and a deterministic event sample of fast ones."""

    decisions: dict[str, bool] = {}
    selected: list[dict[str, Any]] = []
    for original in markets:
        row = dict(original)
        series = series_by_ticker.get(str(row.get("series_ticker", "")), {})
        fast = str(series.get("category", row.get("category", ""))).casefold() == "sports" or is_fast_series(
            str(series.get("frequency", row.get("frequency", ""))),
            open_time=row.get("open_time"),
            close_time=row.get("close_time"),
        )
        event = str(row.get("event_ticker") or row.get("ticker"))
        keep = not fast
        probability = 1.0
        if fast:
            keep = decisions.setdefault(
                event, event_is_selected(event, seed=seed, sample_rate=sample_rate)
            )
            probability = sample_rate
        if keep:
            row["selection_probability"] = probability
            row["sampling_weight"] = 1.0 / probability
            row["weight"] = 1.0 / probability
            selected.append(row)
    return selected


def _candle_value(candle: Mapping[str, Any], side: str) -> float | None:
    aliases = {"last_trade": "price", "last_trade_price": "price"}
    section = candle.get(aliases.get(side, side))
    if not isinstance(section, Mapping):
        return None
    for field in ("close_dollars", "close"):
        value = section.get(field)
        if value is not None:
            try:
                return float(value)
            except (TypeError, ValueError):
                return None
    return None


def extract_fixed_horizon_price(
    candles: Iterable[Mapping[str, Any]], *, target: datetime | str, side: str
) -> float | None:
    """Take the last hourly candle close at or before an exact UTC horizon."""

    target_ts = _utc(target).timestamp()
    eligible = []
    for candle in candles:
        try:
            timestamp = float(candle["end_period_ts"])
        except (KeyError, TypeError, ValueError):
            continue
        if target_ts - 6 * 3600 <= timestamp <= target_ts and _candle_value(candle, side) is not None:
            eligible.append((timestamp, candle))
    if not eligible:
        return None
    return _candle_value(max(eligible, key=lambda pair: pair[0])[1], side)


def extract_price_snapshot(
    candles: Iterable[Mapping[str, Any]], *, target: datetime | str
) -> dict[str, Any]:
    target_ts = _utc(target).timestamp()
    eligible: list[tuple[float, Mapping[str, Any]]] = []
    for candle in candles:
        try:
            timestamp = float(candle["end_period_ts"])
        except (KeyError, TypeError, ValueError):
            continue
        usable = any(_candle_value(candle, side) is not None for side in ("price", "yes_bid", "yes_ask"))
        if target_ts - 6 * 3600 <= timestamp <= target_ts and usable:
            eligible.append((timestamp, candle))
    if not eligible:
        return _null_snapshot()
    timestamp, chosen = max(eligible, key=lambda pair: pair[0])
    last = _candle_value(chosen, "price")
    bid = _candle_value(chosen, "yes_bid")
    ask = _candle_value(chosen, "yes_ask")
    return {
        "last_trade_price": last,
        "yes_bid": bid,
        "yes_ask": ask,
        "spread": ask - bid if ask is not None and bid is not None else None,
        "source_timestamp": int(timestamp),
    }


def summarize_market(
    market: Mapping[str, Any],
    *,
    event: Mapping[str, Any],
    series: Mapping[str, Any],
    candles: Iterable[Mapping[str, Any]],
    selection_probability: float = 1.0,
) -> dict[str, Any]:
    """Build the flat, one-row-per-market archive record."""

    candle_rows = list(candles)
    opened = _utc(str(market["open_time"]))
    closed = _utc(str(market["close_time"]))
    probability = float(selection_probability)
    row: dict[str, Any] = {
        "ticker": market.get("ticker"),
        "event_ticker": market.get("event_ticker") or event.get("event_ticker") or event.get("ticker"),
        "series_ticker": event.get("series_ticker") or market.get("series_ticker") or series.get("ticker"),
        "category": series.get("category") or event.get("category"),
        "frequency": series.get("frequency"),
        "is_mention": int(bool(series.get("is_mention", False))),
        "fee_type": series.get("fee_type"),
        "fee_multiplier": series.get("fee_multiplier"),
        "open_time": opened.isoformat().replace("+00:00", "Z"),
        "close_time": closed.isoformat().replace("+00:00", "Z"),
        "settlement_time": market.get("settlement_ts"),
        "result": market.get("result"),
        "volume": _number(market.get("volume_fp", market.get("volume"))),
        "selection_probability": probability,
        "sampling_weight": 1.0 / probability,
        "weight": 1.0 / probability,
    }
    for label, distance in PRE_CLOSE_HORIZONS.items():
        target = closed - distance
        snapshot = (
            extract_price_snapshot(candle_rows, target=target) if target >= opened else _null_snapshot()
        )
        _flatten_snapshot(row, f"close_minus_{label}", snapshot)
    for label, distance in POST_OPEN_HORIZONS.items():
        target = opened + distance
        snapshot = (
            extract_price_snapshot(candle_rows, target=target) if target <= closed else _null_snapshot()
        )
        _flatten_snapshot(row, f"open_plus_{label}", snapshot)
    return row


def _null_snapshot() -> dict[str, None]:
    return {
        "last_trade_price": None,
        "yes_bid": None,
        "yes_ask": None,
        "spread": None,
        "source_timestamp": None,
    }


def _flatten_snapshot(row: dict[str, Any], label: str, snapshot: Mapping[str, Any]) -> None:
    for measure, value in snapshot.items():
        # The analysis layer's compact flat schema calls this measure
        # ``last_trade``; keep ``_price`` only in the snapshot helper's prose.
        column_measure = "last_trade" if measure == "last_trade_price" else measure
        row[f"{label}_{column_measure}"] = value


def _number(value: Any) -> float | None:
    try:
        return float(value) if value is not None else None
    except (TypeError, ValueError):
        return None


def _iso_seconds(value: Any) -> str:
    if value in (None, ""):
        return ""
    if isinstance(value, (int, float)):
        parsed = datetime.fromtimestamp(float(value), tz=timezone.utc)
    else:
        parsed = _utc(str(value))
    return parsed.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _compact_number(value: Any, *, decimals: int = 4) -> str:
    if value in (None, ""):
        return ""
    return f"{float(value):.{decimals}f}"


def _compact_row(original: Mapping[str, Any]) -> dict[str, Any]:
    row = dict(original)
    compact: dict[str, Any] = {column: "" for column in CHUNK_COLUMNS}
    for column in ("ticker", "event_ticker", "series_ticker", "category", "frequency", "result"):
        compact[column] = row.get(column) or ""
    mention = row.get("is_mention", 0)
    if isinstance(mention, str):
        mention = mention.strip().lower() in {"1", "true", "yes"}
    compact["is_mention"] = str(int(bool(mention)))
    for column in ("open_time", "close_time", "settlement_time"):
        compact[column] = _iso_seconds(row.get(column))
    volume = row.get("volume")
    compact["volume"] = "" if volume in (None, "") else str(int(float(volume)))
    compact["sampling_weight"] = _compact_number(row.get("sampling_weight", row.get("weight", 1.0)))
    for horizon in HORIZON_LABELS:
        for measure in PRICE_MEASURES:
            column = f"{horizon}_{measure}"
            compact[column] = _compact_number(row.get(column))
        timestamp = row.get(f"{horizon}_source_timestamp")
        compact[f"{horizon}_source_timestamp"] = _iso_seconds(timestamp)
    return compact


def _row_month(row: Mapping[str, Any]) -> str:
    settled = row.get("settlement_time") or row.get("close_time")
    return _utc(str(settled)).strftime("%Y-%m") if settled else ""


def _read_chunk_rows(chunk_dir: Path) -> Iterator[dict[str, str]]:
    for path in sorted(chunk_dir.glob("*.csv.gz")):
        with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
            yield from csv.DictReader(handle)


class MonthlyArchive:
    """One in-memory run buffer plus immutable append-only gzip CSV chunks."""

    def __init__(self, root: str | Path) -> None:
        self.root = Path(root)
        self.chunk_dir = self.root / "chunks"
        self.cache_dir = self.root / "_cache"
        self.state_path = self.root / "archive-state.json"
        self.catalog_cache_path = self.cache_dir / "series-catalog.json"
        # Committed with the archive (not in _cache/, which isn't carried between
        # GitHub runs), so the report job can label rows written before is_mention.
        self.mention_cache_path = self.root / "mention-series.json"
        self._pending_rows: dict[str, dict[str, Any]] = {}
        self._pending_months: dict[str, str] = {}
        self.defer_state_writes = False
        self._deferred_state: dict[str, Any] | None = None

    def ingest_month(
        self,
        month: str,
        rows: Iterable[Mapping[str, Any]],
        *,
        return_rows: bool = True,
    ) -> list[dict[str, Any]]:
        """Buffer rows for this run, deduplicated by ticker.

        ``month`` remains in the compatibility API so older callers can group
        pages, but chunk storage is deliberately independent of partitions.
        """

        _validate_month(month)
        for original in rows:
            row = dict(original)
            ticker = str(row.get("ticker") or "")
            if ticker:
                self._pending_rows[ticker] = row
                settled = row.get("settlement_time") or row.get("settlement_ts")
                self._pending_months[ticker] = _utc(str(settled)).strftime("%Y-%m") if settled else month
        return self.read_month(month) if return_rows else []

    def read_month(self, month: str) -> list[dict[str, Any]]:
        _validate_month(month)
        rows = {
            str(row.get("ticker")): row
            for row in _read_chunk_rows(self.chunk_dir)
            if _row_month(row) == month
        }
        for ticker, row in self._pending_rows.items():
            if self._pending_months.get(ticker, _row_month(row)) == month:
                rows[ticker] = dict(row)
        return list(rows.values())

    @property
    def pending_rows(self) -> list[dict[str, Any]]:
        return list(self._pending_rows.values())

    def chunk_path(self, run_started_at: datetime) -> Path:
        stamp = _utc(run_started_at).replace(microsecond=0).strftime("%Y%m%dT%H%M%SZ")
        return self.chunk_dir / f"{stamp}.csv.gz"

    def write_chunk(
        self,
        rows: Iterable[Mapping[str, Any]],
        *,
        run_started_at: datetime,
    ) -> Path:
        """Atomically create one chunk without ever replacing an existing one."""

        final = self.chunk_path(run_started_at)
        if final.exists():
            raise FileExistsError(f"archive chunk already exists: {final}")
        final.parent.mkdir(parents=True, exist_ok=True)
        temporary = final.with_suffix(final.suffix + ".tmp")
        compact = [_compact_row(row) for row in rows]
        try:
            with gzip.open(temporary, "wt", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=CHUNK_COLUMNS, extrasaction="ignore")
                writer.writeheader()
                writer.writerows(compact)
            os.replace(temporary, final)
        finally:
            if temporary.exists():
                temporary.unlink()

        state = self.load_state()
        metrics = dict(state.get("metrics") or {})
        chunk_bytes = final.stat().st_size
        metrics.update(
            rows_written=len(compact),
            chunk_bytes=chunk_bytes,
            cumulative_rows_written=int(metrics.get("cumulative_rows_written", 0)) + len(compact),
            cumulative_chunk_bytes=sum(path.stat().st_size for path in self.chunk_dir.glob("*.csv.gz")),
        )
        state["metrics"] = metrics
        self.save_state(state)
        self._pending_rows.clear()
        self._pending_months.clear()
        return final

    def load_state(self) -> dict[str, Any]:
        if self._deferred_state is not None:
            return json.loads(json.dumps(self._deferred_state))
        if not self.state_path.exists():
            return {"caught_up": False, "finished_series": [], "series": {}, "metrics": {}}
        state = json.loads(self.state_path.read_text(encoding="utf-8"))
        state.pop("series_catalog", None)
        return state

    def save_state(self, state: Mapping[str, Any]) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        document = dict(state)
        document.pop("series_catalog", None)
        if self.defer_state_writes:
            self._deferred_state = json.loads(json.dumps(document))
            return
        self._write_state(document)

    def _write_state(self, document: Mapping[str, Any]) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        temporary = self.state_path.with_suffix(".json.tmp")
        temporary.write_text(
            json.dumps(dict(document), indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        os.replace(temporary, self.state_path)

    def flush_state(self) -> None:
        """Commit the latest deferred cursor state after its chunk is durable."""

        document = self._deferred_state
        self._deferred_state = None
        self.defer_state_writes = False
        if document is not None:
            self._write_state(document)


class ArchiveCollector:
    """Series-driven, resumable collector with event-first sampling."""

    def __init__(self, client: KalshiClient, archive: MonthlyArchive, *, sample_rate: float = DEFAULT_FAST_SAMPLE_RATE) -> None:
        self.client = client
        self.archive = archive
        self.sample_rate = sample_rate
        self.kept = 0
        self.skipped = 0
        self.events_skipped = 0

    def load_series_catalog(self, state: dict[str, Any]) -> dict[str, dict[str, Any]]:
        del state
        cache = self.archive.catalog_cache_path
        if cache.exists() and time.time() - cache.stat().st_mtime < SERIES_CACHE_TTL_SECONDS:
            try:
                cached = json.loads(cache.read_text(encoding="utf-8"))
                if isinstance(cached, dict) and cached:
                    return {str(key): dict(value) for key, value in cached.items()}
            except (OSError, ValueError, TypeError):
                pass
        catalog = {}
        for row in self.client.series_list():
            if not row.get("ticker"):
                continue
            catalog[str(row["ticker"])] = {
                key: row.get(key)
                for key in ("ticker", "category", "frequency", "fee_type", "fee_multiplier")
            }
        cache.parent.mkdir(parents=True, exist_ok=True)
        temporary = cache.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(catalog, sort_keys=True), encoding="utf-8")
        os.replace(temporary, cache)
        return catalog

    def load_mention_series(self) -> set[str]:
        """Load the case-sensitive Mentions category membership, refreshed daily."""

        # Freshness comes from the timestamp inside the file: a git checkout resets
        # file modification times, so mtime would look fresh on every GitHub run.
        cache = self.archive.mention_cache_path
        try:
            cached = json.loads(cache.read_text(encoding="utf-8"))
            fetched = _utc(cached["fetched_at"]).timestamp()
            if time.time() - fetched < MENTION_CACHE_TTL_SECONDS and isinstance(cached.get("tickers"), list):
                return {str(ticker) for ticker in cached["tickers"] if ticker}
        except (OSError, ValueError, TypeError, KeyError, AttributeError):
            pass
        tickers = {
            str(row["ticker"])
            for row in self.client.series_list(category="Mentions")
            if row.get("ticker")
        }
        cache.parent.mkdir(parents=True, exist_ok=True)
        temporary = cache.with_suffix(".json.tmp")
        fetched_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        temporary.write_text(json.dumps({"fetched_at": fetched_at, "tickers": sorted(tickers)}, indent=0),
                             encoding="utf-8")
        os.replace(temporary, cache)
        return tickers

    def collect(self, *, cutoff: datetime, deadline: float, incremental: bool = False) -> bool:
        state = self.archive.load_state()
        mention_tickers = self.load_mention_series()
        catalog = self.load_series_catalog(state)
        for ticker in mention_tickers:
            catalog.setdefault(ticker, {"ticker": ticker})
        for ticker, metadata in catalog.items():
            metadata["is_mention"] = ticker in mention_tickers
        finished = set(state.setdefault("finished_series", []))
        series_state = state.setdefault("series", {})
        now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        if incremental:
            # Keep a fixed upper watermark across every resume of this pass.
            # Advancing to completion time would skip settlements that arrive
            # after an early series was scanned but before the run finishes.
            watermark = state.setdefault("incremental_watermark", now)
            incremental_finished = set(state.setdefault("incremental_finished_series", []))
            since = state.get("last_run_at") or "1970-01-01T00:00:00Z"
        else:
            watermark = state.setdefault("backfill_live_watermark", now)
            incremental_finished = set()
            since = None
        self.archive.save_state(state)
        ordered_catalog = sorted(
            catalog.items(), key=lambda item: (item[0] not in mention_tickers,)
        )
        for ticker, metadata in ordered_catalog:
            if time.monotonic() >= deadline:
                return False
            if ticker.upper().startswith("KXMVE"):
                continue  # combo (multivariate) collections: enormous, never archived
            if not incremental and ticker in finished:
                continue
            if incremental and ticker in incremental_finished:
                continue
            progress = series_state.setdefault(ticker, {})
            # A series first seen after the original backfill needs its full
            # history once; already-finished series use the incremental mark.
            series_since = since if not incremental or ticker in finished else None
            complete = (
                self._collect_fast(ticker, metadata, progress, state, cutoff, deadline, series_since)
                if str(metadata.get("category", "")).casefold() == "sports"
                or is_fast_series(str(metadata.get("frequency", "")))
                else self._collect_slow(ticker, metadata, progress, state, cutoff, deadline, series_since)
            )
            if not complete:
                return False
            if not incremental:
                finished.add(ticker)
                state["finished_series"] = sorted(finished)
            else:
                incremental_finished.add(ticker)
                state["incremental_finished_series"] = sorted(incremental_finished)
                if ticker not in finished:
                    finished.add(ticker)
                    state["finished_series"] = sorted(finished)
            self.archive.save_state(state)
        if not incremental:
            state["caught_up"] = True
            state.pop("backfill_live_watermark", None)
        else:
            state.pop("incremental_watermark", None)
            state.pop("incremental_finished_series", None)
        state["last_run_at"] = watermark
        self.archive.save_state(state)
        return True

    def _collect_slow(self, ticker: str, series: Mapping[str, Any], progress: dict[str, Any], state: dict[str, Any], cutoff: datetime, deadline: float, since: str | None) -> bool:
        tiers = ("live",) if since else ("historical", "live")
        for tier in tiers:
            marker = progress.setdefault(tier, {"cursor": "", "complete": False})
            if marker.get("complete") and not since:
                continue
            params: dict[str, Any] = {"series_ticker": ticker}
            path = "/historical/markets" if tier == "historical" else "/markets"
            if tier == "live":
                params["status"] = "settled"
                if since:
                    params["min_settled_ts"] = int(_utc(since).timestamp()) + 1
            if marker.get("cursor"):
                params["cursor"] = marker["cursor"]
            if not self._walk_market_pages(path, params, series, 1.0, tier, marker, state, cutoff, deadline):
                return False
        return True

    def _collect_fast(self, ticker: str, series: Mapping[str, Any], progress: dict[str, Any], state: dict[str, Any], cutoff: datetime, deadline: float, since: str | None) -> bool:
        event_marker = progress.setdefault("events", {"cursor": "", "complete": False})
        params: dict[str, Any] = {"series_ticker": ticker}
        if event_marker.get("cursor"):
            params["cursor"] = event_marker["cursor"]
        for page in self.client.iter_pages("/events", params=params):
            for event in page.get("events", []):
                event_ticker = str(event.get("event_ticker") or event.get("ticker") or "")
                if not event_is_selected(event_ticker, seed=FAST_SAMPLE_SEED, sample_rate=self.sample_rate):
                    self.events_skipped += 1
                    known_count = event.get("market_count")
                    if known_count is None and isinstance(event.get("markets"), list):
                        known_count = len(event["markets"])
                    if known_count is not None:
                        self.skipped += int(known_count)
                    continue
                tiers = ("live",) if since else ("historical", "live")
                event_progress = progress.setdefault("selected_events", {}).setdefault(event_ticker, {})
                for tier in tiers:
                    marker = event_progress.setdefault(tier, {"cursor": "", "complete": False})
                    market_params: dict[str, Any] = {"event_ticker": event_ticker}
                    path = "/historical/markets" if tier == "historical" else "/markets"
                    if tier == "live":
                        market_params["status"] = "settled"
                        if since:
                            market_params["min_settled_ts"] = int(_utc(since).timestamp()) + 1
                    if marker.get("cursor"):
                        market_params["cursor"] = marker["cursor"]
                    if not self._walk_market_pages(path, market_params, series, self.sample_rate, tier, marker, state, cutoff, deadline):
                        return False
            event_marker["cursor"] = str(page.get("cursor") or "")
            self.archive.save_state(state)
            if time.monotonic() >= deadline and event_marker["cursor"]:
                return False
        event_marker.update(cursor="", complete=True)
        event_marker.pop("frontier", None)
        self.archive.save_state(state)
        return True

    def _walk_market_pages(self, path: str, params: dict[str, Any], series: Mapping[str, Any], probability: float, tier: str, marker: dict[str, Any], state: dict[str, Any], cutoff: datetime, deadline: float) -> bool:
        for page in self.client.iter_pages(path, params=params):
            # Scoped queries can't ask Kalshi to exclude combos, so drop them here.
            markets = [m for m in page.get("markets", []) if not m.get("mve_collection_ticker")]
            groups: list[tuple[list[Mapping[str, Any]], float]] = [(markets, probability)]
            # A series labelled custom can still consist of intraday markets.
            # The list response is enough to identify those; discard them
            # before issuing any candle (per-market) request.
            if probability == 1.0:
                slow: list[Mapping[str, Any]] = []
                selected_short: list[Mapping[str, Any]] = []
                for market in markets:
                    short = is_fast_series(
                        str(series.get("frequency", "")),
                        open_time=market.get("open_time"), close_time=market.get("close_time"),
                    )
                    event_ticker = str(market.get("event_ticker") or market.get("ticker") or "")
                    if not short:
                        slow.append(market)
                    elif event_is_selected(event_ticker, seed=FAST_SAMPLE_SEED, sample_rate=self.sample_rate):
                        selected_short.append(market)
                    else:
                        self.skipped += 1
                groups = [(slow, 1.0), (selected_short, self.sample_rate)]
            summaries = [
                summary
                for group, group_probability in groups
                for summary in self._summarize_page(group, series, group_probability, tier, cutoff)
            ]
            by_month: dict[str, list[dict[str, Any]]] = {}
            for summary in summaries:
                settled = summary.get("settlement_time") or summary.get("close_time")
                month = _utc(str(settled)).strftime("%Y-%m")
                by_month.setdefault(month, []).append(summary)
            for month, month_rows in by_month.items():
                self.archive.ingest_month(month, month_rows, return_rows=False)
            self.kept += len(summaries)
            marker["cursor"] = str(page.get("cursor") or "")
            self.archive.save_state(state)
            if time.monotonic() >= deadline and marker["cursor"]:
                return False
        marker.update(cursor="", complete=True)
        self.archive.save_state(state)
        return True

    def _summarize_page(self, markets: list[Mapping[str, Any]], series: Mapping[str, Any], probability: float, tier: str, cutoff: datetime) -> list[dict[str, Any]]:
        if not markets:
            return []
        if tier == "live":
            candles: dict[str, list[dict[str, Any]]] = {}
            ordered = sorted(markets, key=lambda row: _utc(str(row["open_time"])))
            batch: list[Mapping[str, Any]] = []
            batch_start: datetime | None = None
            batch_end: datetime | None = None

            def flush() -> None:
                nonlocal batch, batch_start, batch_end
                if not batch or batch_start is None or batch_end is None:
                    return
                candles.update(self.client.batch_candlesticks(
                    [str(row["ticker"]) for row in batch],
                    start_ts=int(batch_start.timestamp()), end_ts=int(batch_end.timestamp()),
                    period_interval=60,
                ))
                batch, batch_start, batch_end = [], None, None

            for market in ordered:
                opened = _utc(str(market["open_time"]))
                closed = _utc(str(market["close_time"]))
                candidate_start = min(batch_start, opened) if batch_start else opened
                candidate_end = max(batch_end, closed) if batch_end else closed
                slots = int((candidate_end - candidate_start).total_seconds() // 3600) + 1
                if batch and (len(batch) >= 100 or slots * (len(batch) + 1) > 10_000):
                    flush()
                    candidate_start, candidate_end = opened, closed
                batch.append(market)
                batch_start, batch_end = candidate_start, candidate_end
            flush()
            return [self._summarize(row, series, candles.get(str(row["ticker"]), []), probability) for row in markets]

        def historical(row: Mapping[str, Any]) -> dict[str, Any]:
            opened = _utc(str(row["open_time"]))
            closed = _utc(str(row["close_time"]))
            candles = self.client.candlesticks(
                str(row["ticker"]), series_ticker=str(series.get("ticker") or row.get("series_ticker") or ""),
                start_ts=int(opened.timestamp()), end_ts=int(closed.timestamp()), period_interval=60,
                settlement_ts=str(row.get("settlement_ts") or row.get("close_time")), historical_cutoff=cutoff,
            )
            return self._summarize(row, series, candles, probability)

        with ThreadPoolExecutor(max_workers=6) as pool:
            return list(pool.map(historical, markets))

    @staticmethod
    def _summarize(market: Mapping[str, Any], series: Mapping[str, Any], candles: Iterable[Mapping[str, Any]], probability: float) -> dict[str, Any]:
        event = {"event_ticker": market.get("event_ticker"), "series_ticker": series.get("ticker") or market.get("series_ticker")}
        return summarize_market(market, event=event, series=series, candles=candles, selection_probability=probability)


def _validate_month(month: str) -> None:
    try:
        parsed = datetime.strptime(month, "%Y-%m")
    except ValueError as error:
        raise ValueError("month must have YYYY-MM form") from error
    if parsed.strftime("%Y-%m") != month:
        raise ValueError("month must have YYYY-MM form")


def _month_bounds(month: str) -> tuple[datetime, datetime]:
    _validate_month(month)
    start = datetime.strptime(month, "%Y-%m").replace(tzinfo=timezone.utc)
    return start, _utc(f"{_next_month(month)}-01T00:00:00Z")


def _next_month(month: str) -> str:
    parsed = datetime.strptime(month, "%Y-%m")
    year = parsed.year + (parsed.month == 12)
    number = 1 if parsed.month == 12 else parsed.month + 1
    return f"{year:04d}-{number:02d}"


def _month_sources(
    start: datetime, end: datetime, cutoff: datetime
) -> list[tuple[str, datetime, datetime, datetime]]:
    sources = []
    if start <= cutoff:
        historical_end = min(end, cutoff + timedelta(seconds=1))
        sources.append(("historical", start, historical_end, min(cutoff, historical_end)))
    live_start = max(start, cutoff + timedelta(seconds=1))
    if live_start < end:
        sources.append(("live", live_start, end, live_start))
    return sources


def run_archive(
    *,
    data_dir: str | Path = "data/kalshi",
    mode: str = "auto",
    max_minutes: float = 45.0,
) -> None:
    archive = MonthlyArchive(data_dir)
    run_started_at = datetime.now(timezone.utc)
    while archive.chunk_path(run_started_at).exists():
        time.sleep(0.05)
        run_started_at = datetime.now(timezone.utc)
    client = KalshiClient()
    collector = ArchiveCollector(client, archive)
    started = time.monotonic()
    requests_before = getattr(client, "request_count", 0)
    cutoff = client.historical_cutoff()
    deadline = time.monotonic() + max_minutes * 60
    state = archive.load_state()
    incremental = mode == "incremental" or (mode == "auto" and bool(state.get("caught_up")))
    archive.defer_state_writes = True
    stopped_early = None
    try:
        completed = collector.collect(cutoff=cutoff, deadline=deadline, incremental=incremental)
    except KalshiHTTPError as error:
        # Kalshi kept refusing (429 rate limit or 5xx) after the client's own retries.
        # Keep every finished page instead of crashing: on Sep 29-30, 2026 three runs in a
        # row died this way and each lost ~25 minutes of backfill, because nothing was
        # written. Cursors only advance after a page's rows are pending, so saving now is
        # consistent; the next run resumes from here.
        if error.status_code not in (429, 500, 502, 503, 504):
            raise
        completed = False
        stopped_early = f"Kalshi HTTP {error.status_code} after retries"
    rows_written = len(archive.pending_rows)
    chunk = archive.write_chunk(archive.pending_rows, run_started_at=run_started_at)
    elapsed = time.monotonic() - started
    state = archive.load_state()
    metrics = dict(state.get("metrics") or {})
    metrics.update(
        requests_made=getattr(client, "request_count", requests_before) - requests_before,
        markets_kept=collector.kept,
        markets_skipped_by_sampling=collector.skipped,
        events_skipped_by_sampling=collector.events_skipped,
        elapsed_seconds=round(elapsed, 3),
        completed=completed,
        rows_written=rows_written,
        chunk_bytes=chunk.stat().st_size,
        stopped_early=stopped_early,
    )
    state["metrics"] = metrics
    archive.save_state(state)
    archive.flush_state()
    print(
        "kalshi archive: "
        f"requests={metrics['requests_made']} "
        f"kept={collector.kept} markets_skipped_by_sampling={collector.skipped} "
        f"events_skipped_by_sampling={collector.events_skipped} "
        f"rows_written={metrics['rows_written']} chunk_bytes={metrics['chunk_bytes']} "
        f"cumulative_rows={metrics['cumulative_rows_written']} "
        f"cumulative_chunk_bytes={metrics['cumulative_chunk_bytes']} "
        f"elapsed={elapsed:.1f}s"
        + (f" stopped_early={stopped_early!r}" if stopped_early else "")
    )
    if int(metrics["cumulative_chunk_bytes"]) > SIZE_WARNING_BYTES:
        print("WARNING: Kalshi chunk storage exceeds 250 MB; review the 300 MB repository budget.")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Archive public settled Kalshi markets (never trades)")
    parser.add_argument("--data-dir", default="data/kalshi")
    parser.add_argument("--mode", choices=("auto", "backfill", "incremental"), default="auto")
    parser.add_argument("--max-minutes", type=float, default=45.0)
    args = parser.parse_args(argv)
    run_archive(data_dir=args.data_dir, mode=args.mode, max_minutes=args.max_minutes)


if __name__ == "__main__":
    main()


__all__ = [
    "ArchiveCollector",
    "DEFAULT_FAST_SAMPLE_RATE",
    "FAST_SAMPLE_SEED",
    "MonthlyArchive",
    "apply_sampling",
    "deterministic_sample",
    "event_is_selected",
    "extract_fixed_horizon_price",
    "extract_price_snapshot",
    "is_fast_series",
    "run_archive",
    "summarize_market",
]
