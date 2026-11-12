# FAM:SF-APPS-090 | Study family SF-APPS-090 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict null
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-090
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-APPS-090; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPS-090 | Finding of SF-APPS-090: untestable
- confidence: 0.95
- derived_from: EXP:APPS-090 {family=SF-APPS-090; rule=family member}
- statement: Binary match rate 15.7%. Taxonomy CONNECTOR delta match vs mis med +0.540 vs +0.069 p=0.156 n=5/14. Travel-check delta p=0.413. All-movers delta p=0.0283 (med +0.160 vs +0.053) but Spearman(match_score, delta)=-0.034 p=0.631 n=198. Connector-only Spearmans all ns.
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-APPS-090 | Hypothesis of SF-APPS-090
- addresses: RQC:RQC-047 {family=SF-APPS-090; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPS-090 {decided_by=APPS-090; family=SF-APPS-090; rule=automated adjudication stratum}
- source_record: APPS-090
- tested_by: EXP:APPS-090 {record=APPS-090; rule=family hypothesis tested by member record}
- text: Diet-matching to a destination's thin initiation jobs predicts better post-move outcomes than mismatch.
