# APPA-065: Freeform agent sequential demo: MIA vs BOS 2023 G7

- Project: Team Adaptation
- Date: 2026-05-23 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: inconclusive
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups; Playoff series outcomes; LLM or agent outputs
- Method tags: LLM agent run
- Limitation tags: small sample
- Variable tags: PPP (points per possession); net rating / ORtg
- Paper: 

## Hypothesis
An agent given only possession sequences can recover a conditional decision tree and series-level adaptation in one high-stakes game.

## Design
One Game 7 (0042200307); MIA 75 poss in thirds of 25; Markov-1 after make/miss; BOS next-PPP aftershock; 7-game PT table.

## Result
MIA thirds ORtg 108.0 / 136.0 / 156.0. After missed PNR (n=10) next PULL_UP 40%. POST_UP aftershock: BOS next-PPP 1.40 (miss n=5) and 1.50 (make n=4) vs PULL_UP make 0.00 (n=5). G4 POST_UP 0.40; G6 PNR 0.60; G7 PNR volume 10 to 18, PPP 0.60 to 1.06.

## Failure evidence
Most tree cells n=3-10; doc states branches are hypotheses until validated across series.

## Power and reliability
1 game; 75 MIA possessions; cells n=3-10

## Related
APPA-025; APPA-009

## Notes
Demo explicitly does not claim engine recovery (separate Test A). Series score G7 103-84 MIA in Boston.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FREEFORM_AGENT_DEMO_BOS_MIA_2023.md

## Related records (ids resolved to merged records)
APPA-025, APPA-009
