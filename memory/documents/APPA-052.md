# APPA-052: CUT feasibility cap: BEST-AVOID gap without CUT-heavy games

- Project: Defensive Suppression
- Date: 2026-06-20 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: no
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: correlation
- Limitation tags: 
- Variable tags: play-type share / mix
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
The BEST vs AVOID gap is inflated by games where CUT exceeds 15% of H2 mix.

## Design
55-series trigger table + Neo4j H2 mix; exclude games with CUT share >15%.

## Result
All games BEST 1.473 vs AVOID 0.853 gap +0.620 MW p=0.0000 Spearman -0.316 n=2,544. CUT<=15%: +0.625 n=2,508. CUT>15%: +0.163 n.s. n=36. Only 4/272 games had CUT>15%.

## Failure evidence
Removing the 4 CUT-heavy games slightly strengthens the gap (+0.620 to +0.625).

## Power and reliability
2,544 rows; 272 games

## Related
APPA-036; APPA-033

## Notes
This uses the ungated +0.620 55-series gap (stale relative to n-gated +0.375 / BEST-vs-continue +0.445). Robustness direction still holds on this CSV.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPA-036, APPA-033
