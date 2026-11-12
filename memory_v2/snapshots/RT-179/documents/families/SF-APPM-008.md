# FAM:SF-APPM-008 | Study family SF-APPM-008 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inadequately tested: verdict null, mechanism B_powered_null, no power information
- confidence: 0.75
- confidence_level: high
- deciding_record: APPM-008
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- validation_evidence: APPM-008: 'r2_hol +0.1244 (lift +0.0094); adding more features lowered holdout r2 (12f +0.1167). max lift +0.0094; doc calls ~0.12 the p'
- validation_status: same_pipeline_validation

# FIND:SF-APPM-008 | Finding of SF-APPM-008: uncertain
- confidence: 0.75
- derived_from: EXP:APPM-008 {family=SF-APPM-008; rule=family member}
- statement: Best +xPPP + per-pt interaction R2_hol +0.1244 (lift +0.0094); adding more features lowered holdout R2 (12f +0.1167).
- status: uncertain
- validation_status: same_pipeline_validation

# HYP:SF-APPM-008 | Hypothesis of SF-APPM-008
- addresses: RQC:RQC-084 {family=SF-APPM-008; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-APPM-008 {decided_by=APPM-008; family=SF-APPM-008; rule=automated adjudication stratum}
- source_record: APPM-008
- tested_by: EXP:APPM-008 {record=APPM-008; rule=family hypothesis tested by member record}
- text: Stacking all clean-signal features raises the R2 ceiling materially.
