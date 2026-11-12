# APPM-019: Within-series learning: distribution shift vs outcomes

- Project: Strategy app
- Date: 2026-05-16 (mtime)
- Topic: In-game and series adaptation
- Pre-specified: no
- Verdict: null
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups; Playoff series outcomes
- Method tags: 
- Limitation tags: 
- Variable tags: play-type share / mix; win probability / series outcome
- Paper: 

## Hypothesis
Teams shift play-type mix more after losses, and higher-adapting teams win series.

## Design
Playoff possessions with series property; TVD shift between consecutive games (478 pairs); series-level comparison.

## Result
Shift after loss 31.85 vs after win 32.69 pp; higher-shift team won 28/52 series (53.8%).

## Failure evidence
53.8% 'effectively a coin flip'; loss-win diff -0.85 pp.

## Power and reliability
478 game pairs; 52 series

## Related


## Notes
Header says 33 series/58,455 possessions but table lists 52 series; inconsistent.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\within_series_learning_findings.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_analyze_series_learning.py
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\series_adaptation_data.csv
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_series_learning_out.txt
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_series_learning_out2.txt

## Also recorded as
CHT-011
