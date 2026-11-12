# FAM:SF-TMP-026 | Study family SF-TMP-026 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 0.95
- confidence_level: high
- deciding_record: TMP-026
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- validation_evidence: TMP-026: '2022-24. da_def vs matched-size random-split null; odd/even split-half; year-to-year same-team vs traded; ppp-allowed payoff. foll'
- validation_status: same_pipeline_validation

# FIND:SF-TMP-026 | Finding of SF-TMP-026: artifact
- confidence: 0.95
- derived_from: EXP:TMP-026 {family=SF-TMP-026; rule=family member}
- rules_out: HYP:SF-TMP-026 {family=SF-TMP-026; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: Gate/test3: mean DA_def 0.0712 vs null 0.0874 (paired t=-11.20), i.e. below null; size-adjusted split-half rho=-0.083 (p=0.00729); unbalanced 28-cell cosine mean=+0.4556 (t=+42.17); trade portability n=175 cosine +0.2401; Spearman(DA_def_r, dPPP_allowed)=-0.050 (p=0.1). structural_diag: self cosine +0.4491 vs random-other-team +0.1280, excess +0.3211; mover self-sim +0.2432 vs decoy +0.1193, excess +0.1239, 62.3%>0, binom p=0.001. def_sig_check: BALANCED odd-even self-cosine mean=+0.0371 vs unbalanced +0.4516; share_on-matched different-team cosine unbalanced +0.4583, balanced +0.0298; balanced mover portability mean=+0.0340.
- status: artifact
- validation_status: same_pipeline_validation

# HYP:SF-TMP-026 | Hypothesis of SF-TMP-026
- addresses: RQC:RQC-178 {family=SF-TMP-026; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-TMP-026 {decided_by=TMP-026; family=SF-TMP-026; rule=automated adjudication stratum}
- source_record: TMP-026
- tested_by: EXP:TMP-026 {record=TMP-026; rule=family hypothesis tested by member record}
- text: A defender on the floor reliably rewires the opposing offense (DA_def above a random-split null; odd/even 28-cell signature cosine and trade portability exceed decoys).
