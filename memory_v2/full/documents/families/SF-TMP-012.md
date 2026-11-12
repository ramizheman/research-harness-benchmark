# FAM:SF-TMP-012 | Study family SF-TMP-012 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 0.95
- confidence_level: high
- deciding_record: TMP-012
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_basis: earlier family (by recorded point dates) with overlapping limitation
- knowable_before_outcome_auto: yes_from_history_probable
- limitation_precedent: FAM:SF-TMP-001 {family=SF-TMP-012; rule=knowability: earlier family with overlapping limitation}
- limited_by: LIM:drift {family=SF-TMP-012; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:insufficient_exposure {family=SF-TMP-012; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:selection_or_regression_to_the_mean {family=SF-TMP-012; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- repeat_order_unknown: FAM:SF-TMP-001 {family=SF-TMP-012; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.349}
- risk_code: DRIFT_NONSTATIONARITY
- risk_code: EXPOSURE_SPARSITY
- risk_code: MECHANICAL_FLOOR
- risk_code: PLACEBO_DEPENDENCE
- validation_evidence: TMP-012: 'published estimator on frozen csv (f) and current graph (g), thresholds 0.10-0.50, five n'
- validation_status: same_pipeline_validation

# FIND:SF-TMP-012 | Finding of SF-TMP-012: artifact
- confidence: 0.95
- derived_from: EXP:TMP-012 {family=SF-TMP-012; rule=family member}
- rules_out: HYP:SF-TMP-012 {family=SF-TMP-012; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: Reproduced excess 0.4080 CI [0.378,0.438]; G within-unit perm at 0.25: obs 0.3798 null 0.3744 resid +0.0054 z 0.40; asym neg-pos 0.0176 p 0.258; drift-centered tail mass ratio 1.007.
- status: artifact
- validation_status: same_pipeline_validation

# HYP:SF-TMP-012 | Hypothesis of SF-TMP-012
- addresses: RQC:RQC-073 {family=SF-TMP-012; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-TMP-012 {decided_by=TMP-012; family=SF-TMP-012; rule=automated adjudication stratum}
- source_record: TMP-012
- tested_by: EXP:TMP-012 {record=TMP-012; rule=family hypothesis tested by member record}
- text: The published suppression excess (trigger drop minus matched control drop) exceeds appropriate null models and is asymmetric between decline and improvement tails.
