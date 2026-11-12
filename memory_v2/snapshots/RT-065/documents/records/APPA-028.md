# EXP:APPA-028 | Agent Test C: 3-agent halftime debate vs optimizer counter
- also_recorded_as: APPS-047
- date: 2026-06-16
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: 5 suppression triggers; agreement and H2 PPP when they disagree.
- hypothesis: The LLM debate adds value over the deterministic optimizer counter.
- knowable_in_advance: yes
- measures: VAR:PPP_points_per_possession {record=APPA-028; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPA-028 {record=APPA-028; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Debate decision text and picked PT disagree in some rows (e.g. picked POST_UP while decision says SPOT_UP or CUT), suggesting a parsing bug.
- prespecified: no
- produced: RES:APPA-028 {record=APPA-028; rule=record fields}
- project: Strategy app
- related_as_recorded: APPA-027
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\AGENT_TEST_C_optimizer_vs_debate.md
- title: Agent Test C: 3-agent halftime debate vs optimizer counter
- uses_dataset: DS:LLM_or_agent_outputs {record=APPA-028; rule=keyword rule DATASET_RULES}
- uses_method: METH:LLM_agent_run {record=APPA-028; rule=keyword rule METHOD_RULES}

# RES:APPA-028 | Result of APPA-028
- failure_evidence: n=5 triggers, 3 disagreements.
- failure_type: A_unanswerable
- power_info: n=5
- primary_result: Agreement 2/5 (40%); disagreements 3: debate wins 1, optimizer 1, tie 1; mean H2 PPP optimizer 1.812 vs debate 1.683.
- record_stratum: untestable
- record_substatus: mechanism A_unanswerable with verdict inconclusive
- verdict: inconclusive
