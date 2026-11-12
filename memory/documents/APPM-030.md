# APPM-030: BEST vs AVOID counter-tier OOS gap

- Project: Defensive Suppression
- Date: 2026-06-19 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Playoff series outcomes
- Method tags: holdout, backtest or replay; correlation
- Limitation tags: leakage
- Variable tags: 
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
After suppression, pre-ranked BEST counters score more than AVOID counters out of sample.

## Design
55 playoff series / 272 games (175 BEST / 456 AVOID rows) and RS holdout 2025-26 1,148 games (980 BEST / 691 AVOID), n>=5 gate.

## Result
Corrected gap +0.375 (PO) / +0.422 (RS) per v8 stale note; earlier +0.476/+0.413 and ungated +0.620; within-trigger paired +0.588 (86) / +0.445 (221); Spearman rho -0.316; KW H 644.84.

## Failure evidence
Gap survives CUT removal (+0.389), turnover correction (+0.371), within-PT FE (+0.363).

## Power and reliability
PO 175/456 rows; RS 980/691

## Related
FINAL_NUMBERS_SHEET.md (A-L); Counter-tier validation Test 1

## Notes
Numbers changed across versions (+0.620 -> +0.476 -> +0.375 after leakage fix); INSUFF_EVIDENCE 34-80%.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\PRESENTATION_SLIDE_NUMBERS.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\PRESENTATION_STRUCTURE_v8.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_three_condition_gap.py
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_within_trigger_regret.py

## Finding status
supported in source; independent replication not recorded

## Same study family
SF03 (repeat_runs_or_robustness): APPA-036, APPS-019, APPS-020, PAP-043, CHT-042
shared BEST-AVOID gaps +0.375 (PO) and +0.422 (RS), BEST 1.298/1.423, AVOID 0.923/1.001 | Same BEST vs AVOID counter-gap design run on playoff and regular-season samples before and after the leakage correction.
