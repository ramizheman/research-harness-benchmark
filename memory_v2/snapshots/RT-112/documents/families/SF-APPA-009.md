# FAM:SF-APPA-009 | Study family SF-APPA-009 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inadequately tested: verdict null, mechanism C_artifact
- confidence: 0.8
- confidence_level: high
- deciding_record: APPA-009
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-APPA-009; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: not_supported
- validation_status: no_validation_recorded

# FIND:SF-APPA-009 | Finding of SF-APPA-009: uncertain
- confidence: 0.8
- derived_from: EXP:APPA-009 {family=SF-APPA-009; rule=family member}
- statement: Rolling beats or ties static in all 12 (e.g. bos_mia 0.835 vs 0.748; den_okc tie agents=rolling 0.859). Agents below rolling in 11/12. Agent Dir%/Mag% 0.0 and L1 scheme 0.000 in every series. Hypothesis precision 0/0 in 9 series, 0/1 (den_min_2324, ind_nyk_2425), 0/2 (lal_hou_2526).
- status: uncertain
- validation_status: no_validation_recorded

# HYP:SF-APPA-009 | Hypothesis of SF-APPA-009
- addresses: RQC:RQC-070 {family=SF-APPA-009; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-APPA-009 {decided_by=APPA-009; family=SF-APPA-009; rule=automated adjudication stratum}
- source_record: APPA-009
- tested_by: EXP:APPA-009 {record=APPA-009; rule=family hypothesis tested by member record}
- text: Adversarial LLM agents predict next-game play-type mix better than static and rolling baselines.
