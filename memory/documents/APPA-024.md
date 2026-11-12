# APPA-024: Alignment regression: shift toward engine recommendation vs series ORtg

- Project: Strategy app
- Date: 2026-05-23 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: null
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Box score and traditional stats; Playoff series outcomes
- Method tags: bootstrap interval; regression; holdout, backtest or replay; correlation
- Limitation tags: small sample
- Variable tags: play-type share / mix; net rating / ORtg
- Paper: 

## Hypothesis
Teams whose playoff mix shifted toward the engine's recommended PT have higher series ORtg residuals.

## Design
68 (team, series) pairs; Pearson/Spearman, bootstrap CI, OLS with mix-shift control; provisional tuning/holdout split.

## Result
Pearson r -0.032, CI [-0.283, +0.209]; Spearman -0.067; OLS beta -5.33 (SE 19.64); clean subset r -0.079 (n=54); tuning fold +0.135, holdout -0.125.

## Failure evidence
n=68 with CI width ~0.49 on r; doc says sample thin.

## Power and reliability
n=68; 95% CI [-0.283, +0.209]

## Related
APPA-031

## Notes
Conflicts with the CASE_STUDIES claim of a +3.3 ORtg alignment effect.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ALIGNMENT_REGRESSION_findings.md

## Related records (ids resolved to merged records)
APPA-031

## Also recorded as
APPS-007, CHT-022
