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
