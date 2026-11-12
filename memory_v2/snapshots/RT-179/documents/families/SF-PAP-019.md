# FAM:SF-PAP-019 | Study family SF-PAP-019 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict null
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-019
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-PAP-019; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-PAP-019 | Finding of SF-PAP-019: untestable
- confidence: 1.0
- derived_from: EXP:PAP-019 {family=SF-PAP-019; rule=family member}
- statement: corr(fit,Delta)=-0.09; corr(fit,portable)=-0.39; high-travel/high-fit cell 33% portable (n=6) vs 58% base
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-PAP-019 | Hypothesis of SF-PAP-019
- addresses: RQC:RQC-056 {family=SF-PAP-019; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-PAP-019 {decided_by=PAP-019; family=SF-PAP-019; rule=automated adjudication stratum}
- source_record: PAP-019
- tested_by: EXP:PAP-019 {record=PAP-019; rule=family hypothesis tested by member record}
- text: Shaper roles travel when the destination lacks a structurally similar incumbent.
