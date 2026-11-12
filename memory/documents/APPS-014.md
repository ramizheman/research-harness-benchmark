# APPS-014: Within-game DRIVE decline by game third

- Project: Strategy app
- Date: 2026-05-08 (mtime)
- Topic: In-game and series adaptation
- Pre-specified: no
- Verdict: reversed
- Failure type: B_powered_null
- Knowable in advance: no
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups; Playoff series outcomes
- Method tags: 
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
DRIVE efficiency drops within a single playoff game (defense moves first) before cross-game adaptation.

## Design
Pooled playoff possessions split into game thirds by elapsed time; Game 1 only and all games.

## Result
Game 1 DRIVE 0.864 (n=323) -> 0.942 (n=346), +0.078; all games 0.880 (n=1746) -> 0.973 (n=1987), +0.093.

## Failure evidence
DRIVE rises early-to-late (+0.078 G1, +0.093 all games) instead of dropping.

## Power and reliability
n=1746-1987 per third (all games)

## Related
Play-type PPP change across series game buckets

## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\_drive_within_game.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\drive_within_game_run.log
