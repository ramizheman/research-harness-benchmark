# FAM:SF-APPM-010 | Study family SF-APPM-010 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPM-010
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:small_sample {family=SF-APPM-010; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPM-010 | Finding of SF-APPM-010: supported
- confidence: 0.95
- derived_from: EXP:APPM-010 {family=SF-APPM-010; rule=family member}
- statement: Mean Spearman +0.524 -> +0.579 (median +0.548 -> +0.631); improves 42/84, worsens 8/84, noise 34/84.
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-APPM-010 | Hypothesis of SF-APPM-010
- addresses: RQC:RQC-090 {family=SF-APPM-010; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPM-010
- supported_by: FIND:SF-APPM-010 {decided_by=APPM-010; family=SF-APPM-010; rule=automated adjudication stratum}
- tested_by: EXP:APPM-010 {record=APPM-010; rule=family hypothesis tested by member record}
- text: Scheme-adjusted engine (Step 2) ranks play types better than baseline (Step 1).
