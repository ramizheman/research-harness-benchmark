# APPS-020: RS 2025-26 holdout n-gated BEST vs AVOID counter gap

- Project: Strategy app
- Date: 2026-06-21 (doc)
- Topic: Player absence and offensive reorganization
- Pre-specified: partial
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: no
- Runs: 1
- Dataset tags: 
- Method tags: holdout, backtest or replay; correlation
- Limitation tags: leakage
- Variable tags: 
- Paper: 

## Hypothesis
The same n-gated BEST vs AVOID ranking replicates on a regular-season 2025-26 holdout with Scout exclude_gids.

## Design
RS games 00225*, 1148 games, 2779 triggers, 11337 counter rows; 870/870 direction runs post-fix. Same counter_h2_n>=5 row-mean as PO.

## Result
Canonical n-gated gap +0.422 (BEST 1.423 n=796 vs AVOID 1.001 n=494, p=0.0). Spearman rho=-0.3436, n=11337. Oracle BEST 1.498 (+0.497 vs AVOID); routing regret +0.124 (72.4% oracle>actual). rot8_n5 conservative regret +0.094 (oracle 1.508 vs actual 1.414, n=970).

## Failure evidence
Replicates and slightly exceeds PO +0.375 at the same n-gate after leakage fix.

## Power and reliability
796 BEST / 494 AVOID n-gated rows; 1148 games

## Related
APPS-019

## Notes
Pre-fix leaky RS numbers (~+0.413 n-gated, routing regret +0.137, oracle 1.552) must not be cited. rs_validation_report header says 'Games: 0 RS games' but body has 11337 rows / 870 runs ? numbers copied from the stats tables.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\COHERENT_NUMBERS.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\rs_holdout_25_26\rs_validation_report_clean.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\oracle_sensitivity.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPS-019

## Same study family
SF03 (repeat_runs_or_robustness): APPA-036, APPM-030, APPS-019, PAP-043, CHT-042
shared BEST-AVOID gaps +0.375 (PO) and +0.422 (RS), BEST 1.298/1.423, AVOID 0.923/1.001 | Same BEST vs AVOID counter-gap design run on playoff and regular-season samples before and after the leakage correction.
