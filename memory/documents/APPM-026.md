# APPM-026: Counter-tier validation Test 1 (BEST vs AVOID, 2025-26 and 2024-25 playoffs)

- Project: Strategy app
- Date: 2026-06-19 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 2
- Dataset tags: Playoff series outcomes
- Method tags: correlation
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Pre-game BEST-tier counters outscore AVOID-tier counters after suppression triggers.

## Design
10 series 2025-26 (n=519 obs) and 15 series 2024-25 (n=634); Spearman tier rank vs PPP, Kruskal-Wallis, Mann-Whitney.

## Result
2025-26 rho -0.3246 (n=519), BEST 1.460 vs AVOID 0.845; 2024-25 rho -0.2625 (n=634), BEST 1.424 vs AVOID 0.799; KW H 158.7/158.96.

## Failure evidence
BEST > AVOID p=0.0 in both seasons.

## Power and reliability
n=519 / 634

## Related
BEST-AVOID OOS gap (presentation)

## Notes
AVOID_OVERRIDE tier reclassifies AVOID by rest-of-game PPP (outcome-based), so smart-vs-AVOID comparisons are circular; INSUFF_EVIDENCE 220/519 and 324/634.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\OVERNIGHT_SUMMARY.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_run_10series_validation.py
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_overnight_batch.py

## Finding status
supported in source; independent replication not recorded
