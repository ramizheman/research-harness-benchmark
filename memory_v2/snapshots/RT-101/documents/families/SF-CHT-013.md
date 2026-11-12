# FAM:SF-CHT-013 | Study family SF-CHT-013 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 1.0
- confidence_level: high
- deciding_record: CHT-013
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:implementation_bug {family=SF-CHT-013; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- risk_code: IMPLEMENTATION_BUG
- validation_status: no_validation_recorded

# FIND:SF-CHT-013 | Finding of SF-CHT-013: artifact
- confidence: 1.0
- derived_from: EXP:CHT-013 {family=SF-CHT-013; rule=family member}
- rules_out: HYP:SF-CHT-013 {family=SF-CHT-013; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: cmd_phase3 reads team_profiles but aggregate_series_profiles writes by_team, so observed_ppp stays empty on the pipeline path; backtest path reads by_team correctly.
- status: artifact
- validation_status: no_validation_recorded

# HYP:SF-CHT-013 | Hypothesis of SF-CHT-013
- addresses: RQC:RQC-109 {family=SF-CHT-013; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-CHT-013 {decided_by=CHT-013; family=SF-CHT-013; rule=automated adjudication stratum}
- source_record: CHT-013
- tested_by: EXP:CHT-013 {record=CHT-013; rule=family hypothesis tested by member record}
- text: A 46.9% scheme-correction hit rate (some series 0%) reflects model failure rather than a logging bug.
