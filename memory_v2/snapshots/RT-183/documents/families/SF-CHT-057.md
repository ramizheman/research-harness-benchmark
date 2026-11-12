# FAM:SF-CHT-057 | Study family SF-CHT-057 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 1.0
- confidence_level: high
- deciding_record: CHT-057
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:small_sample {family=SF-CHT-057; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- risk_code: SAMPLE_SIZE_POWER
- validation_evidence: CHT-057: 'dian delta +0.167; bottom 35% median -0.039. loo auc 0.622; permutation p=0.005. drop gafford rho=+0.244 p=0.020. exploratory scrip'
- validation_status: same_pipeline_validation

# FIND:SF-CHT-057 | Finding of SF-CHT-057: supported
- confidence: 1.0
- derived_from: EXP:CHT-057 {family=SF-CHT-057; rule=family member}
- statement: Cut share rho=+0.265 p=0.011 AUC 0.653. Cut-drive rho=+0.314 p=0.002 AUC 0.656. Drive rho=-0.278 p=0.007. Top cut tercile 65% portable median Delta +0.167; bottom 35% median -0.039. LOO AUC 0.622; permutation p=0.005. Drop Gafford rho=+0.244 p=0.020.
- status: supported
- validation_status: same_pipeline_validation

# HYP:SF-CHT-057 | Hypothesis of SF-CHT-057
- addresses: RQC:RQC-128 {family=SF-CHT-057; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: CHT-057
- supported_by: FIND:SF-CHT-057 {decided_by=CHT-057; family=SF-CHT-057; rule=automated adjudication stratum}
- tested_by: EXP:CHT-057 {record=CHT-057; rule=family hypothesis tested by member record}
- text: Pre-move cut share (vs drive share) predicts whether a connector's organizational function reproduces after a move.
