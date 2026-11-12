# Scope-annotation sources (family records from the task snapshots; no answer-key content)

## SF-APPA-005 (gold in RT-012; record identical across these snapshots: True)

Snapshot RT-012; member records: APPA-005
- _label: Study family SF-APPA-005: Defensive scheme change within game and across games (inferred labels)
- auto_adjudication_basis: R0 single record; automated rule-based adjudication, not human adjudication
- auto_confidence: high (0.95)
- auto_failure_mechanism: A_unanswerable (question not answerable with the data or design)
- auto_knowable_before_outcome: yes_from_history_probable
- auto_members_disagree: no
- auto_outcome_status: untestable
- auto_validation_status: no_validation_recorded; evidence: NOT_RECORDED
- observed_dates: APPA-005: 2026-05-23 (mtime)
- observed_failure_evidence: Doc caveat: inferred label cannot separate real defensive adjustment from offense executing differently; near-uniform transition matrices consistent with label noise.
- observed_failure_type: A_unanswerable
- observed_hypothesis: Playoff defenses change scheme within games and between games, especially after the opponent ran a play type heavily.
- observed_method: A1 vote-rule scheme inference from opponent PT PPP; 523 comparable within-game cells; 440 consecutive game pairs; heavy-PT conditioning (>=5pp).
- observed_notes: Reverse-inferred labels from PPP outcomes; late-third votes use min_n_per_pt=2.
- observed_project: Team Adaptation
- observed_research_question: Defensive scheme change within game and across games (inferred labels)
- observed_result: Within-game change 319/523 (61.0%); cross-game change 298/440 (67.7%); 103/104 units (99.0%) and 52/52 series show a change; transition matrices near-uniform.
- observed_sample_and_power: 523 cells; 440 pairs
- observed_sources: APPA-005: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\DEFENSIVE_ADAPTATION_findings.md
- observed_verdict: inconclusive
- edges: auto_addresses_question RQC:RQC-030; auto_has_risk RISK:LABEL_ERROR; auto_limited_by LIM:label_or_classification_error; auto_measures VAR:PPP_points_per_possession; auto_uses_dataset DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions; auto_uses_dataset DS:Playoff_series_outcomes

## SF-APPA-030 (gold in RT-012; record identical across these snapshots: True)

Snapshot RT-012; member records: APPA-030
- _label: Study family SF-APPA-030: Play-type label backfill verification
- auto_adjudication_basis: R0 single record; automated rule-based adjudication, not human adjudication
- auto_confidence: high (0.8)
- auto_failure_mechanism: C_artifact (apparent effect produced by a construction, selection or labelling flaw)
- auto_knowable_before_outcome: yes_from_history
- auto_members_disagree: no
- auto_outcome_status: inconclusive
- auto_validation_status: no_validation_recorded; evidence: NOT_RECORDED
- observed_dates: APPA-030: 2026-05-24 (doc)
- observed_failure_evidence: 2024-25 PULL_UP shares 0.0-2.0% for many teams; 82.8% of PNR labels proxy_calibrated.
- observed_failure_type: C_artifact
- observed_hypothesis: Backfilled play-type labels match expected league distributions and team identities.
- observed_method: 921,514 labelled possessions; band tests on PT shares, PNR cap, PPP sanity, temporal distribution, team identity and directional checks.
- observed_notes: Report says do not run adaptation analysis until resolved.
- observed_project: Strategy app
- observed_research_question: Play-type label backfill verification
- observed_result: PNR 28.7% FAIL (band 20-28%); PULL_UP 7.9% FAIL; 3100 games with team PNR >33% FAIL; PNR PPP 0.948 PASS; temporal PASS; team identity FAIL; 2024-25 PULL_UP ~0-1% for many teams. Final: FAIL.
- observed_sample_and_power: 921,514 possessions
- observed_sources: APPA-030: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\BACKFILL_VERIFICATION.md
- observed_verdict: failed_gate
- edges: auto_addresses_question RQC:RQC-013; auto_has_risk RISK:LABEL_ERROR; auto_limited_by LIM:label_or_classification_error; auto_measures VAR:PPP_points_per_possession; auto_measures VAR:play_type_share_mix; auto_uses_dataset DS:NBA_play_by_play_possessions_and_reconstructed_lineups; auto_uses_dataset DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions; auto_uses_method METH:matched_control

## SF-APPS-003 (gold in RT-014; record identical across these snapshots: True)

Snapshot RT-014; member records: APPS-003
- _label: Study family SF-APPS-003: SQ2 decision quality hit rate: engine top pt_shift vs team modal PT
- auto_adjudication_basis: R0 single record; automated rule-based adjudication, not human adjudication
- auto_confidence: high (0.95)
- auto_failure_mechanism: C_artifact (apparent effect produced by a construction, selection or labelling flaw)
- auto_knowable_before_outcome: no_evidence
- auto_members_disagree: no
- auto_outcome_status: artifact
- auto_validation_status: same_pipeline_validation; evidence: APPS-003: 'the drive ban and cut ppp level were known before scoring. holdout protocol (tuning 17 series, holdout 25, sha 59a9be48) was w'
- observed_dates: APPS-003: 2026-05-23 (mtime)
- observed_failure_evidence: Headline 'structurally inflated': 14 of 53 pairs compare against banned DRIVE; 13 of 37 hits from CUT recs with structurally high PPP; in-sample, same series used to discover DRIVE failure and tune exclusion.
- observed_failure_type: C_artifact
- observed_hypothesis: The V4 engine's recommended play type outperforms the team's highest-volume play type in that playoff series.
- observed_method: (team, series) pairs across 42 correction_log series (84 rows, 53 scoreable in full-calibrated run); HIT if rec PT PPP > modal PT PPP, both n>=15.
- observed_notes: Knowable: the DRIVE ban and CUT PPP level were known before scoring. Holdout protocol (tuning 17 series, holdout 25, SHA 59a9be48) was written but no holdout result was found in files read.
- observed_project: Strategy app
- observed_research_question: SQ2 decision quality hit rate: engine top pt_shift vs team modal PT
- observed_result: Full-calibrated headline 69.8% (37/53); DRIVE-modal (banned-PT) comparisons 85.7% (12/14); clean comparisons 64.1% (25/39); high-confidence 64.3% (27/42). CUT recs 13/13; POST_UP 0/4. Uncalibrated archival: 51.7% (31/60), high-conf 42.9%, DRIVE recs 8% (n=25).
- observed_sample_and_power: n=53 scoreable; no bootstrap CI computed
- observed_sources: ['APPS-003: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\data\\decision_quality_findings.md', 'APPS-003: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\validation\\README.md', 'APPS-003: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\validation\\proof\\decision_quality_test.py']
- observed_verdict: artifact_found
- edges: auto_addresses_question RQC:RQC-022; auto_has_risk RISK:LEAKAGE_LOOKAHEAD; auto_has_risk RISK:SAMPLE_SIZE_POWER; auto_limited_by LIM:small_sample; auto_measures VAR:PPP_points_per_possession; auto_uses_dataset DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions; auto_uses_dataset DS:Playoff_series_outcomes; auto_uses_method METH:calibration_scoring

## SF-APPS-009 (gold in RT-066; record identical across these snapshots: True)

Snapshot RT-066; member records: APPS-009
- _label: Study family SF-APPS-009: Player routing V4 vs V5 direct scoring
- auto_adjudication_basis: R0 single record; automated rule-based adjudication, not human adjudication
- auto_confidence: high (0.95)
- auto_failure_mechanism: A_unanswerable (question not answerable with the data or design)
- auto_knowable_before_outcome: yes_from_data
- auto_members_disagree: no
- auto_outcome_status: untestable
- auto_validation_status: no_validation_recorded; evidence: NOT_RECORDED
- observed_dates: APPS-009: 2026-05-05 (mtime)
- observed_failure_evidence: Scoreable 0 of 8; V5 mostly routed to 'team' rather than a player.
- observed_failure_type: A_unanswerable
- observed_hypothesis: V5 player routing picks players with higher observed PPP than V4 routing.
- observed_method: Series where V4 and V5 routed to different players; compare observed PPP (n>=5 each).
- observed_notes: Data coverage could be checked before running.
- observed_project: Strategy app
- observed_research_question: Player routing V4 vs V5 direct scoring
- observed_result: 8 divergences, 0 scoreable, 8 unscored (player missing from Neo4j); hit rate n/a.
- observed_sample_and_power: n=8 divergences, 0 scoreable
- observed_sources: APPS-009: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\player_routing_results.md
- observed_verdict: inconclusive
- edges: auto_addresses_question RQC:RQC-017; auto_has_risk RISK:DRIFT_NONSTATIONARITY; auto_has_risk RISK:SAMPLE_SIZE_POWER; auto_limited_by LIM:small_sample; auto_measures VAR:PPP_points_per_possession; auto_uses_dataset DS:Playoff_series_outcomes

## SF-APPS-018 (gold in RT-014, RT-179; record identical across these snapshots: True)

Snapshot RT-014; member records: APPS-018
- _label: Study family SF-APPS-018: Ranked playsheet validation, 10 series (Spearman null; pairwise BEST>AVOID)
- auto_adjudication_basis: R0 single record; automated rule-based adjudication, not human adjudication
- auto_confidence: medium (0.65)
- auto_failure_mechanism: E_unclear (mechanism unclear from the records)
- auto_knowable_before_outcome: no_evidence
- auto_members_disagree: no
- auto_outcome_status: inconclusive
- auto_validation_status: no_validation_recorded; evidence: NOT_RECORDED
- observed_dates: APPS-018: 2026-05-25 (mtime)
- observed_failure_evidence: Full-tier Spearman not significant (rho=-0.0639, p=0.099717) while pairwise BEST vs AVOID is; average counter n=6.9 possessions.
- observed_failure_type: E_unclear
- observed_hypothesis: When a defense drops a play type >=0.25 PPP H1 to H2, playsheet counter ranking predicts which alternative scored better in H2 (BEST > SECOND > AVOID).
- observed_method: 10 completed 2025-26 playoff series; 665 counter observations / 142 unique triggers; Spearman of tier rank vs observed H2 PPP plus Kruskal-Wallis and Mann-Whitney BEST vs AVOID.
- observed_notes: Honest assessment: ranking noisy in full Spearman; pairwise BEST vs AVOID confirmed. Pipeline season_cap_yy=26 may leak R1 into R2 series.
- observed_project: Strategy app
- observed_research_question: Ranked playsheet validation, 10 series (Spearman null; pairwise BEST>AVOID)
- observed_result: Spearman rho=-0.0639, p=0.099717, n=665 (no clear full-rank signal). Kruskal-Wallis H=32.9723, p=2.7e-05. Mann-Whitney BEST 1.257 (n=56) vs AVOID 1.092 (n=160), U=5546.0, p=0.004018. Trigger accuracy rho=0.4525, n=121. Follow rate vs H2 PPP rho=-0.0664, p=0.5486, n=84.
- observed_sample_and_power: 665 counter obs, 142 unique triggers; avg counter n=6.9
- observed_sources: ['APPS-018: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\playsheet_validation\\_validation_run.log', 'APPS-018: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\playsheet_validation\\validation_report.md']
- observed_verdict: inconclusive
- edges: auto_addresses_question RQC:RQC-001; auto_has_risk RISK:DRIFT_NONSTATIONARITY; auto_has_risk RISK:LEAKAGE_LOOKAHEAD; auto_has_risk RISK:MEASURE_RELIABILITY; auto_has_risk RISK:SAMPLE_SIZE_POWER; auto_limited_by LIM:leakage; auto_limited_by LIM:low_measurement_reliability; auto_limited_by LIM:small_sample; auto_measures VAR:PPP_points_per_possession; auto_uses_dataset DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions; auto_uses_dataset DS:Playoff_series_outcomes; auto_uses_method METH:correlation

## SF-APPS-024 (gold in RT-183; record identical across these snapshots: True)

Snapshot RT-183; member records: APPS-024
- _label: Study family SF-APPS-024: DRIVE-as-BEST counter vs constrained mix
- auto_adjudication_basis: R0 single record; automated rule-based adjudication, not human adjudication
- auto_confidence: high (0.95)
- auto_failure_mechanism: A_unanswerable (question not answerable with the data or design)
- auto_knowable_before_outcome: no_evidence
- auto_members_disagree: no
- auto_outcome_status: untestable
- auto_validation_status: no_validation_recorded; evidence: NOT_RECORDED
- observed_dates: APPS-024: 2026-05-30 (mtime)
- observed_failure_evidence: Observed gap -0.066 is below MDE 0.180; n=44 cannot distinguish a true null from an effect up to 0.18 PPP.
- observed_failure_type: A_unanswerable
- observed_hypothesis: When BEST=DRIVE (counter_h2_n>=5), observed DRIVE H2 PPP beats a feasibility-constrained baseline.
- observed_method: 44 qualifying triggers, 39 games, 13 teams. Mix weights CUT 15%/SPOT_UP 35%/DRIVE 30%/OTHER 20%. One-sided MW A>B and A>C.
- observed_notes: A is left-skewed (median 1.279 > B_fixed) so MW p=0.2175 for A>B is consistent with a negative mean gap.
- observed_project: Strategy app
- observed_research_question: DRIVE-as-BEST counter vs constrained mix
- observed_result: A mean=1.178 vs B_game 1.236 (gap=-0.058, p=0.6069) vs B_fixed 1.244 (gap=-0.066, p=0.2175) vs coach default C 1.134 (gap=+0.043, p=0.3052). MDE at 80% power ~0.180 PPP (SD~0.34).
- observed_sample_and_power: n=44; MDE 0.180 PPP at 80% power (SD~0.34); 0.265 if SD~0.5
- observed_sources: APPS-024: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\drive_counter_test.md
- observed_verdict: inconclusive
- edges: auto_addresses_question RQC:RQC-007; auto_has_risk RISK:SAMPLE_SIZE_POWER; auto_limited_by LIM:low_power_large_MDE; auto_limited_by LIM:small_sample; auto_measures VAR:PPP_points_per_possession; auto_measures VAR:play_type_share_mix; auto_uses_dataset DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions

## SF-APPS-058 (gold in RT-012; record identical across these snapshots: True)

Snapshot RT-012; member records: APPS-058
- _label: Study family SF-APPS-058: Observed on-ball defensive scheme labels (ORL-DET G1)
- auto_adjudication_basis: R0 single record; automated rule-based adjudication, not human adjudication
- auto_confidence: high (0.95)
- auto_failure_mechanism: A_unanswerable (question not answerable with the data or design)
- auto_knowable_before_outcome: yes_from_data
- auto_members_disagree: no
- auto_outcome_status: untestable
- auto_validation_status: no_validation_recorded; evidence: NOT_RECORDED
- observed_dates: APPS-058: 2026-04-20 (mtime)
- observed_failure_evidence: Confident label rates 14.9% and 3.3%; NBA matchups feed did not populate switches_on.
- observed_failure_type: A_unanswerable
- observed_hypothesis: NBA matchup/PBP fields can label on-ball coverage (DROP/ICE/SWITCH) at usable rates.
- observed_method: Single game 0042500101. Confident labels vs OTHER.
- observed_notes: ICE_CANDIDATE is unconfirmed without screen-contact tracking.
- observed_project: Strategy app
- observed_research_question: Observed on-ball defensive scheme labels (ORL-DET G1)
- observed_result: DET: 67 on-ball HC poss, 10 labeled (14.9%) ? DROP n=5 PPP=1.20, ICE_CANDIDATE n=5 PPP=0.80, OTHER n=57 PPP=1.42. ORL: 60 poss, 2 labeled (3.3%). switches_on unpopulated.
- observed_sample_and_power: n=67/60 possessions, 10/2 labeled
- observed_sources: APPS-058: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\observed_defense_0042500101.md
- observed_verdict: failed_gate
- edges: auto_addresses_question RQC:RQC-079; auto_has_risk RISK:LABEL_ERROR; auto_has_risk RISK:SAMPLE_SIZE_POWER; auto_limited_by LIM:label_or_classification_error; auto_limited_by LIM:small_sample; auto_measures VAR:PPP_points_per_possession; auto_uses_dataset DS:NBA_play_by_play_possessions_and_reconstructed_lineups; auto_uses_method METH:matched_control

## SF-APPS-068 (gold in RT-014, RT-179; record identical across these snapshots: False)

Snapshot RT-014; member records: APPS-068
- _label: Study family SF-APPS-068: Possession Control Index incremental R2 over ORtg (PCI is DRtg proxy)
- auto_adjudication_basis: R0 single record; automated rule-based adjudication, not human adjudication
- auto_confidence: high (0.95)
- auto_failure_mechanism: C_artifact (apparent effect produced by a construction, selection or labelling flaw)
- auto_knowable_before_outcome: no_evidence
- auto_members_disagree: no
- auto_outcome_status: artifact
- auto_validation_status: same_pipeline_validation; evidence: APPS-068: '120 team-seasons. models a baseline / b pci-only / c full. oos test 2025-26. diagnostic net~ortg+leakage vs +offcontrol. a'
- observed_dates: APPS-068: 2026-06-15 (mtime)
- observed_failure_evidence: Headline PCI gain is leakage tracking DRtg (+0.89); offensive-control dR2=+0.005. Baseline omitted defense by construction (Net=ORtg-DRtg).
- observed_failure_type: C_artifact
- observed_hypothesis: PCI (halfcourt PPP + second-chance - TO - transition leakage) explains Net Rating beyond ORtg, Pace, and FGA/poss.
- observed_method: 120 team-seasons. Models A baseline / B PCI-only / C full. OOS test 2025-26. Diagnostic Net~ORtg+leakage vs +offcontrol.
- observed_notes: Knowable: Net Rating already contains DRtg, so adding a leakage term that correlates 0.89 with DRtg must lift R2.
- observed_project: Strategy app
- observed_research_question: Possession Control Index incremental R2 over ORtg (PCI is DRtg proxy)
- observed_result: A R2=0.763 OOS 0.761; C R2=0.902 OOS 0.919; dR2=+0.139. Offensive-control components add +0.005 R2 beyond ORtg. Net~ORtg+leakage R2=0.948. corr(leakage, DRtg)=+0.894. PCI univariate r=+0.863 vs ORtg +0.866.
- observed_sample_and_power: n=120 team-seasons; OOS 2025-26 30 teams
- observed_sources: ['APPS-068: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\sequence_memory\\output\\pci_feature_importance_summary.md', 'APPS-068: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\sequence_memory\\pci_validation.py']
- observed_verdict: artifact_found
- edges: auto_addresses_question RQC:RQC-089; auto_has_risk RISK:LEAKAGE_LOOKAHEAD; auto_has_risk RISK:MECHANICAL_FLOOR; auto_limited_by LIM:leakage; auto_measures VAR:PPP_points_per_possession; auto_measures VAR:net_rating_ORtg; auto_uses_dataset DS:Box_score_and_traditional_stats; auto_uses_dataset DS:NBA_play_by_play_possessions_and_reconstructed_lineups; auto_uses_dataset DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions; auto_uses_dataset DS:Shot_level_data_with_expected_FG; auto_uses_method METH:correlation; auto_uses_method METH:holdout_backtest_or_replay; auto_uses_method METH:regression

Snapshot RT-179; member records: APPS-068
- _label: Study family SF-APPS-068: Possession Control Index incremental R2 over ORtg (PCI is DRtg proxy)
- auto_adjudication_basis: R0 single record; automated rule-based adjudication, not human adjudication
- auto_confidence: high (0.95)
- auto_failure_mechanism: C_artifact (apparent effect produced by a construction, selection or labelling flaw)
- auto_knowable_before_outcome: no_evidence
- auto_members_disagree: no
- auto_outcome_status: artifact
- auto_validation_status: same_pipeline_validation; evidence: APPS-068: '120 team-seasons. models a baseline / b pci-only / c full. oos test 2025-26. diagnostic net~ortg+leakage vs +offcontrol. a'
- observed_dates: APPS-068: 2026-06-15 (mtime)
- observed_failure_evidence: Headline PCI gain is leakage tracking DRtg (+0.89); offensive-control dR2=+0.005. Baseline omitted defense by construction (Net=ORtg-DRtg).
- observed_failure_type: C_artifact
- observed_hypothesis: PCI (halfcourt PPP + second-chance - TO - transition leakage) explains Net Rating beyond ORtg, Pace, and FGA/poss.
- observed_method: 120 team-seasons. Models A baseline / B PCI-only / C full. OOS test 2025-26. Diagnostic Net~ORtg+leakage vs +offcontrol.
- observed_notes: Knowable: Net Rating already contains DRtg, so adding a leakage term that correlates 0.89 with DRtg must lift R2.
- observed_project: Strategy app
- observed_research_question: Possession Control Index incremental R2 over ORtg (PCI is DRtg proxy)
- observed_result: A R2=0.763 OOS 0.761; C R2=0.902 OOS 0.919; dR2=+0.139. Offensive-control components add +0.005 R2 beyond ORtg. Net~ORtg+leakage R2=0.948. corr(leakage, DRtg)=+0.894. PCI univariate r=+0.863 vs ORtg +0.866.
- observed_sample_and_power: n=120 team-seasons; OOS 2025-26 30 teams
- observed_sources: ['APPS-068: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\sequence_memory\\output\\pci_feature_importance_summary.md', 'APPS-068: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\sequence_memory\\pci_validation.py']
- observed_verdict: artifact_found
- edges: auto_addresses_question RQC:RQC-112; auto_has_risk RISK:LEAKAGE_LOOKAHEAD; auto_has_risk RISK:MECHANICAL_FLOOR; auto_limited_by LIM:leakage; auto_measures VAR:PPP_points_per_possession; auto_measures VAR:net_rating_ORtg; auto_uses_dataset DS:Box_score_and_traditional_stats; auto_uses_dataset DS:NBA_play_by_play_possessions_and_reconstructed_lineups; auto_uses_dataset DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions; auto_uses_dataset DS:Shot_level_data_with_expected_FG; auto_uses_method METH:correlation; auto_uses_method METH:holdout_backtest_or_replay; auto_uses_method METH:regression

## SF-APPS-085 (gold in RT-179; record identical across these snapshots: True)

Snapshot RT-179; member records: APPS-085
- _label: Study family SF-APPS-085: Connector teammate-path quality Q_p split-half reliability
- auto_adjudication_basis: R0 single record; automated rule-based adjudication, not human adjudication
- auto_confidence: high (0.95)
- auto_failure_mechanism: A_unanswerable (question not answerable with the data or design)
- auto_knowable_before_outcome: yes_from_data
- auto_members_disagree: no
- auto_outcome_status: untestable
- auto_validation_status: same_pipeline_validation; evidence: APPS-085: 'fect (true r<=0.25 could still be missed). n=102 connectors split-half r=0.215 / sb 0.355 is too low to treat q_p as a stable scou'
- observed_dates: APPS-085: 2026-07-26 (mtime)
- observed_failure_evidence: Split-half r=0.215 / SB 0.355 is too low to treat Q_p as a stable scoutable trait; most variance is within-player half-to-half.
- observed_failure_type: A_unanswerable
- observed_hypothesis: Connector quality Q_p (teammate-initiated on-off PPP gap) is a stable player-season attribute.
- observed_method: Odd/even game_id split; n=102 connectors with both halves; on&off >=80 poss/half, teammate-init on >=50. Spearman-Brown; ANOVA ICC.
- observed_notes: L(p)/shape nulls are not just attenuation of a large true effect (true r<=0.25 could still be missed).
- observed_project: When a Hub Sits (Paper 2)
- observed_research_question: Connector teammate-path quality Q_p split-half reliability
- observed_result: Pearson r(Q_a,Q_b)=+0.215 p=0.0297; Spearman rho=+0.242. Spearman-Brown Q~0.355, S~0.278. Sign agreement 65.7% (67/102) binomial p=0.000996. ICC(player-season)=0.216 (78.4% within). Attenuation: even a perfect predictor max |r| with Q_p ~0.595; true r=0.30 attenuates to 0.179 (often undetectable).
- observed_sample_and_power: n=102 connectors
- observed_sources: ['APPS-085: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\paper2_output\\connector_qp_reliability_report.md', 'APPS-085: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\paper2_output\\connector_qp_variance_audit_report.md']
- observed_verdict: failed_gate
- edges: auto_addresses_question RQC:RQC-045; auto_has_risk RISK:MEASURE_RELIABILITY; auto_limited_by LIM:low_measurement_reliability; auto_measures VAR:PPP_points_per_possession; auto_uses_dataset DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions; auto_uses_method METH:correlation; auto_uses_method METH:split_half_reliability

## SF-APPS-090 (gold in RT-183; record identical across these snapshots: True)

Snapshot RT-183; member records: APPS-090
- _label: Study family SF-APPS-090: Connector diet x destination structural-gap match
- auto_adjudication_basis: R0 single record; automated rule-based adjudication, not human adjudication
- auto_confidence: high (0.95)
- auto_failure_mechanism: A_unanswerable (question not answerable with the data or design)
- auto_knowable_before_outcome: no_evidence
- auto_members_disagree: no
- auto_outcome_status: untestable
- auto_validation_status: no_validation_recorded; evidence: NOT_RECORDED
- observed_dates: APPS-090: 2026-07-27 (mtime)
- observed_failure_evidence: Connector subsets n=19/40; all-movers binary delta p=0.0283 does not replicate as a continuous Spearman and is not the licensed connector test.
- observed_failure_type: A_unanswerable
- observed_hypothesis: Diet-matching to a destination's thin initiation jobs predicts better post-move outcomes than mismatch.
- observed_method: 198 movers with complete diet+gap; taxonomy CONNECTOR n=19; travel-check n=40. match_score=cosine(diet, gap). Primary outcomes portability delta / embedded / d_mpg / d_hhi_top, not PPP.
- observed_notes: Knowable: 15.7% match rate leaves n_match=5 in the taxonomy CONNECTOR cell.
- observed_project: When a Hub Sits (Paper 2)
- observed_research_question: Connector diet x destination structural-gap match
- observed_result: Binary match rate 15.7%. Taxonomy CONNECTOR delta match vs mis med +0.540 vs +0.069 p=0.156 n=5/14. Travel-check delta p=0.413. All-movers delta p=0.0283 (med +0.160 vs +0.053) but Spearman(match_score, delta)=-0.034 p=0.631 n=198. Connector-only Spearmans all ns.
- observed_sample_and_power: n=19 taxonomy connectors; n=198 all movers
- observed_sources: APPS-090: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\connector_diet_gap_match_report.md
- observed_verdict: null
- edges: auto_addresses_question RQC:RQC-046; auto_has_risk RISK:SAMPLE_SIZE_POWER; auto_limited_by LIM:small_sample; auto_measures VAR:PPP_points_per_possession; auto_measures VAR:win_probability_series_outcome; auto_uses_dataset DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions; auto_uses_method METH:correlation; auto_uses_method METH:matched_control

## SF-CHT-025 (gold in RT-012, RT-147; record identical across these snapshots: False)

Snapshot RT-012; member records: CHT-025
- _label: Study family SF-CHT-025: Play-type labeling audit: OTHER/DRIVE foul leakage
- auto_adjudication_basis: R0 single record; automated rule-based adjudication, not human adjudication
- auto_confidence: high (1.0)
- auto_failure_mechanism: C_artifact (apparent effect produced by a construction, selection or labelling flaw)
- auto_knowable_before_outcome: no_evidence
- auto_members_disagree: no
- auto_outcome_status: artifact
- auto_validation_status: no_validation_recorded; evidence: NOT_RECORDED
- observed_dates: CHT-025: 2026-05-24 (transcript)
- observed_failure_evidence: OTHER PPP inflated by 36% foul endings; DRIVE 12pp below foul benchmark; initiation_type maps 0.7%.
- observed_failure_type: C_artifact
- observed_hypothesis: Play-type PPP differences are real efficiency, not labeling/foul artifacts.
- observed_method: Per-PT diagnostic of foul-ending share vs PPP; initiation_type mapping.
- observed_notes: Results discussed in chat; a findings/diagnostic markdown is implied but path not fully quoted.
- observed_project: Strategy app
- observed_research_question: Play-type labeling audit: OTHER/DRIVE foul leakage
- observed_result: OTHER: 36% end in fouls, PPP inflated (FOUL_BUCKET). DRIVE: 12pp below foul benchmark (FOUL_LEAK). PNR shows 22% foul rate. Only 335 of 50,668 possessions (0.7%) map to a real play type via initiation_type.
- observed_sample_and_power: 50,668 possessions in the initiation_type check
- observed_sources: CHT-025: d2a94a1e-b21a-4a3a-b2cf-3eb526e3f49a
- observed_verdict: artifact_found
- edges: auto_addresses_question RQC:RQC-087; auto_measures VAR:PPP_points_per_possession; auto_measures VAR:free_throws_fouls; auto_measures VAR:play_type_share_mix; auto_uses_dataset DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions

Snapshot RT-147; member records: CHT-025
- _label: Study family SF-CHT-025: Play-type labeling audit: OTHER/DRIVE foul leakage
- auto_adjudication_basis: R0 single record; automated rule-based adjudication, not human adjudication
- auto_confidence: high (1.0)
- auto_failure_mechanism: C_artifact (apparent effect produced by a construction, selection or labelling flaw)
- auto_knowable_before_outcome: no_evidence
- auto_members_disagree: no
- auto_outcome_status: artifact
- auto_validation_status: no_validation_recorded; evidence: NOT_RECORDED
- observed_dates: CHT-025: 2026-05-24 (transcript)
- observed_failure_evidence: OTHER PPP inflated by 36% foul endings; DRIVE 12pp below foul benchmark; initiation_type maps 0.7%.
- observed_failure_type: C_artifact
- observed_hypothesis: Play-type PPP differences are real efficiency, not labeling/foul artifacts.
- observed_method: Per-PT diagnostic of foul-ending share vs PPP; initiation_type mapping.
- observed_notes: Results discussed in chat; a findings/diagnostic markdown is implied but path not fully quoted.
- observed_project: Strategy app
- observed_research_question: Play-type labeling audit: OTHER/DRIVE foul leakage
- observed_result: OTHER: 36% end in fouls, PPP inflated (FOUL_BUCKET). DRIVE: 12pp below foul benchmark (FOUL_LEAK). PNR shows 22% foul rate. Only 335 of 50,668 possessions (0.7%) map to a real play type via initiation_type.
- observed_sample_and_power: 50,668 possessions in the initiation_type check
- observed_sources: CHT-025: d2a94a1e-b21a-4a3a-b2cf-3eb526e3f49a
- observed_verdict: artifact_found
- edges: auto_addresses_question RQC:RQC-035; auto_measures VAR:PPP_points_per_possession; auto_measures VAR:free_throws_fouls; auto_measures VAR:play_type_share_mix; auto_uses_dataset DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions

## SF-CHT-057 (gold in RT-183; record identical across these snapshots: True)

Snapshot RT-183; member records: CHT-057
- _label: Study family SF-CHT-057: Cut- vs drive-based connector portability
- auto_adjudication_basis: R0 single record; automated rule-based adjudication, not human adjudication
- auto_confidence: high (1.0)
- auto_failure_mechanism: D_positive (no failure: positive result)
- auto_knowable_before_outcome: not_applicable
- auto_members_disagree: no
- auto_outcome_status: supported
- auto_validation_status: same_pipeline_validation; evidence: CHT-057: 'dian delta +0.167; bottom 35% median -0.039. loo auc 0.622; permutation p=0.005. drop gafford rho=+0.244 p=0.020. exploratory scrip'
- observed_dates: CHT-057: 2026-07-19 (transcript)
- observed_failure_evidence: NOT_RECORDED
- observed_failure_type: D_positive
- observed_hypothesis: Pre-move cut share (vs drive share) predicts whether a connector's organizational function reproduces after a move.
- observed_method: 92 connector movers; Spearman vs Delta; tercile hit rates; LOO AUC; 5000 label shuffles; drop Gafford / top-3; position splits.
- observed_notes: Exploratory scripts _explore_cut_*.py; paper treats cut share as a boundary condition. Almost all other pre-move predictors were null.
- observed_project: Structural Influence (Paper 1)
- observed_research_question: Cut- vs drive-based connector portability
- observed_result: Cut share rho=+0.265 p=0.011 AUC 0.653. Cut-drive rho=+0.314 p=0.002 AUC 0.656. Drive rho=-0.278 p=0.007. Top cut tercile 65% portable median Delta +0.167; bottom 35% median -0.039. LOO AUC 0.622; permutation p=0.005. Drop Gafford rho=+0.244 p=0.020.
- observed_sample_and_power: n=92 connector movers
- observed_sources: CHT-057: b12a5e7d-6340-4afd-9aae-e0e979f11269
- observed_verdict: supported
- edges: auto_addresses_question RQC:RQC-128; auto_has_risk RISK:SAMPLE_SIZE_POWER; auto_limited_by LIM:small_sample; auto_measures VAR:play_type_share_mix; auto_uses_dataset DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions; auto_uses_method METH:correlation; auto_uses_method METH:placebo_or_permutation_test

## SF-PAP-029 (gold in RT-183; record identical across these snapshots: True)

Snapshot RT-183; member records: PAP-029
- _label: Study family SF-PAP-029: Destination outcome (net rating) checks for movers (archive)
- auto_adjudication_basis: R0 single record; automated rule-based adjudication, not human adjudication
- auto_confidence: high (1.0)
- auto_failure_mechanism: A_unanswerable (question not answerable with the data or design)
- auto_knowable_before_outcome: no_evidence
- auto_members_disagree: no
- auto_outcome_status: untestable
- auto_validation_status: no_validation_recorded; evidence: NOT_RECORDED
- observed_dates: PAP-029: 2026-07-28 (doc)
- observed_failure_evidence: stated underpowered
- observed_failure_type: A_unanswerable
- observed_hypothesis: Portability relates to destination net rating change.
- observed_method: Movers' destination on-court net rating incl. origin-to-destination change.
- observed_notes: Dropped from Paper 1.
- observed_project: Structural Influence (Paper 1)
- observed_research_question: Destination outcome (net rating) checks for movers (archive)
- observed_result: 'underpowered and null once corrected for landing-spot quality' (no numbers)
- observed_sample_and_power: NOT_RECORDED
- observed_sources: PAP-029: C:\Users\lisas\OneDrive\Documents\Basketball\Archive\Paper2 Wiring\paper.tex
- observed_verdict: null
- edges: auto_addresses_question RQC:RQC-004; auto_has_risk RISK:SAMPLE_SIZE_POWER; auto_limited_by LIM:low_power_large_MDE; auto_limited_by LIM:small_sample; auto_measures VAR:net_rating_ORtg; auto_measures VAR:win_probability_series_outcome; auto_uses_dataset DS:Box_score_and_traditional_stats

## SF-TMP-009 (gold in RT-112; record identical across these snapshots: True)

Snapshot RT-112; member records: TMP-009
- _label: Study family SF-TMP-009: PULL_UP exposure-effect diagnostics
- auto_adjudication_basis: R0 single record; automated rule-based adjudication, not human adjudication
- auto_confidence: high (0.95)
- auto_failure_mechanism: C_artifact (apparent effect produced by a construction, selection or labelling flaw)
- auto_knowable_before_outcome: no_evidence
- auto_members_disagree: no
- auto_outcome_status: artifact
- auto_validation_status: same_pipeline_validation; evidence: TMP-009: 'teammates' prior pull_ups, shot-selection controls, fatigue placebo, with (pullup2) and without (pullup3) lineup fe. with lineu'
- observed_dates: TMP-009: 2026-10-07 (mtime)
- observed_failure_evidence: Effect shrinks from -0.0255 to -0.0063 without lineup FE and the same-shooter placebo on other play types is -0.0071/-0.0075, consistent with shooter-level confound.
- observed_failure_type: C_artifact
- observed_hypothesis: The PULL_UP-specific decline with exposure is defensive adaptation rather than shooter selection/lineup artifact.
- observed_method: Exposure bins, shooter's own vs teammates' prior PULL_UPs, shot-selection controls, fatigue placebo, with (pullup2) and without (pullup3) lineup FE.
- observed_notes: Verdict is extractor's reading of diagnostics; no written conclusion.
- observed_project: Lineup/Team Adaptation
- observed_research_question: PULL_UP exposure-effect diagnostics
- observed_result: With lineup FE: slope holding shot fixed -0.0255 (0.0061); shooter's earlier scored -0.1044 vs not scored +0.0693. No lineup FE: -0.0063 (0.0036); placebo other play types -0.0075 (0.0017).
- observed_sample_and_power: NOT_RECORDED
- observed_sources: ['TMP-009: C:\\Users\\lisas\\AppData\\Local\\Temp\\supp_audit\\pu_head.py', 'TMP-009: C:\\Users\\lisas\\AppData\\Local\\Temp\\supp_audit\\pullup2.log', 'TMP-009: C:\\Users\\lisas\\AppData\\Local\\Temp\\supp_audit\\pullup2.py', 'TMP-009: C:\\Users\\lisas\\AppData\\Local\\Temp\\supp_audit\\pullup3.log', 'TMP-009: C:\\Users\\lisas\\AppData\\Local\\Temp\\supp_audit\\pullup3.py']
- observed_verdict: artifact_found
- edges: auto_addresses_question RQC:RQC-066; auto_has_risk RISK:CONFOUNDING; auto_has_risk RISK:PLACEBO_DEPENDENCE; auto_limited_by LIM:confounding; auto_uses_dataset DS:NBA_play_by_play_possessions_and_reconstructed_lineups; auto_uses_dataset DS:Shot_level_data_with_expected_FG; auto_uses_method METH:placebo_or_permutation_test

## SF-TMP-012 (gold in RT-112; record identical across these snapshots: True)

Snapshot RT-112; member records: TMP-012
- _label: Study family SF-TMP-012: Tail/null-model audit of the published suppression excess
- auto_adjudication_basis: R0 single record; automated rule-based adjudication, not human adjudication
- auto_confidence: high (0.95)
- auto_failure_mechanism: C_artifact (apparent effect produced by a construction, selection or labelling flaw)
- auto_knowable_before_outcome: yes_from_history_probable
- auto_members_disagree: no
- auto_outcome_status: artifact
- auto_validation_status: same_pipeline_validation; evidence: TMP-012: 'published estimator on frozen csv (f) and current graph (g), thresholds 0.10-0.50, five n'
- observed_dates: TMP-012: 2026-10-08 (mtime)
- observed_failure_evidence: Within-unit permutation null reproduces excess: 0.3798 vs 0.3744 (z 0.40).
- observed_failure_type: C_artifact
- observed_hypothesis: The published suppression excess (trigger drop minus matched control drop) exceeds appropriate null models and is asymmetric between decline and improvement tails.
- observed_method: Published estimator on frozen CSV (F) and current graph (G), thresholds 0.10-0.50, five null families (within-unit permutation 2000 reps, team-season reassign, bootstrap, parametric, shrunk model), tail-mass and RTM decomposition.
- observed_notes: Excess is mechanical under the selection rule; tail_supp drift-centering removes raw tail asymmetry.
- observed_project: Defensive Suppression (supplementary audit)
- observed_research_question: Tail/null-model audit of the published suppression excess
- observed_result: Reproduced excess 0.4080 CI [0.378,0.438]; G within-unit perm at 0.25: obs 0.3798 null 0.3744 resid +0.0054 z 0.40; asym neg-pos 0.0176 p 0.258; drift-centered tail mass ratio 1.007.
- observed_sample_and_power: 1,136-1,138 caliper pairs; null sd ~0.014
- observed_sources: ['TMP-012: C:\\Users\\lisas\\AppData\\Local\\Temp\\supp_audit\\tail_audit.log', 'TMP-012: C:\\Users\\lisas\\AppData\\Local\\Temp\\supp_audit\\tail_audit.py', 'TMP-012: C:\\Users\\lisas\\AppData\\Local\\Temp\\supp_audit\\tail_audit_plot.png', 'TMP-012: C:\\Users\\lisas\\AppData\\Local\\Temp\\supp_audit\\tail_audit_smoke.log', 'TMP-012: C:\\Users\\lisas\\AppData\\Local\\Temp\\supp_audit\\tail_report.log', 'TMP-012: C:\\Users\\lisas\\AppData\\Local\\Temp\\supp_audit\\tail_report.py', 'TMP-012: C:\\Users\\lisas\\AppData\\Local\\Temp\\supp_audit\\tail_report_partial.log', 'TMP-012: C:\\Users\\lisas\\AppData\\Local\\Temp\\supp_audit\\tail_summary.csv', 'TMP-012: C:\\Users\\lisas\\AppData\\Local\\Temp\\supp_audit\\tail_supp.log', 'TMP-012: C:\\Users\\lisas\\AppData\\Local\\Temp\\supp_audit\\tail_supp.py']
- observed_verdict: artifact_found
- edges: auto_addresses_question RQC:RQC-064; auto_has_risk RISK:DRIFT_NONSTATIONARITY; auto_has_risk RISK:EXPOSURE_SPARSITY; auto_has_risk RISK:MECHANICAL_FLOOR; auto_has_risk RISK:PLACEBO_DEPENDENCE; auto_limited_by LIM:drift; auto_limited_by LIM:insufficient_exposure; auto_limited_by LIM:selection_or_regression_to_the_mean; auto_uses_dataset DS:NBA_play_by_play_possessions_and_reconstructed_lineups; auto_uses_method METH:bootstrap_interval; auto_uses_method METH:matched_control; auto_uses_method METH:placebo_or_permutation_test

## SF-TMP-021 (gold in RT-112; record identical across these snapshots: True)

Snapshot RT-112; member records: TMP-021
- _label: Study family SF-TMP-021: Penalty-state adaptation (Pilot A)
- auto_adjudication_basis: R0 single record; automated rule-based adjudication, not human adjudication
- auto_confidence: medium (0.65)
- auto_failure_mechanism: E_unclear (mechanism unclear from the records)
- auto_knowable_before_outcome: no_evidence
- auto_members_disagree: no
- auto_outcome_status: inconclusive
- auto_validation_status: same_pipeline_validation; evidence: TMP-021: 'with clock>2:30, game x offense x period fe; 2->3 and 4->5+ placebos. any_fta 3->4 -0.151 vs placebos -5.556/-9.655; rim_pct +0'
- observed_dates: TMP-021: 2026-11-01 (mtime)
- observed_failure_evidence: Penalty contrast not distinct from placebo contrasts; SEs not printed (sqrt warning).
- observed_failure_type: E_unclear
- observed_hypothesis: Behavior changes when the defense enters the penalty (3->4 team fouls).
- observed_method: Possessions with clock>2:30, game x offense x period FE; 2->3 and 4->5+ placebos.
- observed_notes: pilots.py had no log; rerun in sweep.
- observed_project: Lineup/Team Adaptation
- observed_research_question: Penalty-state adaptation (Pilot A)
- observed_result: any_fta 3->4 -0.151 vs placebos -5.556/-9.655; rim_pct +0.015 vs +1.666/+2.077; pts +0.020.
- observed_sample_and_power: NOT_RECORDED
- observed_sources: ['TMP-021: C:\\Users\\lisas\\AppData\\Local\\Temp\\supp_audit\\adaptation_sweep.log', 'TMP-021: C:\\Users\\lisas\\AppData\\Local\\Temp\\supp_audit\\adaptation_sweep.py', 'TMP-021: C:\\Users\\lisas\\AppData\\Local\\Temp\\supp_audit\\pilots.py']
- observed_verdict: null
- edges: auto_addresses_question RQC:RQC-176; auto_has_risk RISK:PLACEBO_DEPENDENCE; auto_measures VAR:free_throws_fouls; auto_uses_dataset DS:NBA_play_by_play_possessions_and_reconstructed_lineups; auto_uses_method METH:placebo_or_permutation_test

## SF04 (gold in RT-066; record identical across these snapshots: True)

Snapshot RT-066; member records: APPM-028; APPS-029; APPS-028; CHT-038
- _label: Study family SF04: Live trigger timing: early vs late detection
- auto_adjudication_basis: R5 unresolved conflict: members disagree and no rule applies; automated rule-based adjudication, not human adjudication
- auto_confidence: low (0.26)
- auto_failure_mechanism: none (no failure recorded)
- auto_knowable_before_outcome: no_evidence
- auto_members_disagree: yes
- auto_outcome_status: inconclusive
- auto_validation_status: same_pipeline_validation; evidence: CHT-038: '11 gap 0.25 ppp p=0.000001 over 25 series. multiple on-disk validation artifacts later canonicalized in final_numbers_sheet; chat'
- observed_dates: ['APPM-028: 2026-06-19 (mtime)', 'APPS-028: 2026-05-28 (mtime)', 'APPS-029: 2026-05-28 (mtime)', 'CHT-038: 2026-05-26 (transcript)']
- observed_failure_evidence: ['[APPM-028] rho 0.2859, p=0.031 (n=57).', '[APPS-028] Timing is actionable (100% with >=5 remaining) but BEST vs AVOID ROG PPP p=0.073965 and Spearman p=0.456.', '[APPS-029] BEST vs AVOID ROG PPP confirmed (p=0.0) and Spearman significant; timing still 100% actionable.', '[CHT-038] NOT_RECORDED']
- observed_failure_type: ['[APPM-028] D_positive', '[APPS-028] E_unclear', '[APPS-029] D_positive', '[CHT-038] D_positive']
- observed_hypothesis: Earlier suppression triggers leave time to act and yield better BEST-counter outcomes.
- observed_method: ['[APPM-028] 228 trigger events (2024-26 playoffs); rest-of-game PPP by tier; early (<=12 H2 poss) vs late.', '[APPS-028] Possession-by-possession replay, 10 2025-26 series. Trigger: H2 PPP drop>=0.25, n>=10 (or n>=5 with eff_n>=300). Counter PPP measured after trigger, not full H2.', '[APPS-029] Same Tab 2 logic as APPS-028; 228 unique triggers; AVOID_OVERRIDE rule added.', '[CHT-038] 25-game run of Tab2 triggers; rest-of-game PPP by tier.']
- observed_notes: ['[APPM-028] Weak evidence: single p=0.03 with n=57.', '[APPS-028] Follow-up 25-series replay (APPS-029) confirms BEST vs AVOID.', '[APPS-029] Different conclusion from the 10-series live replay; n_runs kept separate because MW went from p=0.074 to p=0.0.', '[CHT-038] Multiple on-disk validation artifacts later canonicalized in FINAL_NUMBERS_SHEET; chat mixes pre- and post-net_swing-fix numbers.']
- observed_project: Strategy app
- observed_research_question: Live trigger timing: early vs late detection
- observed_result: ['[APPM-028] Tier Spearman rho -0.2066 p=1e-06 n=557; BEST-AVOID gap early 0.701 (26 triggers) vs late 0.415 (202); rho 0.2859 p=0.031 n=57.', '[APPS-028] 101 triggers; 100% actionable (>=5 H2 poss remaining); mean remaining 23.4. Spearman tier vs ROG PPP rho=-0.0457, p=0.45616, n=268. MW BEST 1.227 (n=30) vs AVOID 1.037 (n=95), p=0.073965 (not confirmed at 0.05). Early vs late BEST ROG 1.521 vs 1.182.', '[APPS-029] 228 triggers, 100% actionable, mean remaining 21.0. Spearman rho=-0.2066, p=1e-06, n=557. MW BEST 1.263 (n=57) vs AVOID 0.783 (n=110), p=0.0. Early BEST-AVOID gap 0.701 vs late 0.415.', '[CHT-038] Only 13% fired early (within first 12 H2 possessions of that PT). BEST n=67 avg rest-of-game PPP 1.259. Later honest labeling: BEST ~1.44 vs AVOID ~0.82, gap +0.620, p=0.0. Chat also cites 1.35 vs 1.11 gap 0.25 PPP p=0.000001 over 25 series.']
- observed_sample_and_power: ['[APPM-028] n=57 BEST obs', '[APPS-028] 268 counter obs, 101 triggers; BEST n=30', '[APPS-029] 557 counter obs, 228 triggers', '[CHT-038] 25-game / 25-series runs']
- observed_sources: ['APPM-028: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\OVERNIGHT_SUMMARY.md', 'APPM-028: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_run_live_trigger_validation.py', 'APPS-028: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\playsheet_validation\\live_trigger_validation\\live_trigger_report.md', 'APPS-029: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\playsheet_validation\\live_trigger_validation\\live_trigger_report_seasons_25_26_clean.md', 'CHT-038: fe66194a-4f5a-4778-bf2d-6912b8da2848']
- observed_verdict: ['[APPM-028] supported', '[APPS-028] inconclusive', '[APPS-029] supported', '[CHT-038] descriptive']
- edges: auto_addresses_question RQC:RQC-028; auto_has_risk RISK:SAMPLE_SIZE_POWER; auto_limited_by LIM:small_sample; auto_measures VAR:PPP_points_per_possession; auto_measures VAR:win_probability_series_outcome; auto_uses_dataset DS:NBA_play_by_play_possessions_and_reconstructed_lineups; auto_uses_dataset DS:Playoff_series_outcomes; auto_uses_method METH:correlation; auto_uses_method METH:holdout_backtest_or_replay

## SF07 (gold in RT-147; record identical across these snapshots: True)

Snapshot RT-147; member records: APPA-049; APPS-037
- _label: Study family SF07: Sequential pair premium and defensive aftershock (8/8 PTs)
- auto_adjudication_basis: R1 all members agree; automated rule-based adjudication, not human adjudication
- auto_confidence: high (1.0)
- auto_failure_mechanism: D_positive (no failure: positive result)
- auto_knowable_before_outcome: not_applicable
- auto_members_disagree: yes
- auto_outcome_status: supported
- auto_validation_status: same_pipeline_validation; evidence: APPA-049: 'ium = y ppp after x vs y h2 baseline. a2 aftershock 8/8 pts replicate all-games and playoffs (cut +0.119 n=21,398 / po +0.131 n='
- observed_dates: ['APPA-049: 2026-05-31 (doc)', 'APPS-037: 2026-05-31 (doc)']
- observed_failure_evidence: ['[APPA-049] 8/8 play types replicate in both all-games and playoffs.', '[APPS-037] Large-n aftershock is uniformly positive across PTs (opponent scores ~1.07-1.09 vs baseline 1.206) so it may be a generic dead-ball/score effect rather than PT-specific disruption.']
- observed_failure_type: ['[APPA-049] D_positive', '[APPS-037] E_unclear']
- observed_hypothesis: After the opponent runs play type X, the next offensive play type Y scores above Y's unconditional H2 baseline, and every PT has a defensive aftershock.
- observed_method: ['[APPA-049] own_seq_ec; n=458,604 opp possessions; all-games vs playoffs split; premium = Y PPP after X vs Y H2 baseline.', '[APPS-037] All games H2 sequential pairs. Own-next baseline 0.975 PPP (n=18943); opponent-next baseline 1.206 (n=458604). Aftershock = opp baseline - opp next PPP after X succeeds.']
- observed_notes: ['[APPA-049] Team-level 1-2 punch table includes tiny-n cells (BKN n=16, CHI n=18) marked sig at |t|>=2.0.', '[APPS-037] Sign convention here (positive aftershock = opponent scores LESS) is opposite of the 52-series net-swing table where DRIVE/POST_UP have negative net swing.']
- observed_project: Defensive Suppression; Strategy app
- observed_research_question: Sequential pair premium and defensive aftershock (8/8 PTs)
- observed_result: ['[APPA-049] A2 aftershock 8/8 PTs replicate all-games and playoffs (CUT +0.119 n=21,398 / PO +0.131 n=1,145 through TRANSITION +0.135 n=26,262 / +0.126 n=1,529). Top pair premiums: PUTBACK->TRANSITION +0.084 n=565; CUT->PULL_UP +0.065 n=2,620.', '[APPS-037] All-games aftershock after success: CUT +0.119 (n=21398), DRIVE +0.123 (57621), PNR +0.127 (51194), POST_UP +0.128 (20619), PULL_UP +0.132 (26060), PUTBACK +0.130 (5888), SPOT_UP +0.128 (43857), TRANSITION +0.135 (26262). All 8 replicate in playoffs. Own-next A1 treated as exploratory (~4% of pairs).']
- observed_sample_and_power: ['[APPA-049] n=458,604 opp possessions', '[APPS-037] opp-next n=458604; per-PT success n=5.9k-57.6k']
- observed_sources: ['APPA-049: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\FINAL_NUMBERS_SHEET.md', 'APPS-037: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\playsheet_validation\\sequential_premium\\sequential_premium_report.md', 'APPS-037: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\playsheet_validation\\sequential_premium_run.log']
- observed_verdict: ['[APPA-049] supported', '[APPS-037] descriptive']
- edges: auto_addresses_question RQC:RQC-119; auto_has_risk RISK:SAMPLE_SIZE_POWER; auto_limited_by LIM:small_sample; auto_measures VAR:PPP_points_per_possession; auto_uses_dataset DS:NBA_play_by_play_possessions_and_reconstructed_lineups; auto_uses_dataset DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions; auto_uses_dataset DS:Playoff_series_outcomes

## SF09 (gold in RT-112; record identical across these snapshots: True)

Snapshot RT-112; member records: APPA-057; APPS-042
- _label: Study family SF09: Double-suppression stacking (POST_UP then PUTBACK)
- auto_adjudication_basis: R5 unresolved conflict: members disagree and no rule applies; automated rule-based adjudication, not human adjudication
- auto_confidence: low (0.28)
- auto_failure_mechanism: none (no failure recorded)
- auto_knowable_before_outcome: no_evidence
- auto_members_disagree: yes
- auto_outcome_status: inconclusive
- auto_validation_status: no_validation_recorded; evidence: NOT_RECORDED
- observed_dates: ['APPA-057: 2026-05-31 (doc)', 'APPS-042: 2026-05-31 (doc)']
- observed_failure_evidence: ['[APPA-057] Stacked suppression -0.071 is less than either alone and far below additive -0.232 (n=1,047).', '[APPS-042] PUTBACK vs POST_UP gradients differ as hypothesized, but TRANSITION gradient has the wrong sign and stacked suppression is less than additive; per-player stacked n often <5.']
- observed_failure_type: ['[APPA-057] B_powered_null', '[APPS-042] E_unclear']
- observed_hypothesis: Opponent POST_UP then PUTBACK stacks additively against the next star possession.
- observed_method: ['[APPA-057] League sequence opp POST_UP -> offense -> opp PUTBACK -> star next; vs each alone. Mitchell PUTBACK-by-opponent directional split.', '[APPS-042] POST_UP cluster (Jokic, Doncic, LeBron, Fox, Brown) Q1-Q4 deltas; TRANSITION cluster (Tatum, Morant, Young, Haliburton); league POST_UP then PUTBACK 4-hop stack n=1047.']
- observed_notes: ['[APPA-057] Shared-pathway interpretation: offense adjusts after the first disruption.', '[APPS-042] Authors read POST_UP as rhythm/read disruption not fatigue; TRANSITION unexpected +0.075 flagged to re-examine sample.']
- observed_project: Defensive Suppression; Strategy app
- observed_research_question: Double-suppression stacking (POST_UP then PUTBACK)
- observed_result: ['[APPA-057] Baseline 1.210 n=960,764. After PUTBACK only 1.097 d=-0.113 n=15,898. After POST_UP only 1.091 d=-0.119 n=76,329. Stacked 1.138 d=-0.071 n=1,047 vs additive prediction -0.232. Mitchell after PUTBACK 0.919 vs 1.252 (d=-0.333, n=95); 8/13 teams below baseline n>=5, spread 1.200 PPP.', '[APPS-042] POST_UP Q1->Q4 -0.065 (Q1 -0.119 to Q4 -0.184); PUTBACK -0.374 (0.144 to -0.23). TRANSITION cluster gradient +0.075 (unexpected vs hypothesized flat). Stacked delta -0.071 vs additive prediction -0.232 (less than additive). League after PUTBACK -0.113 (n=15898), after POST_UP -0.119 (n=76329).']
- observed_sample_and_power: ['[APPA-057] n=1,047 stacked; 15,898 / 76,329 singles', '[APPS-042] cluster n=5 players; stacked n=1047 league / typically n<10 per star']
- observed_sources: ['APPA-057: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\FINAL_NUMBERS_SHEET.md', 'APPS-042: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\playsheet_validation\\postup_putback_gradient\\postup_vs_putback_gradient.md', 'APPS-042: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\playsheet_validation\\three_mechanisms\\double_suppression_mitchell_report.md', 'APPS-042: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\playsheet_validation\\three_mechanisms\\transition_immunity_report.md']
- observed_verdict: ['[APPA-057] null', '[APPS-042] inconclusive']
- edges: auto_addresses_question RQC:RQC-009; auto_has_risk RISK:IMPLEMENTATION_BUG; auto_has_risk RISK:PLACEBO_DEPENDENCE; auto_has_risk RISK:SAMPLE_SIZE_POWER; auto_limited_by LIM:implementation_bug; auto_limited_by LIM:small_sample; auto_measures VAR:PPP_points_per_possession; auto_uses_dataset DS:NBA_play_by_play_possessions_and_reconstructed_lineups; auto_uses_dataset DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions

## SF15 (gold in RT-179; record identical across these snapshots: True)

Snapshot RT-179; member records: APPS-063; CHT-035
- _label: Study family SF15: Test 4: foul-trouble sequencing after star 2nd Q1/Q2 foul
- auto_adjudication_basis: R1 all members agree; automated rule-based adjudication, not human adjudication
- auto_confidence: high (0.79)
- auto_failure_mechanism: C_artifact (apparent effect produced by a construction, selection or labelling flaw)
- auto_knowable_before_outcome: yes_from_history_probable
- auto_members_disagree: no
- auto_outcome_status: artifact
- auto_validation_status: same_pipeline_validation; evidence: APPS-063: '0.0655; lag-2 -0.0192; lag-3 -0.0272. no lag clears ci+perm+placebo. knowable: a 2nd foul is often a shooting foul, so lag-1 in'
- observed_dates: ['APPS-063: 2026-06-14 (mtime)', 'CHT-035: 2026-06-14 (transcript)']
- observed_failure_evidence: ['[APPS-063] Headline +0.204 was FT-possession coding; clean lag-1 +0.049 does not clear the pre-specified bars.', '[CHT-035] Raw +0.204 is a free-throw possession-coding artifact (41.8% vs 9.9% FT).']
- observed_failure_type: ['[APPS-063] C_artifact', '[CHT-035] C_artifact']
- observed_hypothesis: Opponent PPP rises on the next 1-3 possessions after a star's 2nd personal foul in Q1/Q2.
- observed_method: ['[APPS-063] 2104 qualifying events. Exact match period x margin x season x offensive team. FT possessions excluded after first-pass artifact.', '[CHT-035] Lag-1 after foul-trouble flag vs control; FT-share diagnostic.']
- observed_notes: ['[APPS-063] Knowable: a 2nd foul is often a shooting foul, so lag-1 includes FT trips unless excluded. On-floor vs benched not verifiable.', '[CHT-035] Results file on disk mentioned. Compositional confound was knowable from FT share.']
- observed_project: Strategy app
- observed_research_question: Test 4: foul-trouble sequencing after star 2nd Q1/Q2 foul
- observed_result: ['[APPS-063] Including FT: lag-1 ATT=+0.204 CI[+0.163,+0.245] (artifact: FT share 41.8% vs 9.9%). Excluding FT: lag-1 +0.0486 [-0.0060,+0.0991] perm p=0.0655; lag-2 -0.0192; lag-3 -0.0272. No lag clears CI+perm+placebo.', '[CHT-035] Raw lag-1 +0.204 (p=0.0005) was 41.8% FT vs 9.9% control. Apples-to-apples +0.049, not significant.']
- observed_sample_and_power: ['[APPS-063] n_treated lag-1=2101', '[CHT-035] NOT_RECORDED']
- observed_sources: ['APPS-063: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\sequence_memory\\output\\test_4_foul_trouble.md', 'CHT-035: 1b9f0f61-d051-4b7b-8eef-8d1253cf67e2', 'CHT-035: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball Strategy\\sequence_memory\\output\\test_4_foul_trouble.md']
- observed_verdict: ['[APPS-063] null', '[CHT-035] artifact_found']
- edges: auto_addresses_question RQC:RQC-049; auto_has_risk RISK:BASE_RATE; auto_has_risk RISK:CONFOUNDING; auto_has_risk RISK:MECHANICAL_FLOOR; auto_limited_by LIM:confounding; auto_measures VAR:PPP_points_per_possession; auto_measures VAR:free_throws_fouls; auto_measures VAR:play_type_share_mix; auto_uses_dataset DS:NBA_play_by_play_possessions_and_reconstructed_lineups; auto_uses_method METH:matched_control; auto_uses_method METH:placebo_or_permutation_test

## SF20 (gold in RT-066; record identical across these snapshots: True)

Snapshot RT-066; member records: APPA-006; APPA-007; APPS-081; CHT-051; PAP-023
- _label: Study family SF20: Absence validation (structure moves under real absence; simulation tracks it)
- auto_adjudication_basis: R4 paper record takes precedence (date order uncertain); automated rule-based adjudication, not human adjudication
- auto_confidence: medium (0.55)
- auto_failure_mechanism: A_unanswerable (question not answerable with the data or design)
- auto_knowable_before_outcome: no_evidence
- auto_members_disagree: yes
- auto_outcome_status: untestable
- auto_validation_status: same_pipeline_validation; evidence: APPA-006: '5; balanced size-m null (amendment a1); franchise-clustered permutation and bootstrap. gate g2 21/23 (91%) above null median; v1(a)'
- observed_dates: ['APPA-006: 2026-07-12 (doc)', 'APPA-007: 2026-07-12 (doc)', 'APPS-081: 2026-07-12 (mtime)', 'CHT-051: 2026-07-12 (transcript)', 'PAP-023: 2026-07-12 (doc)']
- observed_failure_evidence: ['[APPA-006] CI excludes 0; binomial p=2.67e-16.', '[APPA-007] 18 franchises below ~20-franchise floor; CI width ~0.9; gate already warned weak (+0.099).', '[APPS-081] V1 confirmed but V2 dose-response ns with n=23 player-seasons / 18 franchises explicitly underpowered; no re-run per ?9.', '[CHT-051] 18 franchises below registered ~20 floor; rho=+0.288 p=0.077; over-predicts replaceable centers.', '[PAP-023] UNDERPOWERED: <20 franchises (18), n=23']
- observed_failure_type: ['[APPA-006] D_positive', '[APPA-007] A_unanswerable', '[APPS-081] A_unanswerable', '[CHT-051] A_unanswerable', '[PAP-023] A_unanswerable']
- observed_hypothesis: Real player absences move the association structure (V1) and the LOO simulation predicts the magnitude (V2).
- observed_method: ['[APPA-006] Pre-registered; 23 player-seasons, 18 franchises, ON_COURT-verified absences, 2022-25; balanced size-m null (Amendment A1); franchise-clustered permutation and bootstrap.', '[APPA-007] Same pre-registered 23 player-seasons; Spearman with franchise permutation (5000) and cluster bootstrap (2000); post-hoc diagnostics.', '[APPS-081] Gate n_null=150 n_rep=120 core=23. Confirmatory n_null=500 n_perm=5000 player_seasons=23 franchises=18 flagged underpowered.', '[CHT-051] 23 player-seasons / 18 franchises (below ~20 franchise floor). V1: 16/23 above noise. V2 Spearman L vs D_real.', '[PAP-023] 23 player-season absences, 18 franchises; gate then confirmatory.']
- observed_notes: ['[APPA-006] One pre-run amendment (balanced null) because draft null was infeasible when absent>present.', '[APPA-007] Prereg itself said <20 franchises means underpowered, and the user skipped the full-pool sweep that could have added franchises. Diagnostics also point to a substantive absorption/cascade failure mode.', '[APPS-081] Knowable: <20 franchises was the underpowered flag written into the confirmatory output.', '[CHT-051] Diagnostics in paper2_output/absence_diagnose.csv. Underpower was knowable from franchise N. Later full-pool run reversed V2.', '[PAP-023] Cited in Paper 1 Appendix F as registered negative; files live in App\\Strategy (other slice may duplicate).']
- observed_project: Structural Influence (Paper 1); When a Hub Sits (Paper 2)
- observed_research_question: Absence validation (structure moves under real absence; simulation tracks it)
- observed_result: ['[APPA-006] Gate G2 21/23 (91%) above null median; V1(a) 16/23 above own-null p95, binomial p=2.67e-16; V1(b) mean(D_real - median_null)=+0.142, CI [+0.103, +0.187].', '[APPA-007] Gate G3 Spearman +0.099. V2a Spearman +0.288, p=0.077, CI [-0.244, +0.667] FAIL; V2b partial +0.253, p=0.115, CI [-0.262, +0.615] FAIL. Diagnostics: H_code ruled out (rho=0.933); dropping 2 absorption cases rho=+0.444 (n=21).', '[APPS-081] Gate PASS (G2 frac_above_median=0.913; G3 rho=+0.099). Confirmatory V1(a) 16/23 above p95 binomial_p=2.67e-16; V1(b) mean_diff=+0.142 CI[+0.103,+0.187] CONFIRMED. V2a rho=+0.288 p=0.0770 CI[-0.244,+0.667]; V2b partial rho=+0.253 p=0.1152 NOT. VERDICT PARTIAL/NEGATIVE UNDERPOWERED <20 franchises.', '[CHT-051] V1: 16/23 above noise floor, binomial p ~ 10^-16, bootstrap CI [+0.103, +0.187]. V2: recorded rho=+0.288 p=0.077; scale-matched +0.243; drop 2 absorption bigs +0.444. L_pred vs recomputed LOO rho=+0.93 (measurement faithful).', '[PAP-023] V1(a) 16/23 above p95 binomial p=2.67e-16; V1(b) +0.142 CI[+0.103,+0.187] CONFIRMED; V2a rho=+0.288 p=0.077 CI[-0.244,+0.667]; V2b rho=+0.253 p=0.115 NOT']
- observed_sample_and_power: ['[APPA-006] 23 player-seasons, 18 franchises (below ~20 floor, flagged UNDERPOWERED)', '[APPA-007] n=23, 18 franchises; CI [-0.244, +0.667]', '[APPS-081] n=23 player-seasons, 18 franchises', '[CHT-051] n=23 player-seasons / 18 franchises', '[PAP-023] n=23, 18 franchises']
- observed_sources: ['APPA-006: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\ABSENCE_VALIDATION_PREREGISTRATION.md', 'APPA-007: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\ABSENCE_VALIDATION_PREREGISTRATION.md', 'APPS-081: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\paper2_output\\absence_full_result.txt', 'APPS-081: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\paper2_output\\absence_gate_result.txt', 'CHT-051: 9ea66f06-5402-4b05-850e-4b0b12a3afb6', 'CHT-051: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball Strategy\\ABSENCE_VALIDATION_PREREGISTRATION.md', 'PAP-023: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\ABSENCE_VALIDATION_PREREGISTRATION.md', 'PAP-023: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\paper2_output\\absence_full_result.txt', 'PAP-023: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\paper2_output\\absence_gate_result.txt', 'PAP-023: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\Published\\Structural Influence\\paper.tex']
- observed_verdict: ['[APPA-006] supported', '[APPA-007] failed_gate', '[APPS-081] inconclusive', '[CHT-051] failed_gate', '[PAP-023] null']
- edges: auto_addresses_question RQC:RQC-016; auto_has_risk RISK:MECHANICAL_FLOOR; auto_has_risk RISK:SAMPLE_SIZE_POWER; auto_limited_by LIM:low_power_large_MDE; auto_limited_by LIM:small_sample; auto_measures VAR:structural_influence_load_L; auto_uses_dataset DS:NCAA_tournament_and_ratings_data; auto_uses_dataset DS:Player_absence_spells; auto_uses_method METH:bootstrap_interval; auto_uses_method METH:correlation; auto_uses_method METH:matched_control; auto_uses_method METH:placebo_or_permutation_test; auto_uses_method METH:simulation

## SF31 (gold in RT-066; record identical across these snapshots: True)

Snapshot RT-066; member records: APPM-015; CHT-017
- _label: Study family SF31: Routing prior vs H2H posterior gate diagnostic
- auto_adjudication_basis: R1 all members agree; automated rule-based adjudication, not human adjudication
- auto_confidence: high (1.0)
- auto_failure_mechanism: C_artifact (apparent effect produced by a construction, selection or labelling flaw)
- auto_knowable_before_outcome: no_evidence
- auto_members_disagree: no
- auto_outcome_status: artifact
- auto_validation_status: no_validation_recorded; evidence: NOT_RECORDED
- observed_dates: ['APPM-015: 2026-06-10 (mtime)', 'CHT-017: 2026-05-15 (transcript)']
- observed_failure_evidence: ['[APPM-015] Apparent +1.13 PPP edge is small-sample inflation (e.g. n=6, PPP=3.00).', '[CHT-017] Low-n H2H leads are 1-shot 3.00 PPP noise; +1.26 delta is small-sample distortion.']
- observed_failure_type: ['[APPM-015] C_artifact', '[CHT-017] C_artifact']
- observed_hypothesis: The n>=15 H2H gate suppresses real player-routing signal.
- observed_method: ['[APPM-015] 6,221 (offense, opponent, PT) cells; count H2H leaders differing from season default at gates 5/10/15/25.', '[CHT-017] Scan of 6,221 (team, opp, PT) cells; mean PPP delta of lead vs default at n gates.']
- observed_notes: ['[APPM-015] Recommendation: keep n>=15 gate.', '[CHT-017] Results file on disk mentioned: ROUTING_PRIOR_VS_H2H_DIAGNOSTIC.md.']
- observed_project: Strategy app
- observed_research_question: Routing prior vs H2H posterior gate diagnostic
- observed_result: ['[APPM-015] Mean PPP delta lead-default +1.259 (n>=5) to +1.129 (n>=15); low-n leaders are role players with 2-3 PPP on 5-7 possessions.', '[CHT-017] At n=5-9 typical leaders are 1-shot 3.00-PPP role players. Mean PPP delta lead-vs-default +1.26 at n>=5 and +1.13 at n>=15, inflated by small-sample distortion. n>=15 routing-override gate judged to filter noise correctly.']
- observed_sample_and_power: ['[APPM-015] NOT_RECORDED', '[CHT-017] 6,221 cells']
- observed_sources: ['APPM-015: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\ROUTING_PRIOR_VS_H2H_DIAGNOSTIC.md', 'APPM-015: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_diag_routing_vs_h2h.py', 'CHT-017: 69feafdf-b3ec-4450-9564-c9c86979924b', 'CHT-017: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball Strategy\\ROUTING_PRIOR_VS_H2H_DIAGNOSTIC.md']
- observed_verdict: ['[APPM-015] artifact_found', '[CHT-017] artifact_found']
- edges: auto_addresses_question RQC:RQC-175; auto_has_risk RISK:SAMPLE_SIZE_POWER; auto_limited_by LIM:small_sample; auto_measures VAR:PPP_points_per_possession; auto_uses_dataset DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions; auto_uses_method METH:matched_control

## SF37 (gold in RT-014; record identical across these snapshots: True)

Snapshot RT-014; member records: APPM-017; CHT-024
- _label: Study family SF37: Possession-level SQ2 test: proxy engine on all RS games
- auto_adjudication_basis: R1 all members agree; automated rule-based adjudication, not human adjudication
- auto_confidence: medium (0.68)
- auto_failure_mechanism: E_unclear (mechanism unclear from the records)
- auto_knowable_before_outcome: no_evidence
- auto_members_disagree: no
- auto_outcome_status: inconclusive
- auto_validation_status: no_validation_recorded; evidence: NOT_RECORDED
- observed_dates: ['APPM-017: 2026-05-23 (mtime)', 'CHT-024: 2026-05-23 (transcript)']
- observed_failure_evidence: ['[APPM-017] Proxy fidelity 16.5% (<70%); in-sample contamination of RS aggregates; iid SEs.', '[CHT-024] Proxy agrees with production engine on only 16.5% of 79 playoff pairs, so this is not a test of the shipped optimizer.']
- observed_failure_type: ['[APPM-017] E_unclear', '[CHT-024] E_unclear']
- observed_hypothesis: A matchup-conditioned PT picker has possession-level signal at team-game level.
- observed_method: ['[APPM-017] Proxy engine on 4,082 qualifying team-games; Tests A/B/C; 16,921 cells for FE OLS.', '[CHT-024] Proxy = team_PPP x _def_mod ranked by lift; NOT production engine. Fidelity vs production recs 13/79 = 16.5%. 4,082 qualifying pairs (rec_n>=8, nonrec_n>=25).']
- observed_notes: ['[APPM-017] Positive for proxy only; does not validate production engine.', '[CHT-024] No production-engine results file; proxy script and fidelity caveat live in the chat write-up. Knowable that skipping capacity_fit/fingerprint would break fidelity.']
- observed_project: Strategy app
- observed_research_question: Possession-level SQ2 test: proxy engine on all RS games
- observed_result: ['[APPM-017] C gamma +0.0714 SE 0.0057 p=0.0000; B DiD +0.062 [0.051,0.073]; proxy agrees with production engine 13/79 = 16.5%.', '[CHT-024] A +0.047 PPP (p<10^-3); B +0.062 PPP; C +0.0714 PPP, n=16,921 cells, p<10^-4. Coverage: 9,853 RS pairs; 35.7% clear, 33.8% ambiguous, 30.4% no_rec.']
- observed_sample_and_power: ['[APPM-017] n=16,921 cells', '[CHT-024] 4,082 pairs; production engine estimated ~400 hours if run fully']
- observed_sources: ['APPM-017: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\POSSESSION_PPP_ALL_GAMES_findings.md', 'CHT-024: d2a94a1e-b21a-4a3a-b2cf-3eb526e3f49a']
- observed_verdict: ['[APPM-017] inconclusive', '[CHT-024] inconclusive']
- edges: auto_addresses_question RQC:RQC-120; auto_has_risk RISK:LEAKAGE_LOOKAHEAD; auto_has_risk RISK:SAMPLE_SIZE_POWER; auto_limited_by LIM:small_sample; auto_measures VAR:PPP_points_per_possession; auto_uses_dataset DS:NBA_play_by_play_possessions_and_reconstructed_lineups; auto_uses_dataset DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions; auto_uses_method METH:difference_in_differences; auto_uses_method METH:matched_control; auto_uses_method METH:regression
