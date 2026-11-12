# EXP:APPS-074 | Gravity persistence: elite creator -> teammate PPP at lags 1-3
- date: 2026-06-15
- date_basis: mtime
- date_issues: file modification time: upper bound only; 9 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: Exact match offensive lineup_id x margin bucket x period. 8 creators x 3 lags. BH-FDR 24 PPP cells.
- hypothesis: After an elite creator's signature action, teammates score more on the team's next k possessions with the same lineup on the floor.
- knowable_in_advance: unclear
- measures: VAR:PPP_points_per_possession {record=APPS-074; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPS-074 {record=APPS-074; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Usage redistribution without points payoff for Giannis is the only surviving structural cell.
- prespecified: yes
- produced: RES:APPS-074 {record=APPS-074; rule=record fields}
- project: Strategy app
- related_as_recorded: APPS-065
- related_to: EXP:APPS-065 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPS-074; rule=date-ordered record link}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\gravity_persistence.md
- title: Gravity persistence: elite creator -> teammate PPP at lags 1-3
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPS-074; rule=keyword rule DATASET_RULES}
- uses_method: METH:matched_control {record=APPS-074; rule=keyword rule METHOD_RULES}

# RES:APPS-074 | Result of APPS-074
- failure_evidence: No elite creator produces a positive lineup-matched teammate-PPP lift at any lag.
- failure_type: B_powered_null
- power_info: Jokic lag-1 n=1880; Giannis n=1804; Doncic n=325
- primary_result: All 8 creators horizon=0. Jokic lag-1 ATT=+0.0282 CI[-0.043,+0.099] p=0.3779. CLEAN NULL on teammate PPP. Secondary: Antetokounmpo +0.075 distinct initiators over next 3 poss (perm p=0.0002, BH 0.003) ? structure not efficiency.
- record_stratum: rejected
- record_substatus: verdict null, powered null with power information
- verdict: null
