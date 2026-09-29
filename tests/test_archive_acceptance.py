"""Acceptance checks for sampling, resumability, and fixed-horizon prices."""

from __future__ import annotations

from datetime import datetime, timezone
import importlib
import json
from pathlib import Path

import pytest


FIXTURES = Path(__file__).parent / "fixtures" / "kalshi"


def _archive_module():
    return importlib.import_module("observatory.kalshi.archive")


def test_monthly_sampling_is_deterministic_and_inverse_probability_weighted() -> None:
    for population_size, sample_size in [(17, 5), (31, 7), (53, 11)]:
        rows = [{"ticker": f"T{i:03d}"} for i in range(population_size)]
        sample = _archive_module().deterministic_sample(
            rows,
            sample_size=sample_size,
            seed="2026-01",
        )
        repeated = _archive_module().deterministic_sample(
            list(reversed(rows)),
            sample_size=sample_size,
            seed="2026-01",
        )

        assert [row["ticker"] for row in sample] == [row["ticker"] for row in repeated]
        assert len(sample) == sample_size
        assert len({row["ticker"] for row in sample}) == sample_size
        for row in sample:
            assert row["selection_probability"] == pytest.approx(sample_size / population_size)
            assert row["weight"] == pytest.approx(population_size / sample_size)


def test_month_archive_resumes_after_interruption_without_duplicates(tmp_path: Path) -> None:
    archive = _archive_module().MonthlyArchive(tmp_path)
    rows = [{"ticker": f"T{i:02d}"} for i in range(9)]

    def interrupted():
        for index, row in enumerate(rows):
            if index == 4:
                raise RuntimeError("simulated interruption")
            yield row

    with pytest.raises(RuntimeError, match="simulated interruption"):
        archive.ingest_month("2026-01", interrupted())
    result = archive.ingest_month("2026-01", iter(rows))

    assert [row["ticker"] for row in result] == [row["ticker"] for row in rows]
    assert len({row["ticker"] for row in result}) == len(rows)


def test_fixture_candles_extract_latest_ask_at_or_before_fixed_horizon() -> None:
    cases = [
        ("candlesticks_live.json", "close_dollars", 0.26),
        ("candlesticks_historical.json", "close", 0.66),
    ]
    for fixture_name, field, expected in cases:
        payload = json.loads((FIXTURES / fixture_name).read_text(encoding="utf-8"))
        candle_ts = payload["candlesticks"][0]["end_period_ts"]
        target = datetime.fromtimestamp(candle_ts + 30 * 60, tz=timezone.utc)

        observed = _archive_module().extract_fixed_horizon_price(
            payload["candlesticks"],
            target=target,
            side="yes_ask",
        )

        assert observed == pytest.approx(expected)
        assert payload["candlesticks"][0]["yes_ask"][field] == f"{expected:.4f}"
