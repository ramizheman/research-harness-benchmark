# EXP:APPM-018 | Scoring-run microstructure
- date: 2026-05-07
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: 71,383 runs (>=6 unanswered points) over 1,090,642 possessions / 5,207 games.
- hypothesis: Describe what initiates, sustains and breaks scoring runs.
- knowable_in_advance: unclear
- member_of: FAM:SF16 {record=APPM-018; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- prespecified: no
- produced: RES:APPM-018 {record=APPM-018; rule=record fields}
- project: Strategy app
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_analyze_scoring_runs.py
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\run_microstructure_findings.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\run_sequences.csv
- title: Scoring-run microstructure
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPM-018; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPM-018; rule=keyword rule DATASET_RULES}

# RES:APPM-018 | Result of APPM-018
- failure_evidence: No hypothesis test; frequencies not compared to baseline volumes.
- failure_type: E_unclear
- primary_result: SPOT_UP initiates 22.9% of runs; OTHER most common sustaining type 22.8%; DRIVE most common run-breaker 20.4%.
- record_stratum: not_a_test
- record_substatus: descriptive
- verdict: descriptive
