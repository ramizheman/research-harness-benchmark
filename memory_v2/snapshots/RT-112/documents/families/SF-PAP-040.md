# FAM:SF-PAP-040 | Study family SF-PAP-040 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-040
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:small_sample {family=SF-PAP-040; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-PAP-040 | Finding of SF-PAP-040: supported
- confidence: 1.0
- derived_from: EXP:PAP-040 {family=SF-PAP-040; rule=family member}
- statement: H1 baseline 1.522; 1st-5th PPP 0.852 (vs H1 -0.670, n=3,295); 6th-10th 0.952 (-0.570, n=1,897); 11th+ 0.907 (-0.615, n=440)
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-PAP-040 | Hypothesis of SF-PAP-040
- addresses: RQC:RQC-160 {family=SF-PAP-040; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: PAP-040
- supported_by: FIND:SF-PAP-040 {decided_by=PAP-040; family=SF-PAP-040; rule=automated adjudication stratum}
- tested_by: EXP:PAP-040 {record=PAP-040; rule=family hypothesis tested by member record}
- text: The H1-H2 drop is concentrated in late/garbage second-half attempts.
