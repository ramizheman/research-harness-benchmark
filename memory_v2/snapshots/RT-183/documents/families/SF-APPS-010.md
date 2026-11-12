# FAM:SF-APPS-010 | Study family SF-APPS-010 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inadequately tested: verdict null, mechanism E_unclear
- confidence: 0.65
- confidence_level: medium
- deciding_record: APPS-010
- decision_rule: R0 single record
- failure_mechanism: E_unclear
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:selection_or_regression_to_the_mean {family=SF-APPS-010; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: E_unclear=1
- members_disagree: no
- outcome_status: not_supported
- validation_status: no_validation_recorded

# FIND:SF-APPS-010 | Finding of SF-APPS-010: uncertain
- confidence: 0.65
- derived_from: EXP:APPS-010 {family=SF-APPS-010; rule=family member}
- statement: DRIVE 0.889 -> 0.949 (+0.060); CUT +0.114; PNR +0.087; PULL_UP -0.077; POST_UP -0.032.
- status: uncertain
- validation_status: no_validation_recorded

# HYP:SF-APPS-010 | Hypothesis of SF-APPS-010
- addresses: RQC:RQC-034 {family=SF-APPS-010; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-APPS-010 {decided_by=APPS-010; family=SF-APPS-010; rule=automated adjudication stratum}
- source_record: APPS-010
- tested_by: EXP:APPS-010 {record=APPS-010; rule=family hypothesis tested by member record}
- text: Play-type PPP (especially DRIVE) declines as a playoff series progresses, so DRIVE is a good early-series call.
