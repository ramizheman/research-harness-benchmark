# APPM-020: Within-series SHOULD vs DID alignment

- Project: Strategy app
- Date: 2026-05-16 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: inconclusive
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Playoff series outcomes
- Method tags: difference-in-differences; matched control
- Limitation tags: small sample
- Variable tags: PPP (points per possession); play-type share / mix
- Paper: 

## Hypothesis
Teams that shift toward the engine's prescribed mix win more and improve PPP.

## Design
100-104 (series,team) rows; G1 vs G2..N shift; direction-match and cosine vs prescription.

## Result
Shift toward rec PT: win rate 50.0% vs 50.0%; only 8 rows had a SHOULD vector (aligned 4/6 wins vs 1/2); A3 rec PT beat modal PT 87/94 (92.6%).

## Failure evidence
96 of 104 rows had no vector prescription; 'Sample too small at this gate'.

## Power and reliability
n=8 for vector test

## Related


## Notes
Knowable: decision_context files with empty openers existed before analysis.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\within_series_should_vs_did_findings.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\within_series_should_vs_did_data.csv
