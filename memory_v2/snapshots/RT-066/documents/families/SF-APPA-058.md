# FAM:SF-APPA-058 | Study family SF-APPA-058 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 1.0
- confidence_level: high
- deciding_record: APPA-058
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:small_sample {family=SF-APPA-058; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPA-058 | Finding of SF-APPA-058: rejected
- confidence: 1.0
- derived_from: EXP:APPA-058 {family=SF-APPA-058; rule=family member}
- rules_out: HYP:SF-APPA-058 {family=SF-APPA-058; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: 2/30 (7%) stable (>=75% same top suppressor): D. Mitchell PUTBACK 75%, L. James POST_UP 75%. Negative: J. Tatum->K. Porzingis DRIVE->SPOT_UP -0.444 n=31; Giannis->Lillard DRIVE->PNR -0.263 n=31; J. Brown->J. Tatum SPOT_UP->DRIVE -0.186 n=37.
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-APPA-058 | Hypothesis of SF-APPA-058
- addresses: RQC:RQC-009 {family=SF-APPA-058; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPA-058 {decided_by=APPA-058; family=SF-APPA-058; rule=automated adjudication stratum}
- source_record: APPA-058
- tested_by: EXP:APPA-058 {record=APPA-058; rule=family hypothesis tested by member record}
- text: Each star's top sequential suppressor is stable across seasons, and some teammate X->Y sequences have large negative premiums.
