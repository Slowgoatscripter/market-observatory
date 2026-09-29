"""Read-only Kalshi collection and analysis support.

Nothing in this package authenticates, submits orders, or trades.
"""

from .client import KalshiClient

__all__ = ["KalshiClient"]

