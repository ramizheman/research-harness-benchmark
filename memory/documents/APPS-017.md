# APPS-017: Execution conformance of observed mix vs recommended plan

- Project: Strategy app
- Date: 2026-04-20 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 8
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: matched control
- Limitation tags: 
- Variable tags: play-type share / mix
- Paper: 

## Hypothesis
Teams' observed play-type mix in a game matches the model's recommended opener.

## Design
Single 2025-26 playoff G1s, 4 games x 2 offenses; leverage-weighted gap between observed and recommended mix.

## Result
Avg |delta| on leverage buckets 4.5pp to 24.0pp; 4 of 8 sides best matched opener #3, not rank-1.

## Failure evidence
CUT and PNR muted for tagger floor; single-game horizon; no outcome comparison.

## Power and reliability
~100 possessions per game

## Related
Opener leverage decomposition

## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\CONFORMANCE_PHI_vs_BOS_0042500111.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\CONFORMANCE_PHX_vs_OKC_0042500141.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\CONFORMANCE_POR_vs_SAS_0042500151.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\CONFORMANCE_ORL_vs_DET_0042500101.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\execution_conformance_ORL_DET_0042500101.md
