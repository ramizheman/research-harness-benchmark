# EXP:APPA-008 | Audit of overnight LLM adaptation-analysis batch ('9/10 adaptation predicts winning')
- date: 2026-05-24
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: Methodology audit of 104 game reports, 10 series, 2073 tool calls; code and graph verification.
- hypothesis: The agent batch's findings (defensive adjustments, point costs, adaptation predicts series winners 9/10) are valid.
- knowable_in_advance: yes
- measures: VAR:win_probability_series_outcome {record=APPA-008; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPA-008 {record=APPA-008; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Half-level PPP splits verified as real; causal and winning claims not validated.
- prespecified: no
- produced: RES:APPA-008 {record=APPA-008; rule=record fields}
- project: Team Adaptation
- related_as_recorded: APPA-009
- related_to: EXP:APPA-009 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPA-008; rule=date-ordered record link}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADAPTATION_AUDIT.md
- title: Audit of overnight LLM adaptation-analysis batch ('9/10 adaptation predicts winning')
- uses_dataset: DS:LLM_or_agent_outputs {record=APPA-008; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Playoff_series_outcomes {record=APPA-008; rule=keyword rule DATASET_RULES}
- uses_method: METH:LLM_agent_run {record=APPA-008; rule=keyword rule METHOD_RULES}

# RES:APPA-008 | Result of APPA-008
- failure_evidence: Series winners never looked up (0/2073 calls); master '9/10' rule built from LLM inference on inference; low-n claims (e.g. 0.0 PPP on n=3).
- failure_type: C_artifact
- primary_result: 706 findings with n<5; list_h2h_games called 0 times; series winners LLM-inferred; MIA-BOS G7 score invented (BOS 100 vs graph 84); what_came_next skips a possession; point costs are LLM arithmetic.
- record_stratum: artifact
- record_substatus: verdict artifact_found
- verdict: artifact_found
