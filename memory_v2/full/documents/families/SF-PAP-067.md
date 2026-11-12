# FAM:SF-PAP-067 | Study family SF-PAP-067 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 0.95
- confidence_level: high
- deciding_record: PAP-067
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:low_measurement_reliability {family=SF-PAP-067; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- risk_code: MEASURE_RELIABILITY
- validation_evidence: PAP-067: 'same gate2 cross-fit as hub sits; 201 rows vs paper's 148; g1 scaling and odd/ev'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-067 | Finding of SF-PAP-067: supported
- confidence: 0.95
- derived_from: EXP:PAP-067 {family=SF-PAP-067; rule=family member}
- statement: gate2 n=201: mean R=+0.192 vs Rp=+0.022 (diff +0.170); T=+0.157 vs Tp=+0.147 (diff +0.011); L_pre>=0.02 n=79 mean R=+0.216; gate1 n=201: R=+0.567 vs Rp=+0.416; O=+0.474 vs Op=+0.419; g1_mc median=0.0051, g1_scale median=0.0069; R split-half Spearman 0.412 (SB 0.583); O Spearman 0.609 (SB 0.757)
- status: supported
- validation_status: same_pipeline_validation

# HYP:SF-PAP-067 | Hypothesis of SF-PAP-067
- addresses: RQC:RQC-019 {family=SF-PAP-067; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: PAP-067
- supported_by: FIND:SF-PAP-067 {decided_by=PAP-067; family=SF-PAP-067; rule=automated adjudication stratum}
- tested_by: EXP:PAP-067 {record=PAP-067; rule=family hypothesis tested by member record}
- text: Cross-fitted restoration exceeds the no-absence placebo on a broader 201-spell pool (29 franchises).
