"""Acceptance checks for the Phase 2 crypto analyses.

The checks deliberately exercise normalized, timestamped inputs.  Network access is
never needed; the only captured payloads used here live under ``tests/fixtures``.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from decimal import Decimal
import importlib
import json
import math
from pathlib import Path
from statistics import median, pstdev
from typing import Any

import pytest


FIXTURES = Path(__file__).parent / "fixtures" / "crypto"


def _crypto():
    return importlib.import_module("observatory.crypto.checks")


def _stats():
    return importlib.import_module("observatory.stats")


def _fixture(name: str) -> Any:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def _vwap(levels: list[list[Any]], notional: Decimal, *, quantity_is_base: bool) -> Decimal:
    remaining = notional
    base = Decimal(0)
    spent = Decimal(0)
    for raw_price, raw_quantity, *_ in levels:
        price = Decimal(str(raw_price))
        quantity = Decimal(str(raw_quantity))
        level_notional = price * quantity
        take_notional = min(remaining, level_notional)
        if not quantity_is_base:
            # Kalshi's quantity is contracts, but a contract's quoted price is
            # still its dollar notional for walking this book.
            take_notional = min(remaining, level_notional)
        spent += take_notional
        base += take_notional / price
        remaining -= take_notional
        if remaining == 0:
            break
    if remaining:
        raise AssertionError("fixture book is too shallow for requested notional")
    return spent / base


def test_basis_reports_mid_executable_distribution_persistence_and_cost_frequency() -> None:
    start = datetime(2026, 1, 1, tzinfo=timezone.utc)
    samples: list[dict[str, Any]] = []
    deltas = (-31, -9, 7, 22, 38)
    venue_mid_offsets = {"coinbase": Decimal("0"), "kraken": Decimal("0.17")}
    venue_half_spreads = {"coinbase": Decimal("0.03"), "kraken": Decimal("0.08")}
    for index, delta_bps in enumerate(deltas):
        perp_mid = Decimal("100") * (Decimal(1) + Decimal(delta_bps) / Decimal(10_000))
        perp_half_spread = Decimal("0.02") + Decimal(index % 2) / Decimal(100)
        spots: dict[str, dict[str, Decimal]] = {}
        for venue in venue_mid_offsets:
            spot_mid = Decimal("100") + venue_mid_offsets[venue]
            half_spread = venue_half_spreads[venue]
            spots[venue] = {"bid": spot_mid - half_spread, "ask": spot_mid + half_spread}
        samples.append(
            {
                "timestamp": start + timedelta(minutes=13 * index),
                "perp_bid": perp_mid - perp_half_spread,
                "perp_ask": perp_mid + perp_half_spread,
                "spots": spots,
            }
        )

    costs = {"coinbase": 11.0, "kraken": 17.0}
    result = _crypto().basis_summary(samples, full_round_trip_cost_bps=costs)

    assert set(result) == set(venue_mid_offsets)
    for venue, venue_result in result.items():
        expected_rows = []
        for sample in samples:
            spot = sample["spots"][venue]
            perp_mid = (sample["perp_bid"] + sample["perp_ask"]) / 2
            spot_mid = (spot["bid"] + spot["ask"]) / 2
            expected_rows.append(
                {
                    "mid_basis_bps": float((perp_mid / spot_mid - 1) * 10_000),
                    "long_executable_basis_bps": float(
                        (sample["perp_ask"] / spot["bid"] - 1) * 10_000
                    ),
                    "short_executable_basis_bps": float(
                        (sample["perp_bid"] / spot["ask"] - 1) * 10_000
                    ),
                }
            )
        assert len(venue_result["observations"]) == len(samples)
        for actual, expected in zip(venue_result["observations"], expected_rows, strict=True):
            assert actual["mid_basis_bps"] == pytest.approx(expected["mid_basis_bps"])
            assert actual["long_executable_basis_bps"] == pytest.approx(
                expected["long_executable_basis_bps"]
            )
            assert actual["short_executable_basis_bps"] == pytest.approx(
                expected["short_executable_basis_bps"]
            )

        mids = [row["mid_basis_bps"] for row in expected_rows]
        distribution = venue_result["distribution"]["mid_basis_bps"]
        assert distribution == pytest.approx(
            {
                "count": len(mids),
                "mean": sum(mids) / len(mids),
                "median": median(mids),
                "minimum": min(mids),
                "maximum": max(mids),
            }
        )
        same_sign = sum((left > 0) == (right > 0) for left, right in zip(mids, mids[1:]))
        assert venue_result["persistence"]["same_sign_transitions"] == same_sign
        assert venue_result["persistence"]["transition_count"] == len(mids) - 1

        executable_edges = [
            max(row["short_executable_basis_bps"], -row["long_executable_basis_bps"])
            for row in expected_rows
        ]
        expected_frequency = sum(edge > costs[venue] for edge in executable_edges) / len(
            executable_edges
        )
        assert venue_result["frequency_above_full_round_trip_cost"] == pytest.approx(
            expected_frequency
        )


def test_funding_estimate_enters_next_sample_and_only_settled_cash_is_credited() -> None:
    start = datetime(2026, 2, 1, tzinfo=timezone.utc)
    estimates = [Decimal("0.0011"), Decimal("-0.0003"), Decimal("0.0027"), Decimal("0.0004")]
    samples = [
        {"timestamp": start + timedelta(hours=index), "funding_estimate": estimate}
        for index, estimate in enumerate(estimates)
    ]
    settlements = [
        {"funding_time": start + timedelta(minutes=90), "cash_amount": Decimal("1.25")},
        {"funding_time": start + timedelta(hours=3, minutes=1), "cash_amount": Decimal("-0.40")},
    ]

    rows = _crypto().funding_carry(samples, settlements)

    assert rows[0]["active_estimate"] is None
    assert [float(row["active_estimate"]) for row in rows[1:]] == pytest.approx(
        [float(value) for value in estimates[:-1]]
    )
    assert [float(row["settled_funding_cash"]) for row in rows] == pytest.approx(
        [0, 0, 1.25, 1.25]
    )
    assert all(
        row["estimate_known_at"] is None or row["estimate_known_at"] < row["timestamp"]
        for row in rows
    )
    assert all(
        funding["funding_time"] <= row["timestamp"]
        for row in rows
        for funding in row["credited_settlements"]
    )


def test_named_fee_cases_are_applied_to_measured_100_and_1000_dollar_execution() -> None:
    kalshi = _fixture("kalshi_perps_orderbook.json")["orderbook"]
    coinbase = _fixture("coinbase_book_l2.json")
    schedules = _crypto().fee_schedules()

    assert set(schedules) == {"kalshi_perps", "coinbase_base", "coinbase_pessimistic"}
    expected_schedules = {
        "kalshi_perps": {"maker_bps": Decimal("2"), "taker_bps": Decimal("12")},
        "coinbase_base": {"maker_bps": Decimal("50"), "taker_bps": Decimal("90")},
        "coinbase_pessimistic": {
            "maker_bps": Decimal("60"),
            "taker_bps": Decimal("120"),
        },
    }
    for name, expected in expected_schedules.items():
        assert set(schedules[name]) == set(expected)
        assert {
            key: Decimal(str(value)) for key, value in schedules[name].items()
        } == expected

    result = _crypto().executable_spreads(
        kalshi,
        coinbase,
        contract_size=Decimal("0.0001"),
        notionals=(Decimal("100"), Decimal("1000")),
        fee_schedules=schedules,
    )
    # The fixtures intentionally have different price/quantity units.  Walking
    # both books catches midpoint substitution and top-of-book-only shortcuts.
    for notional in (Decimal("100"), Decimal("1000")):
        measured = result[notional]
        kalshi_buy_contract = _vwap(list(reversed(kalshi["asks"])), notional, quantity_is_base=False)
        kalshi_sell_contract = _vwap(list(reversed(kalshi["bids"])), notional, quantity_is_base=False)
        coinbase_buy = _vwap(coinbase["asks"], notional, quantity_is_base=True)
        coinbase_sell = _vwap(coinbase["bids"], notional, quantity_is_base=True)
        assert measured["kalshi_buy_price"] == pytest.approx(
            float(kalshi_buy_contract / Decimal("0.0001"))
        )
        assert measured["kalshi_sell_price"] == pytest.approx(
            float(kalshi_sell_contract / Decimal("0.0001"))
        )
        assert measured["coinbase_buy_price"] == pytest.approx(float(coinbase_buy))
        assert measured["coinbase_sell_price"] == pytest.approx(float(coinbase_sell))

        for case in ("coinbase_base", "coinbase_pessimistic"):
            expected_fee_bps = Decimal(
                str(schedules["kalshi_perps"]["taker_bps"])
            ) + Decimal(str(schedules[case]["taker_bps"]))
            assert measured["round_trip_cost_bps"][case] == pytest.approx(
                measured["gross_cross_venue_spread_bps"] + float(expected_fee_bps)
            )


def test_bracket_ladders_and_exclusive_sums_use_executable_prices_after_fees() -> None:
    directional = []
    probabilities = (Decimal("0.81"), Decimal("0.66"), Decimal("0.69"), Decimal("0.22"))
    for index, probability in enumerate(probabilities):
        directional.append(
            {
                "ticker": f"above-{index}",
                "strike": 80_000 + 500 * index,
                "yes_bid": probability - Decimal("0.01"),
                "yes_ask": probability + Decimal("0.01"),
                "buy_fee": Decimal("0.004") + Decimal(index) / Decimal("10000"),
                "sell_fee": Decimal("0.003") + Decimal(index) / Decimal("10000"),
            }
        )
    ladder = _crypto().analyze_bracket_group(directional, mutually_exclusive=False)
    assert ladder["monotonic"] is False
    assert ladder["monotonicity_violations"] == [("above-1", "above-2")]

    for count, ask_total, bid_total in (
        (5, Decimal("0.94"), Decimal("0.89")),
        (7, Decimal("0.96"), Decimal("1.08")),
    ):
        rows = []
        for index in range(count):
            weight = Decimal(index + 1) / Decimal(count * (count + 1) // 2)
            rows.append(
                {
                    "ticker": f"range-{count}-{index}",
                    "floor": 70_000 + 250 * index,
                    "cap": 70_249.99 + 250 * index,
                    "yes_ask": ask_total * weight,
                    "yes_bid": bid_total * weight,
                    "buy_fee": Decimal("0.003") * (index + 1),
                    "sell_fee": Decimal("0.002") * (index + 1),
                }
            )
        summary = _crypto().analyze_bracket_group(rows, mutually_exclusive=True)
        buy_cost = sum(row["yes_ask"] + row["buy_fee"] for row in rows)
        sell_proceeds = sum(row["yes_bid"] - row["sell_fee"] for row in rows)
        assert summary["sum_yes_asks"] == pytest.approx(float(ask_total))
        assert summary["sum_yes_bids"] == pytest.approx(float(bid_total))
        assert summary["buy_all_executable_after_fees"] is (buy_cost < 1)
        assert summary["sell_all_executable_after_fees"] is (sell_proceeds > 1)


def test_bracket_calibration_uses_only_prior_24h_volatility_and_scores_after_settlement() -> None:
    start = datetime(2026, 3, 2, tzinfo=timezone.utc)
    quote_times = [start + timedelta(days=offset) for offset in range(3)]
    probabilities = (0.17, 0.53, 0.86)
    outcomes = (0, 1, 1)
    candles: list[dict[str, Any]] = []
    quotes: list[dict[str, Any]] = []
    settlements: list[dict[str, Any]] = []
    expected_volatility: dict[str, float] = {}
    for quote_index, (quote_time, probability, outcome) in enumerate(
        zip(quote_times, probabilities, outcomes, strict=True)
    ):
        returns = []
        for interval in range(96):
            value = ((interval % 9) - 4) * (quote_index + 1) / 100_000
            returns.append(value)
            candles.append(
                {
                    "end_time": quote_time - timedelta(minutes=15 * (96 - interval)),
                    "log_return": value,
                }
            )
        # This extreme return is timestamped exactly at the quote.  Including it
        # is the deliberate discriminator for a <= look-ahead bug.
        candles.append({"end_time": quote_time, "log_return": 0.75})
        quote_id = f"q-{quote_index}"
        quotes.append(
            {
                "quote_id": quote_id,
                "quoted_at": quote_time,
                "yes_probability": probability,
            }
        )
        settlements.append(
            {
                "quote_id": quote_id,
                "settled_at": quote_time + timedelta(hours=7 + quote_index),
                "outcome": outcome,
            }
        )
        expected_volatility[quote_id] = pstdev(returns)

    scores = _crypto().score_bracket_calibration(quotes, candles, settlements)

    assert {row["quote_id"] for row in scores} == set(expected_volatility)
    for row, probability, outcome in zip(scores, probabilities, outcomes, strict=True):
        assert row["volatility_observations"] == 96
        assert row["volatility_window_hours"] == 24
        assert row["volatility_window_end"] < row["quoted_at"]
        assert row["volatility_24h"] == pytest.approx(expected_volatility[row["quote_id"]])
        assert row["settled_at"] > row["quoted_at"]
        assert row["brier_score"] == pytest.approx((probability - outcome) ** 2)
        expected_log_loss = -(
            outcome * math.log(probability) + (1 - outcome) * math.log(1 - probability)
        )
        assert row["log_loss"] == pytest.approx(expected_log_loss)


def test_crypto_hypotheses_reuse_phase1_ledger_bh_day_clusters_and_holdout(
    tmp_path: Path,
) -> None:
    crypto = _crypto()
    stats = _stats()
    ledger = stats.HypothesisLedger(tmp_path / "crypto-hypotheses.jsonl")
    observations: list[dict[str, Any]] = []
    discovery_start = datetime(2026, 1, 1, tzinfo=timezone.utc)
    confirmation_start = datetime(2026, 5, 1, tzinfo=timezone.utc)
    for hypothesis_index, hypothesis_id in enumerate(("basis:coinbase", "funding:carry")):
        for phase_start, days in ((discovery_start, 32), (confirmation_start, 31)):
            for day in range(days):
                value = ((day * (hypothesis_index + 3)) % 13 - 6) / 100
                repeats = 1 + day % 4
                for repeat in range(repeats):
                    observations.append(
                        {
                            "hypothesis_id": hypothesis_id,
                            "value": value,
                            "day": (phase_start + timedelta(days=day)).date().isoformat(),
                            "record_id": f"{hypothesis_id}-{phase_start:%m}-{day}-{repeat}",
                            "settled_at": phase_start + timedelta(days=day, minutes=repeat),
                        }
                    )

    discovery = crypto.summarize_crypto_hypotheses(
        observations, ledger=ledger, caught_up=False
    )
    assert {row["phase"] for row in discovery} == {"discovery"}
    assert all(row["independent_days"] == 32 for row in discovery)
    entries_after_discovery = ledger.entries()
    assert len(entries_after_discovery) == 2
    assert {entry["phase"] for entry in entries_after_discovery} == {"discovery"}

    confirmation = crypto.summarize_crypto_hypotheses(
        observations, ledger=ledger, caught_up=True
    )
    confirmed = [row for row in confirmation if row["phase"] == "confirmation"]
    assert len(confirmed) == 2
    assert all(row["independent_days"] == 31 for row in confirmed)
    assert {entry["phase"] for entry in ledger.entries()} == {"discovery", "confirmation"}

    for phase_rows in (discovery, confirmed):
        assert [row["q_value"] for row in phase_rows] == pytest.approx(
            stats.benjamini_hochberg([row["p_value"] for row in phase_rows])
        )
        for finding in phase_rows:
            phase_observations = [
                row
                for row in observations
                if row["hypothesis_id"] == finding["hypothesis_id"]
                and (
                    (finding["phase"] == "discovery" and row["settled_at"] < confirmation_start)
                    or (finding["phase"] == "confirmation" and row["settled_at"] >= confirmation_start)
                )
            ]
            expected = stats.clustered_mean_ci(
                [row["value"] for row in phase_observations],
                [row["day"] for row in phase_observations],
            )
            assert finding["estimate"] == pytest.approx(expected[0])
            assert finding["confidence_interval"] == pytest.approx(expected[1:])

    short_history = [row for row in observations if row["settled_at"] < discovery_start + timedelta(days=17)]
    not_tested = crypto.summarize_crypto_hypotheses(short_history, ledger=None, caught_up=False)
    assert not_tested
    assert all(row["status"] == "Not tested: only 17 independent days (needs 30)" for row in not_tested)
    assert all(row["tested"] is False for row in not_tested)
