# FAM:SF-APPS-061 | Study family SF-APPS-061 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-061
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:low_power_large_MDE {family=SF-APPS-061; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-APPS-061; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- risk_code: PLACEBO_DEPENDENCE
- risk_code: SAMPLE_SIZE_POWER
- validation_evidence: APPS-061: 'matched att by quarter; ivw trend; quarter-shuffle placebo 5000x; cochran-armitage p(score). treated=2481, control cap'
- validation_status: same_pipeline_validation

# FIND:SF-APPS-061 | Finding of SF-APPS-061: supported
- confidence: 0.95
- derived_from: EXP:APPS-061 {family=SF-APPS-061; rule=family member}
- statement: Q1 ATT=+0.0671 to Q4 -0.1394. IVW slope=-0.0649/qtr (z=-2.98, one-sided p=0.0014). Placebo p=0.0028. RS Q4 -0.1262 [-0.2240,-0.0284] n_t=465; close -0.1949; playoffs Q4 CI[-0.444,+0.138] n_t=55 underpowered. CA p=0.0378.
- status: supported
- validation_status: same_pipeline_validation

# HYP:SF-APPS-061 | Hypothesis of SF-APPS-061
- addresses: RQC:RQC-025 {family=SF-APPS-061; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPS-061
- supported_by: FIND:SF-APPS-061 {decided_by=APPS-061; family=SF-APPS-061; rule=automated adjudication stratum}
- tested_by: EXP:APPS-061 {record=APPS-061; rule=family hypothesis tested by member record}
- text: Star PPP after conceding a putback declines monotonically Q1->Q4.
