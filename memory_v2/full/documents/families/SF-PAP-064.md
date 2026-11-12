# FAM:SF-PAP-064 | Study family SF-PAP-064 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-064
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- repeat_order_unknown: FAM:SF25 {family=SF-PAP-064; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.45}
- validation_status: no_validation_recorded

# FIND:SF-PAP-064 | Finding of SF-PAP-064: rejected
- confidence: 1.0
- derived_from: EXP:PAP-064 {family=SF-PAP-064; rule=family member}
- rules_out: HYP:SF-PAP-064 {family=SF-PAP-064; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: play types: +0.0003 after 1 game, +0.0023 after 5; F3 never beats F2 (diffs ~0.00002, p>=0.14); initiators: +0.134/+0.201/+0.233/+0.269/+0.309 after 1-5 games; partial rho with L -0.02 to -0.11
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-PAP-064 | Hypothesis of SF-PAP-064
- addresses: RQC:RQC-021 {family=SF-PAP-064; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-PAP-064 {decided_by=PAP-064; family=SF-PAP-064; rule=automated adjudication stratum}
- source_record: PAP-064
- tested_by: EXP:PAP-064 {record=PAP-064; rule=family hypothesis tested by member record}
- text: Early spell games improve mix/initiator forecasts more when L_pre is high, and an F3 prior beats F2.
