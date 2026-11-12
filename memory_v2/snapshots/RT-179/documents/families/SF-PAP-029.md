# FAM:SF-PAP-029 | Study family SF-PAP-029 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict null
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-029
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:low_power_large_MDE {family=SF-PAP-029; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-PAP-029; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-PAP-029 | Finding of SF-PAP-029: untestable
- confidence: 1.0
- derived_from: EXP:PAP-029 {family=SF-PAP-029; rule=family member}
- statement: 'underpowered and null once corrected for landing-spot quality' (no numbers)
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-PAP-029 | Hypothesis of SF-PAP-029
- addresses: RQC:RQC-004 {family=SF-PAP-029; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-PAP-029 {decided_by=PAP-029; family=SF-PAP-029; rule=automated adjudication stratum}
- source_record: PAP-029
- tested_by: EXP:PAP-029 {record=PAP-029; rule=family hypothesis tested by member record}
- text: Portability relates to destination net rating change.
