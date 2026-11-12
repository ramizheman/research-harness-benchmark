# APPS-071: Memoryless Monte Carlo possession simulation (generative check)

- Project: Strategy app
- Date: 2026-06-15 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: matched control; regression; simulation; calibration scoring
- Limitation tags: 
- Variable tags: PPP (points per possession); play-type share / mix
- Paper: 

## Hypothesis
A memoryless state-driven process calibrated to NBA micro-stats can match uncalibrated distributional targets (esp. lag-1 scoring autocorr).

## Design
10000 games x 200 possessions. Constraint state_{t+1} indep play_type_t | state_t. Not a validation of empirical findings used as anchors.

## Result
Uncalibrated: PPP std 1.149 vs sim 1.152; lag-1 scoring autocorr real -0.0022 vs sim +0.0029; share 0 pts 0.475 vs 0.484. Sequence-only R2=0.00000; state-only 0.00002.

## Failure evidence
Generative existence proof, not independent evidence. Sequence R2~0 by construction of the constraint.

## Power and reliability
10,000 games x 200 possessions

## Related
APPS-072

## Notes
Status line in the report: GENERATIVE / ILLUSTRATIVE, not validation.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\mc_simulation.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\mc_simulation.py

## Related records (ids resolved to merged records)
APPS-072
