# APPA-010: Adversarial best-response v1: equilibrium strategy vs actual

- Project: Strategy app
- Date: 2026-04-14 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: inconclusive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups
- Method tags: matched control; holdout, backtest or replay
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
The system's offensive strategy survives optimal defensive adjustment and beats what teams ran.

## Design
240 matchups, 23,922 holdout possessions; iterative best-response to approximate Nash equilibrium, model-scored PPP.

## Result
Eq vs actual +1.16 pts/100; beats actual 127/240 (53%); vs baseline eq +8.52 pts/100; converged 159/240.

## Failure evidence
Doc verdict 'MARGINAL'; equilibrium PPP is model-implied not observed.

## Power and reliability
240 matchups

## Related
APPA-011

## Notes
Model-scored counterfactual compared to realized PPP.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADVERSARIAL_REPORT.md

## Related records (ids resolved to merged records)
APPA-011
