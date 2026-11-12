# FAM:SF-APPS-025 | Study family SF-APPS-025 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict inconclusive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-025
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: inconclusive
- risk_code: PLACEBO_DEPENDENCE
- risk_code: SAMPLE_SIZE_POWER
- validation_evidence: APPS-025: 'me-game opponent control, 0.10 h1-ppp caliper, game-cluster-robust se. caliper 0.10: a excess +0.076 [+0.068,+0.084] n=3421 p='
- validation_status: same_pipeline_validation

# FIND:SF-APPS-025 | Finding of SF-APPS-025: untestable
- confidence: 0.95
- derived_from: EXP:APPS-025 {family=SF-APPS-025; rule=family member}
- statement: Caliper 0.10: A excess +0.076 [+0.068,+0.084] n=3421 p=0; B excess +0.014 [-0.019,+0.046] n=255 p=0.386. Gap B-A = -0.062. Caliper sweep B CIs include 0 except 0.15.
- status: untestable
- validation_status: same_pipeline_validation

# HYP:SF-APPS-025 | Hypothesis of SF-APPS-025
- addresses: RQC:RQC-036 {family=SF-APPS-025; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPS-025 {decided_by=APPS-025; family=SF-APPS-025; rule=automated adjudication stratum}
- source_record: APPS-025
- tested_by: EXP:APPS-025 {record=APPS-025; rule=family hypothesis tested by member record}
- text: Teams that abandon a suppressed play type (h2_n<=1) show a smaller matched-pair overall six-PT H1->H2 excess decline than teams that continue (h2_n>=5).
