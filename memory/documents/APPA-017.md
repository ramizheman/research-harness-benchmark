# APPA-017: A5 player-routing and A5b defensive attention penalty

- Project: Strategy app
- Date: 2026-04-15 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: no
- Runs: 3
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: matched control; calibration scoring
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
Routing possessions to each play type's best player adds value over A3, and survives defensive attention adaptation.

## Design
Calibration framework V4-V6; A5 vs A3 and A5b vs A5 signal in pts/100.

## Result
V4 A5 vs A3 +0.77; V5 +0.94 (A5b vs A5 +0.01); V6 (520 matchups) A5 vs A3 +0.03, A5b vs A5 -0.00.

## Failure evidence
Shrinks from +0.94 to +0.03 pts/100 on the larger 520-matchup sample.

## Power and reliability
520 matchups

## Related
APPA-016

## Notes
Model-scored, not observed outcomes.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\CALIBRATION_REPORT_V6.md

## Related records (ids resolved to merged records)
APPA-016
