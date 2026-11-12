# FAM:SF-PAP-087 | Study family SF-PAP-087 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-087
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- validation_evidence: PAP-087: 'same loso/oof protocol; revert if brier not improved. examples: conf'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-087 | Finding of SF-PAP-087: rejected
- confidence: 1.0
- derived_from: EXP:PAP-087 {family=SF-PAP-087; rule=family member}
- rules_out: HYP:SF-PAP-087 {family=SF-PAP-087; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: examples: conf strength 0.19356 vs 0.19319; last5 0.19330 vs 0.19227; coach tenure meta 0.18146 vs 0.18063; tempo mismatch 0.18205 vs 0.18063; POM slope 0.18235 vs 0.18063; 3P rate not formally logged; FT 15v2 0.17547 vs 0.17545; recent-era seed 0.17608 vs 0.17536; monotonicity 0.17642 vs 0.17535
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-PAP-087 | Hypothesis of SF-PAP-087
- addresses: RQC:RQC-059 {family=SF-PAP-087; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-PAP-087 {decided_by=PAP-087; family=SF-PAP-087; rule=automated adjudication stratum}
- source_record: PAP-087
- tested_by: EXP:PAP-087 {record=PAP-087; rule=family hypothesis tested by member record}
- text: Conference strength, tourney appearances, last-5 win%, conf-tourney win%, avg margin, 3P rate, coach tenure, tempo mismatch, late mean net rating, def consistency, home-road gap, end streak, adj off eff, POM slope, FT-rate 15/2 nudge, upset-susceptibility profile, recent-era seed weights, 8/9 sharpening, seed-gap monotonicity add signal.
