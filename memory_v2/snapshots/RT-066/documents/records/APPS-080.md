# EXP:APPS-080 | Paper 2 topological-identity gate and confirmatory (P1a/P1b)
- date: 2026-07-12
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: Gate: 8 team-seasons, N_NULL=1000 N_PERM=5000. Full: 120 team-seasons, 30 franchises. Frobenius and cosine; residualized P1b.
- hypothesis: Team offenses have a rate-irreducible topological identity (within-franchise similarity exceeds between).
- knowable_in_advance: no
- member_of: FAM:SF17 {record=APPS-080; rule=audit/study_family_review.csv or singleton}
- n_runs: 2
- notes: PAP slice also covers When a Hub Sits scripts; this record is from paper2_output artifacts only.
- prespecified: yes
- produced: RES:APPS-080 {record=APPS-080; rule=record fields}
- project: When a Hub Sits (Paper 2)
- related_as_recorded: APPS-084
- related_to: EXP:APPS-084 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPS-080; rule=date-ordered record link}
- reported_in: PAPER:When_a_Hub_Sits_manuscript {record=APPS-080; rule=project field}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\paper2_full_result.txt
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\paper2_gate_result.txt
- title: Paper 2 topological-identity gate and confirmatory (P1a/P1b)
- uses_method: METH:regression {record=APPS-080; rule=keyword rule METHOD_RULES}

# RES:APPS-080 | Result of APPS-080
- failure_evidence: Gate passed and confirmatory P1a/P1b both confirmed at 120 team-seasons.
- failure_type: D_positive
- power_info: n=120 team-seasons, 30 franchises; n_perm=5000
- primary_result: Gate: C1 8/8 p<0.05; C2 S=0.319 perm_p=0.0002; C3 R2=0.080 PASS. Full: frobenius P1a S=0.352 p=0.0000 CI[0.327,0.378]; P1b S=0.353 CI[0.329,0.379]; cosine P1a 0.155 / P1b 0.144. residual_R2=0.043. D_obs mean=373.7. P1a=CONFIRMED P1b=CONFIRMED.
- record_stratum: supported
- record_substatus: mechanism D_positive
- verdict: supported
