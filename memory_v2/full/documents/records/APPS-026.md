# EXP:APPS-026 | Dose-response of continuation ratio vs matched excess decline
- date: 2026-07-26
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: OLS excess ~ cont_ratio + self_h1 + C(season)+C(play_type), cluster-robust SE by game. Exploratory post-hoc.
- hypothesis: Among 11064 suppression triggers, higher h2_n/h1_n continuation predicts larger matched-pair excess decline.
- knowable_in_advance: unclear
- member_of: FAM:SF14 {record=APPS-026; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Pre-specified read was that a CI including zero means no dose-response at this sample size.
- prespecified: partial
- produced: RES:APPS-026 {record=APPS-026; rule=record fields}
- project: Strategy app
- related_as_recorded: APPS-025
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\dose_response_continuation_results.md
- title: Dose-response of continuation ratio vs matched excess decline
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPS-026; rule=keyword rule DATASET_RULES}
- uses_method: METH:matched_control {record=APPS-026; rule=keyword rule METHOD_RULES}
- uses_method: METH:regression {record=APPS-026; rule=keyword rule METHOD_RULES}

# RES:APPS-026 | Result of APPS-026
- failure_evidence: Primary CI includes 0 at n=11064 (p=0.09336); every caliper 0.05-0.30 and all six play types ns.
- failure_type: B_powered_null
- power_info: n=11064 triggers, 4606 game clusters
- primary_result: Raw n=11064: beta_cont=+0.0120, 95% CI [-0.0020,+0.0261], p=0.09336. Caliper 0.10: +0.0095 [-0.0122,+0.0312], p=0.392. All caliper and play-type strata not significant.
- record_stratum: rejected
- record_substatus: verdict null, powered null with power information
- verdict: null
