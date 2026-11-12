# FAM:SF-APPS-030 | Study family SF-APPS-030 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict null
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-030
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-APPS-030; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- repeat_order_unknown: FAM:SF05 {family=SF-APPS-030; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.446}
- validation_status: no_validation_recorded

# FIND:SF-APPS-030 | Finding of SF-APPS-030: untestable
- confidence: 0.95
- derived_from: EXP:APPS-030 {family=SF-APPS-030; rule=family member}
- statement: % ran BEST 44.7% of triggers / 9.7% volume; % ran AVOID 61.1% / 23.3% volume. Spearman BEST vs won rho=+0.131 p=0.1723; AVOID vs won rho=-0.098 p=0.3099. Mean PPP BEST 1.395 vs AVOID 0.865.
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-APPS-030 | Hypothesis of SF-APPS-030
- addresses: RQC:RQC-001 {family=SF-APPS-030; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPS-030 {decided_by=APPS-030; family=SF-APPS-030; rule=automated adjudication stratum}
- source_record: APPS-030
- tested_by: EXP:APPS-030 {record=APPS-030; rule=family hypothesis tested by member record}
- text: Teams that run BEST counters more (and AVOID less) after suppression win more series.
