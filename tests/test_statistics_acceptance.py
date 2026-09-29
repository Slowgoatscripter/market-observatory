"""Acceptance checks for the preregistration and inference safeguards."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from decimal import Decimal, ROUND_CEILING
import importlib
from pathlib import Path

import pytest


def _stats():
    return importlib.import_module("observatory.stats")


def _checks():
    return importlib.import_module("observatory.kalshi.checks")


def _expected_bh(p_values: list[float]) -> list[float]:
    count = len(p_values)
    order = sorted(range(count), key=p_values.__getitem__)
    adjusted = [0.0] * count
    running = 1.0
    for reverse_rank, index in enumerate(reversed(order), start=1):
        rank = count - reverse_rank + 1
        running = min(running, p_values[index] * count / rank)
        adjusted[index] = running
    return adjusted


def test_newest_thirty_percent_is_locked_for_confirmation() -> None:
    start = datetime(2024, 1, 1, tzinfo=timezone.utc)
    records = [
        {"id": f"r{i}", "settled_at": start + timedelta(days=i * i + i)}
        for i in range(20)
    ]

    discovery, confirmation = _stats().split_discovery_confirmation(
        list(reversed(records)), confirmation_fraction=0.30
    )

    assert len(discovery) == 14
    assert len(confirmation) == 6
    assert {row["id"] for row in confirmation} == {f"r{i}" for i in range(14, 20)}
    assert max(row["settled_at"] for row in discovery) < min(
        row["settled_at"] for row in confirmation
    )


def test_ledger_compacts_runs_locks_time_windows_and_adjusts_latest_discoveries(
    tmp_path: Path,
) -> None:
    stats = _stats()
    ledger = stats.HypothesisLedger(tmp_path / "hypotheses.jsonl")
    latest_p_values = [0.021, 0.18, 0.61]
    latest_run_ids = []
    for hypothesis, latest_p in enumerate(latest_p_values):
        for run, p_value in enumerate((0.8 - hypothesis / 10, latest_p)):
            entry = ledger.log_run(
                hypothesis_id=f"h{hypothesis}",
                phase="discovery",
                p_value=p_value,
                record_ids=[f"d-{hypothesis}-{run}-{index}" for index in range(3 + run)],
                settlement_times=[
                    datetime(2026, 3, 1 + hypothesis * 3 + run, tzinfo=timezone.utc).isoformat()
                ]
                * (3 + run),
            )
        latest_run_ids.append(entry["run_id"])

    with pytest.raises(stats.ConfirmationLockError, match="window|start|overlap"):
        ledger.log_run(
            hypothesis_id="h0",
            phase="confirmation",
            p_value=0.01,
            record_ids=["new-confirmation-id"],
            settlement_times=["2026-03-31T23:59:59+00:00"],
            caught_up=True,
        )

    entries = ledger.entries()
    assert len(entries) == 2 * len(latest_p_values)
    assert all("record_ids" not in entry for entry in entries)
    assert all(entry["record_count"] in {3, 4} for entry in entries)
    by_run = {entry["run_id"]: entry for entry in entries}
    assert [by_run[run_id]["q_value"] for run_id in latest_run_ids] == pytest.approx(
        _expected_bh(latest_p_values)
    )


def test_ask_side_fee_uses_quadratic_kalshi_fee_rounded_up() -> None:
    for contracts in [1, 2, 7, 19, 83]:
        for cents in [1, 7, 23, 50, 81, 97]:
            price = Decimal(cents) / Decimal(100)
            unrounded = Decimal("0.07") * contracts * price * (1 - price)
            expected = unrounded.quantize(Decimal("0.01"), rounding=ROUND_CEILING)

            assert _stats().kalshi_fee(contracts, price, side="ask") == expected


def test_clustered_interval_treats_event_not_contract_as_independent_unit() -> None:
    values: list[float] = []
    event_ids: list[str] = []
    for event in range(18):
        repeats = (2, 3, 5)[event % 3]
        event_value = -1.0 if event % 2 == 0 else 1.0
        values.extend([event_value] * repeats)
        event_ids.extend([f"e{event}"] * repeats)

    _, clustered_low, clustered_high = _stats().clustered_mean_ci(values, event_ids)
    _, naive_low, naive_high = _stats().clustered_mean_ci(
        values, [f"row{i}" for i in range(len(values))]
    )

    assert clustered_low < 0 < clustered_high
    assert clustered_high - clustered_low > naive_high - naive_low


def test_standard_checks_emit_each_required_finding_kind() -> None:
    start = datetime(2024, 1, 1, tzinfo=timezone.utc)
    records = [
        {
            "ticker": f"T{i}",
            "event_id": f"E{i // 3}",
            "yes_ask": 0.05 + (i % 18) * 0.05,
            "outcome": int((i * 7) % 11 < (i % 9)),
            "segment": ("economics", "politics", "sports")[i % 3],
            "listed_at": start + timedelta(days=i * 11),
            "settled_at": start + timedelta(days=i * 11 + 5),
            "weight": 1.0 + (i % 4) / 4,
        }
        for i in range(60)
    ]

    findings = _checks().run_standard_checks(records)

    assert {finding["check"] for finding in findings} >= {
        "calibration",
        "favorite_longshot",
        "segmented",
        "listing_drift",
    }
