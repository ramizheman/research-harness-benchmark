# EXP:APPA-027 | Agent Test B: LLM counter selection vs deterministic BEST tier
- also_recorded_as: APPS-046
- date: 2026-06-15
- date_basis: mtime
- date_issues: file modification time: upper bound only; 9 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: 3 suppression triggers; H2 PPP as referee.
- hypothesis: The LLM picks the same counter as the BEST tier, and when it disagrees it is right in H2.
- knowable_in_advance: yes
- measures: VAR:PPP_points_per_possession {record=APPA-027; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPA-027 {record=APPA-027; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- prespecified: no
- produced: RES:APPA-027 {record=APPA-027; rule=record fields}
- project: Strategy app
- related_as_recorded: APPA-028
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\AGENT_TEST_B_findings_gemini_2_5_flash.md
- title: Agent Test B: LLM counter selection vs deterministic BEST tier
- uses_dataset: DS:LLM_or_agent_outputs {record=APPA-027; rule=keyword rule DATASET_RULES}
- uses_method: METH:LLM_agent_run {record=APPA-027; rule=keyword rule METHOD_RULES}

# RES:APPA-027 | Result of APPA-027
- failure_evidence: n=3 triggers; caveat says 230+ disagreements needed.
- failure_type: A_unanswerable
- power_info: n=3
- primary_result: Agrees with BEST 1/3; picks AVOID 2/3; disagreements engine right 2/2; mean H2 PPP BEST 1.650, agent 1.154, AVOID 0.642.
- record_stratum: untestable
- record_substatus: mechanism A_unanswerable with verdict inconclusive
- verdict: inconclusive
