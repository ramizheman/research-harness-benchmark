# FAM:SF-PAP-086 | Study family SF-PAP-086 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-086
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- validation_evidence: PAP-086: 'xgboost then meta-ensemble loso cv 2003-2025; keep if any brier drop. sos 0.19735->0.19319;'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-086 | Finding of SF-PAP-086: supported
- confidence: 1.0
- derived_from: EXP:PAP-086 {family=SF-PAP-086; rule=family member}
- statement: SOS 0.19735->0.19319; FT rate 0.19319->0.19227; neutral site 0.19227->0.19199; rank_variance 0.19199->0.19170; net_rating_volatility 0.18089->0.18077 (with adj 0.17993->0.17975); late_season_slope 0.18077->0.18063 (adj 0.17975->0.17962)
- status: supported
- validation_status: same_pipeline_validation

# HYP:SF-PAP-086 | Hypothesis of SF-PAP-086
- addresses: RQC:RQC-052 {family=SF-PAP-086; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: PAP-086
- supported_by: FIND:SF-PAP-086 {decided_by=PAP-086; family=SF-PAP-086; rule=automated adjudication stratum}
- tested_by: EXP:PAP-086 {record=PAP-086; rule=family hypothesis tested by member record}
- text: Added team-season features (SOS, FT rate, neutral-site ratio, rank variance, net-rating volatility, late-season slope) improve men's LOSO/OOF Brier.
