# FAM:SF-APPS-087 | Study family SF-APPS-087 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-087
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:confounding {family=SF-APPS-087; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-APPS-087; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: CONFOUNDING
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPS-087 | Finding of SF-APPS-087: rejected
- confidence: 0.95
- derived_from: EXP:APPS-087 {family=SF-APPS-087; rule=family member}
- rules_out: HYP:SF-APPS-087 {family=SF-APPS-087; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: Star dTS +0.05 pp p=0.937; dTO +0.74 pp p=0.00364 (wrong sign for shielding). Star-init TO~HasConn beta=+0.34 pp p=0.439. HasConn on-off PPP BOTH_NULL (mean -0.041 p=0.939, median +0.528 p=0.731, n=73). Frequent-conn lineup ORtg lift LOO +1.559 p=0.0184 but talent-controlled beta +0.915 p=0.51 n=428. Held-4 swap dORtg +0.427 p=0.565 n=296.
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-APPS-087 | Hypothesis of SF-APPS-087
- addresses: RQC:RQC-127 {family=SF-APPS-087; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPS-087 {decided_by=APPS-087; family=SF-APPS-087; rule=automated adjudication stratum}
- source_record: APPS-087
- tested_by: EXP:APPS-087 {record=APPS-087; rule=family hypothesis tested by member record}
- text: Connector presence shields stars (higher TS, lower TO) and lifts lineup ORtg beyond talent.
