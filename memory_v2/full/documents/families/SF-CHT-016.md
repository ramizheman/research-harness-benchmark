# FAM:SF-CHT-016 | Study family SF-CHT-016 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: not_a_test
- automated_substatus: tool_eval_pass
- confidence: 1.0
- confidence_level: high
- deciding_record: CHT-016
- decision_rule: R0 no member is a hypothesis test
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:leakage {family=SF-CHT-016; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: tool_evaluation
- risk_code: DRIFT_NONSTATIONARITY
- risk_code: LEAKAGE_LOOKAHEAD
- validation_evidence: CHT-016: 'predictive calibrator (fit on val with train-only features; holdout never in coefficient estimation). two external constants (p'
- validation_status: same_pipeline_validation

# HYP:SF-CHT-016 | Hypothesis of SF-CHT-016
- addresses: RQC:RQC-141 {family=SF-CHT-016; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: CHT-016
- tested_by: EXP:CHT-016 {record=CHT-016; rule=family hypothesis tested by member record}
- text: Pooled splits feed holdout information into fitted calibrator/kernel parameters.
