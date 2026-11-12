# FAM:SF-APPA-026 | Study family SF-APPA-026 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict abandoned
- confidence: 0.95
- confidence_level: high
- deciding_record: APPA-026
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-APPA-026; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: abandoned
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPA-026 | Finding of SF-APPA-026: untestable
- confidence: 0.95
- derived_from: EXP:APPA-026 {family=SF-APPA-026; rule=family member}
- statement: Pairs with both agent and engine recs: 0; agent scoreable n=0; engine hit 2/3 (66.7%).
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-APPA-026 | Hypothesis of SF-APPA-026
- addresses: RQC:RQC-027 {family=SF-APPA-026; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPA-026 {decided_by=APPA-026; family=SF-APPA-026; rule=automated adjudication stratum}
- source_record: APPA-026
- tested_by: EXP:APPA-026 {record=APPA-026; rule=family hypothesis tested by member record}
- text: A generalist LLM (gemini-2.5-flash) on raw aggregates agrees with the engine and beats the team modal PT.
