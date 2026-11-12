# APPS-062: Test 3: cumulative Q1-Q3 star load -> Q4 PPP

- Project: Strategy app
- Date: 2026-06-14 (mtime)
- Topic: Structural roles and influence
- Pre-specified: yes
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: placebo or permutation test; matched control
- Limitation tags: 
- Variable tags: PPP (points per possession); structural influence / load (L)
- Paper: 

## Hypothesis
High Q1-Q3 initiator load lowers Q4 star PPP (mechanism for Test 2).

## Design
Unit=(star, game). Top vs bottom tercile Q1-Q3 load; match Q4 margin x opp def-rating quartile x season x home.

## Result
Matched ATT=-0.0052, 95% CI[-0.0387,+0.0239], perm p=0.7706, placebo p=0.7760. Raw high-low -0.0146. high-load games=1854, low=2375.

## Failure evidence
ATT~0, CI excludes large load effects; perm/placebo ~0.77. Test 2 Q4 decline is not explained by raw possession load.

## Power and reliability
1854 high-load vs 2375 low-load games

## Related
APPS-061

## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\test_3_star_load.md

## Related records (ids resolved to merged records)
APPS-061
