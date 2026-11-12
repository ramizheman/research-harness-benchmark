# FAM:SF-CHT-006 | Study family SF-CHT-006 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: mechanism C_artifact with verdict failed_gate
- confidence: 0.8
- confidence_level: high
- deciding_record: CHT-006
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: not_supported
- validation_evidence: CHT-006: 'layer ablation of holdout r^2 contributors (optimizer, usage-decay, scheme/suppressio'
- validation_status: same_pipeline_validation

# FIND:SF-CHT-006 | Finding of SF-CHT-006: artifact
- confidence: 0.8
- derived_from: EXP:CHT-006 {family=SF-CHT-006; rule=family member}
- rules_out: HYP:SF-CHT-006 {family=SF-CHT-006; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: Offense best-response optimizer delta R^2 = -0.488 (primary culprit); usage-decay curves -0.077; scheme/suppression listed as secondary in the ranked table.
- status: artifact
- validation_status: same_pipeline_validation

# HYP:SF-CHT-006 | Hypothesis of SF-CHT-006
- addresses: RQC:RQC-138 {family=SF-CHT-006; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-CHT-006 {decided_by=CHT-006; family=SF-CHT-006; rule=automated adjudication stratum}
- source_record: CHT-006
- tested_by: EXP:CHT-006 {record=CHT-006; rule=family hypothesis tested by member record}
- text: The remaining R^2 gap after calibration is from data, not from the equilibrium optimizer compressing variance.
