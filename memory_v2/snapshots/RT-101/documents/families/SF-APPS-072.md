# FAM:SF-APPS-072 | Study family SF-APPS-072 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-072
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:selection_or_regression_to_the_mean {family=SF-APPS-072; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- risk_code: RTM_SELECTION
- validation_status: no_validation_recorded

# FIND:SF-APPS-072 | Finding of SF-APPS-072: supported
- confidence: 0.95
- derived_from: EXP:APPS-072 {family=SF-APPS-072; rule=family member}
- statement: Sim DiD ATT=-0.076 [-0.081,-0.071] n_pairs=25561 vs real +0.408; gap +0.484. Trigger count 25564 (32.9% of game x PT cells) vs ~5500 RS. Raw unmatched decline sim -0.504 vs real ~-0.655.
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-APPS-072 | Hypothesis of SF-APPS-072
- addresses: RQC:RQC-038 {family=SF-APPS-072; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPS-072
- supported_by: FIND:SF-APPS-072 {decided_by=APPS-072; family=SF-APPS-072; rule=automated adjudication stratum}
- tested_by: EXP:APPS-072 {record=APPS-072; rule=family hypothesis tested by member record}
- text: A memoryless process matching possession micro-stats will reproduce the Paper 1 matched DiD suppression excess.
