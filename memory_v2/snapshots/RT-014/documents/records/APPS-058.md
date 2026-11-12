# EXP:APPS-058 | Observed on-ball defensive scheme labels (ORL-DET G1)
- date: 2026-04-20
- date_basis: mtime
- date_issues: file modification time: upper bound only; 11 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: Single game 0042500101. Confident labels vs OTHER.
- hypothesis: NBA matchup/PBP fields can label on-ball coverage (DROP/ICE/SWITCH) at usable rates.
- knowable_in_advance: yes
- measures: VAR:PPP_points_per_possession {record=APPS-058; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPS-058 {record=APPS-058; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: ICE_CANDIDATE is unconfirmed without screen-contact tracking.
- prespecified: no
- produced: RES:APPS-058 {record=APPS-058; rule=record fields}
- project: Strategy app
- related_as_recorded: APPS-054
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\observed_defense_0042500101.md
- title: Observed on-ball defensive scheme labels (ORL-DET G1)
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPS-058; rule=keyword rule DATASET_RULES}
- uses_method: METH:matched_control {record=APPS-058; rule=keyword rule METHOD_RULES}

# RES:APPS-058 | Result of APPS-058
- failure_evidence: Confident label rates 14.9% and 3.3%; NBA matchups feed did not populate switches_on.
- failure_type: A_unanswerable
- power_info: n=67/60 possessions, 10/2 labeled
- primary_result: DET: 67 on-ball HC poss, 10 labeled (14.9%) ? DROP n=5 PPP=1.20, ICE_CANDIDATE n=5 PPP=0.80, OTHER n=57 PPP=1.42. ORL: 60 poss, 2 labeled (3.3%). switches_on unpopulated.
- record_stratum: untestable
- record_substatus: mechanism A_unanswerable with verdict failed_gate
- verdict: failed_gate
