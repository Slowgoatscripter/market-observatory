"""Statistical safeguards shared by the market observers.

The functions in this module deliberately have a small dependency surface: the
archive and all inference tests can run with the Python standard library alone.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable, Mapping, Sequence
from datetime import date, datetime, timezone
from decimal import Decimal, ROUND_CEILING
import hashlib
import json
import math
from pathlib import Path
from statistics import NormalDist
from typing import Any
from uuid import uuid4


class ConfirmationLockError(RuntimeError):
    """Raised when held-back observations are requested out of order."""


CONFIRMATION_START = datetime(2026, 4, 1, tzinfo=timezone.utc)


def _time_value(record: Mapping[str, Any]) -> datetime:
    value = next(
        (
            record[key]
            for key in ("settled_at", "settlement_time", "settled_time", "close_time")
            if record.get(key) is not None
        ),
        None,
    )
    if isinstance(value, datetime):
        parsed = value
    elif isinstance(value, date):
        parsed = datetime(value.year, value.month, value.day, tzinfo=timezone.utc)
    elif isinstance(value, (int, float)):
        parsed = datetime.fromtimestamp(value, tz=timezone.utc)
    elif isinstance(value, str):
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    else:
        raise ValueError("record has no usable settlement timestamp")
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def split_discovery_confirmation(
    records: Iterable[Mapping[str, Any]], confirmation_fraction: float | None = None
) -> tuple[list[Mapping[str, Any]], list[Mapping[str, Any]]]:
    """Split records at the preregistered calendar boundary.

    An explicitly supplied ``confirmation_fraction`` retains the phase-one API
    for callers replaying an old analysis. New analyses use the fixed boundary,
    so adding old or new archive rows cannot silently move the holdout.
    """

    ordered = sorted(records, key=_time_value)
    if confirmation_fraction is None:
        return (
            [row for row in ordered if _time_value(row) < CONFIRMATION_START],
            [row for row in ordered if _time_value(row) >= CONFIRMATION_START],
        )
    if not 0 < confirmation_fraction < 1:
        raise ValueError("confirmation_fraction must be between zero and one")
    if not ordered:
        return [], []
    confirmation_count = min(len(ordered), math.ceil(len(ordered) * confirmation_fraction))
    boundary = len(ordered) - confirmation_count
    return ordered[:boundary], ordered[boundary:]


def benjamini_hochberg(p_values: Sequence[float]) -> list[float]:
    """Return monotone Benjamini-Hochberg adjusted p-values."""

    count = len(p_values)
    if count == 0:
        return []
    cleaned = [min(1.0, max(0.0, float(value))) for value in p_values]
    order = sorted(range(count), key=cleaned.__getitem__)
    adjusted = [1.0] * count
    running = 1.0
    for rank in range(count, 0, -1):
        index = order[rank - 1]
        running = min(running, cleaned[index] * count / rank)
        adjusted[index] = running
    return adjusted


class HypothesisLedger:
    """Append-only audit log with phase-separated, current-run BH values.

    Every attempt remains on disk. Only the latest discovery run for each
    hypothesis participates in discovery FDR; one-time confirmation runs form
    their own family.
    """

    def __init__(self, path: str | Path):
        self.path = Path(path)

    def _raw_entries(self) -> list[dict[str, Any]]:
        if not self.path.exists():
            return []
        result: list[dict[str, Any]] = []
        with self.path.open("r", encoding="utf-8") as stream:
            for line_number, line in enumerate(stream, 1):
                if not line.strip():
                    continue
                try:
                    item = json.loads(line)
                except json.JSONDecodeError as error:
                    raise ValueError(f"invalid ledger JSON on line {line_number}") from error
                result.append(item)
        return result

    def entries(self) -> list[dict[str, Any]]:
        entries = self._raw_entries()
        # Discovery reruns are audit history, not additional hypotheses. Only
        # the latest run for each hypothesis participates in discovery FDR.
        latest_discovery: dict[str, int] = {}
        confirmations: list[int] = []
        for index, entry in enumerate(entries):
            if entry.get("phase") == "discovery":
                latest_discovery[str(entry.get("hypothesis_id"))] = index
            elif entry.get("phase") == "confirmation":
                confirmations.append(index)
        adjusted: list[float | None] = [None] * len(entries)
        discovery_indices = list(latest_discovery.values())
        for index, q_value in zip(
            discovery_indices,
            benjamini_hochberg([float(entries[index]["p_value"]) for index in discovery_indices]),
        ):
            adjusted[index] = q_value
        for index, q_value in zip(
            confirmations,
            benjamini_hochberg([float(entries[index]["p_value"]) for index in confirmations]),
        ):
            adjusted[index] = q_value
        return [dict(entry, q_value=q_value) for entry, q_value in zip(entries, adjusted)]

    def has_discovery(self, hypothesis_id: str) -> bool:
        return any(
            row.get("hypothesis_id") == hypothesis_id and row.get("phase") == "discovery"
            for row in self._raw_entries()
        )

    def has_confirmation(self, hypothesis_id: str) -> bool:
        return any(
            row.get("hypothesis_id") == hypothesis_id and row.get("phase") == "confirmation"
            for row in self._raw_entries()
        )

    def assert_confirmation_allowed(
        self,
        hypothesis_id: str,
        record_ids: Iterable[str] = (),
        *,
        settlement_times: Iterable[Any] = (),
        caught_up: bool = False,
    ) -> None:
        entries = self._raw_entries()
        discovery = [
            row
            for row in entries
            if row.get("hypothesis_id") == hypothesis_id and row.get("phase") == "discovery"
        ]
        if not discovery:
            raise ConfirmationLockError(
                f"confirmation for {hypothesis_id!r} is locked until discovery is recorded"
            )
        if any(
            row.get("hypothesis_id") == hypothesis_id and row.get("phase") == "confirmation"
            for row in entries
        ):
            raise ConfirmationLockError(
                f"confirmation for {hypothesis_id!r} has already been run"
            )
        if not caught_up:
            raise ConfirmationLockError(
                "confirmation is locked until the archive backfill is caught up"
            )
        del record_ids  # IDs are deliberately never retained or used as a lock.
        times = [_coerce_time(value) for value in settlement_times]
        if not times or min(times) < CONFIRMATION_START:
            raise ConfirmationLockError(
                "confirmation window overlaps discovery or starts before CONFIRMATION_START"
            )

    def confirmation_records(
        self,
        hypothesis_id: str,
        records: Iterable[Mapping[str, Any]],
        *,
        id_key: str = "ticker",
        caught_up: bool = False,
    ) -> list[Mapping[str, Any]]:
        """Return a held-back set only after the hypothesis passes the lock."""

        result = list(records)
        record_ids = [str(row.get(id_key, row.get("id", index))) for index, row in enumerate(result)]
        self.assert_confirmation_allowed(
            hypothesis_id,
            record_ids,
            settlement_times=[_time_value(row) for row in result],
            caught_up=caught_up,
        )
        return result

    def log_run(
        self,
        *,
        hypothesis_id: str,
        phase: str,
        p_value: float,
        record_ids: Iterable[str],
        settlement_times: Iterable[Any] = (),
        caught_up: bool = False,
        **metadata: Any,
    ) -> dict[str, Any]:
        if phase not in {"discovery", "confirmation"}:
            raise ValueError("phase must be 'discovery' or 'confirmation'")
        ids = [str(value) for value in record_ids]
        times = [_coerce_time(value) for value in settlement_times]
        if len(times) != len(ids):
            raise ValueError("settlement_times must contain one value per record")
        if phase == "discovery" and times and max(times) >= CONFIRMATION_START:
            raise ConfirmationLockError(
                "discovery window overlaps confirmation or ends after CONFIRMATION_START"
            )
        if phase == "confirmation":
            self.assert_confirmation_allowed(
                hypothesis_id,
                ids,
                settlement_times=times,
                caught_up=caught_up,
            )
            if times and max(times) > datetime.now(timezone.utc):
                raise ConfirmationLockError(
                    "confirmation window cannot extend beyond the confirmation run date"
                )
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
            "record_ids_sha256": hashlib.sha256(
                "\n".join(sorted(ids)).encode("utf-8")
            ).hexdigest(),
            "min_settlement_time": min(times).isoformat() if times else None,
            "max_settlement_time": max(times).isoformat() if times else None,
            **metadata,
        }
        entry.pop("q_value", None)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8", newline="\n") as stream:
            stream.write(json.dumps(entry, sort_keys=True, separators=(",", ":")) + "\n")
            stream.flush()
        return next(row for row in self.entries() if row["run_id"] == entry["run_id"])


def _coerce_time(value: Any) -> datetime:
    if isinstance(value, datetime):
        parsed = value
    elif isinstance(value, date):
        parsed = datetime(value.year, value.month, value.day, tzinfo=timezone.utc)
    elif isinstance(value, (int, float)):
        parsed = datetime.fromtimestamp(value, tz=timezone.utc)
    elif isinstance(value, str):
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    else:
        raise ValueError("invalid settlement timestamp")
    return parsed.astimezone(timezone.utc) if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def kalshi_fee(
    contracts: int | Decimal,
    price: Decimal | float | str,
    *,
    side: str = "ask",
    fee_multiplier: Decimal | float | str = Decimal("1"),
    coefficient: Decimal | float | str = Decimal("0.07"),
) -> Decimal:
    """Calculate a taker order fee, rounded upward once at the order level."""

    if side not in {"ask", "taker"}:
        raise ValueError("observer cost calculations support taker/ask orders only")
    quantity = Decimal(str(contracts))
    probability = Decimal(str(price))
    multiplier = Decimal(str(fee_multiplier))
    if quantity < 0 or multiplier < 0 or not Decimal(0) <= probability <= Decimal(1):
        raise ValueError("contracts/multiplier must be nonnegative and price must be in [0, 1]")
    raw = Decimal(str(coefficient)) * multiplier * quantity * probability * (1 - probability)
    return raw.quantize(Decimal("0.01"), rounding=ROUND_CEILING)


def clustered_mean_ci(
    values: Sequence[float],
    event_ids: Sequence[str],
    weights: Sequence[float] | None = None,
    *,
    confidence: float = 0.95,
) -> tuple[float, float, float]:
    """Weighted mean and event-clustered sandwich confidence interval."""

    if len(values) != len(event_ids):
        raise ValueError("values and event_ids must have equal length")
    if weights is None:
        weights = [1.0] * len(values)
    if len(weights) != len(values):
        raise ValueError("weights and values must have equal length")
    observations = [
        (float(value), str(event), float(weight))
        for value, event, weight in zip(values, event_ids, weights)
        if math.isfinite(float(value)) and math.isfinite(float(weight)) and float(weight) > 0
    ]
    if not observations:
        return math.nan, math.nan, math.nan
    total_weight = sum(weight for _, _, weight in observations)
    mean = sum(value * weight for value, _, weight in observations) / total_weight
    scores: dict[str, float] = defaultdict(float)
    for value, event, weight in observations:
        scores[event] += weight * (value - mean)
    clusters = len(scores)
    if clusters < 2:
        return mean, math.nan, math.nan
    variance = (clusters / (clusters - 1)) * sum(score * score for score in scores.values())
    variance /= total_weight * total_weight
    critical = NormalDist().inv_cdf(0.5 + confidence / 2)
    margin = critical * math.sqrt(max(0.0, variance))
    return mean, mean - margin, mean + margin


__all__ = [
    "ConfirmationLockError",
    "CONFIRMATION_START",
    "HypothesisLedger",
    "benjamini_hochberg",
    "clustered_mean_ci",
    "kalshi_fee",
    "split_discovery_confirmation",
]
