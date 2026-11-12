# FAM:SF-PAP-083 | Study family SF-PAP-083 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict failed_gate, powered null with power information
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-083
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:small_sample {family=SF-PAP-083; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: PLACEBO_DEPENDENCE
- risk_code: SAMPLE_SIZE_POWER
- validation_evidence: PAP-083: 'here t substitutes next; types from earlier dates only; 200 placebos pairing delta t with other-game delta o in the same period'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-083 | Finding of SF-PAP-083: rejected
- confidence: 1.0
- derived_from: EXP:PAP-083 {family=SF-PAP-083; rule=family member}
- rules_out: HYP:SF-PAP-083 {family=SF-PAP-083; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: three slope 0.011 SE 0.008 std=0.011 placebo p97.5=0.014 p=0.06; rim 0.024 SE 0.008 std=0.025 placebo p=0.005; tier benchmark 0.051 std=0.052
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-PAP-083 | Hypothesis of SF-PAP-083
- addresses: RQC:RQC-179 {family=SF-PAP-083; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-PAP-083 {decided_by=PAP-083; family=SF-PAP-083; rule=automated adjudication stratum}
- source_record: PAP-083
- tested_by: EXP:PAP-083 {record=PAP-083; rule=family hypothesis tested by member record}
- text: When T substitutes next, Delta T three-point rate tracks Delta O three-point rate at >=0.25 SD, above a clock-matched placebo.
