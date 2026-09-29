"""Small, read-only client for Kalshi's public Trade API.

The client deliberately exposes only HTTP GET operations.  A transport can be
injected for completely offline tests; the default transport uses the standard
library, so collection itself does not require a particular HTTP package.
"""

from __future__ import annotations

from collections.abc import Iterator, Mapping
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import json
import threading
import time
from typing import Any, Protocol
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


DEFAULT_BASE_URL = "https://external-api.kalshi.com/trade-api/v2"


class _Response(Protocol):
    status_code: int
    headers: Mapping[str, str]

    def json(self) -> dict[str, Any]: ...


class _Transport(Protocol):
    def request(
        self,
        method: str,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> _Response: ...


class _UrlLibResponse:
    def __init__(self, status: int, body: bytes, headers: Mapping[str, str]) -> None:
        self.status_code = status
        self._body = body
        self.headers = headers

    def json(self) -> dict[str, Any]:
        value = json.loads(self._body.decode("utf-8"))
        if not isinstance(value, dict):
            raise ValueError("Kalshi returned a non-object JSON response")
        return value


class _UrlLibTransport:
    def request(
        self,
        method: str,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> _UrlLibResponse:
        query = urlencode(
            [(key, item) for key, value in (params or {}).items() for item in _values(value)]
        )
        request = Request(f"{url}?{query}" if query else url, method=method)
        request.add_header("Accept", "application/json")
        request.add_header("User-Agent", "market-observatory/phase-1")
        try:
            with urlopen(request, timeout=timeout) as response:  # noqa: S310 - fixed API URL
                return _UrlLibResponse(response.status, response.read(), response.headers)
        except HTTPError as error:
            return _UrlLibResponse(error.code, error.read(), error.headers)


def _values(value: Any) -> list[Any]:
    if isinstance(value, (list, tuple)):
        return list(value)
    return [value]


def _as_utc(value: datetime | str) -> datetime:
    if isinstance(value, str):
        value = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


class KalshiHTTPError(RuntimeError):
    """Raised after a public API request fails or exhausts its retries."""

    def __init__(self, status_code: int, url: str, payload: Any = None) -> None:
        super().__init__(f"Kalshi GET {url} failed with HTTP {status_code}: {payload!r}")
        self.status_code = status_code
        self.url = url
        self.payload = payload


EVENTS_PAGE_LIMIT = 200


class KalshiClient:
    """Rate-limited client for unauthenticated Kalshi market-data endpoints."""

    def __init__(
        self,
        *,
        base_url: str = DEFAULT_BASE_URL,
        transport: _Transport | None = None,
        requests_per_second: float = 6.0,
        max_retries: int = 8,
        backoff_seconds: float = 0.5,
        timeout: float = 30.0,
        sleeper: Any = time.sleep,
        clock: Any = time.monotonic,
    ) -> None:
        if requests_per_second <= 0:
            raise ValueError("requests_per_second must be positive")
        if max_retries < 0:
            raise ValueError("max_retries cannot be negative")
        self.base_url = base_url.rstrip("/")
        self.transport = transport or _UrlLibTransport()
        self.requests_per_second = float(requests_per_second)
        self.max_retries = max_retries
        self.backoff_seconds = float(backoff_seconds)
        self.timeout = timeout
        self._sleep = sleeper
        self._clock = clock
        self._last_request_at: float | None = None
        self._rate_lock = threading.Lock()
        self._count_lock = threading.Lock()
        self.request_count = 0

    def _throttle(self) -> None:
        interval = 1.0 / self.requests_per_second
        with self._rate_lock:
            now = self._clock()
            if self._last_request_at is not None:
                delay = interval - (now - self._last_request_at)
                if delay > 0:
                    self._sleep(delay)
                    now = self._clock()
            self._last_request_at = now

    @staticmethod
    def _retry_after(response: _Response) -> float | None:
        headers = {str(k).lower(): str(v) for k, v in (response.headers or {}).items()}
        value = headers.get("retry-after")
        if not value:
            return None
        try:
            return max(0.0, float(value))
        except ValueError:
            try:
                when = parsedate_to_datetime(value)
                return max(0.0, (when - datetime.now(timezone.utc)).total_seconds())
            except (TypeError, ValueError, OverflowError):
                return None

    def get(self, path: str, *, params: Mapping[str, Any] | None = None) -> dict[str, Any]:
        """GET one public endpoint, retrying throttles and transient failures."""

        normalized = "/" + path.lstrip("/")
        url = f"{self.base_url}{normalized}"
        request_params = dict(params or {})
        self._throttle()
        for attempt in range(self.max_retries + 1):
            with self._count_lock:
                self.request_count += 1
            try:
                response = self.transport.request(
                    "GET", url, params=request_params, timeout=self.timeout
                )
            except (OSError, TimeoutError):
                if attempt == self.max_retries:
                    raise
                self._sleep(min(30.0, self.backoff_seconds * (2**attempt)))
                continue
            status = response.status_code
            if 200 <= status < 300:
                return response.json()
            if status != 429 and not (500 <= status < 600):
                raise KalshiHTTPError(status, url, _safe_json(response))
            if attempt == self.max_retries:
                raise KalshiHTTPError(status, url, _safe_json(response))
            delay = self._retry_after(response)
            if delay is None:
                delay = min(30.0, self.backoff_seconds * (2**attempt))
            self._sleep(delay)
            # The explicit backoff is also the limiter wait.  Keeping retries in
            # this loop ensures the URL and parameters are byte-for-byte stable.
        raise AssertionError("unreachable")

    @staticmethod
    def route_path(
        path: str,
        *,
        timestamp: datetime | str | None,
        historical_cutoff: datetime | str | None,
    ) -> str:
        """Route a partitioned endpoint according to the historical cutoff.

        Kalshi publishes the cutoff as an instant.  At the boundary we choose
        historical, which is conservative and avoids omitting a settled market.
        """

        normalized = "/" + path.lstrip("/")
        if timestamp is None or historical_cutoff is None or normalized.startswith("/historical/"):
            return normalized
        if _as_utc(timestamp) <= _as_utc(historical_cutoff):
            return f"/historical{normalized}"
        return normalized

    @staticmethod
    def _is_market_list(path: str) -> bool:
        return path.rstrip("/") in {"/markets", "/historical/markets"}

    def iter_pages(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        timestamp: datetime | str | None = None,
        historical_cutoff: datetime | str | None = None,
        limit: int = 1000,
    ) -> Iterator[dict[str, Any]]:
        """Yield complete response pages while following every non-empty cursor."""

        if not 1 <= limit <= 1000:
            raise ValueError("Kalshi page limit must be between 1 and 1000")
        routed = self.route_path(
            path, timestamp=timestamp, historical_cutoff=historical_cutoff
        )
        page_params = dict(params or {})
        page_params.setdefault("limit", limit)
        if routed.rstrip("/") == "/events":
            # /events rejects limit > 200 with HTTP 400 (verified live 2026-09-29).
            page_params["limit"] = min(int(page_params["limit"]), EVENTS_PAGE_LIMIT)
        scoped = any(page_params.get(key) for key in ("tickers", "event_ticker", "series_ticker"))
        if self._is_market_list(routed) and not scoped:
            # Callers cannot accidentally collect the enormous MVE/combo corpus.
            # Kalshi rejects mve_filter combined with a tickers/event/series
            # filter (HTTP 400 on /historical/markets, verified 2026-09-29), so
            # scoped queries rely on the archive dropping combo rows itself.
            page_params["mve_filter"] = "exclude"
        initial_cursor = page_params.pop("cursor", None)
        cursor: str | None = str(initial_cursor) if initial_cursor else None
        while True:
            if cursor:
                page_params["cursor"] = cursor
            else:
                page_params.pop("cursor", None)
            page = self.get(routed, params=page_params)
            yield page
            next_cursor = page.get("cursor")
            if not next_cursor:
                return
            cursor = str(next_cursor)

    def paginate(
        self,
        path: str,
        *,
        item_key: str,
        params: Mapping[str, Any] | None = None,
        timestamp: datetime | str | None = None,
        historical_cutoff: datetime | str | None = None,
        limit: int = 1000,
    ) -> Iterator[dict[str, Any]]:
        for page in self.iter_pages(
            path,
            params=params,
            timestamp=timestamp,
            historical_cutoff=historical_cutoff,
            limit=limit,
        ):
            items = page.get(item_key, [])
            if not isinstance(items, list):
                raise ValueError(f"response field {item_key!r} is not a list")
            yield from items

    def historical_cutoff(self) -> datetime:
        payload = self.get("/historical/cutoff")
        return _as_utc(payload["market_settled_ts"])

    def markets(
        self,
        *,
        status: str = "settled",
        timestamp: datetime | str | None = None,
        historical_cutoff: datetime | str | None = None,
        **params: Any,
    ) -> Iterator[dict[str, Any]]:
        routed = self.route_path(
            "/markets", timestamp=timestamp, historical_cutoff=historical_cutoff
        )
        if not routed.startswith("/historical/"):
            params.setdefault("status", status)
        return self.paginate(
            routed,
            item_key="markets",
            params=params,
        )

    def event(self, ticker: str, *, with_nested_markets: bool = False) -> dict[str, Any]:
        params = {"with_nested_markets": "true"} if with_nested_markets else None
        return self.get(f"/events/{ticker}", params=params).get("event", {})

    def series(self, ticker: str) -> dict[str, Any]:
        return self.get(f"/series/{ticker}").get("series", {})

    def series_list(self, **params: Any) -> Iterator[dict[str, Any]]:
        return self.paginate("/series", item_key="series", params=params)

    def events(self, **params: Any) -> Iterator[dict[str, Any]]:
        return self.paginate("/events", item_key="events", params=params)

    def candlesticks(
        self,
        ticker: str,
        *,
        series_ticker: str,
        start_ts: int,
        end_ts: int,
        period_interval: int = 60,
        settlement_ts: datetime | str | None = None,
        historical_cutoff: datetime | str | None = None,
    ) -> list[dict[str, Any]]:
        if period_interval not in {1, 60, 1440}:
            raise ValueError("period_interval must be 1, 60, or 1440 minutes")
        historical = (
            settlement_ts is not None
            and historical_cutoff is not None
            and _as_utc(settlement_ts) <= _as_utc(historical_cutoff)
        )
        if historical:
            path = f"/historical/markets/{ticker}/candlesticks"
            duration = int(end_ts) - int(start_ts)
            if duration <= 9 * 86_400:
                windows = [(int(start_ts), int(end_ts))]
            else:
                windows = [
                    (int(start_ts), min(int(end_ts), int(start_ts) + 25 * 3_600)),
                    (max(int(start_ts), int(end_ts) - 7 * 86_400 - 3_600), int(end_ts)),
                ]
        else:
            path = f"/series/{series_ticker}/markets/{ticker}/candlesticks"
            windows = [(int(start_ts), int(end_ts))]
        rows: list[dict[str, Any]] = []
        for window_start, window_end in windows:
            payload = self.get(
                path,
                params={
                    "start_ts": window_start,
                    "end_ts": window_end,
                    "period_interval": period_interval,
                },
            )
            rows.extend(payload.get("candlesticks", []))
        return rows

    def batch_candlesticks(
        self,
        tickers: list[str],
        *,
        start_ts: int,
        end_ts: int,
        period_interval: int = 60,
    ) -> dict[str, list[dict[str, Any]]]:
        if not tickers:
            return {}
        if period_interval not in {1, 60, 1440}:
            raise ValueError("period_interval must be 1, 60, or 1440 minutes")
        result: dict[str, list[dict[str, Any]]] = {str(ticker): [] for ticker in tickers}
        step = period_interval * 60
        window_start = int(start_ts)
        final_end = int(end_ts)
        # A single ticker can itself span more than 10,000 hourly slots, so
        # split time first and ticker count second.
        max_span = step * 9_999
        while window_start <= final_end:
            window_end = min(final_end, window_start + max_span)
            slots = (window_end - window_start) // step + 1
            batch_size = min(100, max(1, 10_000 // slots))
            for offset in range(0, len(tickers), batch_size):
                batch = tickers[offset : offset + batch_size]
                payload = self.get(
                    "/markets/candlesticks",
                    params={
                        "market_tickers": ",".join(batch),
                        "start_ts": window_start,
                        "end_ts": window_end,
                        "period_interval": period_interval,
                    },
                )
                for row in payload.get("markets", []):
                    result.setdefault(str(row["market_ticker"]), []).extend(
                        row.get("candlesticks", [])
                    )
            if window_end >= final_end:
                break
            window_start = window_end + step
        return result


def _safe_json(response: _Response) -> Any:
    try:
        return response.json()
    except Exception:  # pragma: no cover - only malformed upstream error pages
        return None


__all__ = ["DEFAULT_BASE_URL", "KalshiClient", "KalshiHTTPError"]
