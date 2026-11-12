# FAM:SF-PAP-021 | Study family SF-PAP-021 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict inconclusive
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-021
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-PAP-021; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: inconclusive
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-PAP-021 | Finding of SF-PAP-021: untestable
- confidence: 1.0
- derived_from: EXP:PAP-021 {family=SF-PAP-021; rule=family member}
- statement: cut rho=+0.32 p=0.125, AUC=0.71 (perm p=0.041); cut-minus-drive rho=+0.38 p=0.07; high-cut 75% vs low-cut 37.5% portable; drop top-3 rho=+0.22 p=0.33
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-PAP-021 | Hypothesis of SF-PAP-021
- addresses: RQC:RQC-051 {family=SF-PAP-021; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-PAP-021 {decided_by=PAP-021; family=SF-PAP-021; rule=automated adjudication stratum}
- source_record: PAP-021
- tested_by: EXP:PAP-021 {record=PAP-021; rule=family hypothesis tested by member record}
- text: Cut-heavy shapers' roles travel better than drive-heavy ones.
