# APPA-031: Case studies: alignment with engine mix vs ORtg (+3.3 claim)

- Project: Strategy app
- Date: 2026-04-18 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: supported
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Box score and traditional stats
- Method tags: regression; holdout, backtest or replay; correlation; case study; calibration scoring
- Limitation tags: label or classification error
- Variable tags: play-type share / mix; net rating / ORtg
- Paper: 

## Hypothesis
Games where the team mix was closest to the engine recommendation score more after strength adjustment.

## Design
908 holdout game-team pairs; terciles of L1 distance; 6 illustrative cases with kernel unconstrained vs +/-5pp coachable vs calibrated (10-feature residual calibrator val R2 +0.1244) and 4 named-scheme robustness.

## Result
Closest vs most-deviated tercile +3.3 ORtg adjusted (raw +5.2); Spearman rho >0.4 in 62% of games. Cases: GSW-LAL rho 1.00 coachable +28.0 ORtg; MIA-BOS rho 0.80 aligned residual +27.9; NYK-LAL rho 0.80 coachable +25.0; CLE-PHX rho -0.80; LAL-GSW rho 0.90 residual +12.3 despite deviation; MIN-DEN rho 0.10 L1=0.99 residual -29.8.

## Failure evidence
No CI or test reported for +3.3; in-game PT ranking used as rho target shares outcome data; 3 of 6 cases are labeled honest counter-examples; every kernel rec is CUT-heavy.

## Power and reliability
908 game-team pairs; 6 cases

## Related
APPA-024; APPA-033; APPA-063

## Notes
Contradicted by series-level alignment regression r=-0.032 (APPA-024). Coachable caps still +14.3 to +28.0 ORtg, which are model-internal not observed. Full file now read.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\CASE_STUDIES.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\LAYER_AUDIT.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPA-024, APPA-033, APPA-063
