# APPM-011: Net-swing play-type scoring prototype

- Project: Strategy app
- Date: 2026-05-23 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups; Playoff series outcomes
- Method tags: 
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Scoring PTs by own PPP minus opponent next-possession PPP changes recommendations.

## Design
52 playoff series / 104 team-offense units; compare rank orderings own-PPP vs net-swing.

## Result
Top recommendation changes in 40/104 = 38% units; DRIVE median net swing -0.27 (negative 88%), POST_UP -0.22 (77%).

## Failure evidence
Not evaluated against outcomes; uses in-series observed opp_next_PPP.

## Power and reliability


## Related


## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\NET_SWING_SCORING_PROTOTYPE.md

## Also recorded as
APPS-050
