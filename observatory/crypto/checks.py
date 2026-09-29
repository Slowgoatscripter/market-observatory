"""Honest, read-only analyses for the Phase 2 crypto observer.

The small public functions are intentionally useful with normalized in-memory
records as well as the collector's compact CSV chunks.  All timestamps are UTC,
all decisions use information strictly available at the time, and inferential
results reuse the phase-one statistical safeguards.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import math
from collections import defaultdict
from collections.abc import Iterable, Mapping, Sequence
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path
from statistics import NormalDist, mean, median, pstdev
from typing import Any
from uuid import uuid4

from observatory.stats import (
    ConfirmationLockError,
    HypothesisLedger,
    benjamini_hochberg,
    clustered_mean_ci,
    kalshi_fee,
    split_discovery_confirmation,
)


MIN_INDEPENDENT_DAYS = 30
PHASE2_CONFIRMATION_START = datetime(2027, 1, 1, tzinfo=timezone.utc)
SCALE = Decimal("1000000")
RATE_SCALE = Decimal("1000000000000")


class CryptoHypothesisLedger(HypothesisLedger):
    """Phase 2 ledger with its own prospective calendar holdout.

    Storage deliberately matches :class:`HypothesisLedger`: append-only JSONL,
    hashed record IDs, actual observation ranges, and phase-separated BH values.
    Only the calendar lock differs because crypto collection launched after the
    Phase 1 confirmation boundary.
    """

    def __init__(self, path: str | Path, boundary: datetime = PHASE2_CONFIRMATION_START):
        super().__init__(path)
        self.boundary = _time(boundary)

    def log_run(
        self, *, hypothesis_id: str, phase: str, p_value: float,
        record_ids: Iterable[str], settlement_times: Iterable[Any] = (),
        caught_up: bool = False, **metadata: Any,
    ) -> dict[str, Any]:
        if phase not in {"discovery", "confirmation"}:
            raise ValueError("phase must be 'discovery' or 'confirmation'")
        ids = [str(value) for value in record_ids]
        times = [_time(value) for value in settlement_times]
        if len(times) != len(ids):
            raise ValueError("settlement_times must contain one value per record")
        if phase == "discovery" and times and max(times) >= self.boundary:
            raise ConfirmationLockError("Phase 2 discovery overlaps its fixed confirmation window")
        if phase == "confirmation":
            if not self.has_discovery(hypothesis_id):
                raise ConfirmationLockError("confirmation is locked until discovery is recorded")
            if self.has_confirmation(hypothesis_id):
                raise ConfirmationLockError("confirmation has already been run")
            if not caught_up:
                raise ConfirmationLockError("confirmation is locked until explicitly caught up")
            if not times or min(times) < self.boundary:
                raise ConfirmationLockError("confirmation overlaps the Phase 2 discovery window")
            if max(times) > datetime.now(timezone.utc):
                raise ConfirmationLockError("confirmation cannot include future observations")
        p = float(p_value)
        if not math.isfinite(p) or not 0 <= p <= 1:
            raise ValueError("p_value must be finite and between zero and one")
        entry = {
            "run_id": uuid4().hex,
            "recorded_at": datetime.now(timezone.utc).isoformat(),
            "hypothesis_id": hypothesis_id,
            "phase": phase,
            "p_value": p,
            "record_count": len(ids),
            "record_ids_sha256": hashlib.sha256("\n".join(sorted(ids)).encode()).hexdigest(),
            "min_settlement_time": min(times).isoformat() if times else None,
            "max_settlement_time": max(times).isoformat() if times else None,
            "confirmation_start": self.boundary.isoformat(),
            **metadata,
        }
        entry.pop("q_value", None)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8", newline="\n") as stream:
            stream.write(json.dumps(entry, sort_keys=True, separators=(",", ":")) + "\n")
            stream.flush()
        return next(row for row in self.entries() if row["run_id"] == entry["run_id"])


def _decimal(value: Any, default: Decimal | None = None) -> Decimal:
    if value in (None, ""):
        if default is None:
            raise ValueError("missing decimal")
        return default
    return Decimal(str(value))


def _time(value: Any) -> datetime:
    if isinstance(value, datetime):
        result = value
    elif isinstance(value, (int, float, Decimal)) or (
        isinstance(value, str) and value.strip().lstrip("-").replace(".", "", 1).isdigit()
    ):
        raw = float(value)
        # Collector timestamps may be seconds, milliseconds, or microseconds.
        while abs(raw) > 10_000_000_000:
            raw /= 1000
        result = datetime.fromtimestamp(raw, timezone.utc)
    else:
        result = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    return result.astimezone(timezone.utc) if result.tzinfo else result.replace(tzinfo=timezone.utc)


def _distribution(values: Sequence[float]) -> dict[str, float | int]:
    return {
        "count": len(values),
        "mean": mean(values) if values else math.nan,
        "median": median(values) if values else math.nan,
        "minimum": min(values) if values else math.nan,
        "maximum": max(values) if values else math.nan,
    }


def basis_summary(
    samples: Iterable[Mapping[str, Any]],
    *,
    full_round_trip_cost_bps: Mapping[str, float] | None = None,
) -> dict[str, dict[str, Any]]:
    """Describe perp/spot basis using both midpoint and executable quotes."""

    costs = dict(full_round_trip_cost_bps or {})
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for sample in sorted(samples, key=lambda row: _time(row["timestamp"])):
        perp_bid, perp_ask = _decimal(sample["perp_bid"]), _decimal(sample["perp_ask"])
        perp_mid = (perp_bid + perp_ask) / 2
        for venue, spot in sample.get("spots", {}).items():
            spot_bid, spot_ask = _decimal(spot["bid"]), _decimal(spot["ask"])
            if min(perp_bid, perp_ask, spot_bid, spot_ask) <= 0:
                continue
            spot_mid = (spot_bid + spot_ask) / 2
            row = {
                "timestamp": _time(sample["timestamp"]),
                "mid_basis_bps": float((perp_mid / spot_mid - 1) * 10_000),
                "long_executable_basis_bps": float((perp_ask / spot_bid - 1) * 10_000),
                "short_executable_basis_bps": float((perp_bid / spot_ask - 1) * 10_000),
            }
            # If the collector retained both depth-walk books, use executable
            # prices on both legs (never a top-of-book substitute).
            perp_book = sample.get("perp_book", {})
            for notional in (100, 1000):
                perp_buy = perp_book.get(f"ask_{notional}")
                perp_sell = perp_book.get(f"bid_{notional}")
                spot_sell = spot.get(f"bid_{notional}")
                spot_buy = spot.get(f"ask_{notional}")
                if perp_buy not in (None, "") and spot_sell not in (None, ""):
                    row[f"long_executable_{notional}_bps"] = float((_decimal(perp_buy) / _decimal(spot_sell) - 1) * 10_000)
                if perp_sell not in (None, "") and spot_buy not in (None, ""):
                    row[f"short_executable_{notional}_bps"] = float((_decimal(perp_sell) / _decimal(spot_buy) - 1) * 10_000)
            grouped[str(venue)].append(row)

    result: dict[str, dict[str, Any]] = {}
    for venue, rows in grouped.items():
        mids = [row["mid_basis_bps"] for row in rows]
        transitions = list(zip(mids, mids[1:]))
        same_sign = sum((left > 0) == (right > 0) for left, right in transitions)
        if len(mids) > 1 and pstdev(mids) > 0:
            center = mean(mids)
            left = [value - center for value in mids[:-1]]
            right = [value - center for value in mids[1:]]
            denominator = math.sqrt(sum(v * v for v in left) * sum(v * v for v in right))
            autocorrelation = sum(a * b for a, b in zip(left, right)) / denominator if denominator else math.nan
        else:
            autocorrelation = math.nan
        edges = [max(row["short_executable_basis_bps"], -row["long_executable_basis_bps"]) for row in rows]
        cost = float(costs.get(venue, math.inf))
        result[venue] = {
            "observations": rows,
            "distribution": {
                "mid_basis_bps": _distribution(mids),
                "long_executable_basis_bps": _distribution([row["long_executable_basis_bps"] for row in rows]),
                "short_executable_basis_bps": _distribution([row["short_executable_basis_bps"] for row in rows]),
            },
            "persistence": {
                "lag_1_autocorrelation": autocorrelation,
                "same_sign_transitions": same_sign,
                "transition_count": len(transitions),
            },
            "full_round_trip_cost_bps": None if math.isinf(cost) else cost,
            "frequency_above_full_round_trip_cost": (
                sum(edge > cost for edge in edges) / len(edges) if edges else math.nan
            ),
        }
        for notional in (100, 1000):
            long_key, short_key = f"long_executable_{notional}_bps", f"short_executable_{notional}_bps"
            depth_rows = [row for row in rows if long_key in row and short_key in row]
            if depth_rows:
                result[venue]["distribution"][long_key] = _distribution([row[long_key] for row in depth_rows])
                result[venue]["distribution"][short_key] = _distribution([row[short_key] for row in depth_rows])
                depth_edges = [max(row[short_key], -row[long_key]) for row in depth_rows]
                result[venue][f"frequency_above_full_round_trip_cost_{notional}"] = sum(edge > cost for edge in depth_edges) / len(depth_edges)
    return result


def funding_carry(
    samples: Iterable[Mapping[str, Any]], settlements: Iterable[Mapping[str, Any]]
) -> list[dict[str, Any]]:
    """Align estimates and settled cash without using either prematurely.

    The estimate observed in sample *i* first becomes active in sample *i+1*.
    ``settled_funding_cash`` is cumulative settled cash known by each sample.
    """

    ordered = sorted(samples, key=lambda row: _time(row["timestamp"]))
    funding = sorted(settlements, key=lambda row: _time(row["funding_time"]))
    rows: list[dict[str, Any]] = []
    for index, sample in enumerate(ordered):
        timestamp = _time(sample["timestamp"])
        active = ordered[index - 1].get("funding_estimate") if index else None
        known_at = _time(ordered[index - 1]["timestamp"]) if index and active is not None else None
        credited = [item for item in funding if _time(item["funding_time"]) <= timestamp]
        rows.append(
            {
                **dict(sample),
                "timestamp": timestamp,
                "active_estimate": active,
                "estimate_known_at": known_at,
                "credited_settlements": credited,
                "settled_funding_cash": sum((_decimal(item.get("cash_amount"), Decimal(0)) for item in credited), Decimal(0)),
            }
        )
    return rows


def simulate_funding_carry(
    samples: Iterable[Mapping[str, Any]],
    settlements: Iterable[Mapping[str, Any]],
    *,
    notional: Decimal = Decimal("100"),
    spread_costs: Mapping[str, Decimal | float] | None = None,
) -> dict[str, dict[str, float | int]]:
    """Simulate a delta-hedged carry decision under every disclosed fee case.

    An estimate's sign chooses the position only from the following sample.
    Each later, not-previously-used settlement closes that position. Positive
    funding is treated as cash to a short perp; negative funding as cash to a
    long perp. Entry and exit each charge both venue fees. ``spread_costs`` are
    dollar costs per round trip keyed by ``"100"``/``"1000"`` or by case name.
    """

    aligned = funding_carry(samples, [])
    events = sorted(settlements, key=lambda row: _time(row["funding_time"]))
    schedules = fee_schedules()
    spread_costs = spread_costs or {}
    results: dict[str, dict[str, float | int]] = {}
    for liquidity in ("maker", "taker"):
        for spot_case in ("coinbase_base", "coinbase_pessimistic"):
            key = f"{liquidity}:{spot_case}"
            fee_bps = schedules["kalshi_perps"][f"{liquidity}_bps"] + schedules[spot_case][f"{liquidity}_bps"]
            round_trip_fees = notional * Decimal(2) * fee_bps / Decimal(10_000)
            configured_spread = _decimal(spread_costs.get(key, spread_costs.get(str(notional), 0)), Decimal(0))
            equity = Decimal(0)
            peak = Decimal(0)
            worst = Decimal(0)
            trades = 0
            measured_spread_total = Decimal(0)
            for event in events:
                funding_time = _time(event["funding_time"])
                eligible = [row for row in aligned if row["timestamp"] < funding_time and row.get("active_estimate") is not None]
                if not eligible:
                    continue
                decision = eligible[-1]
                estimate = _decimal(decision["active_estimate"])
                if estimate == 0:
                    continue
                realized = _decimal(event.get("funding_rate", event.get("cash_amount", 0)), Decimal(0))
                funding_cash = notional * abs(realized) if (estimate > 0) == (realized > 0) else -notional * abs(realized)
                spread = _decimal(decision.get("round_trip_spread_cost", configured_spread), configured_spread)
                equity += funding_cash - round_trip_fees - spread
                measured_spread_total += spread
                peak = max(peak, equity)
                worst = max(worst, peak - equity)
                trades += 1
            results[key] = {
                "net_per_100": float(equity * Decimal(100) / notional),
                "worst_drawdown": float(worst * Decimal(100) / notional),
                "trades": trades,
                "entry_and_exit_fee_bps": float(2 * fee_bps),
                "mean_measured_spread_cost": float(measured_spread_total / trades) if trades else math.nan,
                "measured_spread_cost": float(measured_spread_total / trades) if trades else math.nan,
            }
    return results


def fee_schedules() -> dict[str, dict[str, Decimal]]:
    return {
        "kalshi_perps": {"maker_bps": Decimal("2"), "taker_bps": Decimal("12")},
        "coinbase_base": {"maker_bps": Decimal("50"), "taker_bps": Decimal("90")},
        "coinbase_pessimistic": {"maker_bps": Decimal("60"), "taker_bps": Decimal("120")},
    }


def _vwap(levels: Iterable[Sequence[Any]], notional: Decimal) -> Decimal:
    remaining, base, spent = notional, Decimal(0), Decimal(0)
    for level in levels:
        price, quantity = _decimal(level[0]), _decimal(level[1])
        take = min(remaining, price * quantity)
        if take <= 0:
            continue
        base += take / price
        spent += take
        remaining -= take
        if remaining == 0:
            return spent / base
    raise ValueError(f"book has insufficient depth for ${notional}")


def executable_spreads(
    kalshi_book: Mapping[str, Any],
    coinbase_book: Mapping[str, Any],
    *,
    contract_size: Decimal,
    notionals: Iterable[Decimal] = (Decimal("100"), Decimal("1000")),
    fee_schedules: Mapping[str, Mapping[str, Any]] | None = None,
) -> dict[Decimal, dict[str, Any]]:
    """Walk both captured books and disclose fee-inclusive crossing cost."""

    schedules = fee_schedules or globals()["fee_schedules"]()
    result: dict[Decimal, dict[str, Any]] = {}
    for raw_notional in notionals:
        notional = _decimal(raw_notional)
        # Kalshi's fixture/API is worst-to-best, unlike Coinbase.
        k_buy_contract = _vwap(reversed(kalshi_book["asks"]), notional)
        k_sell_contract = _vwap(reversed(kalshi_book["bids"]), notional)
        k_buy, k_sell = k_buy_contract / contract_size, k_sell_contract / contract_size
        c_buy = _vwap(coinbase_book["asks"], notional)
        c_sell = _vwap(coinbase_book["bids"], notional)
        gross = float(((k_buy / c_sell - 1) + (c_buy / k_sell - 1)) * Decimal(10_000))
        costs: dict[str, float] = {}
        for case in ("coinbase_base", "coinbase_pessimistic"):
            fees = _decimal(schedules["kalshi_perps"]["taker_bps"]) + _decimal(schedules[case]["taker_bps"])
            costs[case] = gross + float(fees)
        result[notional] = {
            "kalshi_buy_price": float(k_buy),
            "kalshi_sell_price": float(k_sell),
            "coinbase_buy_price": float(c_buy),
            "coinbase_sell_price": float(c_sell),
            "gross_cross_venue_spread_bps": gross,
            "round_trip_cost_bps": costs,
        }
    return result


def _row_fee(row: Mapping[str, Any], kind: str) -> Decimal:
    explicit = row.get(f"{kind}_fee")
    if explicit not in (None, ""):
        return _decimal(explicit)
    price = _decimal(row["yes_ask" if kind == "buy" else "yes_bid"])
    # One-contract executable package. Phase-one rounds each order once.
    return kalshi_fee(1, price)


def analyze_bracket_group(
    markets: Iterable[Mapping[str, Any]], *, mutually_exclusive: bool
) -> dict[str, Any]:
    rows = list(markets)
    ordered = sorted(rows, key=lambda row: _decimal(row.get("strike", row.get("floor", 0))))
    violations = [
        (str(left.get("ticker")), str(right.get("ticker")))
        for left, right in zip(ordered, ordered[1:])
        if _decimal(right["yes_bid"]) > _decimal(left["yes_bid"])
        or _decimal(right["yes_ask"]) > _decimal(left["yes_ask"])
    ] if not mutually_exclusive else []
    asks = sum((_decimal(row["yes_ask"]) for row in rows), Decimal(0))
    bids = sum((_decimal(row["yes_bid"]) for row in rows), Decimal(0))
    buy_cost = sum((_decimal(row["yes_ask"]) + _row_fee(row, "buy") for row in rows), Decimal(0))
    sell_proceeds = sum((_decimal(row["yes_bid"]) - _row_fee(row, "sell") for row in rows), Decimal(0))
    return {
        "market_count": len(rows),
        "mutually_exclusive": mutually_exclusive,
        "monotonic": not violations,
        "monotonicity_violations": violations,
        "sum_yes_asks": float(asks),
        "sum_yes_bids": float(bids),
        "buy_all_cost_after_fees": float(buy_cost),
        "sell_all_proceeds_after_fees": float(sell_proceeds),
        "buy_all_executable_after_fees": mutually_exclusive and buy_cost < 1,
        "sell_all_executable_after_fees": mutually_exclusive and sell_proceeds > 1,
    }


def _normal_cdf(value: float) -> float:
    return NormalDist().cdf(value)


def _lognormal_probability(quote: Mapping[str, Any], sigma_24h: float) -> float | None:
    """Risk-neutral-free descriptive probability under zero-drift lognormal."""

    try:
        spot = float(quote["spot_price"])
        expiry = _time(quote.get("close_time", quote["quoted_at"]))
        quoted = _time(quote["quoted_at"])
    except (KeyError, ValueError, TypeError):
        return None
    fraction = max(0.0, (expiry - quoted).total_seconds() / (24 * 3600))
    # The tested ``volatility_24h`` statistic is the dispersion of 15-minute
    # returns in the prior-day window. Scale that interval volatility by the
    # number of 15-minute periods remaining to expiry.
    sigma = sigma_24h * math.sqrt(fraction * 96)
    if spot <= 0 or sigma <= 0:
        return None
    def below(strike: float) -> float:
        return _normal_cdf((math.log(strike / spot) + 0.5 * sigma * sigma) / sigma)
    if quote.get("floor") not in (None, "") or quote.get("cap") not in (None, ""):
        lower = 0.0 if quote.get("floor") in (None, "") else below(float(quote["floor"]))
        upper = 1.0 if quote.get("cap") in (None, "") else below(float(quote["cap"]))
        return min(1.0, max(0.0, upper - lower))
    strike = float(quote["strike"])
    return 1 - below(strike) if str(quote.get("direction", "above")).lower() in {"above", "greater", "gt"} else below(strike)


def score_bracket_calibration(
    quotes: Iterable[Mapping[str, Any]],
    candles: Iterable[Mapping[str, Any]],
    settlements: Iterable[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    """Use the strictly-prior 24h volatility window, then score settled quotes."""

    candle_rows = [dict(row, end_time=_time(row["end_time"])) for row in candles]
    settled = {str(row["quote_id"]): row for row in settlements}
    result: list[dict[str, Any]] = []
    for quote in sorted(quotes, key=lambda row: _time(row["quoted_at"])):
        quote_id, quoted_at = str(quote["quote_id"]), _time(quote["quoted_at"])
        settlement = settled.get(quote_id)
        if settlement is None or _time(settlement["settled_at"]) <= quoted_at:
            continue
        # Real candles have one close per interval.  Defensive de-duplication is
        # important when adjacent fixture/download windows share a boundary;
        # the later downloaded observation is authoritative for that close.
        prior_by_time = {
            row["end_time"]: row
            for row in candle_rows
            if quoted_at - timedelta(hours=24) <= row["end_time"] < quoted_at
        }
        prior = [prior_by_time[key] for key in sorted(prior_by_time)]
        returns = [float(row["log_return"]) for row in prior]
        if not returns:
            continue
        volatility = pstdev(returns)
        probability = float(quote["yes_probability"])
        outcome = int(settlement["outcome"])
        clipped = min(1 - 1e-15, max(1e-15, probability))
        model_probability = _lognormal_probability(quote, volatility)
        model_clipped = None if model_probability is None else min(1 - 1e-15, max(1e-15, model_probability))
        result.append(
            {
                **dict(quote),
                "quote_id": quote_id,
                "quoted_at": quoted_at,
                "settled_at": _time(settlement["settled_at"]),
                "outcome": outcome,
                "volatility_24h": volatility,
                "volatility_observations": len(returns),
                "volatility_window_hours": 24,
                "volatility_window_start": quoted_at - timedelta(hours=24),
                "volatility_window_end": max(row["end_time"] for row in prior),
                "lognormal_probability": model_probability,
                "brier_score": (probability - outcome) ** 2,
                "log_loss": -(outcome * math.log(clipped) + (1 - outcome) * math.log(1 - clipped)),
                "lognormal_brier_score": None if model_probability is None else (model_probability - outcome) ** 2,
                "lognormal_log_loss": None if model_clipped is None else -(outcome * math.log(model_clipped) + (1 - outcome) * math.log(1 - model_clipped)),
            }
        )
    return result


def _p_value(values: Sequence[float], days: Sequence[str]) -> float:
    by_day: dict[str, list[float]] = defaultdict(list)
    for value, day in zip(values, days):
        by_day[day].append(float(value))
    clusters = [mean(group) for group in by_day.values()]
    if len(clusters) < 2 or pstdev(clusters) == 0:
        return 1.0
    z = abs(mean(clusters)) / (pstdev(clusters) / math.sqrt(len(clusters)))
    return min(1.0, 2 * (1 - NormalDist().cdf(z)))


def summarize_crypto_hypotheses(
    observations: Iterable[Mapping[str, Any]],
    *,
    ledger: HypothesisLedger | str | Path | None,
    caught_up: bool,
    confirmation_start: datetime | None = None,
) -> list[dict[str, Any]]:
    """Apply fixed holdout, day clustering, ledger locking, and phase-wise BH.

    ``confirmation_start=None`` intentionally retains Phase 1's shared cutoff
    for API compatibility. Production passes the prospectively fixed Phase 2
    boundary and therefore uses :class:`CryptoHypothesisLedger`.
    """

    all_rows = list(observations)
    if confirmation_start is None:
        discovery, confirmation = split_discovery_confirmation(all_rows)
        ledger_obj = HypothesisLedger(ledger) if isinstance(ledger, (str, Path)) else ledger
    else:
        boundary = _time(confirmation_start)
        ordered = sorted(all_rows, key=lambda row: _time(row["settled_at"]))
        discovery = [row for row in ordered if _time(row["settled_at"]) < boundary]
        confirmation = [row for row in ordered if _time(row["settled_at"]) >= boundary]
        ledger_obj = CryptoHypothesisLedger(ledger, boundary) if isinstance(ledger, (str, Path)) else ledger
    findings: list[dict[str, Any]] = []
    phases = [("discovery", discovery)]
    if caught_up:
        phases.append(("confirmation", confirmation))
    for phase, phase_rows in phases:
        grouped: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
        for row in phase_rows:
            grouped[str(row["hypothesis_id"])].append(row)
        for hypothesis, rows in sorted(grouped.items()):
            if phase == "confirmation" and ledger_obj is not None:
                if not ledger_obj.has_discovery(hypothesis) or ledger_obj.has_confirmation(hypothesis):
                    continue
            values = [float(row["value"]) for row in rows]
            days = [str(row.get("day") or _time(row["settled_at"]).date().isoformat()) for row in rows]
            independent = len(set(days))
            estimate, low, high = clustered_mean_ci(values, days)
            tested = independent >= MIN_INDEPENDENT_DAYS
            p_value = _p_value(values, days) if tested else 1.0
            finding = {
                "hypothesis_id": hypothesis,
                "phase": phase,
                "sample_size": len(rows),
                "independent_days": independent,
                "estimate": estimate,
                "confidence_interval": [low, high],
                "p_value": p_value,
                "tested": tested,
                "status": "Tested" if tested else f"Not tested: only {independent} independent day{'' if independent == 1 else 's'} (needs 30)",
            }
            if ledger_obj is not None and tested:
                try:
                    entry = ledger_obj.log_run(
                        hypothesis_id=hypothesis,
                        phase=phase,
                        p_value=p_value,
                        record_ids=[str(row.get("record_id", index)) for index, row in enumerate(rows)],
                        settlement_times=[row["settled_at"] for row in rows],
                        caught_up=caught_up,
                        cluster="UTC day",
                    )
                    finding["ledger_run_id"] = entry["run_id"]
                except ConfirmationLockError:
                    continue
            findings.append(finding)
    for phase in {str(row["phase"]) for row in findings}:
        family = [row for row in findings if row["phase"] == phase]
        for row, q_value in zip(family, benjamini_hochberg([row["p_value"] for row in family])):
            row["q_value"] = q_value
    return findings


def load_crypto_chunks(data_dir: str | Path = "data/crypto") -> list[dict[str, Any]]:
    """Read all recursive immutable gzip chunks and decode compact values.

    The collector schema is deliberately accepted by meaning as well as compact
    aliases (``rt`` record type, ``t`` timestamp, ``s`` symbol). Unknown columns
    are retained so schema additions do not make historical data unreadable.
    """

    aliases = {"rt": "record_type", "t": "timestamp", "s": "source", "tk": "ticker", "as": "asset", "pa": "pair"}
    record_types = {
        "kp": "perp", "po": "perp_book", "st": "spot_ticker", "sb": "spot_book",
        "fe": "funding_estimate", "fs": "funding_settlement", "bm": "bracket_market",
        "be": "bracket_event", "cc": "coinbase_candle", "pc": "perp_candle",
    }
    price_fields = {
        "bb": "bid", "aa": "ask", "lp": "last", "mp": "mark", "rp": "reference",
        "b1": "bid_100", "a1": "ask_100", "b2": "bid_1000", "a2": "ask_1000",
        "yb": "yes_bid", "ya": "yes_ask", "fl": "floor", "cp": "cap",
        "op": "open", "hi": "high", "lo": "low", "cl": "close", "cs": "contract_size",
    }
    time_fields = {"ft": "funding_time", "ct": "close_time", "ep": "end_time", "etm": "exchange_time", "kt": "known_time"}
    scaled_names = {"bid_i", "ask_i", "last_i", "mark_i", "reference_i", "price_i", "funding_i", "strike_i", "floor_i", "cap_i"}
    rows: list[dict[str, Any]] = []
    for path in sorted(Path(data_dir).glob("chunks/**/*.csv.gz")):
        try:
            with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
                for raw in csv.DictReader(handle):
                    row = {aliases.get(key, key): value for key, value in raw.items()}
                    row["record_type"] = record_types.get(str(row.get("record_type")), row.get("record_type"))
                    if row["record_type"] in {"bracket_market", "bracket_event"} and raw.get("et"):
                        row["event_ticker"] = raw["et"]
                    if raw.get("st"):
                        row["series_ticker"] = raw["st"]
                    if raw.get("ty"):
                        row["strike_type"] = raw["ty"]
                    if raw.get("rs"):
                        row["result"] = raw["rs"]
                    for compact, expanded in price_fields.items():
                        if raw.get(compact) not in (None, ""):
                            row[expanded] = _decimal(raw[compact]) / SCALE
                    if raw.get("fr") not in (None, ""):
                        row["funding_rate"] = _decimal(raw["fr"]) / RATE_SCALE
                    for compact, expanded in time_fields.items():
                        if raw.get(compact) not in (None, ""):
                            row[expanded] = _time(raw[compact])
                    for key in list(row):
                        if key in scaled_names and row[key] not in (None, ""):
                            row[key.removesuffix("_i")] = _decimal(row[key]) / SCALE
                    if row.get("timestamp") not in (None, ""):
                        try:
                            row["timestamp"] = _time(row["timestamp"])
                        except (ValueError, TypeError, OSError):
                            pass
                    if row.get("record_type") == "perp" and row.get("contract_size"):
                        for name in ("bid", "ask", "last", "mark", "reference"):
                            if row.get(name) is not None:
                                row[f"underlying_{name}"] = row[name] / row["contract_size"]
                    row["_chunk"] = str(path)
                    rows.append(row)
        except (OSError, csv.Error, UnicodeError):
            # A partial/corrupt chunk is never silently rewritten; skip it and
            # let the report's data-availability section make scarcity visible.
            continue
    return rows


def _carry_cases(rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    """Summarize fee/spread-aware cash paths where normalized fields exist."""
    estimates = [row for row in rows if row.get("record_type") == "funding_estimate" and row.get("ticker")]
    settlements = [row for row in rows if row.get("record_type") == "funding_settlement" and row.get("ticker")]
    perp_markets = {(row.get("ticker"), row.get("timestamp")): row for row in rows if row.get("record_type") == "perp"}
    perp_books = {(row.get("ticker"), row.get("timestamp")): row for row in rows if row.get("record_type") == "perp_book"}
    spot_books = {
        (row.get("asset"), row.get("timestamp")): row for row in rows
        if row.get("record_type") == "spot_book" and row.get("source") == "coinbase"
    }
    result: dict[str, Any] = {}
    for ticker in sorted({str(row["ticker"]) for row in estimates}):
        ticker_estimates = [row for row in estimates if str(row["ticker"]) == ticker]
        ticker_settled = [
            {"funding_time": row["funding_time"], "funding_rate": row["funding_rate"]}
            for row in settlements if str(row["ticker"]) == ticker and row.get("funding_time") is not None
        ]
        for notional in (100, 1000):
            samples = []
            for row in ticker_estimates:
                timestamp = row["timestamp"]
                market = perp_markets.get((ticker, timestamp), {})
                perp = perp_books.get((ticker, timestamp), {})
                spot = spot_books.get((market.get("asset"), timestamp), {})
                pb, pa = perp.get(f"bid_{notional}"), perp.get(f"ask_{notional}")
                sb, sa = spot.get(f"bid_{notional}"), spot.get(f"ask_{notional}")
                spread_cost = None
                if all(value not in (None, "") for value in (pb, pa, sb, sa)):
                    perp_mid = (_decimal(pb) + _decimal(pa)) / 2
                    spot_mid = (_decimal(sb) + _decimal(sa)) / 2
                    spread_cost = Decimal(notional) * (
                        (_decimal(pa) - _decimal(pb)) / perp_mid
                        + (_decimal(sa) - _decimal(sb)) / spot_mid
                    )
                if spread_cost is not None:
                    samples.append({
                        "timestamp": timestamp, "funding_estimate": row["funding_rate"],
                        "round_trip_spread_cost": spread_cost,
                    })
            if not samples:
                continue
            for case, summary in simulate_funding_carry(samples, ticker_settled, notional=Decimal(notional)).items():
                result[f"{ticker}:${notional}:{case}"] = summary
    return result


def _archive_basis(rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    perps = [row for row in rows if row.get("record_type") == "perp" and row.get("asset")]
    perp_books = {(row.get("ticker"), row.get("timestamp")): row for row in rows if row.get("record_type") == "perp_book"}
    spots = [row for row in rows if row.get("record_type") == "spot_book" and row.get("asset")]
    output: dict[str, Any] = {}
    schedules = fee_schedules()
    for ticker in sorted({str(row.get("ticker")) for row in perps}):
        observations = []
        for perp in [row for row in perps if str(row.get("ticker")) == ticker]:
            if not perp.get("underlying_bid") or not perp.get("underlying_ask"):
                continue
            perp_book = perp_books.get((ticker, perp.get("timestamp")), {})
            venue_rows: dict[str, Mapping[str, Any]] = {}
            for venue in ("coinbase", "kraken"):
                candidates = [
                    row for row in spots
                    if row.get("asset") == perp.get("asset") and venue in str(row.get("source", ""))
                    and row.get("timestamp") == perp.get("timestamp") and row.get("bid") and row.get("ask")
                ]
                if candidates:
                    venue_rows[venue] = candidates[-1]
            if venue_rows:
                observations.append({
                    "timestamp": perp["timestamp"], "perp_bid": perp["underlying_bid"],
                    "perp_ask": perp["underlying_ask"], "perp_book": perp_book, "spots": venue_rows,
                })
        costs = {
            # Coinbase uses the pessimistic disclosed taker case here. Both
            # entry and exit, both legs, are represented (2 × each venue fee).
            "coinbase": float(2 * (schedules["kalshi_perps"]["taker_bps"] + schedules["coinbase_pessimistic"]["taker_bps"])),
            # Kraken commission is deliberately absent: this is a lower bound.
            "kraken": float(2 * schedules["kalshi_perps"]["taker_bps"]),
        }
        output[ticker] = basis_summary(observations, full_round_trip_cost_bps=costs)
    return output


def _archive_brackets(rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for row in rows:
        if row.get("record_type") == "bracket_market" and row.get("event_ticker"):
            grouped[str(row["event_ticker"])].append(row)
    summaries = []
    for event, event_rows in sorted(grouped.items()):
        # KXBTC/KXETH are ranges; D suffixed series are directional ladders.
        series = str(event_rows[0].get("series_ticker", ""))
        mutually_exclusive = not series.endswith("D") if series else any(row.get("floor") is not None or row.get("cap") is not None for row in event_rows)
        usable = [row for row in event_rows if row.get("yes_bid") is not None and row.get("yes_ask") is not None]
        if usable:
            summaries.append({"event_ticker": event, "series_ticker": series, **analyze_bracket_group(usable, mutually_exclusive=mutually_exclusive)})
    return summaries


def _archive_calibration(rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    """Construct quote/outcome/candle joins, then run the public scorer."""
    markets = [row for row in rows if row.get("record_type") == "bracket_market" and row.get("ticker")]
    settled_by_ticker: dict[str, Mapping[str, Any]] = {}
    for row in markets:
        if str(row.get("result", "")).lower() in {"yes", "no", "1", "0", "true", "false"}:
            ticker = str(row["ticker"])
            if ticker not in settled_by_ticker or _time(row["timestamp"]) < _time(settled_by_ticker[ticker]["timestamp"]):
                settled_by_ticker[ticker] = row

    candle_returns: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for asset in ("BTC", "ETH"):
        by_end = {
            _time(row["end_time"]): row for row in rows
            if row.get("record_type") == "coinbase_candle" and row.get("asset") == asset
            and row.get("end_time") is not None and row.get("close") not in (None, "")
        }
        ordered = [by_end[key] for key in sorted(by_end)]
        for previous, current in zip(ordered, ordered[1:]):
            if _decimal(previous["close"]) > 0 and _decimal(current["close"]) > 0:
                candle_returns[asset].append({
                    "end_time": current["end_time"],
                    "log_return": math.log(float(_decimal(current["close"]) / _decimal(previous["close"]))),
                })

    spot_by_key = {
        (row.get("asset"), row.get("timestamp")): row for row in rows
        if row.get("record_type") in {"spot_ticker", "spot_book"}
        and row.get("source") == "coinbase" and row.get("bid") and row.get("ask")
    }
    scores: list[dict[str, Any]] = []
    for asset in ("BTC", "ETH"):
        quotes, settlements = [], []
        for row in markets:
            ticker = str(row.get("ticker", ""))
            series = str(row.get("series_ticker", ""))
            if asset not in series or row.get("result") or ticker not in settled_by_ticker:
                continue
            spot = spot_by_key.get((asset, row.get("timestamp")))
            if not spot or row.get("yes_bid") is None or row.get("yes_ask") is None:
                continue
            quote_id = f"{ticker}:{_time(row['timestamp']).isoformat()}"
            quote = {
                "quote_id": quote_id,
                "ticker": ticker,
                "series_ticker": series,
                "quoted_at": row["timestamp"],
                "close_time": row.get("close_time"),
                "yes_probability": float((_decimal(row["yes_bid"]) + _decimal(row["yes_ask"])) / 2),
                "spot_price": float((_decimal(spot["bid"]) + _decimal(spot["ask"])) / 2),
                "floor": row.get("floor"), "cap": row.get("cap"),
            }
            if series.endswith("D"):
                quote["strike"] = row.get("floor", row.get("cap"))
                quote["floor"], quote["cap"] = None, None
                quote["direction"] = "below" if "less" in str(row.get("strike_type", "")).lower() else "above"
            if quote.get("close_time") is None or (
                quote.get("floor") is None and quote.get("cap") is None and quote.get("strike") is None
            ):
                continue
            settled = settled_by_ticker[ticker]
            result = str(settled.get("result", "")).lower()
            outcome = 1 if result in {"yes", "1", "true"} else 0
            quotes.append(quote)
            settlements.append({"quote_id": quote_id, "settled_at": settled["timestamp"], "outcome": outcome})
        scores.extend(score_bracket_calibration(quotes, candle_returns[asset], settlements))
    return scores


def _archive_hypotheses(rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    observations: list[dict[str, Any]] = []
    for ticker, venues in _archive_basis(rows).items():
        for venue, summary in venues.items():
            for index, observation in enumerate(summary["observations"]):
                timestamp = observation["timestamp"]
                observations.append({
                    "hypothesis_id": f"basis:{ticker}:{venue}",
                    "value": observation["mid_basis_bps"],
                    "day": timestamp.date().isoformat(),
                    "record_id": f"{ticker}:{venue}:{timestamp.isoformat()}:{index}",
                    "settled_at": timestamp,
                })
    for score in _archive_calibration(rows):
        if score.get("lognormal_brier_score") is None:
            continue
        observations.append({
            "hypothesis_id": f"calibration:{score.get('series_ticker', 'unknown')}:market-vs-lognormal-brier",
            # Positive means the simple prior-volatility model scored better.
            "value": float(score["brier_score"] - score["lognormal_brier_score"]),
            "day": score["settled_at"].date().isoformat(),
            "record_id": score["quote_id"],
            "settled_at": score["settled_at"],
        })
    return observations


def write_report(
    rows: Sequence[Mapping[str, Any]], findings: Sequence[Mapping[str, Any]],
    *, report_path: str | Path, findings_path: str | Path,
) -> None:
    report_path, findings_path = Path(report_path), Path(findings_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    findings_path.parent.mkdir(parents=True, exist_ok=True)
    artifact = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "methods": {
            "cluster": "UTC day", "minimum_independent_days": 30,
            "multiple_testing": "Benjamini-Hochberg, separately by phase",
            "phase2_confirmation_start": PHASE2_CONFIRMATION_START.isoformat(),
        },
        "carry_cases": _carry_cases(rows),
        "basis": _archive_basis(rows),
        "bracket_consistency": _archive_brackets(rows),
        "bracket_calibration": _archive_calibration(rows),
        "findings": list(findings),
    }
    findings_path.write_text(json.dumps(artifact, indent=2, default=str, sort_keys=True) + "\n", encoding="utf-8")
    lines = [
        "# Crypto observatory — Phase 2", "",
        "This observer uses public data only, never trades or places orders, and does not publish an edge or trading signal.", "",
        "## Data availability", "", f"Loaded {len(rows)} rows from immutable compressed chunks.", "",
        "## Method", "",
        "Basis uses both midpoint and executable prices at $100 and $1,000 where depth is available. Persistence is reported as lag-1 autocorrelation. A claimed excess must clear the full disclosed round-trip cost.", "",
        "Funding carry enters from an estimate only at the next sample and credits only a later settled funding event. Results charge genuine entry and exit fees plus measured executable spreads. Coinbase base and pessimistic maker/taker cases are reported; Kraken comparisons are a lower bound unless a Kraken commission is configured.", "",
        "Bracket ladders use executable bids and asks after fees. Calibration is discovery-only until at least 30 independent UTC days exist; every volatility window is the strictly prior 24 hours of 15-minute Coinbase returns.", "",
        f"Inference reuses the Phase 1 ledger format, clustered confidence intervals, and Benjamini–Hochberg correction. Phase 2 discovery ends at {PHASE2_CONFIRMATION_START.isoformat()}; later observations stay held back until an explicit caught-up run, and confirmation is one-shot. Discovery and confirmation are separate families.", "",
        "## Findings", "",
    ]
    if not findings:
        lines.append("Not tested: only 0 days. No settled observations were available.")
    for finding in findings:
        lines.extend([f"### {finding['hypothesis_id']} — {finding['phase']}", "", str(finding["status"]), ""])
    lines.extend(["## Perp basis", ""])
    if not artifact["basis"]:
        lines.extend(["No aligned perp/spot observations were available.", ""])
    for ticker, venues in artifact["basis"].items():
        for venue, summary in venues.items():
            distribution = summary["distribution"]["mid_basis_bps"]
            persistence = summary["persistence"]["lag_1_autocorrelation"]
            qualifier = " (cost lower bound: Kraken commission not configured)" if venue == "kraken" else ""
            lines.append(
                f"- `{ticker}` vs {venue}{qualifier}: n={distribution['count']}, mean basis "
                f"{distribution['mean']:.3f} bps, lag-1 autocorrelation {persistence:.3f}, "
                f"frequency above full cost {summary['frequency_above_full_round_trip_cost']:.3f}."
            )
            for notional in (100, 1000):
                key = f"long_executable_{notional}_bps"
                if key in summary["distribution"]:
                    long_dist = summary["distribution"][key]
                    short_dist = summary["distribution"][f"short_executable_{notional}_bps"]
                    lines.append(
                        f"  - ${notional} walked books: long mean {long_dist['mean']:.3f} bps, "
                        f"short mean {short_dist['mean']:.3f} bps; frequency above full cost "
                        f"{summary[f'frequency_above_full_round_trip_cost_{notional}']:.3f}."
                    )
    lines.append("")
    lines.extend(["## Bracket consistency", ""])
    if not artifact["bracket_consistency"]:
        lines.extend(["No complete bracket groups were available.", ""])
    for bracket in artifact["bracket_consistency"]:
        if bracket["mutually_exclusive"]:
            lines.append(
                f"- `{bracket['event_ticker']}`: bids sum {bracket['sum_yes_bids']:.4f}, asks sum "
                f"{bracket['sum_yes_asks']:.4f}; buy-all executable after fees="
                f"{bracket['buy_all_executable_after_fees']}, sell-all="
                f"{bracket['sell_all_executable_after_fees']}."
            )
        else:
            lines.append(f"- `{bracket['event_ticker']}`: monotonic={bracket['monotonic']}; violations={len(bracket['monotonicity_violations'])}.")
    lines.append("")
    lines.extend(["## Bracket calibration", ""])
    if not artifact["bracket_calibration"]:
        lines.extend(["Not tested: only 0 settled quote-days with a complete strictly-prior volatility window.", ""])
    for score in artifact["bracket_calibration"]:
        model = "not available" if score["lognormal_probability"] is None else f"{score['lognormal_probability']:.4f}"
        model_brier = "not available" if score["lognormal_brier_score"] is None else f"{score['lognormal_brier_score']:.4f}"
        model_log = "not available" if score["lognormal_log_loss"] is None else f"{score['lognormal_log_loss']:.4f}"
        lines.append(
            f"- `{score['ticker']}` quoted {score['quoted_at'].isoformat()}: market p={score['yes_probability']:.4f}, "
            f"lognormal p={model}; market Brier/log loss={score['brier_score']:.4f}/{score['log_loss']:.4f}; "
            f"lognormal Brier/log loss={model_brier}/{model_log}."
        )
    lines.append("")
    lines.extend(["## Carry simulation", ""])
    if not artifact["carry_cases"]:
        lines.append("No per-ticker estimate, settled-funding, and aligned executable-book history was available.")
    for name, case in artifact["carry_cases"].items():
        lines.append(
            f"- `{name}`: net ${case['net_per_100']:.4f} per $100; worst drawdown "
            f"${case['worst_drawdown']:.4f}; trades={case['trades']}; mean measured full-round-trip "
            f"spread=${case['mean_measured_spread_cost']:.4f}."
        )
    report_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Generate the read-only weekly crypto report")
    parser.add_argument("--data-dir", default="data/crypto")
    parser.add_argument("--ledger", default="data/crypto/hypotheses.jsonl")
    parser.add_argument("--findings", default="data/crypto/findings.json")
    parser.add_argument("--report", default="reports/crypto.md")
    parser.add_argument("--caught-up", action="store_true")
    args = parser.parse_args(argv)
    rows = load_crypto_chunks(args.data_dir)
    observations: list[dict[str, Any]] = _archive_hypotheses(rows)
    for index, row in enumerate(rows):
        if row.get("hypothesis_id") and row.get("value") not in (None, ""):
            timestamp = row.get("settled_at", row.get("timestamp"))
            observations.append({**row, "record_id": row.get("record_id", f"crypto-{index}"), "settled_at": timestamp, "day": _time(timestamp).date().isoformat(), "value": float(row["value"])})
    findings = summarize_crypto_hypotheses(
        observations, ledger=args.ledger, caught_up=args.caught_up,
        confirmation_start=PHASE2_CONFIRMATION_START,
    ) if observations else []
    write_report(rows, findings, report_path=args.report, findings_path=args.findings)


if __name__ == "__main__":
    main()


__all__ = [
    "analyze_bracket_group", "basis_summary", "executable_spreads", "fee_schedules",
    "funding_carry", "load_crypto_chunks", "main", "score_bracket_calibration",
    "summarize_crypto_hypotheses", "write_report",
]
