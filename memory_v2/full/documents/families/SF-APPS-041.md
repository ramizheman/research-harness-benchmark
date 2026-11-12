# FAM:SF-APPS-041 | Study family SF-APPS-041 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: mechanism C_artifact with verdict null
- confidence: 0.75
- confidence_level: high
- deciding_record: APPS-041
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:confounding {family=SF-APPS-041; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: CONFOUNDING
- validation_status: no_validation_recorded

# FIND:SF-APPS-041 | Finding of SF-APPS-041: artifact
- confidence: 0.75
- derived_from: EXP:APPS-041 {family=SF-APPS-041; rule=family member}
- rules_out: HYP:SF-APPS-041 {family=SF-APPS-041; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: TEAM ATT=-0.0038 CI[-0.025,+0.015] perm p=0.890 n_t=15614. STAR ATT=+0.0040 [-0.049,+0.052] p=0.834 n_t=2481. STAR Q4 ATT=-0.1045 [-0.217,+0.010] p=0.032 (gradient does not survive matching as a FINDING).
- status: artifact
- validation_status: no_validation_recorded

# HYP:SF-APPS-041 | Hypothesis of SF-APPS-041
- addresses: RQC:RQC-045 {family=SF-APPS-041; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-APPS-041 {decided_by=APPS-041; family=SF-APPS-041; rule=automated adjudication stratum}
- source_record: APPS-041
- tested_by: EXP:APPS-041 {record=APPS-041; rule=family hypothesis tested by member record}
- text: Conceding a PUTBACK causally suppresses the next offensive possession after matching on game state.
