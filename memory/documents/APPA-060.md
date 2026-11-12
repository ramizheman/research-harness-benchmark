# APPA-060: PT-shift layer diagnostic across four upset series

- Project: Strategy app
- Date: 2026-04-21 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: null
- Failure type: C_artifact
- Knowable in advance: yes
- Runs: 4
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: matched control
- Limitation tags: 
- Variable tags: play-type share / mix; win probability / series outcome
- Paper: 

## Hypothesis
The play-type mix optimizer produces different feasible destination PTs by matchup (prescriptive) rather than one universal clipped destination (diagnostic).

## Design
Same 4 leakage-safe series; top feasible PT-shift destination, ceiling vs aspirational pp, muDelta.

## Result
No feasible PT shift in any of 4 series. Distinct top-feasible destination PTs: 0 (none).

## Failure evidence
0/4 series surfaced a feasible PT shift; verdict 'Confirmed diagnostic, not prescriptive.' Continuous feasibility still collapses away from a matchup-specific opener.

## Power and reliability
4 series

## Related
APPA-033; APPA-059

## Notes
Knowable from the CUT-everywhere / personnel-feasibility failure (APPA-033).

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\HISTORICAL_UPSET_BACKTEST.md

## Related records (ids resolved to merged records)
APPA-033, APPA-059
