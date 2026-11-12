# FAM:SF-APPA-062 | Study family SF-APPA-062 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict inconclusive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPA-062
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-APPA-062; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: inconclusive
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPA-062 | Finding of SF-APPA-062: untestable
- confidence: 0.95
- derived_from: EXP:APPA-062 {family=SF-APPA-062; rule=family member}
- statement: Mean regret: V0_NEUTRAL 0.1072, V0_TEAM 0.1053, V2_TEAM 0.1003, V4 0.1148, V5 0.0979. V2 vs V0_NEUTRAL mean_diff -0.0069 p=0.190. V4 vs V0_NEUTRAL +0.0075 p=0.563 (V4 worse). V5 vs V4 n_diff=15 beat_rate 0.275 / cond 0.733 mean_diff -0.0169 p=0.0309. V5 vs V0_NEUTRAL -0.0093 p=0.2589.
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-APPA-062 | Hypothesis of SF-APPA-062
- addresses: RQC:RQC-079 {family=SF-APPA-062; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPA-062 {decided_by=APPA-062; family=SF-APPA-062; rule=automated adjudication stratum}
- source_record: APPA-062
- tested_by: EXP:APPA-062 {record=APPA-062; rule=family hypothesis tested by member record}
- text: Scheme fingerprint (V2), optimizer (V4), and agents (V5) beat a scheme-neutral team PPP baseline on |projected-observed| regret.
