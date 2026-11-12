# APPA-035: Relative-structure single-game validation BOS vs OKC

- Project: Strategy app
- Date: 2026-04-17 (mtime)
- Topic: Other / unclassified
- Pre-specified: partial
- Verdict: inconclusive
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: holdout, backtest or replay; correlation
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Model's top-ranked play types score above team average in a held-out game.

## Design
One holdout game 0022400946; Spearman of predicted vs actual PT PPP (PTs >=3 poss); top-3/bottom-3 hits.

## Result
BOS rho 0.200, top-3 n/a, bottom-3 1/3; OKC rho 0.543, top-3 2/2, lift +0.308, bottom-3 1/3.

## Failure evidence
One game; 5-6 PTs per team with 4-35 possessions.

## Power and reliability
1 game

## Related


## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\HISTORICAL_VALIDATION_BOS_OKC.md
