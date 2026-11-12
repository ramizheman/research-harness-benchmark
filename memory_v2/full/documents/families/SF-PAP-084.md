# FAM:SF-PAP-084 | Study family SF-PAP-084 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: mechanism C_artifact with verdict null
- confidence: 0.8
- confidence_level: high
- deciding_record: PAP-084
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_basis: earlier family (date order certain) with overlapping limitation
- knowable_before_outcome_auto: yes_from_history
- limitation_precedent: FAM:SF-APPA-001 {family=SF-PAP-084; rule=knowability: earlier family with overlapping limitation}
- limitation_precedent: FAM:SF-APPS-058 {family=SF-PAP-084; rule=knowability: earlier family with overlapping limitation}
- limitation_precedent: FAM:SF-TMP-007 {family=SF-PAP-084; rule=knowability: earlier family with overlapping limitation}
- limited_by: LIM:label_or_classification_error {family=SF-PAP-084; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:low_power_large_MDE {family=SF-PAP-084; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-PAP-084; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: not_supported
- repeat_order_unknown: FAM:SF-PAP-081 {family=SF-PAP-084; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.423}
- risk_code: DRIFT_NONSTATIONARITY
- risk_code: LABEL_ERROR
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-PAP-084 | Finding of SF-PAP-084: artifact
- confidence: 0.8
- derived_from: EXP:PAP-084 {family=SF-PAP-084; rule=family member}
- rules_out: HYP:SF-PAP-084 {family=SF-PAP-084; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: team-season timing r=0.59 CI[0.43,0.71] n=90; pair-specific r=-0.01 [-0.05,+0.03] n=2,553; personnel slope halves r=0.00; post hoc within clock mean effect +0.8 pp then +0.4 with stint, half-to-half r=0.27-0.32
- status: artifact
- validation_status: no_validation_recorded

# HYP:SF-PAP-084 | Hypothesis of SF-PAP-084
- addresses: RQC:RQC-070 {family=SF-PAP-084; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-PAP-084 {decided_by=PAP-084; family=SF-PAP-084; rule=automated adjudication stratum}
- source_record: PAP-084
- tested_by: EXP:PAP-084 {record=PAP-084; rule=family hypothesis tested by member record}
- text: Timing or personnel response repeats across season halves or across meetings with the same opponent.
