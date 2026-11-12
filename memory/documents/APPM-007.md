# APPM-007: Shot-quality (xPPP, team shot-making) features

- Project: Strategy app
- Date: 2026-04-17 (mtime)
- Topic: Shot selection and shot quality
- Pre-specified: partial
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Shot-level data with expected FG; Box score and traditional stats
- Method tags: regression; holdout, backtest or replay
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Shot-zone expected PPP and team shot-making skill add signal beyond box-score features.

## Design
Add xPPP and team make-skill features to 8-feat OLS; holdout R2.

## Result
Best +xPPP only R2_hol +0.1204 (lift +0.0054); shot-skills -0.0003.

## Failure evidence
Lift +0.0054 below the +0.02 'real signal' threshold (doc: mostly absorbed).

## Power and reliability


## Related
STACK_FINAL.md

## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\SHOT_QUALITY.md
