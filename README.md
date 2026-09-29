# Market Observatory

Market Observatory is a public, read-only research project. Phase 1 collects public
Kalshi settlement and hourly candle data, keeps a scale-aware sample, runs preregistered
statistical checks, and publishes the results in plain English.

It never trades, never places orders, and never uses a Kalshi account. Findings are
descriptive statistics—not trading signals. A result that survives held-back confirmation
is not published as an “edge”; any later strategy research belongs in a private project.

## What it records

Each retained settled market has its identity, outcome, volume, sampling weight, and price
snapshots one hour, one day, and seven days before close plus one hour and one day after
listing. Combo/parlay markets are excluded at the API. Slow series are retained in full.
Fast series (hourly or faster, or markets open for at most a day) are sampled
deterministically by event at 1%; every retained fast event receives weight 100 so aggregate
estimates remain unbiased. Sampling whole events also preserves the dependence structure
used by event-clustered intervals. Sports are treated the same way regardless of series
frequency: a deterministic 1% sample by event with weight 100. Every slower non-Sports
category remains complete. This also limits retention of markets the Montana-based owner
cannot trade.

Each successful archive run creates exactly one append-only compressed CSV chunk under
`data/kalshi/chunks/`, named with the run's UTC start time, such as
`20260929T123456Z.csv.gz`. Committed chunks are never rewritten or deleted. The report
loader reads every chunk and deduplicates by ticker, keeping the row from the newest chunk.
Rows contain only compact identity/outcome fields and fixed-horizon prices; times use UTC
ISO seconds and prices are rounded to four decimals. The committed archive budget is about
300 MB. Archive jobs emit a prominent warning once cumulative chunk storage exceeds 250 MB.
Cursor updates are committed only after the run's chunk is durable, so a failed run safely
repeats its last page instead of advancing past unwritten rows.

Backfill is series-driven because Kalshi's historical market endpoint is newest-first and
has no time filters. The collector caches the paginated series catalog for one hour in the
git-ignored `data/kalshi/_cache/` directory, never in committed archive state. Newly seen
series receive a complete first walk before joining incremental updates. Slow series are
walked by `series_ticker`. For fast series, events are paged and hash-sampled before any
market or candle request. Per-series cursors and finished series are stored in
`data/kalshi/archive-state.json`. Once every series is complete the state records
`caught_up: true`, and later runs update only the live tier. Each run prints request,
kept-market, sampling-skip, rows-written, chunk-byte, cumulative-size, and elapsed-time
counts in the job log.

## Statistical discipline

Discovery contains markets settled before April 1, 2026 (`2026-04-01T00:00:00Z`). The
confirmation window begins at that instant and ends on the date its check is run. A
hypothesis may use that window once, and confirmation is refused until archive state says
`caught_up: true`. Until then reports say that confirmation waits for archive completion.

The append-only `data/hypotheses.jsonl` audit log retains every run, but the ledger stores
only a record count, settlement-time range, and SHA-256 digest of sorted market IDs—not the
IDs themselves. Benjamini–Hochberg correction counts the latest discovery run for each
unique hypothesis; confirmation runs form a separate correction family. Discovery reruns
therefore do not inflate the current test count. Confidence intervals cluster by event, not
by contract.

Return checks assume an immediately executable taker purchase: YES at the YES ask and NO
at `1 - YES bid`. The modeled quadratic taker fee is
`ceil_to_cent(0.07 × contracts × P × (1-P))`. We do not model maker execution. The compact
chunk schema deliberately omits series fee metadata, so reports use the standard quadratic
taker multiplier of 1; this assumption is stated in every machine-readable report.

## Run locally

Install [uv](https://docs.astral.sh/uv/) and Python 3.13, then:

```console
uv sync --dev
uv run pytest
uv run kalshi-archive --mode auto --max-minutes 43
uv run kalshi-report
```

All tests are offline and use the captured responses in `tests/fixtures/kalshi/`. The
archive command is the only command that contacts Kalshi. It defaults to the public
`https://external-api.kalshi.com/trade-api/v2` host and requires no credentials.

To receive the weekly digest, set `NTFY_TOPIC` in the job environment. It may be either a
topic name (sent through `https://ntfy.sh`) or a complete ntfy URL. Notification failure is
best-effort and never fails report generation. Never commit topic names or other secrets.

## Outputs

- `data/kalshi/chunks/YYYYMMDDTHHMMSSZ.csv.gz` — immutable append-only run chunks
- `data/findings.json` — machine-readable findings
- `reports/kalshi.md` — plain-English report with discovery/confirmation labels
- `data/hypotheses.jsonl` — append-only audit trail of every statistical test run

Scheduled GitHub Actions continue backfill every three hours until `caught_up`, then run the
live incremental update. The weekly report gates confirmation on that state. Both jobs share
one concurrency group, expose the per-run counts in their logs, and commit only generated
data/report changes as `github-actions[bot]`.

## Phase 2: crypto observatory

Phase 2 is also a public-data, watch-only research project: it performs no trading, never
places an order, and never publishes an edge. It uses keyless, public endpoints that were
available from a U.S. IP when the collector was built. The supported sources are Kalshi
perpetual futures and crypto brackets, Coinbase Exchange spot, and Kraken spot.

For every active Kalshi perp, the collector records compact, scaled-integer bid, ask, last,
mark, reference-price, open-interest, funding-estimate, and top-of-book observations. It
then looks for an exact USD spot market for the same underlying: the Coinbase policy is
`UNDERLYING-USD`; the Kraken policy selects Kraken's enabled USD pair for that underlying
(including Kraken's exchange symbols such as XBT for BTC), without silently substituting a
stablecoin quote. Missing USD pairs are skipped. Spot books retain the depth required to
calculate executable prices at $100 and $1,000 notionals.

The bracket collector covers KXBTC, KXBTCD, KXETH, and KXETHD. For each series it selects
the nearest open event by close time and also the next distinct daily-close event, when one
exists. KXBTC and KXETH are mutually exclusive ranges; KXBTCD and KXETHD are directional
threshold ladders. These contracts settle from the CF Benchmarks Real Time Index (RTI),
using its 60-second average immediately before expiry. Reports check executable range sums
and ladder monotonicity, study perp basis and funding carry without look-ahead, and keep
bracket calibration in discovery until at least 30 independent days are available. The
Phase 1 hypothesis-ledger, Benjamini–Hochberg, and day-clustered interval discipline applies.

Collection writes one immutable, append-only `csv.gz` chunk per source per UTC hour under
`data/crypto/chunks/`; a committed chunk is never rewritten. Only cursors and the last
settled funding event fetched are kept in the small `data/crypto/crypto-state.json` state
file. Every chunk logs its bytes and cumulative storage. The annual budget is under 300 MB,
and collection warns when cumulative storage exceeds 250 MB.

The funding simulations state costs explicitly. Kalshi perps use 0.02% maker or 0.12%
taker per side. Coinbase spot uses a 0.50% maker / 0.90% taker base case and a 0.60% maker /
1.20% taker pessimistic case, per side, plus measured executable spread at both notionals.
Kraken observations provide an independent spot basis comparison, but the carry simulation
does not assume a Kraken trading fee: Kraken fees are tier-dependent and must be supplied
for any separate executable analysis. These are fee assumptions for retrospective research,
not claims about any user's actual fee tier.

Deribit, OKX global, and Bybit are excluded because they are not U.S.-compatible under this
project's source policy. Hyperliquid is optional and disabled by default because its terms
restrict U.S. users; scheduled collection does not enable it.

Run the offline tests or the Phase 2 commands locally with:

```console
uv run pytest -q
uv run crypto-collect --interval-minutes 15 --max-minutes 340
uv run crypto-report
```

The collector is the only Phase 2 command that contacts source APIs. The report reads the
immutable local chunks and writes `reports/crypto.md` plus the append-only
`data/crypto/hypotheses.jsonl` audit ledger. As throughout Market Observatory: no trading,
and no publishing an edge.
