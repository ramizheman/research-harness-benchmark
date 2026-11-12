# FAM:SF-CHT-068 | Study family SF-CHT-068 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 1.0
- confidence_level: high
- deciding_record: CHT-068
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-CHT-068; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-CHT-068 | Finding of SF-CHT-068: artifact
- confidence: 1.0
- derived_from: EXP:CHT-068 {family=SF-CHT-068; rule=family member}
- rules_out: HYP:SF-CHT-068 {family=SF-CHT-068; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: CHA defense +0.366 n=14, 95% CI [+0.161, +0.572]; 2025-26 n=5 mean +0.681; pre-2025-26 ~+0.19 across 9 pairs. Top 3 games 54% of excess mass. Offense +0.480 n=17, not LaMelo-centered (Nurkic/Oubre/Smith/Knueppel).
- status: artifact
- validation_status: no_validation_recorded

# HYP:SF-CHT-068 | Hypothesis of SF-CHT-068
- addresses: RQC:RQC-146 {family=SF-CHT-068; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-CHT-068 {decided_by=CHT-068; family=SF-CHT-068; rule=automated adjudication stratum}
- source_record: CHT-068
- tested_by: EXP:CHT-068 {record=CHT-068; rule=family hypothesis tested by member record}
- text: Charlotte is a real multi-year PNR suppressor (and a star-hunting offensive victim) in the league table.
