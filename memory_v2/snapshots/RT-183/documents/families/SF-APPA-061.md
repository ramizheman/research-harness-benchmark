# FAM:SF-APPA-061 | Study family SF-APPA-061 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict null
- confidence: 0.95
- confidence_level: high
- deciding_record: APPA-061
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:multiple_testing {family=SF-APPA-061; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-APPA-061; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: MULTIPLE_TESTING
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPA-061 | Finding of SF-APPA-061: untestable
- confidence: 0.95
- derived_from: EXP:APPA-061 {family=SF-APPA-061; rule=family member}
- statement: Median regret V4 0.102 [0.067, 0.128] vs V5 0.067 [0.050, 0.100], Holm p=0.062. V5 beats V4 11/40 vs 4/40, McNemar p=0.118. Override 8/40 (20%); override hit rate 25.0% [0.000, 1.000]. Brittle precision 7.5%. Parse 40/40. Runtime 60.1s vs 349.6s (5.816x).
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-APPA-061 | Hypothesis of SF-APPA-061
- addresses: RQC:RQC-069 {family=SF-APPA-061; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPA-061 {decided_by=APPA-061; family=SF-APPA-061; rule=automated adjudication stratum}
- source_record: APPA-061
- tested_by: EXP:APPA-061 {record=APPA-061; rule=family hypothesis tested by member record}
- text: LangGraph agents (V5) improve play-type recommendations over the deterministic engine (V4).
