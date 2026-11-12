# APPS-072: MC suppression check: memoryless sim vs Paper 1 DiD +0.408

- Project: Strategy app
- Date: 2026-07-12 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: partial
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups
- Method tags: difference-in-differences; matched control; simulation
- Limitation tags: selection or regression to the mean
- Variable tags: 
- Paper: 

## Hypothesis
A memoryless process matching possession micro-stats will reproduce the Paper 1 matched DiD suppression excess.

## Design
Same 10000x200 sim; H1 steps 0-49 / H2 50-99; trigger h1_ppp>=1.15 and drop; NN match caliper 0.1.

## Result
Sim DiD ATT=-0.076 [-0.081,-0.071] n_pairs=25561 vs real +0.408; gap +0.484. Trigger count 25564 (32.9% of game x PT cells) vs ~5500 RS. Raw unmatched decline sim -0.504 vs real ~-0.655.

## Failure evidence
Sim ATT near 0 (slightly negative) as RTM+matching requires; cannot close the +0.408 real excess. Supports that half-level suppression is not memoryless microdynamics.

## Power and reliability
25561 matched sim pairs; 1000 bootstrap

## Related
APPS-022; APPS-071

## Notes
Verdict of this check is that the real Paper 1 number is an anomaly vs the sim (near-zero sim ATT). Runtime field '1783832484s' is a clock artifact, not a measured runtime.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\mc_suppression_check.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\mc_suppression_check.py

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
PAP-036, APPS-071
