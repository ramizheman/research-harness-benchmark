# APPS-042: POST_UP vs PUTBACK Q1-Q4 gradient and double-suppression stack

- Project: Strategy app
- Date: 2026-05-31 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: inconclusive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: 
- Limitation tags: small sample; implementation bug
- Variable tags: 
- Paper: 

## Hypothesis
PUTBACK suppression is fatigue (Q4-heavy); POST_UP is immediate rhythm disruption; stacking them is additive.

## Design
POST_UP cluster (Jokic, Doncic, LeBron, Fox, Brown) Q1-Q4 deltas; TRANSITION cluster (Tatum, Morant, Young, Haliburton); league POST_UP then PUTBACK 4-hop stack n=1047.

## Result
POST_UP Q1->Q4 -0.065 (Q1 -0.119 to Q4 -0.184); PUTBACK -0.374 (0.144 to -0.23). TRANSITION cluster gradient +0.075 (unexpected vs hypothesized flat). Stacked delta -0.071 vs additive prediction -0.232 (less than additive). League after PUTBACK -0.113 (n=15898), after POST_UP -0.119 (n=76329).

## Failure evidence
PUTBACK vs POST_UP gradients differ as hypothesized, but TRANSITION gradient has the wrong sign and stacked suppression is less than additive; per-player stacked n often <5.

## Power and reliability
cluster n=5 players; stacked n=1047 league / typically n<10 per star

## Related
APPS-040

## Notes
Authors read POST_UP as rhythm/read disruption not fatigue; TRANSITION unexpected +0.075 flagged to re-examine sample.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\postup_putback_gradient\postup_vs_putback_gradient.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\three_mechanisms\transition_immunity_report.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\three_mechanisms\double_suppression_mitchell_report.md

## Related records (ids resolved to merged records)
APPA-054

## Same study family
SF09 (duplicate_records): APPA-057
shared 0.113 / 0.119 / 0.232 and n=15,898 / 76,329 | Verdicts differ: null vs inconclusive.
