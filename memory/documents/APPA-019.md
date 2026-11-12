# APPA-019: Usage-curve constrained optimizer (A2) vs baseline

- Project: Strategy app
- Date: 2026-04-14 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: no
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups; Box score and traditional stats
- Method tags: holdout, backtest or replay
- Limitation tags: label or classification error
- Variable tags: play-type share / mix
- Paper: 

## Hypothesis
Diminishing-returns usage curves improve recommendations over static argmax and baseline.

## Design
Same 23,922 holdout possessions; per-possession and distribution-level evaluation.

## Result
A2 -8.32 pts/100 vs baseline; A2 vs A -6.84; A2 outperforms baseline 47/240. Distribution: A2 mix +13.40 pts/100 vs actual (beats 217/240) but -24.85 vs B argmax.

## Failure evidence
-8.32 pts/100 vs baseline on 23,922 possessions.

## Power and reliability
23,922 possessions

## Related
APPA-018

## Notes
Doc labels -6.84 as an 'improvement'; number and wording disagree.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\EVAL_REPORT_v3.md

## Related records (ids resolved to merged records)
APPA-018
