# APPM-015: Routing prior vs H2H posterior gate diagnostic

- Project: Strategy app
- Date: 2026-06-10 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: artifact_found
- Failure type: C_artifact
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: 
- Limitation tags: small sample
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
The n>=15 H2H gate suppresses real player-routing signal.

## Design
6,221 (offense, opponent, PT) cells; count H2H leaders differing from season default at gates 5/10/15/25.

## Result
Mean PPP delta lead-default +1.259 (n>=5) to +1.129 (n>=15); low-n leaders are role players with 2-3 PPP on 5-7 possessions.

## Failure evidence
Apparent +1.13 PPP edge is small-sample inflation (e.g. n=6, PPP=3.00).

## Power and reliability


## Related


## Notes
Recommendation: keep n>=15 gate.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ROUTING_PRIOR_VS_H2H_DIAGNOSTIC.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_diag_routing_vs_h2h.py

## Same study family
SF31 (duplicate_records): CHT-017
shared lead-vs-default +1.26 (n>=5) and +1.13 (n>=15)
