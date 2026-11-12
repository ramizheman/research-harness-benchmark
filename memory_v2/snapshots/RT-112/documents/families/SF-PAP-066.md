# FAM:SF-PAP-066 | Study family SF-PAP-066 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-066
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- risk_code: LEAKAGE_LOOKAHEAD
- validation_status: no_validation_recorded

# FIND:SF-PAP-066 | Finding of SF-PAP-066: supported
- confidence: 1.0
- derived_from: EXP:PAP-066 {family=SF-PAP-066; rule=family member}
- statement: Spearman(init_share, D_real)=+0.029 CI[-0.108,+0.178] p=0.73; partial(L_pre, D_real | init_share, n_spell, n_pre)=+0.369 CI[+0.209,+0.494] p=0.0005; partial(init_share | L_pre,...)=-0.116 p=0.19; Spearman(init_share, L_pre)=+0.332
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-PAP-066 | Hypothesis of SF-PAP-066
- addresses: RQC:RQC-061 {family=SF-PAP-066; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: PAP-066
- supported_by: FIND:SF-PAP-066 {decided_by=PAP-066; family=SF-PAP-066; rule=automated adjudication stratum}
- tested_by: EXP:PAP-066 {record=PAP-066; rule=family hypothesis tested by member record}
- text: L_pre predicts D_real after controlling initiation share; initiation share does not after controlling L_pre.
