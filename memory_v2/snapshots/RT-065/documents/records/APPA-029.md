# EXP:APPA-029 | Crunch-time identity stability year over year
- also_recorded_as: CHT-012
- date: 2026-05-06
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: 93 team-seasons 2022-25, gate >=100 crunch possessions; YoY Pearson across 62 pairs; player-attribution heuristic.
- hypothesis: Team crunch-time PPP delta vs baseline is a stable organizational identity.
- knowable_in_advance: yes
- measures: VAR:PPP_points_per_possession {record=APPA-029; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPA-029 {record=APPA-029; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Doc still calls consistently positive teams 'genuine crunch-time performers' despite r~0, and has a blank team row. Knowable because single-season PPP on ~100 possessions has SE comparable to the deltas.
- prespecified: partial
- produced: RES:APPA-029 {record=APPA-029; rule=record fields}
- project: Strategy app
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\crunch_identity_findings.md
- title: Crunch-time identity stability year over year
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPA-029; rule=keyword rule DATASET_RULES}
- uses_method: METH:correlation {record=APPA-029; rule=keyword rule METHOD_RULES}

# RES:APPA-029 | Result of APPA-029
- failure_evidence: r=-0.023 on 62 pairs; per-team-season crunch samples ~100+ possessions, so deltas of +/-0.05 PPP are within sampling noise.
- failure_type: A_unanswerable
- power_info: 62 pairs; >=100 crunch poss per team-season
- primary_result: YoY r = -0.023 (n=62 pairs); consistently positive CHI +0.056, CHA +0.040; negative NOP -0.074.
- record_stratum: untestable
- record_substatus: mechanism A_unanswerable with verdict null
- verdict: null
