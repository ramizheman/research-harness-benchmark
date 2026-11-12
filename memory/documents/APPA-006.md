# APPA-006: Absence validation V1: real absence restructures offense beyond noise

- Project: When a Hub Sits (Paper 2)
- Date: 2026-07-12 (doc)
- Topic: Player absence and offensive reorganization
- Pre-specified: yes
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: no
- Runs: 1
- Dataset tags: Player absence spells
- Method tags: placebo or permutation test; bootstrap interval; matched control
- Limitation tags: small sample; low power / large MDE
- Variable tags: 
- Paper: When a Hub Sits (manuscript)

## Hypothesis
Real present-vs-absent structural displacement D_real exceeds a size-matched subsampling null.

## Design
Pre-registered; 23 player-seasons, 18 franchises, ON_COURT-verified absences, 2022-25; balanced size-m null (Amendment A1); franchise-clustered permutation and bootstrap.

## Result
Gate G2 21/23 (91%) above null median; V1(a) 16/23 above own-null p95, binomial p=2.67e-16; V1(b) mean(D_real - median_null)=+0.142, CI [+0.103, +0.187].

## Failure evidence
CI excludes 0; binomial p=2.67e-16.

## Power and reliability
23 player-seasons, 18 franchises (below ~20 floor, flagged UNDERPOWERED)

## Related
APPA-007

## Notes
One pre-run amendment (balanced null) because draft null was infeasible when absent>present.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ABSENCE_VALIDATION_PREREGISTRATION.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPA-007

## Same study family
SF20 (duplicate_records): APPA-007, APPS-081, CHT-051, PAP-023
shared V1 16/23 above p95 (p=2.67e-16), +0.142 [0.103, 0.187]; V2a rho=+0.288 [-0.244, +0.667], V2b +0.253 | 23-case absence validation. APPA-006 records V1 and APPA-007 records V2; the others record both. Verdicts differ: supported / failed_gate / inconclusive / null.
