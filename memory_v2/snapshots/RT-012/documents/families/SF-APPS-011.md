# FAM:SF-APPS-011 | Study family SF-APPS-011 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-011
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- validation_status: no_validation_recorded

# FIND:SF-APPS-011 | Finding of SF-APPS-011: supported
- confidence: 0.95
- derived_from: EXP:APPS-011 {family=SF-APPS-011; rule=family member}
- statement: DRIVE RS 1.198 vs PO 0.912 (-0.286, 25 teams); PNR -0.173; PULL_UP +0.301; others within -0.07.
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-APPS-011 | Hypothesis of SF-APPS-011
- addresses: RQC:RQC-024 {family=SF-APPS-011; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPS-011
- supported_by: FIND:SF-APPS-011 {decided_by=APPS-011; family=SF-APPS-011; rule=automated adjudication stratum}
- tested_by: EXP:APPS-011 {record=APPS-011; rule=family hypothesis tested by member record}
- text: DRIVE PPP is materially higher in RS than playoffs, so an RS-calibrated optimizer over-recommends DRIVE.
