# APPM-004: Calibration variance diagnostic (matchup signal collapse)

- Project: Strategy app
- Date: 2026-04-17 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: artifact_found
- Failure type: C_artifact
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: 
- Method tags: matched control; regression; holdout, backtest or replay; ablation; calibration scoring
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
The calibrated pipeline preserves enough variance and the matchup model pred_raw carries usable signal.

## Design
690 val / 520 holdout cells: variance ratios, slope test, drop-one and single-feature ablation, residual structure.

## Result
pred_cal variance 3.9% of actual; pred_raw alone R2 +0.0042; dropping pred_raw changes R2 by +0.0002; team_mult alone +0.0392.

## Failure evidence
pred_raw contributes ~0 (dR2 +0.0002); SHRINKAGE_SWEEP later showed the equilibrium optimizer collapses signal (R2 +0.004 vs +0.045 with actual usage).

## Power and reliability
holdout 520 cells

## Related
Shrinkage sweep (SHRINKAGE_SWEEP.md)

## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\VARIANCE_DIAG.md
