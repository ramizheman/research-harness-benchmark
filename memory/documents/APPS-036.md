# APPS-036: Player-level BEST vs AVOID PPP gap (initiators, 55-series)

- Project: Strategy app
- Date: 2026-05-31 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups; Playoff series outcomes
- Method tags: 
- Limitation tags: small sample
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
The team-level BEST vs AVOID gap holds when H2 possessions are filtered to initiating player.

## Design
trigger_table_clean.csv; gate n>=10 per tier to report. League aggregate players with n>=15 each tier.

## Result
Mean gap (n>=10 each tier) +0.427 PPP. Mean BEST 1.347 (38 players) vs AVOID 0.920 (94 players). Stars mean gap +0.542 (n=15) vs role +0.428 (n=16). Only 3 players clear n>=30 both tiers (all BOS: White +0.864, Brown +0.466, Tatum +0.391).

## Failure evidence
Pooled player gap +0.427 in the same direction as the team gap; most star cells are below the n>=30 gate.

## Power and reliability
38/94 players at n>=15; only 3 at n>=30 both tiers

## Related
APPS-015; APPS-019

## Notes
Player samples are thin; Brunson BEST n=8 below gate. Related to APPS-015 tendency tables but this is PPP gap not mix share.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\player_tier_gap\player_tier_gap_report.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\player_tier_gap_run.log

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPS-015, APPS-019
