# FAM:SF-APPS-002 | Study family SF-APPS-002 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: not_a_test
- automated_substatus: tool_eval_pass
- confidence: 0.65
- confidence_level: medium
- deciding_record: APPS-002
- decision_rule: R0 no member is a hypothesis test
- failure_mechanism: E_unclear
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:small_sample {family=SF-APPS-002; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: E_unclear=1
- members_disagree: no
- outcome_status: tool_evaluation
- repeat_order_unknown: FAM:SF-APPM-052 {family=SF-APPS-002; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.392}
- validation_evidence: APPS-002: '5 tool calls, ~124-227 s each); mia_bos tiered playsheet: 5 robust, 5 fragile, 1 structural of 11 entries. pipeline smoke test'
- validation_status: same_pipeline_validation

# HYP:SF-APPS-002 | Hypothesis of SF-APPS-002
- addresses: RQC:RQC-007 {family=SF-APPS-002; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPS-002
- tested_by: EXP:APPS-002 {record=APPS-002; rule=family hypothesis tested by member record}
- text: The agent adaptation-review and v2 playsheet pipeline runs end to end on full playoff series.
