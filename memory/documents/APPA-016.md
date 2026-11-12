# APPA-016: Per-team calibration: model 'signal' (bias) vs actual PPP, V1-V6

- Project: Strategy app
- Date: 2026-04-15 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: no
- Runs: 6
- Dataset tags: 
- Method tags: matched control; regression; calibration scoring
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
A3 predicted PPP exceeds actual (treated as validated optimization signal) and is well calibrated.

## Design
V1-V5: 240 matchups, 23,922 poss; V6: 520 matchups, 69,876 poss (season_engines); bias, MAE, RMSE, R2, win-side accuracy.

## Result
V1 bias +0.0112 (+1.12 pts/100), R2 -0.1758, win-side 58.8%; V2 +1.69; V3 +1.26; V6 bias -0.0012 (-0.12 pts/100), R2 0.0323, win-side 61.9%, model>actual 47.5%.

## Failure evidence
At 520 matchups / 69,876 poss the signal is -0.12 pts/100 and R2 0.03.

## Power and reliability
520 matchups, 69,876 possessions

## Related
APPA-017; APPA-020

## Notes
Treating positive prediction bias as 'validated signal' is conceptually flawed. V6 template text says 'it does: 47.5%' for an expected >50%, so the conclusion contradicts the number.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\CALIBRATION_REPORT.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\CALIBRATION_REPORT_V6.md

## Related records (ids resolved to merged records)
APPA-017, APPA-020
