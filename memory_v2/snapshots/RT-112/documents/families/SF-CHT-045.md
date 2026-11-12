# FAM:SF-CHT-045 | Study family SF-CHT-045 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 1.0
- confidence_level: high
- deciding_record: CHT-045
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:leakage {family=SF-CHT-045; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- risk_code: LEAKAGE_LOOKAHEAD
- validation_evidence: CHT-045: 'eam-games; leaky target uses this-game h2 ppp; ex-ante uses loso historical degradation from other 54 series. leaky within-t'
- validation_status: same_pipeline_validation

# FIND:SF-CHT-045 | Finding of SF-CHT-045: artifact
- confidence: 1.0
- derived_from: EXP:CHT-045 {family=SF-CHT-045; rule=family member}
- rules_out: HYP:SF-CHT-045 {family=SF-CHT-045; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: Leaky within-team win gap +11.5% (team-FE p=0.039). Ex-ante -2.7%, coef +0.25 p=0.47; Spearman(cost, H2 PPP) -0.33 to -0.04. Head-to-head ex-ante p=0.32 vs general mix p=0.008. Capped general eq-mix +8.8pp win still cited as standing.
- status: artifact
- validation_status: same_pipeline_validation

# HYP:SF-CHT-045 | Hypothesis of SF-CHT-045
- addresses: RQC:RQC-142 {family=SF-CHT-045; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-CHT-045 {decided_by=CHT-045; family=SF-CHT-045; rule=automated adjudication stratum}
- source_record: CHT-045
- tested_by: EXP:CHT-045 {record=CHT-045; rule=family hypothesis tested by member record}
- text: Adhering to a suppression-conditional recommended mix predicts winning.
