# APPA-009: Series adaptation experiment: static vs rolling vs adversarial-agent predictors

- Project: Team Adaptation
- Date: 2026-05-05 (doc)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: unknown
- Verdict: null
- Failure type: C_artifact
- Knowable in advance: unclear
- Runs: 12
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes; LLM or agent outputs
- Method tags: LLM agent run
- Limitation tags: small sample
- Variable tags: play-type share / mix
- Paper: 

## Hypothesis
Adversarial LLM agents predict next-game play-type mix better than static and rolling baselines.

## Design
12 playoff series, 4-6 game transitions each (68 transitions); composite accuracy, L1 PT distance, direction/magnitude hit rates, agent hypothesis precision.

## Result
Rolling beats or ties static in all 12 (e.g. bos_mia 0.835 vs 0.748; den_okc tie agents=rolling 0.859). Agents below rolling in 11/12. Agent Dir%/Mag% 0.0 and L1 scheme 0.000 in every series. Hypothesis precision 0/0 in 9 series, 0/1 (den_min_2324, ind_nyk_2425), 0/2 (lal_hou_2526).

## Failure evidence
Agent Dir%/Mag% 0.0 in all 12 series and empty Agent predictions sections in most transitions; the few listed hypotheses (e.g. lal_hou 0/2) never scored as hits.

## Power and reliability
4-6 transitions per series; 68 total

## Related
APPA-008

## Notes
Updated after reading the remaining 9 series files. Agent arm still looks broken rather than tested; rolling vs static is a real comparison.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADAPTATION_EXPERIMENT_BATCH.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADAPTATION_EXPERIMENT_bos_mia_2223.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADAPTATION_EXPERIMENT_bos_nyk_2425.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADAPTATION_EXPERIMENT_den_lac_2425.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADAPTATION_EXPERIMENT_den_min_2324.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADAPTATION_EXPERIMENT_den_okc_2425.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADAPTATION_EXPERIMENT_gsw_hou_2425.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADAPTATION_EXPERIMENT_ind_nyk_2324.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADAPTATION_EXPERIMENT_ind_nyk_2425.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADAPTATION_EXPERIMENT_ind_okc_2425.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADAPTATION_EXPERIMENT_lal_hou_2526.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADAPTATION_EXPERIMENT_min_okc_2425.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADAPTATION_EXPERIMENT_phi_bos_2526.md

## Related records (ids resolved to merged records)
APPA-008
