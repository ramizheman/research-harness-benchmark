# APPM-039: Travel x fit screen and outcome holdout validation

- Project: Structural Influence (Paper 1)
- Date: 2026-07-18 (mtime)
- Topic: Structural roles and influence
- Pre-specified: partial
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Box score and traditional stats
- Method tags: holdout, backtest or replay; calibration scoring
- Limitation tags: 
- Variable tags: minutes / playing time; net rating / ORtg; win probability / series outcome
- Paper: Structural Influence (published)

## Hypothesis
Forecast portability (travel) and fit quadrants predict mover outcomes (embedded minutes, net rating).

## Design
296 movers (230 with outcomes); LOO travel forecast; 500 random 50/50 calibration/holdout splits.

## Result
LOO corr 0.1998, AUC 0.5986; holdout additive embedded 89.59% vs irrelevant 48.11%; P(add emb > irr)=0.984; P(add net > irr)=0.99; corr(travel,net) 0.1881.

## Failure evidence
Additive > irrelevant in 98.4% of splits.

## Power and reliability
n=230

## Related
Portability

## Notes
Modest AUC 0.60.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\PAPER_NUMBERS_SHEET.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\travel_fit_screen.py
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\outcome_check.py
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\outcome_split_validation.py

## Finding status
supported in source; independent replication not recorded
