# APPA-055: All play types x Q1-Q4 gradient on 30 stars

- Project: Defensive Suppression
- Date: 2026-06-03 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: no
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: 
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
Only PUTBACK shows a fatigue signature (near-zero Q1 suppression compounding to Q4) across the full 30-star panel.

## Design
Possession-weighted league delta of star PPP vs own-quarter baseline; no n floor; 30 stars x 9 opp PTs.

## Result
PUTBACK Q1 d=-0.001 to Q4 d=-0.233, Q1->Q4 -0.232 (Q1 poss 722 / Q4 531). Other PTs suppress in Q1 already; largest other gradient DRIVE -0.060. CUT reverses +0.020. TRANSITION -0.053.

## Failure evidence
On the full 30-star weighted panel, only PUTBACK is near-zero in Q1 and heavy in Q4.

## Power and reliability
30 stars; PUTBACK Q4 n=531 poss

## Related
APPA-054; APPA-056

## Notes
Section Q n>=30 gate gave Q1 -0.009 to Q4 -0.289; no-floor weighted gives the same qualitative story.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPA-054, APPA-056
