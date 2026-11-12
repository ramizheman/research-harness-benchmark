# FAM:SF-APPA-063 | Study family SF-APPA-063 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism C_artifact
- confidence: 0.75
- confidence_level: high
- deciding_record: APPA-063
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: supported
- repeat_order_unknown: FAM:SF-APPA-035 {family=SF-APPA-063; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.44}
- risk_code: DRIFT_NONSTATIONARITY
- validation_evidence: APPA-063: 'train 523,517 possession sequences; 454 holdout games; 908 (game, team) rows; spearman of predicted vs actu'
- validation_status: same_pipeline_validation

# FIND:SF-APPA-063 | Finding of SF-APPA-063: supported
- confidence: 0.75
- derived_from: EXP:APPA-063 {family=SF-APPA-063; rule=family member}
- statement: Median rho +0.539 (IQR +0.245 to +0.750); 62.4% rho>0.4; 88.4% rho>0; 10.5% rho<0. Top-3 median hit 100%; >=2/3 hits 78.9%; median lift +0.4261 PPP; 90.8% positive lift. Bottom-3 median suppression 66.7%. MAE cited in later reports 0.0922 PPP.
- status: supported
- validation_status: same_pipeline_validation

# HYP:SF-APPA-063 | Hypothesis of SF-APPA-063
- addresses: RQC:RQC-024 {family=SF-APPA-063; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPA-063
- supported_by: FIND:SF-APPA-063 {decided_by=APPA-063; family=SF-APPA-063; rule=automated adjudication stratum}
- tested_by: EXP:APPA-063 {record=APPA-063; rule=family hypothesis tested by member record}
- text: Pre-game PT PPP ranking from training data correlates with actual efficiency ranking in held-out games.
