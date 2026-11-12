# FAM:SF-APPM-002 | Study family SF-APPM-002 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPM-002
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- repeat_order_unknown: FAM:SF-APPM-006 {family=SF-APPM-002; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.482}
- validation_evidence: APPM-002: 'per top-n player, swept k_player shrinkage; val 690 cells, holdout 520 cells; compare r2_hol to 8-feat baseline +0.1150. top_n'
- validation_status: same_pipeline_validation

# FIND:SF-APPM-002 | Finding of SF-APPM-002: rejected
- confidence: 0.95
- derived_from: EXP:APPM-002 {family=SF-APPM-002; rule=family member}
- rules_out: HYP:SF-APPM-002 {family=SF-APPM-002; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: top_n=3 best R2_hol +0.0971 (lift -0.0179); top_n=1 best R2_hol +0.0865 (lift -0.0285).
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-APPM-002 | Hypothesis of SF-APPM-002
- addresses: RQC:RQC-037 {family=SF-APPM-002; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPM-002 {decided_by=APPM-002; family=SF-APPM-002; rule=automated adjudication stratum}
- source_record: APPM-002
- tested_by: EXP:APPM-002 {record=APPM-002; rule=family hypothesis tested by member record}
- text: Adding star on/off presence features (top-1 or top-3 players) improves holdout R2 over shipped 8-feature OLS.
