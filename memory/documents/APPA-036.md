# APPA-036: Suppression tier ranking: BEST vs AVOID / BEST vs continue

- Project: Defensive Suppression
- Date: 2026-06-21 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: partial
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: no
- Runs: 3
- Dataset tags: Playoff series outcomes
- Method tags: holdout, backtest or replay; correlation
- Limitation tags: selection or regression to the mean; leakage
- Variable tags: PPP (points per possession)
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
After an H1 suppression trigger, BEST-tier counters score more in H2 than AVOID counters or continuing the suppressed play.

## Design
Triggers H1/H2 n>=5, drop >=0.25; 25-series (290 triggers), 55-series (633 triggers) and RS 2025-26 holdout (2,779 triggers); row-mean H2 PPP by tier.

## Result
25-series BEST-AVOID +0.581, MW p=5.16e-24; 55-series ungated +0.548, n-gated +0.375; BEST vs continue +0.445 PO / +0.584 RS; robustness: CUT removed +0.279, n>=10 +0.221, within-PT fixed effects +0.100; RS Spearman -0.344; INSUFF 55.7-57.3% of rows.

## Failure evidence
Gap survives the leakage fix but shrinks to +0.100 with within-play-type fixed effects.

## Power and reliability
633 PO / 2,779 RS triggers

## Related
APPA-037

## Notes
Pre-fix leaky gap ~+0.488 and the 25-series sample was not rerun after the Scout leakage fix. BEST is what teams actually ran (selection effect).

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPA-037

## Same study family
SF03 (repeat_runs_or_robustness): APPM-030, APPS-019, APPS-020, PAP-043, CHT-042
shared BEST-AVOID gaps +0.375 (PO) and +0.422 (RS), BEST 1.298/1.423, AVOID 0.923/1.001 | Same BEST vs AVOID counter-gap design run on playoff and regular-season samples before and after the leakage correction.
