# EXP:APPS-024 | DRIVE-as-BEST counter vs constrained mix
- date: 2026-05-30
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: 44 qualifying triggers, 39 games, 13 teams. Mix weights CUT 15%/SPOT_UP 35%/DRIVE 30%/OTHER 20%. One-sided MW A>B and A>C.
- hypothesis: When BEST=DRIVE (counter_h2_n>=5), observed DRIVE H2 PPP beats a feasibility-constrained baseline.
- knowable_in_advance: yes
- measures: VAR:PPP_points_per_possession {record=APPS-024; rule=keyword rule VARIABLE_RULES}
- measures: VAR:play_type_share_mix {record=APPS-024; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPS-024 {record=APPS-024; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: A is left-skewed (median 1.279 > B_fixed) so MW p=0.2175 for A>B is consistent with a negative mean gap.
- prespecified: no
- produced: RES:APPS-024 {record=APPS-024; rule=record fields}
- project: Strategy app
- related_as_recorded: APPS-023
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\drive_counter_test.md
- title: DRIVE-as-BEST counter vs constrained mix
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPS-024; rule=keyword rule DATASET_RULES}

# RES:APPS-024 | Result of APPS-024
- failure_evidence: Observed gap -0.066 is below MDE 0.180; n=44 cannot distinguish a true null from an effect up to 0.18 PPP.
- failure_type: A_unanswerable
- power_info: n=44; MDE 0.180 PPP at 80% power (SD~0.34); 0.265 if SD~0.5
- primary_result: A mean=1.178 vs B_game 1.236 (gap=-0.058, p=0.6069) vs B_fixed 1.244 (gap=-0.066, p=0.2175) vs coach default C 1.134 (gap=+0.043, p=0.3052). MDE at 80% power ~0.180 PPP (SD~0.34).
- record_stratum: untestable
- record_substatus: mechanism A_unanswerable with verdict inconclusive
- verdict: inconclusive
