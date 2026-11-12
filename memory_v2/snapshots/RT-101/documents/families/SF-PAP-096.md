# FAM:SF-PAP-096 | Study family SF-PAP-096 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-096
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- validation_status: no_validation_recorded

# FIND:SF-PAP-096 | Finding of SF-PAP-096: artifact
- confidence: 1.0
- derived_from: EXP:PAP-096 {family=SF-PAP-096; rule=family member}
- rules_out: HYP:SF-PAP-096 {family=SF-PAP-096; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: SPOT_UP 2.83 PPP (100% makes) and TRANSITION 0.62 PPP because assisted flag exists only on makes; after rewrite SPOT_UP ~1.16, TRANSITION ~1.20
- status: artifact
- validation_status: no_validation_recorded

# HYP:SF-PAP-096 | Hypothesis of SF-PAP-096
- addresses: RQC:RQC-130 {family=SF-PAP-096; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-PAP-096 {decided_by=PAP-096; family=SF-PAP-096; rule=automated adjudication stratum}
- source_record: PAP-096
- tested_by: EXP:PAP-096 {record=PAP-096; rule=family hypothesis tested by member record}
- text: Possession-level play types from PBP contain unbiased predictive structure.
