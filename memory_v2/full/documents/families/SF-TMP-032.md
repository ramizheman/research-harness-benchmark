# FAM:SF-TMP-032 | Study family SF-TMP-032 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: TMP-032
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:label_or_classification_error {family=SF-TMP-032; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: LABEL_ERROR
- risk_code: PLACEBO_DEPENDENCE
- validation_evidence: TMP-032: 'games, before march 1)=0.690 is not worse than the 2023-24 placebo 0.667; high-load counts stay within 19-22 vs published 21.'
- validation_status: same_pipeline_validation

# FIND:SF-TMP-032 | Finding of SF-TMP-032: rejected
- confidence: 0.95
- derived_from: EXP:TMP-032 {family=SF-TMP-032; rule=family member}
- rules_out: HYP:SF-TMP-032 {family=SF-TMP-032; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: Label shares 2024-25: Oct inferrer 0.827 / Apr inferrer 0.016 untagged 0.798; Mar inferrer 0.499. Definitive 500-null run: 2023-24 n=414, rho(this run, published)=0.755, rho(all games, before March 1)=0.667 (L>=0.03 n=61: 0.772), high-load>=0.10: 16 full / 15 trunc / 16 published. 2024-25 n=439, rho(this run, published)=0.719, rho(all, trunc)=0.690 (L>=0.03 n=72: 0.819), high-load: 19 / 22 / 21. First run (different estimator): 2023-24 Spearman(full,trunc)=0.465 median |diff|=0.0070, 19 high-load flips; 2024-25 0.531 / 0.0084 / 20 flips; role-class print crashed (TypeError).
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-TMP-032 | Hypothesis of SF-TMP-032
- addresses: RQC:RQC-196 {family=SF-TMP-032; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-TMP-032 {decided_by=TMP-032; family=SF-TMP-032; rule=automated adjudication stratum}
- source_record: TMP-032
- tested_by: EXP:TMP-032 {record=TMP-032; rule=family hypothesis tested by member record}
- text: The March-April 2025 play-type labeling switch changes season-level Structural Influence L and role classes beyond the effect of merely dropping post-March games (2023-24 placebo).
