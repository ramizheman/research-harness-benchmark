# APPM-013: Playoff within-game three-thirds adaptation (A1 playoffs)

- Project: Strategy app
- Date: 2026-05-16 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Playoff series outcomes
- Method tags: 
- Limitation tags: selection or regression to the mean
- Variable tags: PPP (points per possession); three-point attempts or luck
- Paper: 

## Hypothesis
Playoff teams that shift toward scheme counters in mid+late thirds see PPP rise more than non-adapters.

## Design
586 (game,team) rows, 529 with inferred scheme; adapters 229 vs non-adapters 300; one-sided Mann-Whitney.

## Result
Adapter dPPP +0.0613 vs +0.0131; advantage +0.0482 PPP, p=0.0199. SWITCH subgroup reversed (-0.0160).

## Failure evidence
p=0.0199 one-sided.

## Power and reliability
n=529

## Related
A1_FALSIFICATION_findings.md (A-L); DID_ADAPT_NYK_vs_PHI_2526.md

## Notes
Scheme is inferred from the same early-third PPP that defines the baseline, so regression to the mean may contribute; not addressed in doc.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\PLAYOFF_A1_THIRDS_findings.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\PLAYOFF_A1_THIRDS_data.csv
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_playoff_a1_thirds.py

## Finding status
supported in source; independent replication not recorded

## Also recorded as
APPS-052

## Same study family
SF13 (repeat_runs_or_robustness): APPA-003, CHT-018
APPA-003 and CHT-018 share adapters +0.0701 vs +0.0121; CHT-018's first run (+0.0613, n=229) is APPM-013's playoff estimate | Verdicts differ: artifact_found vs supported. The later RTM falsification overturned the first run.
