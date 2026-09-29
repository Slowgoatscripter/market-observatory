"""Acceptance checks for the offline-testable Kalshi client contract."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import importlib
from typing import Any


@dataclass
class _Response:
    status_code: int
    payload: dict[str, Any]
    headers: dict[str, str] | None = None

    def json(self) -> dict[str, Any]:
        return self.payload


class _ScriptedTransport:
    def __init__(self, responses: list[_Response]) -> None:
        self.responses = iter(responses)
        self.calls: list[tuple[str, str, dict[str, Any]]] = []

    def request(
        self,
        method: str,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> _Response:
        del timeout
        self.calls.append((method, url, dict(params or {})))
        return next(self.responses)


def _client_class():
    return importlib.import_module("observatory.kalshi.client").KalshiClient


def _make_client(
    responses: list[_Response],
    *,
    sleeper: Callable[[float], None] = lambda _: None,
):
    transport = _ScriptedTransport(responses)
    client = _client_class()(
        transport=transport,
        sleeper=sleeper,
        requests_per_second=1_000,
        max_retries=3,
    )
    return client, transport


def test_pagination_follows_every_cursor_and_excludes_mve() -> None:
    pages = [
        _Response(200, {"markets": [{"ticker": f"M{i}"}], "cursor": f"c{i}"})
        for i in range(4)
    ]
    pages[-1].payload["cursor"] = ""
    client, transport = _make_client(pages)

    rows = list(client.paginate("/markets", item_key="markets", params={"status": "settled"}))

    assert [row["ticker"] for row in rows] == [f"M{i}" for i in range(4)]
    assert [call[2].get("cursor") for call in transport.calls] == [None, "c0", "c1", "c2"]
    assert all(call[2]["mve_filter"] == "exclude" for call in transport.calls)


def test_429_uses_retry_after_or_exponential_fallback_and_retries_same_request() -> None:
    header_sleeps: list[float] = []
    client, transport = _make_client(
        [
            _Response(429, {}, {"Retry-After": "2.5"}),
            _Response(200, {"markets": [{"ticker": "M"}], "cursor": ""}),
        ],
        sleeper=header_sleeps.append,
    )

    assert [row["ticker"] for row in client.paginate("/markets", item_key="markets")] == ["M"]
    assert header_sleeps == [2.5]
    assert transport.calls[0] == transport.calls[1]

    fallback_sleeps: list[float] = []
    fallback_client, fallback_transport = _make_client(
        [
            _Response(429, {}, {}),
            _Response(429, {}, {}),
            _Response(200, {"markets": [{"ticker": "M"}], "cursor": ""}),
        ],
        sleeper=fallback_sleeps.append,
    )
    assert [
        row["ticker"] for row in fallback_client.paginate("/markets", item_key="markets")
    ] == ["M"]
    assert fallback_sleeps[0] > 0
    assert fallback_sleeps[1] == 2 * fallback_sleeps[0]
    assert fallback_transport.calls[0] == fallback_transport.calls[1] == fallback_transport.calls[2]


def test_timestamp_routing_selects_historical_before_cutoff_and_live_after() -> None:
    cutoff = datetime(2026, 7, 31, tzinfo=timezone.utc)
    moments = [cutoff - timedelta(days=days) for days in (3, 1, 0)] + [
        cutoff + timedelta(days=days) for days in (1, 3)
    ]
    responses = [_Response(200, {"trades": [], "cursor": ""}) for _ in moments]
    client, transport = _make_client(responses)

    for moment in moments:
        list(
            client.paginate(
                "/trades",
                item_key="trades",
                timestamp=moment,
                historical_cutoff=cutoff,
            )
        )

    historical = ["/historical/" in call[1] for call in transport.calls]
    assert historical == [True, True, True, False, False]
