# APPM-008: Final feature stacking ceiling

- Project: Strategy app
- Date: 2026-04-17 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Shot-level data with expected FG
- Method tags: regression; holdout, backtest or replay
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
Stacking all clean-signal features raises the R2 ceiling materially.

## Design
Nested OLS models on 8-feat baseline plus xPPP, per-PT interaction, shot_rate, pct_3s.

## Result
Best +xPPP + per-pt interaction R2_hol +0.1244 (lift +0.0094); adding more features lowered holdout R2 (12f +0.1167).

## Failure evidence
Max lift +0.0094; doc calls ~0.12 the practical ceiling.

## Power and reliability


## Related
SHOT_QUALITY.md; STARTER_SHARE.md

## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\STACK_FINAL.md
