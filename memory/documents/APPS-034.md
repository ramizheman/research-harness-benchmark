# APPS-034: Oracle player-routing sensitivity (RS holdout)

- Project: Strategy app
- Date: 2026-06-18 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: 
- Method tags: holdout, backtest or replay
- Limitation tags: small sample
- Variable tags: 
- Paper: 

## Hypothesis
Routing regret (+0.137 baseline) is not an artifact of low-volume bench oracles.

## Design
RS holdout BEST rows n>=5 (980). Ablate min_n gate and top-K rotation filter.

## Result
Baseline min_n=3: regret +0.137, 63.0% oracle>actual, n=980. min_n=20: +0.050, 52.5%, n=703. Recommended top-8 + min_n=5: +0.094, 57.9%, n=970. Strict top-4+n5: +0.068, 54.8%.

## Failure evidence
Regret shrinks under stricter gates but stays positive; recommended cite is +0.094 not +0.137.

## Power and reliability
n=980 BEST rows baseline

## Related
APPS-020; APPS-009

## Notes
Shrinkage prior weight=50 means n=3 H2H is ~94% league mean. PO oracle player tables flagged exploratory (typical n=3-8).

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\oracle_sensitivity.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\rs_holdout_25_26\rs_player_routing_regret.md

## Related records (ids resolved to merged records)
APPS-020, APPS-009
