# APPM-016: Possession-level SQ2 test: engine recommended PT (playoff series)

- Project: Strategy app
- Date: 2026-05-23 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups; Playoff series outcomes
- Method tags: difference-in-differences; regression
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Possessions on the engine's recommended PT score more than other PTs within the series, beyond inherent PT PPP.

## Design
74 team-series pairs; Test A literal, Test B DiD vs RS, Test C two-way FE OLS on 504 cells.

## Result
A +0.140 PPP [0.084,0.196]; B DiD +0.090 [0.041,0.141]; C gamma +0.0088 SE 0.0239 p=0.7139.

## Failure evidence
Strictest FE test gamma +0.0088, p=0.71; A/B explained by engine picking high-PPP PTs.

## Power and reliability
504 cells, SE 0.0239 (iid)

## Related
Possession-level SQ2 all RS games

## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\POSSESSION_PPP_findings.md

## Also recorded as
APPS-006, CHT-023
