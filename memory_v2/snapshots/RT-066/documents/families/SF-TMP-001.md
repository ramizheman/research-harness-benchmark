# FAM:SF-TMP-001 | Study family SF-TMP-001 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 0.95
- confidence_level: high
- deciding_record: TMP-001
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:insufficient_exposure {family=SF-TMP-001; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:selection_or_regression_to_the_mean {family=SF-TMP-001; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- repeat_order_unknown: FAM:SF-TMP-012 {family=SF-TMP-001; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.351}
- risk_code: EXPOSURE_SPARSITY
- risk_code: MECHANICAL_FLOOR
- risk_code: RTM_SELECTION
- validation_evidence: TMP-001: 'reproduce 1,136 caliper-matched trigger/control pairs from frozen csvs; reverse-trigger placebo; 20-rep multinomial null simu'
- validation_status: same_pipeline_validation

# FIND:SF-TMP-001 | Finding of SF-TMP-001: artifact
- confidence: 0.95
- derived_from: EXP:TMP-001 {family=SF-TMP-001; rule=family member}
- rules_out: HYP:SF-TMP-001 {family=SF-TMP-001; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: No log saved; analytic_bias.py print string cites 'observed 0.408, simulation 0.440' for E[excess|H0].
- status: artifact
- validation_status: same_pipeline_validation

# HYP:SF-TMP-001 | Hypothesis of SF-TMP-001
- addresses: RQC:RQC-061 {family=SF-TMP-001; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-TMP-001 {decided_by=TMP-001; family=SF-TMP-001; rule=automated adjudication stratum}
- source_record: TMP-001
- tested_by: EXP:TMP-001 {record=TMP-001; rule=family hypothesis tested by member record}
- text: The published H1->H2 suppression excess (0.408) exceeds what regression to the mean and selection on the H2 drop produce under no true change.
