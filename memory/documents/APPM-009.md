# APPM-009: More training seasons (fixed-holdout A/B)

- Project: Strategy app
- Date: 2026-04-16 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: reversed
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 2
- Dataset tags: 
- Method tags: regression; holdout, backtest or replay
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
Training on 3 seasons instead of 2024-25 only improves prediction on a fixed late-2024-25 test set.

## Design
Same 155 test games / 240 cells scored by both engines for A3, A5, A5b; raw and normalized variants.

## Result
After worse on 5/5 metrics: A3 R2 -0.0866 -> -0.2225 (normalized -0.2285); win-side accuracy 65.0% -> 48.3% (53.3% normalized).

## Failure evidence
0/5 metric wins in both raw and normalized runs.

## Power and reliability
240 cells, 120 pairs

## Related
STRATEGY_V2_RESULTS recency weighting

## Notes
Later recency weighting (half-life 0.5 seasons) adopted.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\SEASON_COMPARISON_FIXED.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\SEASON_COMPARISON_NORMALIZED.md
