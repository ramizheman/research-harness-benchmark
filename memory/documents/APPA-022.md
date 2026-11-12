# APPA-022: Blended prior-season shrinkage evaluator and k sweep

- Project: Strategy app
- Date: 2026-04-16 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: partial
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: no
- Runs: 4
- Dataset tags: 
- Method tags: regression; simulation
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
Blending prior seasons helps early season without hurting late season.

## Design
Fixed test 155 late-2024-25 games; current-only vs pooled vs blended (k=5,10,20,30); early-season simulation with 150 games.

## Result
Late: blended k=30 worse on 5/5 metrics (R2 -0.1065 vs -0.0866). Early: blended better 5/5 (R2 -0.2624 vs -0.4508; win-side 55.8% vs 52.5%). k sweep recommends k~5.

## Failure evidence
Early-season blend improves all 5 metrics, but all R2 remain negative.

## Power and reliability
155 test games

## Related
APPA-016

## Notes
Supported only as relative improvement; absolute accuracy stays below a mean predictor.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\BLENDED_REPORT.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\K_SWEEP.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPA-016
