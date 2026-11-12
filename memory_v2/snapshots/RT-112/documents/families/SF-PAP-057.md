# FAM:SF-PAP-057 | Study family SF-PAP-057 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inconclusive
- confidence: 0.7
- confidence_level: medium
- deciding_record: PAP-057
- decision_rule: R0 single record
- failure_mechanism: E_unclear
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-PAP-057; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: E_unclear=1
- members_disagree: no
- outcome_status: inconclusive
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-PAP-057 | Finding of SF-PAP-057: uncertain
- confidence: 0.7
- derived_from: EXP:PAP-057 {family=SF-PAP-057; rule=family member}
- statement: 2/6 high-load clean hits (Brunson dir 0.75 [p95 0.49]; Davis 0.88 [0.37]); Booker pattern right magnitude smaller (0.87); Wembanyama magnitude right pattern wrong (0.29 [0.38]); Poeltl and Maxey confounded (co-abs 0.52/0.41); 4/5 low-load accurate; Langford non-specific; descriptive Spearman L vs excess +0.79 (11) / +0.71 (8)
- status: uncertain
- validation_status: no_validation_recorded

# HYP:SF-PAP-057 | Hypothesis of SF-PAP-057
- addresses: RQC:RQC-163 {family=SF-PAP-057; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-PAP-057 {decided_by=PAP-057; family=SF-PAP-057; rule=automated adjudication stratum}
- source_record: PAP-057
- tested_by: EXP:PAP-057 {record=PAP-057; rule=family hypothesis tested by member record}
- text: High L_pre (>=0.10) forecasts large, pattern-matching reorganization; low L_pre forecasts little change.
