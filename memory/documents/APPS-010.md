# APPS-010: Play-type PPP change across playoff series game buckets

- Project: Strategy app
- Date: 2026-05-08 (mtime)
- Topic: In-game and series adaptation
- Pre-specified: no
- Verdict: null
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: 
- Limitation tags: selection or regression to the mean
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Play-type PPP (especially DRIVE) declines as a playoff series progresses, so DRIVE is a good early-series call.

## Design
Pooled (series, team, PT, bucket) records (1197), EARLY G1-2 / MID G3-4 / LATE G5-7, min 10 poss, min 3 series.

## Result
DRIVE 0.889 -> 0.949 (+0.060); CUT +0.114; PNR +0.087; PULL_UP -0.077; POST_UP -0.032.

## Failure evidence
'NO CLEAR SIGNAL - DRIVE PPP is stable or improves across the series'; observational with selection caveats.

## Power and reliability
1197 records; no CIs

## Related
RS vs playoff PPP; Within-game DRIVE decline

## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\_series_game_adaptation.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\game_adaptation_run.log
