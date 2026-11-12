# FAM:SF-APPS-032 | Study family SF-APPS-032 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict reversed, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-032
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:label_or_classification_error {family=SF-APPS-032; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: LABEL_ERROR
- validation_status: no_validation_recorded

# FIND:SF-APPS-032 | Finding of SF-APPS-032: rejected
- confidence: 0.95
- derived_from: EXP:APPS-032 {family=SF-APPS-032; rule=family member}
- rules_out: HYP:SF-APPS-032 {family=SF-APPS-032; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: CUT PPP stable 1.60-1.71 for runs 1-5 (all n>=14); runs 6+ n=4/2/0. 62.0% of team-halves never crossed below SPOT_UP (n=405). Depletion-adjusted rho -0.0415 vs baseline -0.2737 (degraded 0.2322). DP -6.7 pts/100 vs static ? invalidated.
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-APPS-032 | Hypothesis of SF-APPS-032
- addresses: RQC:RQC-100 {family=SF-APPS-032; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPS-032 {decided_by=APPS-032; family=SF-APPS-032; rule=automated adjudication stratum}
- source_record: APPS-032
- tested_by: EXP:APPS-032 {record=APPS-032; rule=family hypothesis tested by member record}
- text: CUT PPP decays across successive H2 runs, so the playsheet should rotate off CUT to SPOT_UP.
