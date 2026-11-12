# APPM-005: Matchup-model shrinkage K sweep

- Project: Strategy app
- Date: 2026-04-17 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Box score and traditional stats
- Method tags: matched control; regression; holdout, backtest or replay; calibration scoring
- Limitation tags: 
- Variable tags: play-type share / mix
- Paper: 

## Hypothesis
Lowering SHRINKAGE_K in MatchupPPPModel recovers signal lost to over-shrinkage.

## Design
Sweep k=5..5000 on 690 val / 520 holdout cells using actual usage mix; R2 raw and OLS-calibrated on holdout.

## Result
Hypothesis REJECTED: k=5 R2 alone +0.018, k=50 +0.045, k=200 +0.058; best OLS R2 +0.0744 at k=500 (lift +0.0072 vs k=50). Actual-usage path R2 +0.045 vs equilibrium path +0.004.

## Failure evidence
Lower k gives wider spread but lower R2 (k=5 +0.018 vs k=200 +0.058).

## Power and reliability
holdout 520 cells

## Related
VARIANCE_DIAG.md

## Notes
Byproduct finding: downstream equilibrium optimizer eats the matchup signal (10x).

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\SHRINKAGE_SWEEP.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\SHRINKAGE_PREDICTIVE.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\SHRINKAGE_PREDICTIVE_HIGH.md
