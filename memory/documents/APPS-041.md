# APPS-041: PUTBACK suppression matched-pair isolation (star vs team)

- Project: Strategy app
- Date: 2026-06-14 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: partial
- Verdict: null
- Failure type: C_artifact
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: matched control
- Limitation tags: confounding
- Variable tags: 
- Paper: 

## Hypothesis
Conceding a PUTBACK causally suppresses the next offensive possession after matching on game state.

## Design
PSM 1:3 ATT, caliper 0.05. Treated=just conceded PUTBACK. Covariates include off_margin (already reflects conceded points).

## Result
TEAM ATT=-0.0038 CI[-0.025,+0.015] perm p=0.890 n_t=15614. STAR ATT=+0.0040 [-0.049,+0.052] p=0.834 n_t=2481. STAR Q4 ATT=-0.1045 [-0.217,+0.010] p=0.032 (gradient does not survive matching as a FINDING).

## Failure evidence
Raw putback suppression collapses once margin/state is matched; original finding was a score/context confound.

## Power and reliability
n_treated team=15614, star=2481

## Related
APPS-040; APPS-065

## Notes
Knowable: margin already includes the putback points, so unmatched H2/Q4 comparisons confound scoreboard state with aftershock.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\putback_matched_isolation.md

## Related records (ids resolved to merged records)
APPA-054, APPS-065

## Also recorded as
CHT-033
