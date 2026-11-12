# FAM:SF-CHT-007 | Study family SF-CHT-007 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 1.0
- confidence_level: high
- deciding_record: CHT-007
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:small_sample {family=SF-CHT-007; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- validation_evidence: CHT-007: '23,922 holdout possessions; model b historical baseline vs a static matchu'
- validation_status: same_pipeline_validation

# FIND:SF-CHT-007 | Finding of SF-CHT-007: rejected
- confidence: 1.0
- derived_from: EXP:CHT-007 {family=SF-CHT-007; rule=family member}
- rules_out: HYP:SF-CHT-007 {family=SF-CHT-007; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: Value added /100: B +37.4, A +35.9, A2 +29.1. A2 underperformed baseline in 96/240 matchups, outperformed in 47/240 (20%). CALIBRATION_REPORT_V6 R^2 = 0.032.
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-CHT-007 | Hypothesis of SF-CHT-007
- addresses: RQC:RQC-010 {family=SF-CHT-007; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-CHT-007 {decided_by=CHT-007; family=SF-CHT-007; rule=automated adjudication stratum}
- source_record: CHT-007
- tested_by: EXP:CHT-007 {record=CHT-007; rule=family hypothesis tested by member record}
- text: Matchup-specific kernel recommendations outperform using each team's own historical numbers.
