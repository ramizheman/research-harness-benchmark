# FAM:SF-APPM-006 | Study family SF-APPM-006 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPM-006
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- repeat_order_unknown: FAM:SF-APPM-002 {family=SF-APPM-006; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.477}
- validation_evidence: APPM-006: 'train possessions) to shipped 6-feat calibrator; val 690 / holdout cells. 8-feat r2_hol +0.1150 vs 6-feat +0.0835 (lift +0.031'
- validation_status: same_pipeline_validation

# FIND:SF-APPM-006 | Finding of SF-APPM-006: supported
- confidence: 0.95
- derived_from: EXP:APPM-006 {family=SF-APPM-006; rule=family member}
- statement: 8-feat R2_hol +0.1150 vs 6-feat +0.0835 (lift +0.0315).
- status: supported
- validation_status: same_pipeline_validation

# HYP:SF-APPM-006 | Hypothesis of SF-APPM-006
- addresses: RQC:RQC-030 {family=SF-APPM-006; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPM-006
- supported_by: FIND:SF-APPM-006 {decided_by=APPM-006; family=SF-APPM-006; rule=automated adjudication stratum}
- tested_by: EXP:APPM-006 {record=APPM-006; rule=family hypothesis tested by member record}
- text: Offensive/defensive starter-share features improve holdout R2.
