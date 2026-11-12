# APPM-010: Scheme-adjusted vs baseline Spearman across canonical series

- Project: Strategy app
- Date: 2026-05-03 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: correlation
- Limitation tags: small sample
- Variable tags: 
- Paper: 

## Hypothesis
Scheme-adjusted engine (Step 2) ranks play types better than baseline (Step 1).

## Design
Per team-series Spearman for 84 team rows across canonical playoff slugs.

## Result
Mean Spearman +0.524 -> +0.579 (median +0.548 -> +0.631); improves 42/84, worsens 8/84, noise 34/84.

## Failure evidence
Mean delta +0.055; 42 improve vs 8 worse.

## Power and reliability
n=84 team rows; no test

## Related


## Notes
Spearman target definition not stated in the file.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\SEASON_COMPARISON.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_season_comparison.py

## Finding status
supported in source; independent replication not recorded
