# FAM:SF-PAP-091 | Study family SF-PAP-091 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: mechanism C_artifact with verdict null
- confidence: 0.8
- confidence_level: high
- deciding_record: PAP-091
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: LEAKAGE_LOOKAHEAD
- validation_evidence: PAP-091: '0.17453 vs 0.17454; xgb sweep best 0.17463 vs 0.17454 later loso 2nd-stage isotonic was kept (~0.17240 vs ~0.17421) after th'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-091 | Finding of SF-PAP-091: artifact
- confidence: 0.8
- derived_from: EXP:PAP-091 {family=SF-PAP-091; rule=family member}
- rules_out: HYP:SF-PAP-091 {family=SF-PAP-091; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: SWA 0.18082 vs 0.18063; per-fold Platt 0.18671 vs 0.17978; beta 0.18361 vs 0.17932; MLP chain 0.16937 flagged overfit (~705 params on 1449 OOF); in-sample 2nd isotonic 0.17301 flagged overfit; RF 0.17453 vs 0.17454; XGB sweep best 0.17463 vs 0.17454
- status: artifact
- validation_status: same_pipeline_validation

# HYP:SF-PAP-091 | Hypothesis of SF-PAP-091
- addresses: RQC:RQC-107 {family=SF-PAP-091; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-PAP-091 {decided_by=PAP-091; family=SF-PAP-091; rule=automated adjudication stratum}
- source_record: PAP-091
- tested_by: EXP:PAP-091 {record=PAP-091; rule=family hypothesis tested by member record}
- text: Further ensemble/calibration complexity improves Brier beyond 0.17454.
