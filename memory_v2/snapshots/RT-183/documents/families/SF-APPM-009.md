# FAM:SF-APPM-009 | Study family SF-APPM-009 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict reversed, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPM-009
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- validation_status: no_validation_recorded

# FIND:SF-APPM-009 | Finding of SF-APPM-009: rejected
- confidence: 0.95
- derived_from: EXP:APPM-009 {family=SF-APPM-009; rule=family member}
- rules_out: HYP:SF-APPM-009 {family=SF-APPM-009; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: After worse on 5/5 metrics: A3 R2 -0.0866 -> -0.2225 (normalized -0.2285); win-side accuracy 65.0% -> 48.3% (53.3% normalized).
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-APPM-009 | Hypothesis of SF-APPM-009
- addresses: RQC:RQC-080 {family=SF-APPM-009; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPM-009 {decided_by=APPM-009; family=SF-APPM-009; rule=automated adjudication stratum}
- source_record: APPM-009
- tested_by: EXP:APPM-009 {record=APPM-009; rule=family hypothesis tested by member record}
- text: Training on 3 seasons instead of 2024-25 only improves prediction on a fixed late-2024-25 test set.
