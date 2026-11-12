# APPS-015: Player BEST/AVOID tier tendency in H2 trigger games (55 series)

- Project: Strategy app
- Date: 2026-06-16 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups; Playoff series outcomes
- Method tags: 
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
Teams and players differ in how often H2 trigger possessions land on the engine's BEST vs AVOID counter.

## Design
trigger_table_clean.csv, 55 series 2022-2026, 179 players, 25 teams, min 10 poss.

## Result
Team AVOID% ranges 50.6% (ORL) to 6.8% (SAC); team BEST% 0.0%-15.8%.

## Failure evidence
No outcome test; player samples 10-178 possessions.

## Power and reliability
min 10 poss per player

## Related
Agent Test B counter recs

## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\player_tier_tendency_league_summary.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\player_tier_tendency_by_team.md
