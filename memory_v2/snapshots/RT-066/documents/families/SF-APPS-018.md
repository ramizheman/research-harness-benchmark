# FAM:SF-APPS-018 | Study family SF-APPS-018 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inconclusive
- confidence: 0.65
- confidence_level: medium
- deciding_record: APPS-018
- decision_rule: R0 single record
- failure_mechanism: E_unclear
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:leakage {family=SF-APPS-018; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:low_measurement_reliability {family=SF-APPS-018; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-APPS-018; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: E_unclear=1
- members_disagree: no
- outcome_status: inconclusive
- repeat_order_unknown: FAM:SF-APPM-026 {family=SF-APPS-018; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.52}
- risk_code: DRIFT_NONSTATIONARITY
- risk_code: LEAKAGE_LOOKAHEAD
- risk_code: MEASURE_RELIABILITY
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPS-018 | Finding of SF-APPS-018: uncertain
- confidence: 0.65
- derived_from: EXP:APPS-018 {family=SF-APPS-018; rule=family member}
- statement: Spearman rho=-0.0639, p=0.099717, n=665 (no clear full-rank signal). Kruskal-Wallis H=32.9723, p=2.7e-05. Mann-Whitney BEST 1.257 (n=56) vs AVOID 1.092 (n=160), U=5546.0, p=0.004018. Trigger accuracy rho=0.4525, n=121. Follow rate vs H2 PPP rho=-0.0664, p=0.5486, n=84.
- status: uncertain
- validation_status: no_validation_recorded

# HYP:SF-APPS-018 | Hypothesis of SF-APPS-018
- addresses: RQC:RQC-001 {family=SF-APPS-018; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-APPS-018 {decided_by=APPS-018; family=SF-APPS-018; rule=automated adjudication stratum}
- source_record: APPS-018
- tested_by: EXP:APPS-018 {record=APPS-018; rule=family hypothesis tested by member record}
- text: When a defense drops a play type >=0.25 PPP H1 to H2, playsheet counter ranking predicts which alternative scored better in H2 (BEST > SECOND > AVOID).
