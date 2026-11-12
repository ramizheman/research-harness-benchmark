# APPA-021: Alpha blend of actual-usage and equilibrium predictions

- Project: Strategy app
- Date: 2026-04-17 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: partial
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: no
- Runs: 1
- Dataset tags: Box score and traditional stats
- Method tags: regression; holdout, backtest or replay; calibration scoring
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
Blending equilibrium with actual-usage prediction beats either alone.

## Design
val 690 cells (84,319 poss), holdout 520 cells (69,876 poss); alpha sweep raw and OLS-calibrated.

## Result
Best alpha = 1.00 (pure actual usage): R2 hol +0.0451 raw, +0.0672 calibrated; fullEQ R2 -0.1981.

## Failure evidence
Best alpha ~1.0, meaning 'equilibrium is NOT predictive' per pre-written cheat sheet.

## Power and reliability
520 holdout cells

## Related
APPA-020

## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ALPHA_BLEND.md

## Related records (ids resolved to merged records)
APPA-020
