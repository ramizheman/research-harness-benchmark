# FAM:SF-APPS-088 | Study family SF-APPS-088 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-088
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:small_sample {family=SF-APPS-088; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- repeated_by_later_family: FAM:SF-PAP-028 {family=SF-APPS-088; order=after; rule=lexical similarity >= repeat threshold; similarity=0.427}
- risk_code: MECHANICAL_FLOOR
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPS-088 | Finding of SF-APPS-088: supported
- confidence: 0.95
- derived_from: EXP:APPS-088 {family=SF-APPS-088; rule=family member}
- statement: Unmatched conn vs role D_A 0.2020 vs 0.1021, t=5.97 p=2.87e-08. Usage-matched vs role: paired dD_A +0.1151, P(conn>ctrl)=81.2%, t=6.35 p=7.35e-09 n=96. Vs terminal: +0.0777 t=2.37 p=0.0261 n=25.
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-APPS-088 | Hypothesis of SF-APPS-088
- addresses: RQC:RQC-044 {family=SF-APPS-088; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPS-088
- supported_by: FIND:SF-APPS-088 {decided_by=APPS-088; family=SF-APPS-088; rule=automated adjudication stratum}
- tested_by: EXP:APPS-088 {record=APPS-088; rule=family hypothesis tested by member record}
- text: Connector absence displaces team offensive identity (D_A) more than usage-matched non-organizer absence.
