# FAM:SF-TMP-009 | Study family SF-TMP-009 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 0.95
- confidence_level: high
- deciding_record: TMP-009
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:confounding {family=SF-TMP-009; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- risk_code: CONFOUNDING
- risk_code: PLACEBO_DEPENDENCE
- validation_evidence: TMP-009: 'teammates' prior pull_ups, shot-selection controls, fatigue placebo, with (pullup2) and without (pullup3) lineup fe. with lineu'
- validation_status: same_pipeline_validation

# FIND:SF-TMP-009 | Finding of SF-TMP-009: artifact
- confidence: 0.95
- derived_from: EXP:TMP-009 {family=SF-TMP-009; rule=family member}
- rules_out: HYP:SF-TMP-009 {family=SF-TMP-009; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: With lineup FE: slope holding shot fixed -0.0255 (0.0061); shooter's earlier scored -0.1044 vs not scored +0.0693. No lineup FE: -0.0063 (0.0036); placebo other play types -0.0075 (0.0017).
- status: artifact
- validation_status: same_pipeline_validation

# HYP:SF-TMP-009 | Hypothesis of SF-TMP-009
- addresses: RQC:RQC-063 {family=SF-TMP-009; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-TMP-009 {decided_by=TMP-009; family=SF-TMP-009; rule=automated adjudication stratum}
- source_record: TMP-009
- tested_by: EXP:TMP-009 {record=TMP-009; rule=family hypothesis tested by member record}
- text: The PULL_UP-specific decline with exposure is defensive adaptation rather than shooter selection/lineup artifact.
