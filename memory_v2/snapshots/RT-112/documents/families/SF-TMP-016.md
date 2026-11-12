# FAM:SF-TMP-016 | Study family SF-TMP-016 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict null
- confidence: 0.95
- confidence_level: high
- deciding_record: TMP-016
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_basis: earlier family (by recorded point dates) with overlapping limitation
- knowable_before_outcome_auto: yes_from_history_probable
- limitation_precedent: FAM:SF-APPS-085 {family=SF-TMP-016; rule=knowability: earlier family with overlapping limitation}
- limitation_precedent: FAM:SF-CHT-064 {family=SF-TMP-016; rule=knowability: earlier family with overlapping limitation}
- limitation_precedent: FAM:SF35 {family=SF-TMP-016; rule=knowability: earlier family with overlapping limitation}
- limited_by: LIM:low_measurement_reliability {family=SF-TMP-016; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: MEASURE_RELIABILITY
- validation_evidence: TMP-016: 'seasons; team-season slopes, true-heterogeneity variance vs permutation null, odd/even split-half. adaptation slope +0.1168 (0.0589'
- validation_status: same_pipeline_validation

# FIND:SF-TMP-016 | Finding of SF-TMP-016: untestable
- confidence: 0.95
- derived_from: EXP:TMP-016 {family=SF-TMP-016; rule=family member}
- statement: Adaptation slope +0.1168 (0.0589); heterogeneity var +0.029821 vs null +0.014085 p=0.363; split-half r=-0.026 p=0.655; persistence split-half r=+0.067 p=0.251.
- status: untestable
- validation_status: same_pipeline_validation

# HYP:SF-TMP-016 | Hypothesis of SF-TMP-016
- addresses: RQC:RQC-003 {family=SF-TMP-016; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-TMP-016 {decided_by=TMP-016; family=SF-TMP-016; rule=automated adjudication stratum}
- source_record: TMP-016
- tested_by: EXP:TMP-016 {record=TMP-016; rule=family hypothesis tested by member record}
- text: Teams differ reliably in how H1 play-type PPP moves H2 usage/persistence.
