# FAM:SF-PAP-090 | Study family SF-PAP-090 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-090
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- validation_evidence: PAP-090: 'loso oof; keep if improved. scipy blend 0.17508->0.17491 (w xgb'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-090 | Finding of SF-PAP-090: supported
- confidence: 1.0
- derived_from: EXP:PAP-090 {family=SF-PAP-090; rule=family member}
- statement: scipy blend 0.17508->0.17491 (w XGB 0.342, Elo 0.000, LR 0.658); T=0.937 -> 0.17476; LGB 4-way -> 0.17472; era 1.5 -> 0.17452 (confirm 0.17454)
- status: supported
- validation_status: same_pipeline_validation

# HYP:SF-PAP-090 | Hypothesis of SF-PAP-090
- addresses: RQC:RQC-137 {family=SF-PAP-090; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: PAP-090
- supported_by: FIND:SF-PAP-090 {decided_by=PAP-090; family=SF-PAP-090; rule=automated adjudication stratum}
- tested_by: EXP:PAP-090 {record=PAP-090; rule=family hypothesis tested by member record}
- text: Replacing LR meta with a convex scipy blend, then T-scaling, adding LightGBM, and era-weighting 2016+ seasons, lowers full-chain Brier.
