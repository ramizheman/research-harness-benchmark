# FAM:SF-PAP-042 | Study family SF-PAP-042 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-042
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:small_sample {family=SF-PAP-042; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: SAMPLE_SIZE_POWER
- validation_evidence: PAP-042: '1,539 analyzed rs holdout triggers; compare suppressed pt vs best observed alternativ'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-042 | Finding of SF-PAP-042: rejected
- confidence: 1.0
- derived_from: EXP:PAP-042 {family=SF-PAP-042; rule=family member}
- rules_out: HYP:SF-PAP-042 {family=SF-PAP-042; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: 1,466/1,539 (95.3%) already had a better option; zero significant pivots (paper); CSV adapts=True on 334/1,539 rows under a looser flag
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-PAP-042 | Hypothesis of SF-PAP-042
- addresses: RQC:RQC-157 {family=SF-PAP-042; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-PAP-042 {decided_by=PAP-042; family=SF-PAP-042; rule=automated adjudication stratum}
- source_record: PAP-042
- tested_by: EXP:PAP-042 {record=PAP-042; rule=family hypothesis tested by member record}
- text: When a higher-scoring play type is already available in the same game, teams shift volume toward it.
