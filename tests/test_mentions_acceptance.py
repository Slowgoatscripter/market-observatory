"""Offline acceptance checks for prioritizing and reporting Mentions markets."""

from __future__ import annotations

import csv
from datetime import datetime, timedelta, timezone
import gzip
import importlib
import json
from pathlib import Path
import time
from typing import Any


UTC = timezone.utc


def _archive():
    return importlib.import_module("observatory.kalshi.archive")


def _checks():
    return importlib.import_module("observatory.kalshi.checks")


class _OrderingClient:
    def __init__(self) -> None:
        self.walked: list[str] = []

    def series_list(self, **params: Any):
        if params == {"category": "Mentions"}:
            yield {"ticker": "MENTION", "category": "Politics", "frequency": "monthly"}
            return
        yield {"ticker": "OTHER", "category": "Economics", "frequency": "monthly"}
        yield {"ticker": "MENTION", "category": "Politics", "frequency": "monthly"}

    def iter_pages(self, path: str, *, params=None, **kwargs: Any):
        del path, kwargs
        self.walked.append(str(params["series_ticker"]))
        yield {"markets": [], "cursor": ""}


def test_unfinished_mention_series_are_walked_first_and_cached(tmp_path: Path) -> None:
    module = _archive()
    client = _OrderingClient()
    store = module.MonthlyArchive(tmp_path)
    collector = module.ArchiveCollector(client, store)

    assert collector.collect(
        cutoff=datetime(2026, 1, 1, tzinfo=UTC),
        deadline=time.monotonic() + 60,
    )

    assert client.walked[:2] == ["MENTION", "MENTION"]
    saved = json.loads(store.mention_cache_path.read_text(encoding="utf-8"))
    assert saved["tickers"] == ["MENTION"] and saved["fetched_at"].endswith("Z")
    # Kept with the committed archive, not in the uncarried _cache/ folder.
    assert store.mention_cache_path.parent == tmp_path

    # A fresh file is reused, whatever its modification time (git resets it).
    calls = client.series_list_calls if hasattr(client, "series_list_calls") else None
    assert collector.load_mention_series() == {"MENTION"}
    if calls is not None:
        assert client.series_list_calls == calls
    assert store.load_state()["finished_series"] == ["MENTION", "OTHER"]


def test_old_chunk_rows_derive_mention_membership_from_cache(tmp_path: Path) -> None:
    chunk_dir = tmp_path / "chunks"
    cache_dir = tmp_path / "_cache"
    chunk_dir.mkdir()
    cache_dir.mkdir()
    (cache_dir / "mention-series.json").write_text('["SERIES-MENTION"]', encoding="utf-8")
    with gzip.open(chunk_dir / "old.csv.gz", "wt", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["ticker", "series_ticker", "result"])
        writer.writeheader()
        writer.writerows(
            [
                {"ticker": "M", "series_ticker": "SERIES-MENTION", "result": "yes"},
                {"ticker": "O", "series_ticker": "SERIES-OTHER", "result": "no"},
            ]
        )

    loaded = {row["ticker"]: row for row in _checks().load_archive_rows(tmp_path)}
    assert loaded["M"]["is_mention"] == 1
    assert loaded["O"]["is_mention"] == 0


def _mention_rows() -> list[dict[str, Any]]:
    start = datetime(2025, 1, 1, tzinfo=UTC)
    return [
        {
            "ticker": f"M-{index}",
            "event_ticker": f"EVENT-{index}",
            "series_ticker": "MENTION",
            "category": "Politics",
            "is_mention": 1,
            "result": "yes" if index % 8 == 0 else "no",
            "close_minus_1d_last_trade": 0.20,
            "close_minus_1d_yes_ask": 0.20,
            "close_minus_1d_yes_bid": 0.19,
            "settlement_time": (start + timedelta(days=index)).isoformat(),
        }
        for index in range(35)
    ]


def test_mentions_are_their_own_segment_and_preregistered_hypothesis_is_first(
    tmp_path: Path,
) -> None:
    checks = _checks()
    ledger = tmp_path / "hypotheses.jsonl"
    findings = checks.run_standard_checks(_mention_rows(), ledger=ledger)

    assert findings[0]["hypothesis_id"] == "mentions_longshot_yes_overpriced"
    assert findings[0]["event_clusters"] == 35
    assert findings[0]["phase"] == "discovery"
    assert any(
        row.get("check") == "calibration" and row.get("segment") == "Mentions"
        for row in findings
    )
    assert any(
        row.get("check") == "favorite_longshot" and row.get("segment") == "Mentions"
        for row in findings
    )
    logged = [json.loads(line) for line in ledger.read_text(encoding="utf-8").splitlines()]
    assert logged[0]["hypothesis_id"] == "mentions_longshot_yes_overpriced"

    report = tmp_path / "report.md"
    checks.write_outputs(findings, report, tmp_path / "findings.json", caught_up=False)
    text = report.read_text(encoding="utf-8")
    assert text.index("Mentions longshot YES") < text.index("Calibration")
    assert "one day before close" in text
    assert "35 independent events" in text
    assert "candidate (discovery only)" in text
