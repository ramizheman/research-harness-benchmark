# APPA-023: Per-play-type interaction residual feature (Phase 1b)

- Project: Strategy app
- Date: 2026-04-17 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: partial
- Verdict: failed_gate
- Failure type: B_powered_null
- Knowable in advance: no
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: regression; holdout, backtest or replay
- Limitation tags: insufficient exposure
- Variable tags: 
- Paper: 

## Hypothesis
Per-PT team-pair interaction deltas add R2 over the 8-feature baseline (ship if lift > +0.005).

## Design
870 train cells (386,675 poss); shrinkage k sweep 25-1000; holdout R2.

## Result
Best k=500 R2_hol +0.1192 vs +0.1150 baseline; lift +0.0042; w_pt negative (-1.4014).

## Failure evidence
Lift +0.0042 < +0.005 ship threshold.

## Power and reliability
870 train cells

## Related
APPA-020

## Notes
Negative weight suggests overfitting sparse cells.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\INTERACTION_PT.md

## Related records (ids resolved to merged records)
APPA-020
