# APPS-004: Post-hoc calibrated decision quality hit rate (--calibrated)

- Project: Strategy app
- Date: 2026-05-23 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: artifact_found
- Failure type: C_artifact
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: calibration scoring
- Limitation tags: small sample
- Variable tags: 
- Paper: 

## Hypothesis
Applying playoff calibration scalars (DRIVE excluded) raises the engine's hit rate vs modal PT.

## Design
Post-hoc scalar reweighting of cached Neo4j PT distributions instead of re-running the engine; 80 scoreable pairs.

## Result
Hit rate 51.7% (31/60) before vs 96.2% (77/80) after; high-conf 42.9% -> 96.6%; CUT recs 66 with 95%.

## Failure evidence
Deprecated: 'Post-hoc PPP scalars on Neo4j mix, not is_playoff=True engine run; ~96%' and 'inflates hit rate'.

## Power and reliability
n=80

## Related
SQ2 decision quality hit rate

## Notes
Calibration was tuned on the same series it was scored on.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\decision_quality_findings.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\validation\deprecated\README.md
