# FAM:SF-CHT-087 | Study family SF-CHT-087 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: mechanism C_artifact with verdict inconclusive
- confidence: 0.8
- confidence_level: high
- deciding_record: CHT-087
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:confounding {family=SF-CHT-087; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-CHT-087; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: inconclusive
- risk_code: CONFOUNDING
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-CHT-087 | Finding of SF-CHT-087: artifact
- confidence: 0.8
- derived_from: EXP:CHT-087 {family=SF-CHT-087; rule=family member}
- rules_out: HYP:SF-CHT-087 {family=SF-CHT-087; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: Current pool 428/428 pass n_decoys>=3. Chat reports a KW p=0.047 / n=92 role-class stratification and organizer-connector MW p=0.07 with bootstrap P(organizer>connector)=0.974 CI [-0.001, +0.180]. Menu-similarity confound: Pearson r(Delta, DeltaNR)=+0.12, Spearman +0.06 p=0.77, t p=0.16, bootstrap CI on mean gap [-1.47, +11.65] includes 0 — 'not a real effect once you correct the confound'.
- status: artifact
- validation_status: no_validation_recorded

# HYP:SF-CHT-087 | Hypothesis of SF-CHT-087
- addresses: RQC:RQC-149 {family=SF-CHT-087; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-CHT-087 {decided_by=CHT-087; family=SF-CHT-087; rule=automated adjudication stratum}
- source_record: CHT-087
- tested_by: EXP:CHT-087 {record=CHT-087; rule=family hypothesis tested by member record}
- text: Portability median Delta is robust to pairing rule among 428 movers with n_decoys>=3.
