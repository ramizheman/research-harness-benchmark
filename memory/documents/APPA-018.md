# APPA-018: Decision value test: kernel argmax vs NBA baseline (v1 leak, v2 fixed)

- Project: Strategy app
- Date: 2026-04-14 (mtime)
- Topic: Lineup and matchup effects
- Pre-specified: no
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: no
- Runs: 2
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: matched control; holdout, backtest or replay; calibration scoring
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
Kernel model A play-type recommendations add value over a league-adjusted baseline on holdout.

## Design
23,922 scored holdout possessions; decision regret, value added per 100, calibration; v2 fixes oracle leakage and adds feasibility filter.

## Result
v1: A -4.51 pts/100 vs baseline; v2: -1.48 pts/100, regret 0.1648 vs 0.1556, A outperforms in 9/240 matchups; recommendations ~88% CUT.

## Failure evidence
Baseline wins on 23,922 possessions in both versions.

## Power and reliability
23,922 possessions, 240 matchups

## Related
APPA-019

## Notes
v1 regret oracle used future (holdout) data; fixed in v2.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\EVAL_REPORT.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\EVAL_REPORT_v2.md

## Related records (ids resolved to merged records)
APPA-019

## Same study family
SF11 (duplicate_records): CHT-005
shared v1 -4.51 and v2 -1.48 pts/100, regret 0.1648 | Verdicts differ: null vs failed_gate.
