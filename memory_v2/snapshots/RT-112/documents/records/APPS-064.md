# EXP:APPS-064 | Gate 1: defensive assignment network modularity vs volume-schedule null
- date: 2026-07-12
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: 2023-24 RS. attackers=257 defenders=252 possessions=196782. Compare Q_obs to Q_null.
- hypothesis: Attacker-defender assignment networks have community structure beyond volume and schedule.
- knowable_in_advance: unclear
- member_of: FAM:SF-APPS-064 {record=APPS-064; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: gate2_reassignment_probe.py exists but no saved result file was found in sequence_memory/output.
- prespecified: yes
- produced: RES:APPS-064 {record=APPS-064; rule=record fields}
- project: Strategy app
- related_as_recorded: APPS-081
- related_to: EXP:APPS-081 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPS-064; rule=date-ordered record link}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\gate1_assignment_structure.py
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\gate1_assignment_structure.txt
- title: Gate 1: defensive assignment network modularity vs volume-schedule null
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPS-064; rule=keyword rule DATASET_RULES}

# RES:APPS-064 | Result of APPS-064
- failure_evidence: Observed modularity is below the volume-schedule null (z=-46.85); gate instruction is do NOT lean on topology.
- failure_type: B_powered_null
- power_info: n=196782 possessions, 257x252
- primary_result: Q_obs=0.3838; Q_null=0.4300+-0.0010 range[0.4282,0.4324]; z=-46.85 p_emp=1.000. VERDICT: KILL ? no structure beyond volume+schedule.
- record_stratum: rejected
- record_substatus: verdict failed_gate, powered null with power information
- verdict: failed_gate
