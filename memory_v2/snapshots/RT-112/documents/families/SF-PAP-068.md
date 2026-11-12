# FAM:SF-PAP-068 | Study family SF-PAP-068 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-068
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:low_measurement_reliability {family=SF-PAP-068; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-PAP-068; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- repeat_order_unknown: FAM:SF36 {family=SF-PAP-068; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.425}
- risk_code: MEASURE_RELIABILITY
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-PAP-068 | Finding of SF-PAP-068: supported
- confidence: 1.0
- derived_from: EXP:PAP-068 {family=SF-PAP-068; rule=family member}
- statement: odd/even reliability: opp 3s 0.004; opp 2s 0.463; XNET 0.585; own luck 0.477; teammate luck 0.427; PM 0.549; H1 opp3 -> H2 opp3 per 100: +0.008 (SE 0.009); H1 opp2 -> H2: +0.009 (SE 0.009)
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-PAP-068 | Hypothesis of SF-PAP-068
- addresses: RQC:RQC-017 {family=SF-PAP-068; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: PAP-068
- supported_by: FIND:SF-PAP-068 {decided_by=PAP-068; family=SF-PAP-068; rule=automated adjudication stratum}
- tested_by: EXP:PAP-068 {record=PAP-068; rule=family hypothesis tested by member record}
- text: Opponent three-point luck is noise: split-half reliability ~0 and H1 does not predict H2.
