# APPM-006: Starter-share features in calibrator

- Project: Strategy app
- Date: 2026-04-17 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: partial
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups
- Method tags: regression; holdout, backtest or replay; calibration scoring
- Limitation tags: 
- Variable tags: play-type share / mix
- Paper: 

## Hypothesis
Offensive/defensive starter-share features improve holdout R2.

## Design
Add 2 OLS features (top-5 by train possessions) to shipped 6-feat calibrator; val 690 / holdout cells.

## Result
8-feat R2_hol +0.1150 vs 6-feat +0.0835 (lift +0.0315).

## Failure evidence
Lift +0.0315 > +0.01 ship threshold.

## Power and reliability


## Related


## Notes
Ship threshold stated in doc.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\STARTER_SHARE.md

## Finding status
supported in source; independent replication not recorded
