# EXP:APPA-026 | Agent Test A: LLM vs engine series-level PT recommendations
- also_recorded_as: APPS-045
- date: 2026-05-23
- date_basis: mtime
- date_issues: file modification time: upper bound only; 12 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: 3 (team, series) pairs scored.
- hypothesis: A generalist LLM (gemini-2.5-flash) on raw aggregates agrees with the engine and beats the team modal PT.
- knowable_in_advance: unclear
- member_of: FAM:SF-APPA-026 {record=APPA-026; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- prespecified: no
- produced: RES:APPA-026 {record=APPA-026; rule=record fields}
- project: Strategy app
- related_as_recorded: APPA-027
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\AGENT_TEST_A_findings.md
- title: Agent Test A: LLM vs engine series-level PT recommendations
- uses_dataset: DS:LLM_or_agent_outputs {record=APPA-026; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPA-026; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Playoff_series_outcomes {record=APPA-026; rule=keyword rule DATASET_RULES}
- uses_method: METH:LLM_agent_run {record=APPA-026; rule=keyword rule METHOD_RULES}

# RES:APPA-026 | Result of APPA-026
- failure_evidence: 0 agent recommendations produced; n=3.
- failure_type: A_unanswerable
- power_info: n=3
- primary_result: Pairs with both agent and engine recs: 0; agent scoreable n=0; engine hit 2/3 (66.7%).
- record_stratum: untestable
- record_substatus: mechanism A_unanswerable with verdict abandoned
- verdict: abandoned
