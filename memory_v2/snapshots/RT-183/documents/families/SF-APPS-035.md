# FAM:SF-APPS-035 | Study family SF-APPS-035 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict reversed, powered null with power information
- confidence: 1.0
- confidence_level: high
- deciding_record: APPS-035
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:selection_or_regression_to_the_mean {family=SF-APPS-035; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-APPS-035; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- repeat_of_earlier_family: FAM:SF-APPS-044 {family=SF-APPS-035; order=before; rule=lexical similarity >= repeat threshold; similarity=0.365}
- risk_code: SAMPLE_SIZE_POWER
- validation_evidence: APPS-035: 'ense already failed to adapt. n=24 players with n_x>=15; po replication not run significant league-wide decline (-0.065 ppp, p=0'
- validation_status: same_pipeline_validation

# FIND:SF-APPS-035 | Finding of SF-APPS-035: rejected
- confidence: 1.0
- derived_from: EXP:APPS-035 {family=SF-APPS-035; rule=family member}
- rules_out: HYP:SF-APPS-035 {family=SF-APPS-035; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: Mean X-Z uplift -0.065, t=-2.41, p=0.025, n=24 (16 negative / 8 positive). Pearson r(uplift, IE%)=0.031, p=0.885. Brunson X-Z=+0.003 (rank 8/24). Raw clutch vs overall: Edwards +0.225, Giannis -0.240; Brunson -0.021.
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-APPS-035 | Hypothesis of SF-APPS-035
- addresses: RQC:RQC-035 {family=SF-APPS-035; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPS-035 {decided_by=APPS-035; family=SF-APPS-035; rule=automated adjudication stratum}
- source_record: APPS-035
- tested_by: EXP:APPS-035 {record=APPS-035; rule=family hypothesis tested by member record}
- text: Stars elevate in clutch possessions of games where their team had a suppression trigger.
