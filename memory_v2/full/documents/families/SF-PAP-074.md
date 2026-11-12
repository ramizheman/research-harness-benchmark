# FAM:SF-PAP-074 | Study family SF-PAP-074 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict null
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-074
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- validation_status: no_validation_recorded

# FIND:SF-PAP-074 | Finding of SF-PAP-074: untestable
- confidence: 1.0
- derived_from: EXP:PAP-074 {family=SF-PAP-074; rule=family member}
- statement: offense tau~0, k~1.4e8; defense tau=1.45 per 100, k~6,700; model B nearly identical to A; player ratings vs single-poss points r=0.03-0.04, SD of predictions 5.2 per 100
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-PAP-074 | Hypothesis of SF-PAP-074
- addresses: RQC:RQC-175 {family=SF-PAP-074; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-PAP-074 {decided_by=PAP-074; family=SF-PAP-074; rule=automated adjudication stratum}
- source_record: PAP-074
- tested_by: EXP:PAP-074 {record=PAP-074; rule=family hypothesis tested by member record}
- text: A lineup layer (EB residuals of the five) improves prediction beyond ridge player ratings.
