# APPS-080: Paper 2 topological-identity gate and confirmatory (P1a/P1b)

- Project: When a Hub Sits (Paper 2)
- Date: 2026-07-12 (mtime)
- Topic: Player absence and offensive reorganization
- Pre-specified: yes
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: no
- Runs: 2
- Dataset tags: 
- Method tags: regression
- Limitation tags: 
- Variable tags: 
- Paper: When a Hub Sits (manuscript)

## Hypothesis
Team offenses have a rate-irreducible topological identity (within-franchise similarity exceeds between).

## Design
Gate: 8 team-seasons, N_NULL=1000 N_PERM=5000. Full: 120 team-seasons, 30 franchises. Frobenius and cosine; residualized P1b.

## Result
Gate: C1 8/8 p<0.05; C2 S=0.319 perm_p=0.0002; C3 R2=0.080 PASS. Full: frobenius P1a S=0.352 p=0.0000 CI[0.327,0.378]; P1b S=0.353 CI[0.329,0.379]; cosine P1a 0.155 / P1b 0.144. residual_R2=0.043. D_obs mean=373.7. P1a=CONFIRMED P1b=CONFIRMED.

## Failure evidence
Gate passed and confirmatory P1a/P1b both confirmed at 120 team-seasons.

## Power and reliability
n=120 team-seasons, 30 franchises; n_perm=5000

## Related
APPS-084

## Notes
PAP slice also covers When a Hub Sits scripts; this record is from paper2_output artifacts only.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\paper2_gate_result.txt
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\paper2_full_result.txt

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPS-084

## Same study family
SF17 (duplicate_records): CHT-049, PAP-002
shared Frobenius P1a S=0.352 [0.327, 0.378], P1b S=0.353 [0.329, 0.379] | PAP-001 is the separate feasibility gate.
