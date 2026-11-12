# EXP:APPS-005 | Within-series should-vs-did hit rate (leverage_argmax contamination)
- date: 2026-06-10
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: Should-vs-did comparison from _analyze_series_learning.py (findings file at repo root, not read).
- hypothesis: Teams' in-series play-type choices matched what the engine said they should do and this predicted success.
- knowable_in_advance: unclear
- member_of: FAM:SF-APPS-005 {record=APPS-005; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Date is mtime of the deprecated README; original findings file is outside this slice.
- prespecified: no
- produced: RES:APPS-005 {record=APPS-005; rule=record fields}
- project: Strategy app
- related_as_recorded: SQ2 decision quality hit rate
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\validation\README.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\validation\deprecated\README.md
- title: Within-series should-vs-did hit rate (leverage_argmax contamination)
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPS-005; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Playoff_series_outcomes {record=APPS-005; rule=keyword rule DATASET_RULES}
- uses_method: METH:difference_in_differences {record=APPS-005; rule=keyword rule METHOD_RULES}
- uses_method: METH:matched_control {record=APPS-005; rule=keyword rule METHOD_RULES}

# RES:APPS-005 | Result of APPS-005
- failure_evidence: 'Engine used leverage_argmax fallback -> inflated CUT-style picks; ~92.6% hit rate'.
- failure_type: C_artifact
- primary_result: ~92.6% hit rate
- record_stratum: artifact
- record_substatus: verdict artifact_found
- verdict: artifact_found
