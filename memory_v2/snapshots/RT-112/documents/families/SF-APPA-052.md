# FAM:SF-APPA-052 | Study family SF-APPA-052 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 1.0
- confidence_level: high
- deciding_record: APPA-052
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- risk_code: BASE_RATE
- validation_evidence: APPA-052: 'tale relative to n-gated +0.375 / best-vs-continue +0.445). robustness direction still holds on this csv. 2,544 rows; 272 game'
- validation_status: same_pipeline_validation

# FIND:SF-APPA-052 | Finding of SF-APPA-052: supported
- confidence: 1.0
- derived_from: EXP:APPA-052 {family=SF-APPA-052; rule=family member}
- statement: All games BEST 1.473 vs AVOID 0.853 gap +0.620 MW p=0.0000 Spearman -0.316 n=2,544. CUT<=15%: +0.625 n=2,508. CUT>15%: +0.163 n.s. n=36. Only 4/272 games had CUT>15%.
- status: supported
- validation_status: same_pipeline_validation

# HYP:SF-APPA-052 | Hypothesis of SF-APPA-052
- addresses: RQC:RQC-008 {family=SF-APPA-052; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPA-052
- supported_by: FIND:SF-APPA-052 {decided_by=APPA-052; family=SF-APPA-052; rule=automated adjudication stratum}
- tested_by: EXP:APPA-052 {record=APPA-052; rule=family hypothesis tested by member record}
- text: The BEST vs AVOID gap is inflated by games where CUT exceeds 15% of H2 mix.
