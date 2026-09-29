"""Fixes found in the first live runs (2026-09-29)."""

from __future__ import annotations

from test_client_acceptance import _make_client, _Response


def test_scoped_market_queries_do_not_send_mve_filter() -> None:
    client, transport = _make_client([_Response(200, {"markets": [], "cursor": ""})])
    list(client.iter_pages("/historical/markets", params={"series_ticker": "KXCPI"}))
    assert "mve_filter" not in transport.calls[0][2]
    assert transport.calls[0][2]["series_ticker"] == "KXCPI"


def test_unscoped_market_queries_still_exclude_combos() -> None:
    client, transport = _make_client([_Response(200, {"markets": [], "cursor": ""})])
    list(client.iter_pages("/markets", params={"status": "settled"}))
    assert transport.calls[0][2]["mve_filter"] == "exclude"


def test_events_pages_are_capped_at_200() -> None:
    client, transport = _make_client([_Response(200, {"events": [], "cursor": ""})])
    list(client.iter_pages("/events", params={"series_ticker": "KXNFLGAME"}))
    assert transport.calls[0][2]["limit"] == 200


def test_findings_from_few_events_are_not_tested() -> None:
    from observatory.kalshi import checks

    few = [(0.1 * (i % 3), f"E{i % 9}", 1.0) for i in range(80)]  # 80 markets, 9 events
    summary = checks._summary([], few)
    assert summary["too_few_events"] is True
    assert summary["p_value"] == 1.0 and summary["confidence_interval"] == [None, None]
    many = [(0.1 * (i % 3), f"E{i}", 1.0) for i in range(80)]  # 80 independent events
    assert checks._summary([], many)["too_few_events"] is False
