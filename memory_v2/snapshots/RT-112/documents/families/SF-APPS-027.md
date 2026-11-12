# FAM:SF-APPS-027 | Study family SF-APPS-027 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict null
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-027
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:confounding {family=SF-APPS-027; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-APPS-027; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: CONFOUNDING
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPS-027 | Finding of SF-APPS-027: untestable
- confidence: 0.95
- derived_from: EXP:APPS-027 {family=SF-APPS-027; rule=family member}
- statement: corr(talent, adapt)=+0.124. Per-series logistic: talent_diff_z +0.737 p=0.0213; adapt_diff_z +0.328 p=0.2755. Team-in-series cluster: talent p=0.0095, adapt p=0.2449. Univariate adapt beta=+0.311 p=0.1128. LPM: talent +0.160 p=0.0046, adapt +0.072 p=0.2633, R2=0.142.
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-APPS-027 | Hypothesis of SF-APPS-027
- addresses: RQC:RQC-112 {family=SF-APPS-027; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPS-027 {decided_by=APPS-027; family=SF-APPS-027; rule=automated adjudication stratum}
- source_record: APPS-027
- tested_by: EXP:APPS-027 {record=APPS-027; rule=family hypothesis tested by member record}
- text: pct_ran_BEST - pct_ran_AVOID predicts series wins after controlling for RS net-rating talent.
