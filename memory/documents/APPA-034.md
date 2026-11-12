# APPA-034: Opponent-relative leverage prevalence sweep

- Project: Strategy app
- Date: 2026-04-20 (mtime)
- Topic: Other / unclassified
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NCAA tournament and ratings data
- Method tags: 
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
How often does an opponent-specific exploitable defensive weakness exist?

## Design
870 ordered team pairs; defense PT edge vs league >= +5% on seed PTs.

## Result
Exploit available 33.3%; trap 23.3%; both 6.7%; neither 50.0%; median best edge 3.79%.

## Failure evidence


## Power and reliability
870 pairs

## Related


## Notes
Edges depend only on the defense (e.g. DAL PNR +9.2% for every offense), so they are not matchup-specific.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\LEVERAGE_PREVALENCE.md
