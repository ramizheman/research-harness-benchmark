# FAM:SF-APPM-014 | Study family SF-APPM-014 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: not_a_test
- automated_substatus: tool_eval_fail
- confidence: 0.75
- confidence_level: high
- deciding_record: APPM-014
- decision_rule: R0 no member is a hypothesis test
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:label_or_classification_error {family=SF-APPM-014; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:leakage {family=SF-APPM-014; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-APPM-014; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: tool_evaluation
- risk_code: LABEL_ERROR
- risk_code: LEAKAGE_LOOKAHEAD
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# HYP:SF-APPM-014 | Hypothesis of SF-APPM-014
- addresses: RQC:RQC-030 {family=SF-APPM-014; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPM-014
- tested_by: EXP:APPM-014 {record=APPM-014; rule=family hypothesis tested by member record}
- text: Inferred play-type labels match benchmark volumes, foul rates, PPP and known team identities.
