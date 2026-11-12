# EXP:APPS-004 | Post-hoc calibrated decision quality hit rate (--calibrated)
- date: 2026-05-23
- date_basis: mtime
- date_issues: file modification time: upper bound only; 12 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: Post-hoc scalar reweighting of cached Neo4j PT distributions instead of re-running the engine; 80 scoreable pairs.
- hypothesis: Applying playoff calibration scalars (DRIVE excluded) raises the engine's hit rate vs modal PT.
- knowable_in_advance: yes
- member_of: FAM:SF-APPS-004 {record=APPS-004; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Calibration was tuned on the same series it was scored on.
- prespecified: no
- produced: RES:APPS-004 {record=APPS-004; rule=record fields}
- project: Strategy app
- related_as_recorded: SQ2 decision quality hit rate
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\decision_quality_findings.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\validation\deprecated\README.md
- title: Post-hoc calibrated decision quality hit rate (--calibrated)
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPS-004; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Playoff_series_outcomes {record=APPS-004; rule=keyword rule DATASET_RULES}
- uses_method: METH:calibration_scoring {record=APPS-004; rule=keyword rule METHOD_RULES}

# RES:APPS-004 | Result of APPS-004
- failure_evidence: Deprecated: 'Post-hoc PPP scalars on Neo4j mix, not is_playoff=True engine run; ~96%' and 'inflates hit rate'.
- failure_type: C_artifact
- power_info: n=80
- primary_result: Hit rate 51.7% (31/60) before vs 96.2% (77/80) after; high-conf 42.9% -> 96.6%; CUT recs 66 with 95%.
- record_stratum: artifact
- record_substatus: verdict artifact_found
- verdict: artifact_found
