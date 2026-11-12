# FAM:SF-CHT-029 | Study family SF-CHT-029 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: mechanism C_artifact with verdict failed_gate
- confidence: 0.8
- confidence_level: high
- deciding_record: CHT-029
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:confounding {family=SF-CHT-029; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: not_supported
- repeat_order_unknown: FAM:SF-APPS-073 {family=SF-CHT-029; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.416}
- risk_code: CONFOUNDING
- validation_status: no_validation_recorded

# FIND:SF-CHT-029 | Finding of SF-CHT-029: artifact
- confidence: 0.8
- derived_from: EXP:CHT-029 {family=SF-CHT-029; rule=family member}
- rules_out: HYP:SF-CHT-029 {family=SF-CHT-029; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: FAIL decay-sanity: DRIVE lifts +0.015,+0.020,+0.018,+0.021,+0.020 (flat). Within-team: DRIVE lag-1 +0.015 to -0.002. Cohen d ~0.01-0.03; p~0 from n>150k. Callable play-type horizons = 0.
- status: artifact
- validation_status: no_validation_recorded

# HYP:SF-CHT-029 | Hypothesis of SF-CHT-029
- addresses: RQC:RQC-015 {family=SF-CHT-029; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-CHT-029 {decided_by=CHT-029; family=SF-CHT-029; rule=automated adjudication stratum}
- source_record: CHT-029
- tested_by: EXP:CHT-029 {record=CHT-029; rule=family hypothesis tested by member record}
- text: Play-type actions have decaying cross-possession memory (lag-1 effect >= lag-2; not just score margin or team quality).
