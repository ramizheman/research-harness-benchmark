# APPS-027: Adaptation quality vs talent as predictor of series wins

- Project: Strategy app
- Date: 2026-06-15 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: null
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Playoff series outcomes
- Method tags: regression
- Limitation tags: small sample; confounding
- Variable tags: win probability / series outcome
- Paper: 

## Hypothesis
pct_ran_BEST - pct_ran_AVOID predicts series wins after controlling for RS net-rating talent.

## Design
110 series-directions / 55 series. Logistic y=won on standardized talent_diff and adapt_diff.

## Result
corr(talent, adapt)=+0.124. Per-series logistic: talent_diff_z +0.737 p=0.0213; adapt_diff_z +0.328 p=0.2755. Team-in-series cluster: talent p=0.0095, adapt p=0.2449. Univariate adapt beta=+0.311 p=0.1128. LPM: talent +0.160 p=0.0046, adapt +0.072 p=0.2633, R2=0.142.

## Failure evidence
After talent control adapt p=0.275; n~55 series cannot separate coaching adaptation from roster quality.

## Power and reliability
n=55 series / 110 directions

## Related
APPS-030

## Notes
Authors' honest null: report as confounded with talent.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\adaptation_talent_control.md

## Related records (ids resolved to merged records)
APPS-030

## Also recorded as
CHT-046
