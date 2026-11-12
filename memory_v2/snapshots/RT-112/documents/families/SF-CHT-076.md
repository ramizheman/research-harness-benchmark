# FAM:SF-CHT-076 | Study family SF-CHT-076 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: mechanism C_artifact with verdict null
- confidence: 0.8
- confidence_level: high
- deciding_record: CHT-076
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_basis: earlier family (date order certain) with overlapping limitation
- knowable_before_outcome_auto: yes_from_history
- limitation_precedent: FAM:SF15 {family=SF-CHT-076; rule=knowability: earlier family with overlapping limitation}
- limited_by: LIM:insufficient_exposure {family=SF-CHT-076; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: not_supported
- repeat_order_unknown: FAM:SF-TMP-022 {family=SF-CHT-076; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.624}
- risk_code: EXPOSURE_SPARSITY
- risk_code: MECHANICAL_FLOOR
- risk_code: PLACEBO_DEPENDENCE
- validation_evidence: CHT-076: '3 vs 4 team fouls (clock>2:30) with 2-3 and 4-5+ placebos; foul-trouble big remaining on court vs guard placebo. bon'
- validation_status: same_pipeline_validation

# FIND:SF-CHT-076 | Finding of SF-CHT-076: artifact
- confidence: 0.8
- derived_from: EXP:CHT-076 {family=SF-CHT-076; rule=family member}
- rules_out: HYP:SF-CHT-076 {family=SF-CHT-076; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: Bonus FTA +5.08pp (SE 0.19) mechanical; DRIVE +0.31pp (SE 0.21) identical to 2-3 placebo +0.33pp. Foul-trouble big: rim +1.36pp (SE 0.41 t=+3.4); DRIVE +0.47pp t=+1.3; PPP +0.008; occurs on 1.44% of possessions.
- status: artifact
- validation_status: same_pipeline_validation

# HYP:SF-CHT-076 | Hypothesis of SF-CHT-076
- addresses: RQC:RQC-016 {family=SF-CHT-076; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-CHT-076 {decided_by=CHT-076; family=SF-CHT-076; rule=automated adjudication stratum}
- source_record: CHT-076
- tested_by: EXP:CHT-076 {record=CHT-076; rule=family hypothesis tested by member record}
- text: Offenses attack more at the bonus threshold and when an opposing big in foul trouble stays on the floor.
