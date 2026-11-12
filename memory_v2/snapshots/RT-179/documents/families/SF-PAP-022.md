# FAM:SF-PAP-022 | Study family SF-PAP-022 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict null
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-022
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-PAP-022; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-PAP-022 | Finding of SF-PAP-022: untestable
- confidence: 1.0
- derived_from: EXP:PAP-022 {family=SF-PAP-022; rule=family member}
- statement: 0 FDR survivors at q<0.05; a few raw p<0.05
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-PAP-022 | Hypothesis of SF-PAP-022
- addresses: RQC:RQC-056 {family=SF-PAP-022; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-PAP-022 {decided_by=PAP-022; family=SF-PAP-022; rule=automated adjudication stratum}
- source_record: PAP-022
- tested_by: EXP:PAP-022 {record=PAP-022; rule=family hypothesis tested by member record}
- text: Some destination context feature predicts shaper portability.
