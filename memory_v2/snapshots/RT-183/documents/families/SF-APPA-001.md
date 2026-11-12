# FAM:SF-APPA-001 | Study family SF-APPA-001 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: mechanism C_artifact with verdict failed_gate
- confidence: 0.75
- confidence_level: high
- deciding_record: APPA-001
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_basis: earlier family (by recorded point dates) with overlapping limitation
- knowable_before_outcome_auto: yes_from_history_probable
- limitation_precedent: FAM:SF-APPS-058 {family=SF-APPA-001; rule=knowability: earlier family with overlapping limitation}
- limited_by: LIM:label_or_classification_error {family=SF-APPA-001; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:selection_or_regression_to_the_mean {family=SF-APPA-001; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: not_supported
- repeat_order_unknown: FAM:SF12 {family=SF-APPA-001; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.412}
- risk_code: LABEL_ERROR
- risk_code: MECHANICAL_FLOOR
- risk_code: RTM_SELECTION
- validation_status: no_validation_recorded

# FIND:SF-APPA-001 | Finding of SF-APPA-001: artifact
- confidence: 0.75
- derived_from: EXP:APPA-001 {family=SF-APPA-001; rule=family member}
- rules_out: HYP:SF-APPA-001 {family=SF-APPA-001; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: T1 dPPP: adapter +0.0667 (n=205), neutral +0.0248 (n=50), no_signal +0.1260 (n=57), wrong_way +0.0111 (n=274). T2: adapter minus no-signal -0.0361 (1 vote), -0.1170 (2 votes). T3 next-game PPP Welch t=-1.003, p=0.842; MW p=0.863; counter-carry Welch t=-2.163, p=0.985.
- status: artifact
- validation_status: no_validation_recorded

# HYP:SF-APPA-001 | Hypothesis of SF-APPA-001
- addresses: RQC:RQC-005 {family=SF-APPA-001; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-APPA-001 {decided_by=APPA-001; family=SF-APPA-001; rule=automated adjudication stratum}
- source_record: APPA-001
- tested_by: EXP:APPA-001 {record=APPA-001; rule=family hypothesis tested by member record}
- text: If the A1 adapter PPP lift is real coverage response, wrong-way teams should do worse than no-signal teams, the gap should widen with scheme-vote confidence, and adapting in Game N should carry over to Game N+1.
