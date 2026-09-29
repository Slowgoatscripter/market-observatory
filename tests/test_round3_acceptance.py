"""Offline acceptance checks for append-only Round 3 archive storage."""

from __future__ import annotations

import csv
from datetime import datetime, timedelta, timezone
import gzip
import importlib
import json
from pathlib import Path
import re
import tomllib
from typing import Any

import pytest


UTC = timezone.utc
HORIZONS = (
    "close_minus_1h",
    "close_minus_1d",
    "close_minus_7d",
    "open_plus_1h",
    "open_plus_24h",
)
PRICE_MEASURES = ("last_trade", "yes_bid", "yes_ask", "spread")
CORE_COLUMNS = {
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
}
HORIZON_COLUMNS = {
    f"{horizon}_{measure}"
    for horizon in HORIZONS
    for measure in (*PRICE_MEASURES, "source_timestamp")
}
EXPECTED_COLUMNS = CORE_COLUMNS | HORIZON_COLUMNS


def _archive():
    return importlib.import_module("observatory.kalshi.archive")


def _checks():
    return importlib.import_module("observatory.kalshi.checks")


def _row(ticker: str, *, value: float = 0.123456, volume: float = 17.0) -> dict[str, Any]:
    row: dict[str, Any] = {
        "ticker": ticker,
        "event_ticker": f"EVENT-{ticker}",
        "series_ticker": "SERIES",
        "category": "Economics",
        "frequency": "monthly",
        "open_time": "2026-01-02T03:04:05.987654Z",
        "close_time": "2026-01-03T04:05:06.876543Z",
        "settlement_time": "2026-01-03T04:06:07.765432Z",
        "result": "yes",
        "volume": volume,
        "sampling_weight": 1.0,
    }
    for index, horizon in enumerate(HORIZONS):
        for measure in PRICE_MEASURES:
            row[f"{horizon}_{measure}"] = value + index / 100
        row[f"{horizon}_source_timestamp"] = 1_767_326_400 + index * 3_600
    # These former duplicate/metadata fields must not enlarge each archived row.
    row.update(
        selection_probability=1.0,
        weight=1.0,
        fee_type="quadratic",
        fee_multiplier=1.0,
    )
    return row


def _read_gzip_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or ()), list(reader)


def test_each_run_creates_one_immutable_compact_gzip_csv_chunk(tmp_path: Path) -> None:
    store = _archive().MonthlyArchive(tmp_path)
    first_start = datetime(2026, 9, 29, 12, 34, 56, tzinfo=UTC)
    first_path = store.write_chunk(
        [_row(f"T-{index}", value=(index + 1) / 7) for index in range(3)],
        run_started_at=first_start,
    )

    assert first_path == tmp_path / "chunks" / "20260929T123456Z.csv.gz"
    assert list((tmp_path / "chunks").glob("*.csv.gz")) == [first_path]
    original_bytes = first_path.read_bytes()
    header, rows = _read_gzip_csv(first_path)
    assert set(header) == EXPECTED_COLUMNS
    assert len(rows) == 3
    assert all(re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", rows[0][name]) for name in ("open_time", "close_time", "settlement_time"))
    assert rows[0]["volume"] == "17"
    assert rows[0]["is_mention"] == "0"
    for horizon in HORIZONS:
        assert rows[0][f"{horizon}_last_trade"] == f"{float(rows[0][f'{horizon}_last_trade']):.4f}"
        assert rows[0][f"{horizon}_source_timestamp"]

    second_path = store.write_chunk(
        [_row("T-later")],
        run_started_at=first_start + timedelta(seconds=37),
    )
    assert second_path.name == "20260929T123533Z.csv.gz"
    assert len(list((tmp_path / "chunks").glob("*.csv.gz"))) == 2
    assert first_path.read_bytes() == original_bytes
    assert not list(tmp_path.rglob("*.jsonl"))
    assert not list(tmp_path.rglob("*.parquet"))


def test_loader_deduplicates_by_ticker_using_the_newest_chunk(tmp_path: Path) -> None:
    store = _archive().MonthlyArchive(tmp_path)
    start = datetime(2026, 8, 1, tzinfo=UTC)
    store.write_chunk([_row("DUP", value=0.11111), _row("OLD-ONLY")], run_started_at=start)
    store.write_chunk([_row("DUP", value=0.88888), _row("NEW-ONLY")], run_started_at=start + timedelta(days=1))

    loaded = {row["ticker"]: row for row in _checks().load_archive_rows(tmp_path)}
    assert set(loaded) == {"DUP", "OLD-ONLY", "NEW-ONLY"}
    assert float(loaded["DUP"]["close_minus_1h_last_trade"]) == pytest.approx(0.8889)


def test_sports_uses_the_same_deterministic_one_percent_event_sample() -> None:
    module = _archive()
    series = {
        "SPORT": {"category": "Sports", "frequency": "weekly"},
        "OTHER": {"category": "Politics", "frequency": "weekly"},
    }
    events = [f"E-{index:05d}" for index in range(2_000)]
    sports = [
        {
            "ticker": f"SPORT-{event}-{contract}",
            "event_ticker": event,
            "series_ticker": "SPORT",
        }
        for event in events
        for contract in range(2)
    ]
    others = [
        {"ticker": f"OTHER-{index}", "event_ticker": f"O-{index}", "series_ticker": "OTHER"}
        for index in range(137)
    ]

    selected = module.apply_sampling(
        sports + others,
        series_by_ticker=series,
        seed=module.FAST_SAMPLE_SEED,
        sample_rate=0.01,
    )
    selected_sports = [row for row in selected if row["series_ticker"] == "SPORT"]
    expected_events = {
        event
        for event in events
        if module.event_is_selected(event, seed=module.FAST_SAMPLE_SEED, sample_rate=0.01)
    }
    assert {row["event_ticker"] for row in selected_sports} == expected_events
    assert len(selected_sports) == 2 * len(expected_events)
    assert expected_events and len(expected_events) < len(events)
    assert all(row["sampling_weight"] == pytest.approx(100) for row in selected_sports)
    assert len([row for row in selected if row["series_ticker"] == "OTHER"]) == len(others)


def test_series_catalog_is_never_saved_in_archive_state(tmp_path: Path) -> None:
    class CatalogClient:
        def series_list(self):
            for index in range(23):
                yield {
                    "ticker": f"S-{index}",
                    "category": "Economics",
                    "frequency": "monthly",
                    "fee_type": "quadratic",
                    "fee_multiplier": 1,
                }

    store = _archive().MonthlyArchive(tmp_path)
    state = {"caught_up": False, "finished_series": [], "series": {}, "metrics": {}}
    catalog = _archive().ArchiveCollector(CatalogClient(), store).load_series_catalog(state)
    store.save_state(state)

    assert len(catalog) == 23
    persisted = json.loads((tmp_path / "archive-state.json").read_text(encoding="utf-8"))
    assert "series_catalog" not in json.dumps(persisted)
    committed = json.loads((Path(__file__).parents[1] / "data" / "kalshi" / "archive-state.json").read_text(encoding="utf-8"))
    assert "series_catalog" not in json.dumps(committed)


def test_chunk_byte_metrics_are_exact_and_cumulative(tmp_path: Path) -> None:
    store = _archive().MonthlyArchive(tmp_path)
    start = datetime(2026, 6, 1, tzinfo=UTC)
    first = store.write_chunk([_row(f"A-{index}") for index in range(5)], run_started_at=start)
    second = store.write_chunk([_row(f"B-{index}") for index in range(7)], run_started_at=start + timedelta(hours=1))
    metrics = store.load_state()["metrics"]

    assert metrics["rows_written"] == 7
    assert metrics["chunk_bytes"] == second.stat().st_size
    assert metrics["cumulative_rows_written"] == 12
    assert metrics["cumulative_chunk_bytes"] == first.stat().st_size + second.stat().st_size


def test_dependencies_documentation_and_workflow_match_chunk_budget() -> None:
    root = Path(__file__).parents[1]
    project = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))
    dependencies = " ".join(project["project"].get("dependencies", ())).lower()
    readme = (root / "README.md").read_text(encoding="utf-8").lower()
    workflow = "\n".join(
        path.read_text(encoding="utf-8").lower()
        for path in (root / ".github" / "workflows").glob("*.y*ml")
    )

    assert "pyarrow" not in dependencies
    assert "csv.gz" in readme and "append-only" in readme
    assert "sports" in readme and "1%" in readme and "weight 100" in readme
    assert re.search(r"300\s*mb", readme)
    combined = readme + "\n" + workflow
    assert re.search(r"250\s*mb", combined)
    assert "chunk" in workflow and "byte" in workflow and "row" in workflow
