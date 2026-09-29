"""Offline acceptance checks for the Round 2 archive and inference safeguards."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
import hashlib
import importlib
import json
import math
from pathlib import Path
import re
import threading
from typing import Any

import pytest


FIXTURES = Path(__file__).parent / "fixtures" / "kalshi"
UTC = timezone.utc


def _archive():
    return importlib.import_module("observatory.kalshi.archive")


def _client():
    return importlib.import_module("observatory.kalshi.client")


def _stats():
    return importlib.import_module("observatory.stats")


def _fixture(name: str) -> dict[str, Any]:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def _as_timestamp(value: Any) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    return datetime.fromisoformat(str(value).replace("Z", "+00:00")).timestamp()


def _timestamp_values(snapshot: dict[str, Any]) -> list[Any]:
    return [
        value
        for key, value in snapshot.items()
        if "timestamp" in key.lower() or key.lower().endswith(("_time", "_ts"))
    ]


def _bh(values: list[float]) -> list[float]:
    order = sorted(range(len(values)), key=values.__getitem__)
    result = [1.0] * len(values)
    running = 1.0
    for rank in range(len(values), 0, -1):
        index = order[rank - 1]
        running = min(running, values[index] * len(values) / rank)
        result[index] = running
    return result


def test_rows_from_a_newest_first_cross_month_page_use_their_settlement_month(
    tmp_path: Path,
) -> None:
    historical = _fixture("markets_historical.json")["markets"][0]
    live = _fixture("markets_settled_live.json")["markets"][0]
    rows = sorted(
        [historical, live], key=lambda row: row["settlement_ts"], reverse=True
    )
    archive = _archive().MonthlyArchive(tmp_path)

    archive.ingest_month(rows[0]["settlement_ts"][:7], rows)

    for row in rows:
        month_rows = archive.read_month(row["settlement_ts"][:7])
        assert [item["ticker"] for item in month_rows] == [row["ticker"]]


def test_sparse_horizon_uses_latest_usable_candle_within_six_hours_and_records_time() -> None:
    for fixture_name in ("candlesticks_live.json", "candlesticks_historical.json"):
        real = _fixture(fixture_name)["candlesticks"][0]
        actual = int(real["end_period_ts"])
        for gap_hours in range(7):
            sparse = [real]
            if gap_hours:
                sparse.append({"end_period_ts": actual + gap_hours * 3600})
            target = datetime.fromtimestamp(actual + gap_hours * 3600, tz=UTC)
            snapshot = _archive().extract_price_snapshot(sparse, target=target)

            assert any(snapshot[name] is not None for name in ("last_trade_price", "yes_bid", "yes_ask"))
            timestamps = _timestamp_values(snapshot)
            assert timestamps and _as_timestamp(timestamps[0]) == pytest.approx(actual)

        too_late = datetime.fromtimestamp(actual + 7 * 3600, tz=UTC)
        expired = _archive().extract_price_snapshot([real], target=too_late)
        assert all(expired[name] is None for name in ("last_trade_price", "yes_bid", "yes_ask"))
        assert not [value for value in _timestamp_values(expired) if value is not None]


class _Response:
    status_code = 200
    headers: dict[str, str] = {}

    def __init__(self, payload: dict[str, Any]) -> None:
        self.payload = payload

    def json(self) -> dict[str, Any]:
        return self.payload


class _RecordingTransport:
    def __init__(self, clock=lambda: 0.0) -> None:
        self.clock = clock
        self.calls: list[tuple[str, dict[str, Any], float]] = []
        self.lock = threading.Lock()

    def request(self, method: str, url: str, *, params=None, timeout=None) -> _Response:
        del method, timeout
        with self.lock:
            self.calls.append((url, dict(params or {}), self.clock()))
        if url.endswith("/markets/candlesticks"):
            return _Response({"markets": []})
        return _Response({"candlesticks": []})


def test_candle_requests_obey_historical_windows_and_live_batch_caps() -> None:
    client_class = _client().KalshiClient
    cutoff = datetime(2026, 8, 1, tzinfo=UTC)
    settled = datetime(2026, 7, 1, tzinfo=UTC)

    for duration_days, expected_calls in ((3, 1), (9, 1), (10, 2), (41, 2)):
        transport = _RecordingTransport()
        client = client_class(transport=transport, requests_per_second=1_000)
        client.candlesticks(
            "MARKET",
            series_ticker="SERIES",
            start_ts=0,
            end_ts=duration_days * 86_400,
            settlement_ts=settled,
            historical_cutoff=cutoff,
        )
        assert len(transport.calls) == expected_calls
        assert all(call[1]["end_ts"] - call[1]["start_ts"] <= 9 * 86_400 for call in transport.calls)

    tickers = [f"T{index:03d}" for index in range(237)]
    transport = _RecordingTransport()
    client = client_class(transport=transport, requests_per_second=1_000)
    client.batch_candlesticks(tickers, start_ts=0, end_ts=24 * 3600)
    observed = set()
    for _, params, _ in transport.calls:
        batch = params["market_tickers"].split(",")
        observed.update(batch)
        candle_slots = math.floor((params["end_ts"] - params["start_ts"]) / 3600) + 1
        assert len(batch) <= 100
        assert len(batch) * candle_slots <= 10_000
    assert observed == set(tickers)


def test_concurrent_requests_share_the_default_eight_rps_limiter() -> None:
    class Clock:
        def __init__(self) -> None:
            self.value = 0.0
            self.lock = threading.Lock()

        def now(self) -> float:
            with self.lock:
                return self.value

        def sleep(self, seconds: float) -> None:
            with self.lock:
                self.value += seconds

    clock = Clock()
    transport = _RecordingTransport(clock.now)
    client = _client().KalshiClient(
        transport=transport, clock=clock.now, sleeper=clock.sleep, max_retries=0
    )
    with ThreadPoolExecutor(max_workers=12) as pool:
        list(pool.map(lambda index: client.get(f"/probe/{index}"), range(25)))

    moments = sorted(call[2] for call in transport.calls)
    assert client.requests_per_second <= 8
    assert all(later - earlier >= 1 / 8 for earlier, later in zip(moments, moments[1:]))


class _SeriesClient:
    """Endpoint-level fake: responses are empty so only traversal is under test."""

    requests_per_second = 8.0

    def __init__(self) -> None:
        self.calls: list[tuple[str, str, dict[str, Any]]] = []
        self.series_list_calls = 0
        self.cutoff = datetime(2026, 7, 15, 12, tzinfo=UTC)
        index = 0
        while _archive().event_is_selected(
            f"DROP-{index}", seed=_archive().FAST_SAMPLE_SEED
        ):
            index += 1
        self.dropped_event = f"DROP-{index}"

    def historical_cutoff(self) -> datetime:
        return self.cutoff

    def series_list(self, **params: Any):
        del params
        self.series_list_calls += 1
        yield {"ticker": "SLOW", "frequency": "monthly"}
        yield {"ticker": "FAST", "frequency": "hourly"}

    def _tier(self, path: str, timestamp: Any) -> str:
        if "/historical/" in path:
            return "historical"
        if timestamp is not None and _as_timestamp(timestamp) <= self.cutoff.timestamp():
            return "historical"
        return "live"

    def iter_pages(self, path: str, *, params=None, timestamp=None, **kwargs: Any):
        del kwargs
        values = dict(params or {})
        normalized = "/" + path.lstrip("/")
        if normalized.endswith("/markets"):
            assert values.get("series_ticker") == "SLOW", "slow markets must be filtered by series"
            self.calls.append(("markets", self._tier(normalized, timestamp), values))
            yield {"markets": [], "cursor": ""}
            return
        if normalized.endswith("/events"):
            assert values.get("series_ticker") == "FAST", "fast events must be filtered by series"
            self.calls.append(("events", self._tier(normalized, timestamp), values))
            yield {
                "events": [
                    {"event_ticker": self.dropped_event, "series_ticker": "FAST"}
                ],
                "cursor": "",
            }
            return
        raise AssertionError(f"unexpected collection endpoint: {path}")

    def paginate(self, path: str, *, item_key: str, **kwargs: Any):
        for page in self.iter_pages(path, **kwargs):
            yield from page[item_key]

    def markets(self, **params: Any):
        return self.paginate("/markets", item_key="markets", params=params)

    def event(self, ticker: str, *, with_nested_markets: bool = False):
        self.calls.append(("event_detail", "live", {"ticker": ticker}))
        return {"event_ticker": ticker, "series_ticker": "FAST", "markets": []}

    def series(self, ticker: str):
        self.calls.append(("series_detail", "live", {"ticker": ticker}))
        raise AssertionError("metadata returned by the series listing must be cached")

    def candlesticks(self, ticker: str, **kwargs: Any):
        self.calls.append(("candles", "live", {"ticker": ticker, **kwargs}))
        return []

    def batch_candlesticks(self, tickers: list[str], **kwargs: Any):
        self.calls.append(("candles", "live", {"tickers": tickers, **kwargs}))
        return {}


def test_series_backfill_state_sampling_order_and_incremental_transition(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    module = _archive()
    client = _SeriesClient()
    monkeypatch.setattr(module, "KalshiClient", lambda: client)
    archive = module.MonthlyArchive(tmp_path)
    archive.save_state({"next_month": "2026-07", "months": {}})

    module.run_archive(data_dir=tmp_path, mode="backfill", max_minutes=5)

    assert client.series_list_calls == 1
    slow_tiers = {tier for kind, tier, _ in client.calls if kind == "markets"}
    assert slow_tiers == {"historical", "live"}
    assert any(kind == "events" and params.get("series_ticker") == "FAST" for kind, _, params in client.calls)
    assert not any(kind in {"event_detail", "candles"} for kind, _, _ in client.calls)

    state = archive.load_state()
    assert state["caught_up"] is True
    assert set(state["finished_series"]) == {"SLOW", "FAST"}
    per_series = state["series"]
    assert set(per_series) == {"SLOW", "FAST"}
    assert all("cursor" in json.dumps(per_series[ticker]).lower() for ticker in per_series)
    assert isinstance(state.get("metrics"), dict) and state["metrics"]

    before = len(client.calls)
    module.run_archive(data_dir=tmp_path, mode="auto", max_minutes=5)
    incremental = client.calls[before:]
    assert incremental and all(tier == "live" for _, tier, _ in incremental)
    assert client.series_list_calls == 1


def test_ledger_summarizes_ids_and_times_and_omits_insufficient_runs(tmp_path: Path) -> None:
    stats = _stats()
    ledger = stats.HypothesisLedger(tmp_path / "ledger.jsonl")
    ids = [f"market-{index * index + 3}" for index in range(11)]
    times = [datetime(2026, 1, 1, tzinfo=UTC) + timedelta(hours=index * index) for index in range(11)]
    digest = hashlib.sha256("\n".join(sorted(ids)).encode()).hexdigest()

    entry = ledger.log_run(
        hypothesis_id="generated",
        phase="discovery",
        p_value=0.2,
        record_ids=reversed(ids),
        settlement_times=[value.isoformat() for value in reversed(times)],
    )
    raw = json.loads((tmp_path / "ledger.jsonl").read_text(encoding="utf-8"))
    assert "record_ids" not in raw and not any(value in json.dumps(raw) for value in ids)
    assert len(ids) in raw.values()
    assert digest in raw.values()
    assert times[0].isoformat() in raw.values()
    assert times[-1].isoformat() in raw.values()
    assert entry["run_id"] == raw["run_id"]

    empty_ledger = stats.HypothesisLedger(tmp_path / "empty.jsonl")
    importlib.import_module("observatory.kalshi.checks").run_standard_checks([], ledger=empty_ledger)
    assert empty_ledger.entries() == []


def test_fixed_confirmation_gate_nonoverlap_one_shot_and_date_logging(tmp_path: Path) -> None:
    stats = _stats()
    boundary = datetime(2026, 4, 1, tzinfo=UTC)
    assert stats.CONFIRMATION_START == boundary
    records = [
        {"ticker": f"R{offset:+d}", "settled_at": boundary + timedelta(days=offset)}
        for offset in range(-8, 9)
    ]
    discovery, confirmation = stats.split_discovery_confirmation(reversed(records))
    assert discovery and confirmation
    assert max(row["settled_at"] for row in discovery) < boundary
    assert min(row["settled_at"] for row in confirmation) >= boundary

    ledger = stats.HypothesisLedger(tmp_path / "gate.jsonl")
    discovery_ids = [row["ticker"] for row in discovery]
    discovery_times = [row["settled_at"] for row in discovery]
    ledger.log_run(
        hypothesis_id="h",
        phase="discovery",
        p_value=0.2,
        record_ids=discovery_ids,
        settlement_times=[value.isoformat() for value in discovery_times],
    )
    with pytest.raises(stats.ConfirmationLockError, match="caught|backfill"):
        ledger.assert_confirmation_allowed("h", caught_up=False)
    with pytest.raises(stats.ConfirmationLockError, match="overlap|window|start"):
        ledger.log_run(
            hypothesis_id="h",
            phase="confirmation",
            p_value=0.1,
            record_ids=["too-early"],
            settlement_times=[(boundary - timedelta(seconds=1)).isoformat()],
            caught_up=True,
        )

    confirmation_entry = ledger.log_run(
        hypothesis_id="h",
        phase="confirmation",
        p_value=0.1,
        record_ids=[row["ticker"] for row in confirmation],
        settlement_times=[row["settled_at"].isoformat() for row in confirmation],
        caught_up=True,
    )
    assert min(row["settled_at"] for row in confirmation).isoformat() in confirmation_entry.values()
    assert max(row["settled_at"] for row in confirmation).isoformat() in confirmation_entry.values()
    with pytest.raises(stats.ConfirmationLockError, match="already"):
        ledger.log_run(
            hypothesis_id="h",
            phase="confirmation",
            p_value=0.05,
            record_ids=["later"],
            settlement_times=[(boundary + timedelta(days=30)).isoformat()],
            caught_up=True,
        )


def test_bh_uses_latest_discovery_per_hypothesis_and_confirmation_separately(
    tmp_path: Path,
) -> None:
    ledger = _stats().HypothesisLedger(tmp_path / "bh.jsonl")
    boundary = datetime(2026, 4, 1, tzinfo=UTC)
    latest_discovery: list[dict[str, Any]] = []
    confirmations: list[dict[str, Any]] = []
    for index, latest_p in enumerate((0.03, 0.20, 0.41)):
        hypothesis = f"h{index}"
        ledger.log_run(
            hypothesis_id=hypothesis,
            phase="discovery",
            p_value=0.9 - index / 10,
            record_ids=[f"old-{index}"],
            settlement_times=[(boundary - timedelta(days=10 + index)).isoformat()],
        )
        latest_discovery.append(
            ledger.log_run(
                hypothesis_id=hypothesis,
                phase="discovery",
                p_value=latest_p,
                record_ids=[f"new-{index}"],
                settlement_times=[(boundary - timedelta(days=index + 1)).isoformat()],
            )
        )
        confirmations.append(
            ledger.log_run(
                hypothesis_id=hypothesis,
                phase="confirmation",
                p_value=(0.01, 0.08, 0.31)[index],
                record_ids=[f"confirm-{index}"],
                settlement_times=[(boundary + timedelta(days=index)).isoformat()],
                caught_up=True,
            )
        )

    entries = ledger.entries()
    assert len(entries) == 9
    by_run = {entry["run_id"]: entry for entry in entries}
    assert [by_run[row["run_id"]]["q_value"] for row in latest_discovery] == pytest.approx(
        _bh([0.03, 0.20, 0.41])
    )
    assert [by_run[row["run_id"]]["q_value"] for row in confirmations] == pytest.approx(
        _bh([0.01, 0.08, 0.31])
    )


def test_readme_and_workflows_explain_caught_up_gating_and_run_counts() -> None:
    root = Path(__file__).parents[1]
    readme = (root / "README.md").read_text(encoding="utf-8").lower()
    workflows = "\n".join(
        path.read_text(encoding="utf-8").lower()
        for path in (root / ".github" / "workflows").glob("*.y*ml")
    )
    assert "caught_up" in readme
    assert "2026-04-01" in readme or "april 1, 2026" in readme
    assert re.search(r"latest\s+discovery\s+run", readme)
    assert re.search(r"confirmation\s+runs?", readme)
    assert re.search(r"retain\w*\s+(all|every)\s+runs?", readme)
    assert "caught_up" in workflows
    assert re.search(r"confirm\w*", workflows)
