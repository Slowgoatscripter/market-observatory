"""Honest, offline statistical checks and publication for the Kalshi archive."""

from __future__ import annotations

import argparse
from collections import defaultdict
from collections.abc import Callable, Iterable, Mapping, Sequence
import csv
from datetime import datetime, timezone
from decimal import Decimal
import gzip
import json
import math
import os
from pathlib import Path
from statistics import NormalDist
from typing import Any
from urllib.parse import quote
from urllib.request import Request, urlopen

from observatory.stats import (
    CONFIRMATION_START,
    ConfirmationLockError,
    HypothesisLedger,
    benjamini_hochberg,
    clustered_mean_ci,
    kalshi_fee,
    split_discovery_confirmation,
)


HORIZONS = ("1h", "1d", "7d")
CHECK_TITLES = {
    "calibration": "Calibration",
    "favorite_longshot": "Favorite-longshot",
    "segmented": "Segmented",
    "listing_drift": "Listing drift",
}
MENTIONS_HYPOTHESIS_ID = "mentions_longshot_yes_overpriced"
MENTIONS_HYPOTHESIS = {
    "check": "favorite_longshot",
    "segment": "Mentions",
    "horizon": "1d",
    "price_range": "$0.10-$0.30",
    "contract": "yes",
    "alternative": "negative mean return",
    "return_basis": "profit per $1 total cost at the ask after taker fee",
    "plain_english": (
        "Tests whether YES contracts in Mentions markets priced from $0.10 through $0.30 "
        "one day before close have a negative mean return when bought at the ask after fees."
    ),
}


def _number(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    # Kalshi's legacy integer fields are cents; dollar fields are already [0, 1].
    if result > 1 and result <= 100:
        result /= 100
    return result if math.isfinite(result) else None


def _outcome(row: Mapping[str, Any]) -> float | None:
    value = next((row.get(key) for key in ("outcome", "result") if row.get(key) is not None), None)
    if isinstance(value, bool):
        return float(value)
    if isinstance(value, (int, float)):
        return float(value) if value in (0, 1) else None
    normalized = str(value).strip().lower()
    if normalized in {"yes", "y", "1", "true"}:
        return 1.0
    if normalized in {"no", "n", "0", "false"}:
        return 0.0
    return None


def _nested_price(row: Mapping[str, Any], horizon: str, field: str) -> float | None:
    aliases = {
        "1h": ("close_minus_1h", "1h", "1_hour", "1_hour_before_close", "1h_before_close", "close_1h"),
        "1d": ("close_minus_1d", "1d", "24h", "1_day", "1_day_before_close", "24h_before_close", "close_1d"),
        "7d": ("close_minus_7d", "7d", "7_days", "7_days_before_close", "7d_before_close", "close_7d"),
        "open_1h": ("open_plus_1h", "open_1h", "1h_after_open", "1_hour_after_open"),
        "open_24h": ("open_plus_24h", "open_24h", "24h_after_open", "1_day_after_open"),
    }
    names = aliases.get(horizon, (horizon,))
    containers = [row.get("prices"), row.get("horizons"), row]
    field_aliases = {
        "last_trade": ("last_price", "last_trade", "last", "price", "yes_price"),
        "yes_ask": ("yes_ask", "ask"),
        "yes_bid": ("yes_bid", "bid"),
    }[field]
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        for name in names:
            item = container.get(name)
            if isinstance(item, Mapping):
                for candidate in field_aliases:
                    value = _number(item.get(candidate))
                    if value is not None:
                        return value
            for candidate in field_aliases:
                for flat_name in (
                    f"{name}_{candidate}",
                    f"{candidate}_{name}",
                    f"price_{name}_{candidate}",
                    f"{candidate}_at_{name}",
                ):
                    value = _number(container.get(flat_name))
                    if value is not None:
                        return value
    # Compact test/input form represents one generic horizon.
    if horizon == "1h":
        for candidate in field_aliases:
            value = _number(row.get(candidate))
            if value is not None:
                return value
    return None


def _record_id(row: Mapping[str, Any], index: int) -> str:
    return str(row.get("ticker", row.get("id", index)))


def _settlement_time(row: Mapping[str, Any]) -> datetime:
    value = next(
        (
            row[key]
            for key in ("settled_at", "settlement_time", "settled_time", "close_time")
            if row.get(key) is not None
        ),
        None,
    )
    if isinstance(value, datetime):
        parsed = value
    elif isinstance(value, (int, float)):
        parsed = datetime.fromtimestamp(value, tz=timezone.utc)
    elif isinstance(value, str):
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    else:
        raise ValueError("record has no usable settlement timestamp")
    return parsed.astimezone(timezone.utc) if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def _event(row: Mapping[str, Any], index: int) -> str:
    return str(row.get("event_ticker", row.get("event_id", _record_id(row, index))))


def _weight(row: Mapping[str, Any]) -> float:
    value = _number(row.get("sampling_weight", row.get("weight", 1.0)))
    return value if value is not None and value > 0 else 1.0


def _p_value(estimate: float, low: float, high: float) -> float:
    if not all(math.isfinite(value) for value in (estimate, low, high)):
        return 1.0
    standard_error = (high - low) / (2 * NormalDist().inv_cdf(0.975))
    if standard_error <= 0:
        return 0.0 if estimate else 1.0
    return min(1.0, 2 * (1 - NormalDist().cdf(abs(estimate / standard_error))))


def _negative_mean_p_value(summary: Mapping[str, Any]) -> float:
    """One-sided p-value for the preregistered negative-mean alternative."""

    estimate = summary.get("estimate")
    interval = summary.get("confidence_interval", [None, None])
    if estimate is None or interval[0] is None or interval[1] is None:
        return 1.0
    standard_error = (float(interval[1]) - float(interval[0])) / (
        2 * NormalDist().inv_cdf(0.975)
    )
    if standard_error <= 0:
        return 0.0 if float(estimate) < 0 else 1.0
    return NormalDist().cdf(float(estimate) / standard_error)


MIN_EVENT_CLUSTERS = 30  # independent events needed before a finding gets a p-value


def _summary(
    rows: Sequence[Mapping[str, Any]],
    observations: Sequence[tuple[float, str, float]],
) -> dict[str, Any]:
    del rows  # retained in the signature so summaries can grow archive diagnostics
    values = [item[0] for item in observations]
    events = [item[1] for item in observations]
    weights = [item[2] for item in observations]
    estimate, low, high = clustered_mean_ci(values, events, weights)
    clusters = len(set(events))
    if clusters < MIN_EVENT_CLUSTERS:
        # A clustered interval from a handful of events is far too narrow (9 events
        # gave p = 0.000 on the first live run), so don't test it at all.
        low = high = math.nan
    finite_values = [value for value in values if math.isfinite(value)]
    serial_estimate = estimate if math.isfinite(estimate) else None
    serial_interval = [low, high] if math.isfinite(low) and math.isfinite(high) else [None, None]
    return {
        "estimate": serial_estimate,
        "confidence_interval": serial_interval,
        "too_few_events": clusters < MIN_EVENT_CLUSTERS,
        "p_value": 1.0 if clusters < MIN_EVENT_CLUSTERS else _p_value(estimate, low, high),
        "sample_size": len(observations),
        "effective_weight": sum(weights),
        "event_clusters": len(set(events)),
        "observed_range": [min(finite_values), max(finite_values)] if finite_values else [None, None],
    }


def _bucket(price: float) -> str:
    lower = min(0.95, max(0.0, math.floor((price + 1e-12) / 0.05) * 0.05))
    return f"{lower:.2f}-{lower + 0.05:.2f}"


def _is_mention(row: Mapping[str, Any]) -> bool:
    value = row.get("is_mention")
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes"}
    return value is True or value == 1


def _fee_multiplier(row: Mapping[str, Any]) -> Decimal | None:
    # The archive joins the public series multiplier. Absent metadata means the
    # standard quadratic taker schedule, never an assumed maker discount.
    fee_type = str(row.get("fee_type") or "quadratic").strip().lower()
    if fee_type != "quadratic":
        return None
    return Decimal(str(row.get("fee_multiplier", 1) or 1))


def _yes_return(row: Mapping[str, Any], horizon: str, outcome: float) -> float | None:
    ask = _nested_price(row, horizon, "yes_ask")
    if ask is None or not 0 < ask < 1:
        return None
    multiplier = _fee_multiplier(row)
    if multiplier is None:
        return None
    fee = float(kalshi_fee(1, Decimal(str(ask)), fee_multiplier=multiplier))
    cost = ask + fee
    return (outcome - cost) / cost


def _no_return(row: Mapping[str, Any], horizon: str, outcome: float) -> float | None:
    yes_bid = _nested_price(row, horizon, "yes_bid")
    # Compact rows contain only yes ask. Do not manufacture a spread; parity is
    # merely a compatibility fallback for this reduced input shape.
    if yes_bid is None and horizon == "1h" and "yes_bid" not in row:
        yes_bid = _number(row.get("yes_ask"))
    if yes_bid is None:
        return None
    no_ask = 1 - yes_bid
    if not 0 < no_ask < 1:
        return None
    multiplier = _fee_multiplier(row)
    if multiplier is None:
        return None
    fee = float(kalshi_fee(1, Decimal(str(no_ask)), fee_multiplier=multiplier))
    cost = no_ask + fee
    return ((1 - outcome) - cost) / cost


def _calibration_groups(rows: Sequence[Mapping[str, Any]]) -> Iterable[tuple[str, dict[str, Any], list[tuple[float, str, float]]]]:
    for horizon in HORIZONS:
        groups: dict[str, list[tuple[float, str, float]]] = defaultdict(list)
        components: dict[str, list[tuple[float, float, float]]] = defaultdict(list)
        for index, row in enumerate(rows):
            outcome = _outcome(row)
            price = _nested_price(row, horizon, "last_trade")
            if price is None:
                price = _nested_price(row, horizon, "yes_ask")
            if outcome is None or price is None or not 0 <= price <= 1:
                continue
            bucket = _bucket(price)
            weight = _weight(row)
            groups[bucket].append((outcome - price, _event(row, index), weight))
            components[bucket].append((outcome, price, weight))
        for bucket, observations in sorted(groups.items()):
            hypothesis = f"calibration:{horizon}:{bucket}"
            parts = components[bucket]
            total_weight = sum(part[2] for part in parts)
            yield hypothesis, {
                "check": "calibration",
                "horizon": horizon,
                "price_bucket": bucket,
                "actual_win_rate": sum(part[0] * part[2] for part in parts) / total_weight,
                "mean_implied_probability": sum(part[1] * part[2] for part in parts) / total_weight,
            }, observations
        mention_rows = [row for row in rows if _is_mention(row)]
        if mention_rows:
            groups = defaultdict(list)
            components = defaultdict(list)
            for index, row in enumerate(mention_rows):
                outcome = _outcome(row)
                price = _nested_price(row, horizon, "last_trade")
                if price is None:
                    price = _nested_price(row, horizon, "yes_ask")
                if outcome is None or price is None or not 0 <= price <= 1:
                    continue
                bucket = _bucket(price)
                weight = _weight(row)
                groups[bucket].append((outcome - price, _event(row, index), weight))
                components[bucket].append((outcome, price, weight))
            for bucket, observations in sorted(groups.items()):
                parts = components[bucket]
                total_weight = sum(part[2] for part in parts)
                yield f"calibration:mentions:{horizon}:{bucket}", {
                    "check": "calibration",
                    "segment": "Mentions",
                    "horizon": horizon,
                    "price_bucket": bucket,
                    "actual_win_rate": sum(part[0] * part[2] for part in parts) / total_weight,
                    "mean_implied_probability": sum(part[1] * part[2] for part in parts) / total_weight,
                }, observations


def _favorite_groups(rows: Sequence[Mapping[str, Any]]) -> Iterable[tuple[str, dict[str, Any], list[tuple[float, str, float]]]]:
    for horizon in HORIZONS:
        grouped: dict[tuple[str, str], list[tuple[float, str, float]]] = defaultdict(list)
        for index, row in enumerate(rows):
            outcome = _outcome(row)
            ask = _nested_price(row, horizon, "yes_ask")
            if outcome is None or ask is None:
                continue
            yes_return = _yes_return(row, horizon, outcome)
            no_return = _no_return(row, horizon, outcome)
            if yes_return is not None:
                grouped[(_bucket(ask), "yes")].append((yes_return, _event(row, index), _weight(row)))
            if no_return is not None:
                grouped[(_bucket(ask), "no")].append((no_return, _event(row, index), _weight(row)))
        for (bucket, contract), observations in sorted(grouped.items()):
            hypothesis = f"favorite_longshot:{horizon}:{bucket}:{contract}"
            yield hypothesis, {
                "check": "favorite_longshot",
                "horizon": horizon,
                "price_bucket": bucket,
                "contract": contract,
                "return_basis": "profit per $1 total cost at the ask after taker fee",
            }, observations
        mention_groups: dict[tuple[str, str], list[tuple[float, str, float]]] = defaultdict(list)
        for index, row in enumerate(rows):
            if not _is_mention(row):
                continue
            outcome = _outcome(row)
            ask = _nested_price(row, horizon, "yes_ask")
            if outcome is None or ask is None:
                continue
            for contract, net_return in (
                ("yes", _yes_return(row, horizon, outcome)),
                ("no", _no_return(row, horizon, outcome)),
            ):
                if net_return is not None:
                    mention_groups[(_bucket(ask), contract)].append(
                        (net_return, _event(row, index), _weight(row))
                    )
        for (bucket, contract), observations in sorted(mention_groups.items()):
            yield f"favorite_longshot:mentions:{horizon}:{bucket}:{contract}", {
                "check": "favorite_longshot",
                "segment": "Mentions",
                "horizon": horizon,
                "price_bucket": bucket,
                "contract": contract,
                "return_basis": "profit per $1 total cost at the ask after taker fee",
            }, observations


def _mentions_preregistered_group(
    rows: Sequence[Mapping[str, Any]],
) -> Iterable[tuple[str, dict[str, Any], list[tuple[float, str, float]]]]:
    observations: list[tuple[float, str, float]] = []
    for index, row in enumerate(rows):
        if not _is_mention(row):
            continue
        outcome = _outcome(row)
        ask = _nested_price(row, "1d", "yes_ask")
        if outcome is None or ask is None or not 0.10 <= ask <= 0.30:
            continue
        net_return = _yes_return(row, "1d", outcome)
        if net_return is not None:
            observations.append((net_return, _event(row, index), _weight(row)))
    if any(_is_mention(row) for row in rows):
        yield MENTIONS_HYPOTHESIS_ID, dict(MENTIONS_HYPOTHESIS), observations


def _duration_band(row: Mapping[str, Any]) -> str | None:
    def parse(value: Any) -> datetime | None:
        if isinstance(value, datetime):
            return value
        if isinstance(value, str):
            try:
                return datetime.fromisoformat(value.replace("Z", "+00:00"))
            except ValueError:
                return None
        return None

    opened = parse(row.get("open_time", row.get("listed_at")))
    closed = parse(row.get("close_time", row.get("settled_at", row.get("settlement_time"))))
    if not opened or not closed:
        return None
    hours = (closed - opened).total_seconds() / 3600
    if hours < 24:
        return "under_1d"
    if hours < 24 * 7:
        return "1d_to_7d"
    return "7d_or_more"


def _segmented_groups(rows: Sequence[Mapping[str, Any]]) -> Iterable[tuple[str, dict[str, Any], list[tuple[float, str, float]]]]:
    dimensions: dict[str, Callable[[Mapping[str, Any]], Any]] = {
        "category": lambda row: row.get("category", row.get("segment")),
        "frequency": lambda row: row.get("frequency"),
    }
    for horizon in HORIZONS:
        horizon_dimensions = {**dimensions, "time_to_close": lambda _row, value=horizon: value}
        for dimension, extractor in horizon_dimensions.items():
            groups: dict[tuple[str, str], list[tuple[float, str, float]]] = defaultdict(list)
            for index, row in enumerate(rows):
                value = extractor(row)
                outcome = _outcome(row)
                if value is None or outcome is None:
                    continue
                for contract, net_return in (
                    ("yes", _yes_return(row, horizon, outcome)),
                    ("no", _no_return(row, horizon, outcome)),
                ):
                    if net_return is not None:
                        groups[(str(value), contract)].append(
                            (net_return, _event(row, index), _weight(row))
                        )
            for (segment, contract), observations in sorted(groups.items()):
                hypothesis = f"segmented:{dimension}:{segment}:{horizon}:{contract}"
                yield hypothesis, {
                    "check": "segmented",
                    "dimension": dimension,
                    "segment": segment,
                    "horizon": horizon,
                    "contract": contract,
                    "return_basis": "profit per $1 total cost at the ask after taker fee",
                }, observations


def _listing_groups(rows: Sequence[Mapping[str, Any]]) -> Iterable[tuple[str, dict[str, Any], list[tuple[float, str, float]]]]:
    observations: list[tuple[float, str, float]] = []
    for index, row in enumerate(rows):
        outcome = _outcome(row)
        early = _nested_price(row, "open_1h", "last_trade")
        later = _nested_price(row, "open_24h", "last_trade")
        if early is None:
            early = _nested_price(row, "open_1h", "yes_ask")
        if later is None:
            later = _nested_price(row, "open_24h", "yes_ask")
        if outcome is None or early is None or later is None:
            continue
        difference = (outcome - early) ** 2 - (outcome - later) ** 2
        observations.append((difference, _event(row, index), _weight(row)))
    if observations:
        yield "listing_drift:brier_1h_vs_24h", {
            "check": "listing_drift",
            "comparison": "1-hour versus 24-hour post-listing Brier error",
            "direction": "positive means the one-hour price was more mispriced",
        }, observations


def _all_groups(rows: Sequence[Mapping[str, Any]]):
    yield from _mentions_preregistered_group(rows)
    yield from _calibration_groups(rows)
    yield from _favorite_groups(rows)
    yield from _segmented_groups(rows)
    yield from _listing_groups(rows)


def run_standard_checks(
    records: Iterable[Mapping[str, Any]],
    *,
    ledger: HypothesisLedger | str | Path | None = None,
    confirmation_fraction: float | None = None,
    caught_up: bool = False,
) -> list[dict[str, Any]]:
    """Run discovery first and each hypothesis's held-back confirmation once.

    Passing a ledger makes the one-shot lock durable across report runs. Without
    one, this invocation still observes the same ordering using an in-memory
    registry, which is useful for previews and tests.
    """

    rows = list(records)
    discovery, confirmation = split_discovery_confirmation(rows, confirmation_fraction)
    ledger_object = HypothesisLedger(ledger) if isinstance(ledger, (str, Path)) else ledger
    findings: list[dict[str, Any]] = []
    discovered_now: set[str] = set()

    discovery_groups = {hypothesis: (metadata, observations) for hypothesis, metadata, observations in _all_groups(discovery)}
    # Required check families remain visible even when a reduced dataset has no
    # usable prices; the finding is explicit rather than silently omitted.
    present = {metadata["check"] for metadata, _ in discovery_groups.values()}
    for check in CHECK_TITLES:
        if check not in present:
            hypothesis = f"{check}:insufficient_data"
            discovery_groups[hypothesis] = ({"check": check, "note": "insufficient usable discovery observations"}, [])

    for hypothesis, (metadata, observations) in discovery_groups.items():
        summary = _summary(discovery, observations)
        if hypothesis == MENTIONS_HYPOTHESIS_ID:
            summary["p_value"] = _negative_mean_p_value(summary)
        finding = {"hypothesis_id": hypothesis, "phase": "discovery", **metadata, **summary}
        if ledger_object is not None and observations:
            preregistration = (
                {
                    "preregistered_hypothesis": metadata["plain_english"],
                    "alternative": metadata["alternative"],
                }
                if hypothesis == MENTIONS_HYPOTHESIS_ID
                else {}
            )
            entry = ledger_object.log_run(
                hypothesis_id=hypothesis,
                phase="discovery",
                p_value=summary["p_value"],
                record_ids=[_record_id(row, index) for index, row in enumerate(discovery)],
                settlement_times=[_settlement_time(row) for row in discovery],
                check=metadata["check"],
                **preregistration,
            )
            finding["ledger_run_id"] = entry["run_id"]
        discovered_now.add(hypothesis)
        findings.append(finding)

    # Do not even derive statistics from the held-back rows until discovery has
    # been durably recorded above. This ordering is the preregistration lock;
    # computing both dictionaries together would quietly peek at confirmation.
    confirmation_groups = (
        {
            hypothesis: (metadata, observations)
            for hypothesis, metadata, observations in _all_groups(confirmation)
        }
        if caught_up
        else {}
    )
    for hypothesis, (metadata, observations) in confirmation_groups.items():
        allowed = hypothesis in discovered_now
        if ledger_object is not None:
            allowed = ledger_object.has_discovery(hypothesis) and not ledger_object.has_confirmation(hypothesis)
        if not allowed:
            continue
        summary = _summary(confirmation, observations)
        if hypothesis == MENTIONS_HYPOTHESIS_ID:
            summary["p_value"] = _negative_mean_p_value(summary)
        finding = {"hypothesis_id": hypothesis, "phase": "confirmation", **metadata, **summary}
        if ledger_object is not None:
            preregistration = (
                {
                    "preregistered_hypothesis": metadata["plain_english"],
                    "alternative": metadata["alternative"],
                }
                if hypothesis == MENTIONS_HYPOTHESIS_ID
                else {}
            )
            try:
                entry = ledger_object.log_run(
                    hypothesis_id=hypothesis,
                    phase="confirmation",
                    p_value=summary["p_value"],
                    record_ids=[_record_id(row, index) for index, row in enumerate(confirmation)],
                    settlement_times=[_settlement_time(row) for row in confirmation],
                    caught_up=caught_up,
                    check=metadata["check"],
                    **preregistration,
                )
            except ConfirmationLockError:
                continue
            finding["ledger_run_id"] = entry["run_id"]
        findings.append(finding)

    if ledger_object is not None:
        q_by_run = {entry["run_id"]: entry["q_value"] for entry in ledger_object.entries()}
        for finding in findings:
            finding["q_value"] = q_by_run.get(finding.get("ledger_run_id"), 1.0)
    else:
        for finding in findings:
            finding["q_value"] = None
        for phase in ("discovery", "confirmation"):
            indices = [
                index
                for index, finding in enumerate(findings)
                if finding.get("phase") == phase and finding.get("sample_size", 0) > 0
            ]
            for index, q_value in zip(
                indices,
                benjamini_hochberg([findings[index]["p_value"] for index in indices]),
            ):
                findings[index]["q_value"] = q_value
    return findings


def _fmt(value: Any, digits: int = 3) -> str:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return "not available"
    return f"{number:.{digits}f}" if math.isfinite(number) else "not available"


def write_outputs(
    findings: Sequence[Mapping[str, Any]],
    report_path: str | Path = "reports/kalshi.md",
    findings_path: str | Path = "data/findings.json",
    *,
    caught_up: bool | None = None,
) -> None:
    """Write a plain-English report and a stable machine-readable artifact."""

    report_path = Path(report_path)
    findings_path = Path(findings_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    findings_path.parent.mkdir(parents=True, exist_ok=True)
    document = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "method": {
            "holdout": f"fixed confirmation window beginning {CONFIRMATION_START.isoformat()}",
            "uncertainty": "95% confidence interval clustered by event",
            "multiple_testing": "Benjamini-Hochberg over the latest discovery run per hypothesis, separately from confirmation runs",
            "fees": "quadratic taker fee ceil-to-cent(0.07 × contracts × P × (1-P)); buys use the ask; compact chunks omit series fee metadata, so fee_multiplier=1 is assumed",
        },
        "findings": list(findings),
    }
    findings_path.write_text(json.dumps(document, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8")

    lines = [
        "# Kalshi market observatory",
        "",
        "This public-data observer never trades or places orders. These estimates are descriptive research and **not a trading signal**.",
        "",
        "## How to read this",
        "",
        f"Discovery uses markets settled before {CONFIRMATION_START.date().isoformat()}; the fixed confirmation window begins at that UTC boundary. Uncertainty is a 95% confidence interval clustered by event. Benjamini-Hochberg adjustment uses the latest discovery run per hypothesis and treats confirmation runs as a separate family.",
        "",
        "Fees and returns assume a taker buys at the ask (never the midpoint) and pays the quadratic fee rounded up per order: `ceil-to-cent(0.07 × series fee multiplier × contracts × P × (1-P))`. We retain the series fee type; a missing type is assumed quadratic, any other fee type is excluded, and maker discounts are not assumed.",
        "",
        "## Findings",
        "",
    ]
    if caught_up is False:
        lines.extend(["Confirmation waits until the archive is complete.", ""])
    if not findings:
        lines.append("No usable settled markets were available.")
    ordered_findings = sorted(
        findings,
        key=lambda finding: finding.get("hypothesis_id") != MENTIONS_HYPOTHESIS_ID,
    )
    for finding in ordered_findings:
        check = str(finding.get("check", "unknown"))
        title = CHECK_TITLES.get(check, check.replace("_", " ").title())
        phase = str(finding.get("phase", "discovery"))
        label = "confirmed on held-back data" if phase == "confirmation" else "candidate (discovery only)"
        interval = finding.get("confidence_interval", [None, None])
        observed_range = finding.get("observed_range", [None, None])
        if finding.get("hypothesis_id") == MENTIONS_HYPOTHESIS_ID:
            result = (
                "negative as preregistered"
                if finding.get("estimate") is not None and float(finding["estimate"]) < 0
                else "not negative as preregistered"
            )
            lines.extend(
                [
                    f"### Mentions longshot YES — {label}",
                    "",
                    str(finding.get("plain_english", MENTIONS_HYPOTHESIS["plain_english"])),
                    f"Result: {result}; mean return {_fmt(finding.get('estimate'))}. Sample: {finding.get('event_clusters', 0)} independent events ({finding.get('sample_size', 0)} contracts). Status: {label}.",
                    (f"Not tested: only {finding.get('event_clusters')} independent events "
                     f"(needs {MIN_EVENT_CLUSTERS})." if finding.get('too_few_events') else
                     f"Raw p-value: {_fmt(finding.get('p_value'))}; multiple-testing adjusted q-value: {_fmt(finding.get('q_value'))}."),
                    "",
                ]
            )
            continue
        lines.extend(
            [
                f"### {title} — {label}",
                "",
                f"Hypothesis `{finding.get('hypothesis_id', 'unspecified')}` used a sample size of {finding.get('sample_size', 'not reported')} markets across {finding.get('event_clusters', 'not reported')} event clusters.",
                f"Estimate: {_fmt(finding.get('estimate'))}. 95% confidence interval: {_fmt(interval[0])} to {_fmt(interval[1])}. Observed range: {_fmt(observed_range[0])} to {_fmt(observed_range[1])}.",
                (f"Not tested: only {finding.get('event_clusters')} independent events "
                 f"(needs {MIN_EVENT_CLUSTERS})." if finding.get('too_few_events') else
                 f"Raw p-value: {_fmt(finding.get('p_value'))}; multiple-testing adjusted q-value: {_fmt(finding.get('q_value'))}."),
                "",
            ]
        )
    report_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def send_ntfy_digest(
    target: str | None = None,
    digest: str = "",
    *,
    transport: Callable[..., Any] | None = None,
) -> bool:
    """Best-effort ntfy notification; configuration and transport never escape."""

    try:
        environment_topic = os.environ.get("NTFY_TOPIC")
        # The production form is ``send_ntfy_digest(digest)`` and obtains its
        # destination only from the environment.  An explicit URL remains an
        # injectable seam for offline transport tests.
        if target and not target.startswith(("https://", "http://")) and not digest:
            digest, target = target, None
        configured = target if target and target.startswith(("https://", "http://")) else environment_topic
        if not configured:
            return False
        url = configured if configured.startswith(("https://", "http://")) else f"https://ntfy.sh/{quote(configured, safe='')}"
        sender = transport or urlopen
        request = Request(
            url,
            data=digest.encode("utf-8"),
            headers={"Content-Type": "text/plain; charset=utf-8", "Title": "Kalshi Observatory"},
            method="POST",
        )
        response = sender(request, timeout=10)
        close = getattr(response, "close", None)
        if close:
            close()
        return True
    except Exception:
        return False


def load_archive_rows(data_dir: str | Path = "data/kalshi") -> list[dict[str, Any]]:
    """Load append-only chunks, keeping the newest row for each ticker."""

    root = Path(data_dir)
    mention_tickers: set[str] | None = None
    for mention_cache in (root / "mention-series.json", root / "_cache" / "mention-series.json"):
        try:
            cached = json.loads(mention_cache.read_text(encoding="utf-8"))
        except (OSError, ValueError, TypeError):
            continue
        if isinstance(cached, dict):
            cached = cached.get("tickers")
        if isinstance(cached, list):
            mention_tickers = {str(ticker) for ticker in cached if ticker}
            break
    rows: dict[str, dict[str, Any]] = {}
    for path in sorted((root / "chunks").glob("*.csv.gz")):
        with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                loaded = dict(row)
                if "is_mention" not in loaded or loaded.get("is_mention") == "":
                    loaded["is_mention"] = (
                        None
                        if mention_tickers is None
                        else int(str(loaded.get("series_ticker")) in mention_tickers)
                    )
                rows[str(row.get("ticker") or f"{path}:{len(rows)}")] = loaded
    return list(rows.values())


def _previous_confirmations(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
        return [
            dict(row)
            for row in document.get("findings", [])
            if row.get("phase") == "confirmation"
        ]
    except (OSError, ValueError, TypeError):
        return []


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Run honest checks on the read-only Kalshi archive"
    )
    parser.add_argument("--data-dir", default="data/kalshi")
    parser.add_argument("--ledger", default="data/hypotheses.jsonl")
    parser.add_argument("--report", default="reports/kalshi.md")
    parser.add_argument("--findings", default="data/findings.json")
    parser.add_argument("--no-notify", action="store_true")
    args = parser.parse_args(argv)

    rows = load_archive_rows(args.data_dir)
    state_path = Path(args.data_dir) / "archive-state.json"
    try:
        archive_state = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, ValueError, TypeError):
        archive_state = {}
    caught_up = archive_state.get("caught_up") is True
    findings_path = Path(args.findings)
    previous = _previous_confirmations(findings_path)
    current = run_standard_checks(rows, ledger=args.ledger, caught_up=caught_up)
    by_key = {
        (str(row.get("hypothesis_id")), str(row.get("phase"))): row
        for row in [*previous, *current]
    }
    findings = list(by_key.values())

    # A growing ledger can change prior q-values; refresh preserved confirmation
    # findings from their immutable run IDs before publishing.
    ledger = HypothesisLedger(args.ledger)
    q_by_run = {row["run_id"]: row["q_value"] for row in ledger.entries()}
    for finding in findings:
        run_id = finding.get("ledger_run_id")
        if run_id in q_by_run:
            finding["q_value"] = q_by_run[run_id]

    write_outputs(findings, args.report, findings_path, caught_up=caught_up)
    if not args.no_notify:
        confirmed = sum(row.get("phase") == "confirmation" for row in findings)
        candidates = sum(row.get("phase") == "discovery" for row in findings)
        send_ntfy_digest(
            f"Kalshi Observatory weekly: {len(rows)} retained markets; "
            f"{confirmed} confirmed findings; {candidates} discovery candidates."
        )


if __name__ == "__main__":
    main()


__all__ = [
    "load_archive_rows",
    "main",
    "run_standard_checks",
    "send_ntfy_digest",
    "write_outputs",
]
