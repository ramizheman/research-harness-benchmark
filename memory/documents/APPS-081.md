# APPS-081: Absence-validation gate and confirmatory (structure moves; dose ns)

- Project: When a Hub Sits (Paper 2)
- Date: 2026-07-12 (mtime)
- Topic: Player absence and offensive reorganization
- Pre-specified: yes
- Verdict: inconclusive
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 2
- Dataset tags: Player absence spells
- Method tags: correlation; simulation
- Limitation tags: small sample; low power / large MDE
- Variable tags: 
- Paper: When a Hub Sits (manuscript)

## Hypothesis
Player absence moves offensive structure (V1) and the size of the move tracks a simulated dose (V2).

## Design
Gate n_null=150 n_rep=120 core=23. Confirmatory n_null=500 n_perm=5000 player_seasons=23 franchises=18 flagged underpowered.

## Result
Gate PASS (G2 frac_above_median=0.913; G3 rho=+0.099). Confirmatory V1(a) 16/23 above p95 binomial_p=2.67e-16; V1(b) mean_diff=+0.142 CI[+0.103,+0.187] CONFIRMED. V2a rho=+0.288 p=0.0770 CI[-0.244,+0.667]; V2b partial rho=+0.253 p=0.1152 NOT. VERDICT PARTIAL/NEGATIVE UNDERPOWERED <20 franchises.

## Failure evidence
V1 confirmed but V2 dose-response ns with n=23 player-seasons / 18 franchises explicitly underpowered; no re-run per ?9.

## Power and reliability
n=23 player-seasons, 18 franchises

## Related
APPS-080

## Notes
Knowable: <20 franchises was the underpowered flag written into the confirmatory output.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\absence_gate_result.txt
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\absence_full_result.txt

## Related records (ids resolved to merged records)
APPS-080

## Same study family
SF20 (duplicate_records): APPA-006, APPA-007, CHT-051, PAP-023
shared V1 16/23 above p95 (p=2.67e-16), +0.142 [0.103, 0.187]; V2a rho=+0.288 [-0.244, +0.667], V2b +0.253 | 23-case absence validation. APPA-006 records V1 and APPA-007 records V2; the others record both. Verdicts differ: supported / failed_gate / inconclusive / null.
