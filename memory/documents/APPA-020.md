# APPA-020: Evaluation-alignment diagnostic and opponent-strength lambda sweep

- Project: Strategy app
- Date: 2026-04-17 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: tool_eval_fail
- Failure type: B_powered_null
- Knowable in advance: no
- Runs: 2
- Dataset tags: 
- Method tags: matched control; regression; holdout, backtest or replay
- Limitation tags: 
- Variable tags: PPP (points per possession); play-type share / mix
- Paper: 

## Hypothesis
Equilibrium and actual-mix predictors explain matchup PPP better than simple means; opponent-strength scaling helps.

## Design
520 holdout matchup cells, 69,876 poss; R2 vs global/team means; lambda 0-1.5 post-hoc sweep.

## Result
Equilibrium R2 -0.1981; actual-mix R2 -0.7167; team-offense mean R2 +0.1197; >=100-poss cells equil -0.2785. Lambda sweep: R2 worsens monotonically (lambda 1.0 -0.2862).

## Failure evidence
Both model predictors have negative R2 while team-mean is +0.1197; R2 more negative in larger cells.

## Power and reliability
520 cells, 69,876 possessions

## Related
APPA-016; APPA-021

## Notes
Opponent-strength adjustment, recommended as high-ROI, made it worse.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\EVAL_DIAGNOSIS.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\EVAL_DIAGNOSIS_SWEEP.md

## Related records (ids resolved to merged records)
APPA-016, APPA-021
