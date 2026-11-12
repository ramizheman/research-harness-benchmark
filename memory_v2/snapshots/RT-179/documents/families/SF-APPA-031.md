# FAM:SF-APPA-031 | Study family SF-APPA-031 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism E_unclear
- confidence: 0.45
- confidence_level: low
- deciding_record: APPA-031
- decision_rule: R0 single record
- failure_mechanism: E_unclear
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:label_or_classification_error {family=SF-APPA-031; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: E_unclear=1
- members_disagree: no
- outcome_status: supported
- risk_code: BASE_RATE
- risk_code: LABEL_ERROR
- validation_evidence: APPA-031: '908 holdout game-team pairs; terciles of l1 distance; 6 illustrative ca'
- validation_status: same_pipeline_validation

# FIND:SF-APPA-031 | Finding of SF-APPA-031: supported
- confidence: 0.45
- derived_from: EXP:APPA-031 {family=SF-APPA-031; rule=family member}
- statement: Closest vs most-deviated tercile +3.3 ORtg adjusted (raw +5.2); Spearman rho >0.4 in 62% of games. Cases: GSW-LAL rho 1.00 coachable +28.0 ORtg; MIA-BOS rho 0.80 aligned residual +27.9; NYK-LAL rho 0.80 coachable +25.0; CLE-PHX rho -0.80; LAL-GSW rho 0.90 residual +12.3 despite deviation; MIN-DEN rho 0.10 L1=0.99 residual -29.8.
- status: supported
- validation_status: same_pipeline_validation

# HYP:SF-APPA-031 | Hypothesis of SF-APPA-031
- addresses: RQC:RQC-022 {family=SF-APPA-031; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPA-031
- supported_by: FIND:SF-APPA-031 {decided_by=APPA-031; family=SF-APPA-031; rule=automated adjudication stratum}
- tested_by: EXP:APPA-031 {record=APPA-031; rule=family hypothesis tested by member record}
- text: Games where the team mix was closest to the engine recommendation score more after strength adjustment.
