# FAM:SF-CHT-072 | Study family SF-CHT-072 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 1.0
- confidence_level: high
- deciding_record: CHT-072
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:low_measurement_reliability {family=SF-CHT-072; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- repeat_of_earlier_family: FAM:SF-CHT-064 {family=SF-CHT-072; order=before; rule=lexical similarity >= repeat threshold; similarity=0.368}
- risk_code: DRIFT_NONSTATIONARITY
- risk_code: MEASURE_RELIABILITY
- validation_evidence: CHT-072: '3,000 units; 120 team-seasons; se ~0.65pp per 1.0 ppp fails split-half, season-to-season, and excess-spread tests; style traits re'
- validation_status: same_pipeline_validation

# FIND:SF-CHT-072 | Finding of SF-CHT-072: rejected
- confidence: 1.0
- derived_from: EXP:CHT-072 {family=SF-CHT-072; rule=family member}
- rules_out: HYP:SF-CHT-072 {family=SF-CHT-072; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: Adaptation odd-even r=-0.03 perm p=0.66; season-to-season -0.17, +0.25, +0.06; spread p=0.36. Persistence r=+0.07 p=0.25. PNR share odd-even r=+0.95, spot-up +0.87. League-wide H1 to H2 slope 0.02. Sampling SE ~0.65pp usage per 1.0 PPP; true spread can't be much above 0.4.
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-CHT-072 | Hypothesis of SF-CHT-072
- addresses: RQC:RQC-003 {family=SF-CHT-072; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-CHT-072 {decided_by=CHT-072; family=SF-CHT-072; rule=automated adjudication stratum}
- source_record: CHT-072
- tested_by: EXP:CHT-072 {record=CHT-072; rule=family hypothesis tested by member record}
- text: Some teams adapt (shift H2 usage with H1 PPP) more than others as a replicable trait.
