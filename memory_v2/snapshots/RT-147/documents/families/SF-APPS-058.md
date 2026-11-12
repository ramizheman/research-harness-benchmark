# FAM:SF-APPS-058 | Study family SF-APPS-058 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict failed_gate
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-058
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_basis: data-level limitation: label or classification error
- knowable_before_outcome_auto: yes_from_data
- limited_by: LIM:label_or_classification_error {family=SF-APPS-058; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-APPS-058; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: LABEL_ERROR
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPS-058 | Finding of SF-APPS-058: untestable
- confidence: 0.95
- derived_from: EXP:APPS-058 {family=SF-APPS-058; rule=family member}
- statement: DET: 67 on-ball HC poss, 10 labeled (14.9%) ? DROP n=5 PPP=1.20, ICE_CANDIDATE n=5 PPP=0.80, OTHER n=57 PPP=1.42. ORL: 60 poss, 2 labeled (3.3%). switches_on unpopulated.
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-APPS-058 | Hypothesis of SF-APPS-058
- addresses: RQC:RQC-088 {family=SF-APPS-058; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPS-058 {decided_by=APPS-058; family=SF-APPS-058; rule=automated adjudication stratum}
- source_record: APPS-058
- tested_by: EXP:APPS-058 {record=APPS-058; rule=family hypothesis tested by member record}
- text: NBA matchup/PBP fields can label on-ball coverage (DROP/ICE/SWITCH) at usable rates.
