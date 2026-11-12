# APPS-013: Defensive Style Index shift RS vs playoffs

- Project: Strategy app
- Date: 2026-05-08 (mtime)
- Topic: In-game and series adaptation
- Pre-specified: no
- Verdict: null
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups; Playoff series outcomes
- Method tags: 
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
Teams shift toward HELP/SWITCH and away from DROP in the playoffs, making RS DSI priors wrong.

## Design
pbpstats Playoffs vs RS aggregates, same DSI formula, 2022-23 and 2023-24 playoff teams.

## Result
SWITCH 0.294 -> 0.336 (+0.0426, 62% of teams); DROP 0.399 -> 0.343 (-0.0561); HELP 0.307 -> 0.321 (+0.0135, 'No meaningful shift').

## Failure evidence
HELP shift +0.0135 'No meaningful shift'; per-team shifts range -0.287 to +0.271 with no test.

## Power and reliability
32 team-seasons; no CIs

## Related
Defensive PPP allowed RS vs playoffs

## Notes
Partial support: SWITCH up and DROP down, but the hypothesized HELP shift was absent.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\_dsi_rs_vs_playoff.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\dsi_rs_playoff_run.log
