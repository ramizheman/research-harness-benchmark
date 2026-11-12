# FAM:SF-TMP-024 | Study family SF-TMP-024 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 0.95
- confidence_level: high
- deciding_record: TMP-024
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:implementation_bug {family=SF-TMP-024; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:low_measurement_reliability {family=SF-TMP-024; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- risk_code: IMPLEMENTATION_BUG
- risk_code: MEASURE_RELIABILITY
- validation_evidence: TMP-024: 'ions), 30 franchises, 2022-24 two-way possessions; odd/even split-half of d_a and gap; spearman of bench cosine similarity with -g'
- validation_status: same_pipeline_validation

# FIND:SF-TMP-024 | Finding of SF-TMP-024: artifact
- confidence: 0.95
- derived_from: EXP:TMP-024 {family=SF-TMP-024; rule=family member}
- rules_out: HYP:SF-TMP-024 {family=SF-TMP-024; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: Gap split-half rho=+0.591 (p=5.43e-127); D_A residualized rho=+0.489; hubs L_on>=0.05 (n=543) Gap rho=+0.599. Mechanism Spearman(agg_sim, -gap_sz)=-0.205 (p=1.13e-14), hubs -0.307. PPP payoff Spearman(-gap_sz, PPP_off-PPP_on)=-0.039 (p=0.144), hubs -0.054 (p=0.209). Balanced: Spearman(Lcos, DA_bal)=+0.345, DA_bal split-half +0.573, gap_bal +0.545. corr(D_A, co_sub_tv)=+0.312 (p=1.26e-32); partial corr(D_A, L_on | co_sub_tv, min_n, u)=+0.335.
- status: artifact
- validation_status: same_pipeline_validation

# HYP:SF-TMP-024 | Hypothesis of SF-TMP-024
- addresses: RQC:RQC-057 {family=SF-TMP-024; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-TMP-024 {decided_by=TMP-024; family=SF-TMP-024; rule=automated adjudication stratum}
- source_record: TMP-024
- tested_by: EXP:TMP-024 {record=TMP-024; rule=family hypothesis tested by member record}
- text: When a rotation player sits, Gap = D_A - L_on is a reliable Absorption vs Cascade trait, predicted by bench-profile redundancy, and Absorption preserves PPP.
