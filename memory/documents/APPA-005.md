# APPA-005: Defensive scheme change within game and across games (inferred labels)

- Project: Team Adaptation
- Date: 2026-05-23 (mtime)
- Topic: Play-type labeling and data quality
- Pre-specified: no
- Verdict: inconclusive
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: 
- Limitation tags: label or classification error
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Playoff defenses change scheme within games and between games, especially after the opponent ran a play type heavily.

## Design
A1 vote-rule scheme inference from opponent PT PPP; 523 comparable within-game cells; 440 consecutive game pairs; heavy-PT conditioning (>=5pp).

## Result
Within-game change 319/523 (61.0%); cross-game change 298/440 (67.7%); 103/104 units (99.0%) and 52/52 series show a change; transition matrices near-uniform.

## Failure evidence
Doc caveat: inferred label cannot separate real defensive adjustment from offense executing differently; near-uniform transition matrices consistent with label noise.

## Power and reliability
523 cells; 440 pairs

## Related
APPA-001

## Notes
Reverse-inferred labels from PPP outcomes; late-third votes use min_n_per_pt=2.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\DEFENSIVE_ADAPTATION_findings.md

## Related records (ids resolved to merged records)
APPA-001

## Also recorded as
APPS-054
