# APPA-007: Absence validation V2: leave-one-out load predicts real displacement

- Project: When a Hub Sits (Paper 2)
- Date: 2026-07-12 (doc)
- Topic: Player absence and offensive reorganization
- Pre-specified: yes
- Verdict: failed_gate
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Player absence spells
- Method tags: placebo or permutation test; bootstrap interval; correlation
- Limitation tags: small sample; low power / large MDE
- Variable tags: structural influence / load (L)
- Paper: When a Hub Sits (manuscript)

## Hypothesis
Fragility leave-one-out load L_pred rank-correlates with real displacement D_real (raw and size-partial).

## Design
Same pre-registered 23 player-seasons; Spearman with franchise permutation (5000) and cluster bootstrap (2000); post-hoc diagnostics.

## Result
Gate G3 Spearman +0.099. V2a Spearman +0.288, p=0.077, CI [-0.244, +0.667] FAIL; V2b partial +0.253, p=0.115, CI [-0.262, +0.615] FAIL. Diagnostics: H_code ruled out (rho=0.933); dropping 2 absorption cases rho=+0.444 (n=21).

## Failure evidence
18 franchises below ~20-franchise floor; CI width ~0.9; gate already warned weak (+0.099).

## Power and reliability
n=23, 18 franchises; CI [-0.244, +0.667]

## Related
APPA-006; Fragility study

## Notes
Prereg itself said <20 franchises means underpowered, and the user skipped the full-pool sweep that could have added franchises. Diagnostics also point to a substantive absorption/cascade failure mode.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ABSENCE_VALIDATION_PREREGISTRATION.md

## Related records (ids resolved to merged records)
APPA-006

## Same study family
SF20 (duplicate_records): APPA-006, APPS-081, CHT-051, PAP-023
shared V1 16/23 above p95 (p=2.67e-16), +0.142 [0.103, 0.187]; V2a rho=+0.288 [-0.244, +0.667], V2b +0.253 | 23-case absence validation. APPA-006 records V1 and APPA-007 records V2; the others record both. Verdicts differ: supported / failed_gate / inconclusive / null.
