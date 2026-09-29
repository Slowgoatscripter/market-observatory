"""Phase 2 acceptance checks for offline crypto collection and storage."""

from __future__ import annotations

import csv
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from decimal import Decimal
import gzip
import importlib
import json
import math
from pathlib import Path
import re
from typing import Any

import pytest


FIXTURES = Path(__file__).parent / "fixtures" / "crypto"
HOUR = datetime(2026, 9, 29, 20, tzinfo=timezone.utc)
COLLECTED_AT_MS = 1_790_714_400_000
NOTIONALS = (Decimal("100"), Decimal("1000"))
WARNING_BYTES = 250_000_000
MAX_BYTES = 300_000_000


def _collector_module():
    return importlib.import_module("observatory.crypto.collector")


def _payload(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _source_records(payload: Any) -> list[Any]:
    if isinstance(payload, list):
        return payload
    for key in ("events", "markets", "funding_rates", "candlesticks", "trades"):
        value = payload.get(key)
        if isinstance(value, list):
            return value
    return [payload]


def _identities(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            if key in {"ticker", "event_ticker", "market_ticker", "trade_id"}:
                found.add(str(child))
            else:
                found.update(_identities(child))
    elif isinstance(value, list):
        for child in value:
            found.update(_identities(child))
    return found


def _parsed_rows(module: Any, fixture: Path) -> list[dict[str, Any]]:
    return module.parse_fixture(
        fixture.stem,
        _payload(fixture),
        collected_at_ms=COLLECTED_AT_MS,
    )


def _vwap_for_quote_notional(
    levels: list[tuple[Decimal, Decimal]], notional: Decimal
) -> Decimal:
    remaining = notional
    base_filled = Decimal(0)
    for price, base_available in levels:
        quote_taken = min(remaining, price * base_available)
        base_filled += quote_taken / price
        remaining -= quote_taken
        if remaining == 0:
            return notional / base_filled
    raise AssertionError("generated book must have enough depth")


def _pilot_chunks(module: Any, root: Path) -> list[Path]:
    chunks: list[Path] = []
    for fixture in sorted(FIXTURES.glob("*.json")):
        chunks.append(
            module.write_hourly_chunk(
                root,
                source=fixture.stem,
                hour=HOUR,
                rows=_parsed_rows(module, fixture),
            )
        )
    return chunks


def test_every_captured_crypto_fixture_has_a_compact_scaled_parser() -> None:
    module = _collector_module()
    fixtures = sorted(FIXTURES.glob("*.json"))

    assert fixtures, "the captured crypto fixture set must not be empty"
    for fixture in fixtures:
        payload = _payload(fixture)
        rows = _parsed_rows(module, fixture)

        assert len(rows) == len(_source_records(payload)), fixture.name
        assert _identities(payload) <= {
            str(value) for row in rows for value in row.values() if value is not None
        }, fixture.name
        for row in rows:
            assert row["s"] == fixture.stem
            assert row["t"] == COLLECTED_AT_MS
            assert all(1 <= len(column) <= 4 for column in row)
            assert all(value is None or isinstance(value, (str, int)) for value in row.values())
            assert any(
                column != "t" and isinstance(value, int) and not isinstance(value, bool)
                for column, value in row.items()
            ), "each parsed record must retain numeric source data as a scaled integer"
            assert not any(
                isinstance(value, str) and re.fullmatch(r"-?\d+\.\d+", value)
                for value in row.values()
            ), "decimal observations must be stored as scaled integers"


def test_executable_bid_ask_prices_sweep_sides_books_and_required_notionals() -> None:
    module = _collector_module()
    generated_books: list[tuple[list[tuple[Decimal, Decimal]], list[tuple[Decimal, Decimal]]]] = []
    for midpoint, spread, quantities in (
        (Decimal("100"), Decimal("1"), ("0.6", "5", "8")),
        (Decimal("250"), Decimal("3"), ("0.25", "1.5", "4")),
        (Decimal("83.25"), Decimal("0.5"), ("1", "4", "20")),
    ):
        bid_prices = [midpoint - spread * offset for offset in (1, 2, 5)]
        ask_prices = [midpoint + spread * offset for offset in (1, 3, 6)]
        bids = list(zip(bid_prices, map(Decimal, quantities), strict=True))
        asks = list(zip(ask_prices, map(Decimal, reversed(quantities)), strict=True))
        generated_books.append((bids, asks))

    for bids, asks in generated_books:
        observed = module.executable_bid_ask(bids, asks, notionals=NOTIONALS)
        for notional in NOTIONALS:
            assert observed[notional]["bid"] == pytest.approx(
                _vwap_for_quote_notional(bids, notional)
            )
            assert observed[notional]["ask"] == pytest.approx(
                _vwap_for_quote_notional(asks, notional)
            )


def test_hourly_gzip_csv_chunks_are_one_per_source_compact_and_immutable(
    tmp_path: Path,
) -> None:
    module = _collector_module()
    fixtures = sorted(FIXTURES.glob("*.json"))
    chunks = _pilot_chunks(module, tmp_path)

    assert len(chunks) == len(fixtures)
    assert len(set(chunks)) == len(fixtures)
    assert sorted(tmp_path.rglob("*.csv.gz")) == sorted(chunks)
    before = {path: path.read_bytes() for path in chunks}
    for fixture, path in zip(fixtures, chunks, strict=True):
        assert path.suffixes[-2:] == [".csv", ".gz"]
        with gzip.open(path, mode="rt", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
        assert rows
        assert reader.fieldnames is not None
        assert all(1 <= len(column) <= 4 for column in reader.fieldnames)
        assert not any(
            re.fullmatch(r"-?\d+\.\d+", value)
            for row in rows
            for value in row.values()
            if value
        )

        with pytest.raises(FileExistsError):
            module.write_hourly_chunk(
                tmp_path,
                source=fixture.stem,
                hour=HOUR,
                rows=_parsed_rows(module, fixture),
            )
        assert path.read_bytes() == before[path]

    later = module.write_hourly_chunk(
        tmp_path,
        source=fixtures[0].stem,
        hour=HOUR + timedelta(hours=1),
        rows=_parsed_rows(module, fixtures[0]),
    )
    assert later not in chunks
    assert len(list(tmp_path.rglob("*.csv.gz"))) == len(fixtures) + 1
    assert {path: path.read_bytes() for path in chunks} == before


def test_funding_event_state_claims_each_event_once_across_restarts(tmp_path: Path) -> None:
    module = _collector_module()
    state_path = tmp_path / "funding-events.json"
    event_ids = [f"KXBTCPERP:{day:02d}:{hour:02d}" for day in range(3) for hour in (4, 12, 20)]

    state = module.FundingEventState(state_path)
    assert [state.claim(event_id) for event_id in event_ids] == [True] * len(event_ids)
    assert [state.claim(event_id) for event_id in reversed(event_ids)] == [False] * len(event_ids)

    reloaded = module.FundingEventState(state_path)
    assert [reloaded.claim(event_id) for event_id in event_ids] == [False] * len(event_ids)
    new_ids = [f"KXBTCPERP:new:{index}" for index in range(4)]
    assert [reloaded.claim(event_id) for event_id in new_ids] == [True] * len(new_ids)


def test_fixture_pilot_size_is_annualized_and_warning_boundary_is_exact(
    tmp_path: Path,
) -> None:
    module = _collector_module()
    chunks = _pilot_chunks(module, tmp_path)
    pilot_bytes = sum(path.stat().st_size for path in chunks)

    estimate = module.estimate_annual_bytes(chunks, pilot_hours=1)

    assert estimate == math.ceil(pilot_bytes * 24 * 365)
    assert estimate < MAX_BYTES
    for delta in (-1, 0, 1, 10_000_003):
        annual_bytes = WARNING_BYTES + delta
        assert module.needs_storage_warning(annual_bytes) is (delta > 0)


class _Clock:
    def __init__(self) -> None:
        self.now = 0.0
        self.sleeps: list[float] = []

    def __call__(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        assert seconds >= 0
        self.sleeps.append(seconds)
        self.now += seconds


def test_fifteen_minute_loop_stops_within_each_injected_time_budget() -> None:
    module = _collector_module()
    interval = 15 * 60
    budgets = sorted(
        {
            interval * multiple + offset
            for multiple in range(3)
            for offset in (1, interval - 1, interval)
        }
    )

    for budget in budgets:
        clock = _Clock()
        calls: list[float] = []
        completed = module.run_collection_loop(
            lambda: calls.append(clock()),
            interval_seconds=interval,
            time_budget_seconds=budget,
            clock=clock,
            sleeper=clock.sleep,
        )

        expected_calls = list(range(0, budget, interval))
        assert calls == expected_calls
        assert completed == len(expected_calls)
        assert clock.now == budget
        assert sum(clock.sleeps) == budget
        assert all(sleep <= interval for sleep in clock.sleeps)


def test_open_brackets_are_snapshotted_every_30_minutes_not_every_sample(tmp_path: Path) -> None:
    module = _collector_module()

    class Core:
        def __init__(self) -> None:
            self.event_calls = 0

        def get(self, path: str, params: dict | None = None):
            if path == "/events":
                self.event_calls += 1
                return {"events": []}
            return {"markets": []}

    core = Core()
    collector = module.CryptoCollector(tmp_path, kalshi=core, kalshi_core=core)
    start = datetime(2026, 9, 29, 21, 0, tzinfo=timezone.utc)
    calls = []
    for minutes in (0, 15, 30, 45, 60):
        now = start + timedelta(minutes=minutes)
        before = core.event_calls
        collector._collect_brackets(defaultdict(list), now, int(now.timestamp() * 1000))
        calls.append(core.event_calls - before)
    per_snapshot = len(module.BRACKET_SERIES)
    assert calls == [per_snapshot, 0, per_snapshot, 0, per_snapshot]
