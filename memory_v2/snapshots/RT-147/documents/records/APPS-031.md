# EXP:APPS-031 | Coaching pickup: H1->H2 share shift toward BEST vs AVOID
- date: 2026-05-30
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: best_pickup = H2 share - H1 share of BEST counter; 591/633 triggers with BEST defined. Also possession-weighted AVOID vs INSUFF mix H1->H2.
- hypothesis: After suppression, teams shift volume toward the sheet BEST counter and away from AVOID.
- knowable_in_advance: unclear
- measures: VAR:play_type_share_mix {record=APPS-031; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF05 {record=APPS-031; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: INSUFF_EVIDENCE dominates (~83-86% of AVOID+INSUFF possessions).
- prespecified: no
- produced: RES:APPS-031 {record=APPS-031; rule=record fields}
- project: Strategy app
- related_as_recorded: APPS-030
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\coaching_pickup_55series\coaching_pickup_report.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\h1h2_tier_mix_shift.md
- title: Coaching pickup: H1->H2 share shift toward BEST vs AVOID
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPS-031; rule=keyword rule DATASET_RULES}

# RES:APPS-031 | Result of APPS-031
- failure_evidence: BEST pickup +0.24 pp is essentially zero; teams do not shift toward BEST; AVOID ticks up slightly.
- failure_type: B_powered_null
- power_info: n=591 triggers with BEST defined
- primary_result: % shifted more toward BEST 51.6%; % used more AVOID 22.4%. Avg best pickup +0.0024 pp; BEST share 10.0%->10.2%. PO AVOID share within AVOID+INSUFF 13.4%->13.7% (+0.3 pp); BEST 12.9%->12.8%. RS AVOID +1.1 pp; BEST 13.1%->12.3%.
- record_stratum: rejected
- record_substatus: verdict null, powered null with power information
- verdict: null
