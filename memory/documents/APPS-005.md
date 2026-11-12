# APPS-005: Within-series should-vs-did hit rate (leverage_argmax contamination)

- Project: Strategy app
- Date: 2026-06-10 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: artifact_found
- Failure type: C_artifact
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: difference-in-differences; matched control
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
Teams' in-series play-type choices matched what the engine said they should do and this predicted success.

## Design
Should-vs-did comparison from _analyze_series_learning.py (findings file at repo root, not read).

## Result
~92.6% hit rate

## Failure evidence
'Engine used leverage_argmax fallback -> inflated CUT-style picks; ~92.6% hit rate'.

## Power and reliability


## Related
SQ2 decision quality hit rate

## Notes
Date is mtime of the deprecated README; original findings file is outside this slice.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\validation\deprecated\README.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\validation\README.md
