# Crypto observatory — Phase 2

This observer uses public data only, never trades or places orders, and does not publish an edge or trading signal.

## Data availability

No production crypto chunks have been collected in this offline build. Not tested: only 0 days.

## Method

The weekly analysis reports Kalshi perp basis against Coinbase and Kraken at midpoint and executable $100/$1,000 prices, funding carry with strict no-look-ahead timing and settled cash only, bracket consistency after fees, and discovery-only bracket calibration from the strictly prior 24 hours of Coinbase 15-minute volatility.

Executable basis walks both the perp and spot books. Carry is separated by perp and notional and charges measured full-round-trip spreads plus genuine entry and exit fees for every maker/taker Coinbase base and pessimistic case. Calibration reports both market and simple-lognormal Brier score and log loss after settlement.

All inference reuses the Phase 1 append-only ledger format, UTC-day clustered intervals, one-shot discovery/confirmation lock, ID digests, actual observation ranges, and Benjamini–Hochberg correction. Phase 2 has its own prospectively fixed holdout: discovery ends at **2027-01-01 00:00 UTC**. Later data remains untouched unless the report is explicitly run as caught up. No hypothesis is tested before 30 independent days. Kraken cost comparisons are labeled a lower bound unless a Kraken commission is configured.
