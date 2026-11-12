# APPM-032: Player routing regret

- Project: Defensive Suppression
- Date: 2026-06-19 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: holdout, backtest or replay
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
Routing counters to the oracle initiator adds PPP beyond play selection.

## Design
RS holdout; shrinkage-blended H2H oracle (prior weight 50), rotation-filtered, n>=10 H2H.

## Result
Routing regret +0.094 PPP (stale) / +0.124 RS (corrected); SPOT_UP +0.183 (n=385), CUT +0.129 (n=295), DRIVE +0.081 (n=280).

## Failure evidence
Positive regret under conservative oracle.

## Power and reliability


## Related
Routing prior vs H2H diagnostic

## Notes
Oracle regret is non-negative by construction-like design; unconstrained oracle +0.549/+0.691.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\PRESENTATION_SLIDE_NUMBERS.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\PRESENTATION_STRUCTURE_v8.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_routing_regret.py
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_routing_constrained_oracle.py
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_oracle_sensitivity.py

## Finding status
supported in source; independent replication not recorded
