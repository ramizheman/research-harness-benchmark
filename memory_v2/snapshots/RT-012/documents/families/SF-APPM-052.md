# FAM:SF-APPM-052 | Study family SF-APPM-052 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inconclusive
- confidence: 0.65
- confidence_level: medium
- deciding_record: APPM-052
- decision_rule: R0 single record
- failure_mechanism: E_unclear
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-APPM-052; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: E_unclear=1
- members_disagree: no
- outcome_status: inconclusive
- repeat_order_unknown: FAM:SF-APPS-002 {family=SF-APPM-052; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.392}
- risk_code: DRIFT_NONSTATIONARITY
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPM-052 | Finding of SF-APPM-052: uncertain
- confidence: 0.65
- derived_from: EXP:APPM-052 {family=SF-APPM-052; rule=family member}
- statement: Agent review: H1 PPP 1.158 -> H2 0.971. PULL_UP 1.6 (n=5) -> 0.5 (n=6); cost vs H2H 1.361: (1.361-0.5)*6=5.166 points. PNR 1.0 (n=4) -> 0.333 (n=6); cost (1.0-0.333)*6=4.002. Combined 9.168 points. Tactical review: reportable-PT overall 1.157 (n=38) -> 1.171 (n=35); PNR 1.0 (n=4) -> 0.333 (n=6), cost vs H2H 1.172: 4.895 points; PULL_UP 1.25 (n=4) -> 0.75 (n=4).
- status: uncertain
- validation_status: no_validation_recorded

# HYP:SF-APPM-052 | Hypothesis of SF-APPM-052
- addresses: RQC:RQC-007 {family=SF-APPM-052; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-APPM-052 {decided_by=APPM-052; family=SF-APPM-052; rule=automated adjudication stratum}
- source_record: APPM-052
- tested_by: EXP:APPM-052 {record=APPM-052; rule=family hypothesis tested by member record}
- text: MIA failed to pivot after H1-H2 suppression of PULL_UP/PNR in 2023 ECF G6 (0042200306), leaving points vs H2H baseline.
