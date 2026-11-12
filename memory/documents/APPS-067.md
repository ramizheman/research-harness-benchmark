# APPS-067: Opponent action T -> your offense T+1 (def-matched 8x8)

- Project: Strategy app
- Date: 2026-06-14 (mtime)
- Topic: Possession sequences and transitions
- Pre-specified: yes
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: placebo or permutation test; matched control
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
The opponent's previous play type changes your next-possession PPP after matching on defensive team.

## Design
64 cells; def_tri matching primary; sensitivity match on own offense. BH-FDR+placebo+FT-clean. prev_made control.

## Result
3/64 FINDING cells survive both matchings: SPOT_UP->TRANSITION ATT=-0.085; POST_UP->TRANSITION -0.083; PNR->DRIVE -0.058 (all also survive +prev_made). PULL_UP->DRIVE dropped as defense-quality confound.

## Failure evidence
Three cells replicate under def-match, off-match, and prev_made control. Most of 64 are null.

## Power and reliability
64 cells tested; 3 FINDING

## Related
APPS-060

## Notes
Weight row-level patterns over single cells per the report. Offensive-team match is the sensitivity file.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\opponent_action_your_offense_defmatch.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\opponent_action_your_offense_offmatch.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPS-060
