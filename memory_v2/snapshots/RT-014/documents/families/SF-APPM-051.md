# FAM:SF-APPM-051 | Study family SF-APPM-051 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 0.95
- confidence_level: high
- deciding_record: APPM-051
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-APPM-051; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPM-051 | Finding of SF-APPM-051: artifact
- confidence: 0.95
- derived_from: EXP:APPM-051 {family=SF-APPM-051; rule=family member}
- rules_out: HYP:SF-APPM-051 {family=SF-APPM-051; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: ORL underdog: CUT-push INFE P=36.7% -> OREB_PUSH +3.0pp P=35.0% (DeltaP -1.7pp); baseline P(overperform) 29.9%, best feasible +5.1pp to 35.0%. DET favorite: TOV_AVOID stays, P=76.8%. PHI: PUTBACK INFE 28.9% -> OREB_PUSH 28.5%. BOS: CUT INFE 80.3% -> OREB_PUSH 79.9%. OKC: CUT INFE 60.5% -> OREB_PUSH 60.1%. PHX/POR/SAS four_factor already FEAS, DeltaP +0.0pp. ORL 18/26 candidates INFEASIBLE; DET 18/38 INFEASIBLE.
- status: artifact
- validation_status: no_validation_recorded

# HYP:SF-APPM-051 | Hypothesis of SF-APPM-051
- addresses: RQC:RQC-020 {family=SF-APPM-051; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-APPM-051 {decided_by=APPM-051; family=SF-APPM-051; rule=automated adjudication stratum}
- source_record: APPM-051
- tested_by: EXP:APPM-051 {record=APPM-051; rule=family hypothesis tested by member record}
- text: Scoring candidates by P(overperform) over 95 possessions and dropping INFEASIBLE personnel pushes changes the rank-1 opener away from CUT for playoff G1s.
