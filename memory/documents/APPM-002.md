# APPM-002: Top-player on/off features in calibrator

- Project: Strategy app
- Date: 2026-04-17 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: 
- Method tags: regression; holdout, backtest or replay; calibration scoring
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
Adding star on/off presence features (top-1 or top-3 players) improves holdout R2 over shipped 8-feature OLS.

## Design
Train-learned on/off deltas per top-N player, swept k_player shrinkage; val 690 cells, holdout 520 cells; compare R2_hol to 8-feat baseline +0.1150.

## Result
top_n=3 best R2_hol +0.0971 (lift -0.0179); top_n=1 best R2_hol +0.0865 (lift -0.0285).

## Failure evidence
Holdout lift negative at every k (-0.0179 / -0.0285).

## Power and reliability
holdout 520 cells

## Related
STARTER_SHARE.md

## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ONOFF.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ONOFF_TOP1.md
