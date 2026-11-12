# APPM-003: Residual calibration A/B (global/linear/OLS/per-team)

- Project: Strategy app
- Date: 2026-04-17 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: 
- Method tags: matched control; regression; holdout, backtest or replay; calibration scoring
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
A residual calibrator fit on VAL improves out-of-sample R2 of the equilibrium matchup evaluator.

## Design
Blended A3 evaluator trained on 523,517 sequences; calibrators fit on VAL (690 cells), scored on HOLDOUT (520 cells); with and without 30-game recency half-life.

## Result
Holdout R2 baseline -0.1981 -> OLS +0.0323 (net lift +0.2305); HL30 variant baseline -0.1587 -> OLS +0.0321. Per-team R2 val +0.2449 but holdout +0.0213.

## Failure evidence
OLS holdout R2 +0.0323 vs baseline -0.1981.

## Power and reliability
val 690 / holdout 520 cells

## Related
VARIANCE_DIAG.md

## Notes
Absolute R2 remains ~0.03; per-team calibrator overfits val (0.24 -> 0.02).

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\RESIDUAL_REPORT.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\RESIDUAL_HL30.md

## Finding status
supported in source; independent replication not recorded
