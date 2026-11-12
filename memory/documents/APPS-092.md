# APPS-092: HasConn share vs pace (possessions per 48)

- Project: When a Hub Sits (Paper 2)
- Date: 2026-07-27 (mtime)
- Topic: Player absence and offensive reorganization
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 2
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: 
- Limitation tags: 
- Variable tags: PPP (points per possession); play-type share / mix
- Paper: When a Hub Sits (manuscript)

## Hypothesis
Connector presence slows pace (substituting half-court organization for transition).

## Design
Period-implied poss/48; n=28569 periods, 90 team-seasons. HasConn share with score-margin/period/opp FE, team-season FE, cluster SE. Play-mix: HasConn>=1 vs 0 within team-season n=73.

## Result
beta(HasConn share -> poss/48)=-0.86 SE=0.38 t=-2.25 p=0.0266; within-ts corr=-0.002 p=0.782. Mix: TRANSITION -0.448 pp p=0.0013; PNR +0.980 p=0.00187; CUT +1.353 p=1.2e-11; DRIVE -0.542 p=0.0206; SPOT_UP -1.248 p=0.000315. PUTBACK +0.148 p=0.0579. TRANSITION PPP | HasConn adj -0.13 t=-0.06 p=0.948.

## Failure evidence
Pace beta p=0.0266 but within-ts correlation is 0; no stint clock so poss/48 is period-implied. Mix shifts are clearer than efficiency.

## Power and reliability
n=28569 periods; mix n_ts=73

## Related
APPS-087

## Notes
HasConn->TRANSITION PPP was mix-licensed and null. Association not causal pace.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\hasconn_pace_report.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\putback_transition_hasconn_report.md

## Related records (ids resolved to merged records)
APPS-087
