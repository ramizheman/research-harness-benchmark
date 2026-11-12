# FAM:SF-APPS-004 | Study family SF-APPS-004 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-004
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-APPS-004; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- repeat_order_unknown: FAM:SF-APPS-003 {family=SF-APPS-004; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.404}
- risk_code: LEAKAGE_LOOKAHEAD
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPS-004 | Finding of SF-APPS-004: artifact
- confidence: 0.95
- derived_from: EXP:APPS-004 {family=SF-APPS-004; rule=family member}
- rules_out: HYP:SF-APPS-004 {family=SF-APPS-004; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: Hit rate 51.7% (31/60) before vs 96.2% (77/80) after; high-conf 42.9% -> 96.6%; CUT recs 66 with 95%.
- status: artifact
- validation_status: no_validation_recorded

# HYP:SF-APPS-004 | Hypothesis of SF-APPS-004
- addresses: RQC:RQC-035 {family=SF-APPS-004; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-APPS-004 {decided_by=APPS-004; family=SF-APPS-004; rule=automated adjudication stratum}
- source_record: APPS-004
- tested_by: EXP:APPS-004 {record=APPS-004; rule=family hypothesis tested by member record}
- text: Applying playoff calibration scalars (DRIVE excluded) raises the engine's hit rate vs modal PT.
