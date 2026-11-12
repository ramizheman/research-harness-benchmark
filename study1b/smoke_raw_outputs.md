# Study 1b smoke test: raw outputs

Final outputs exactly as saved in runs/study1b_smoke_v1/raw. Not scored against the answer key or the predictions.

## RT-012 OS seed 1

File: `runs\study1b_smoke_v1\raw\study1b_smoke_v1_openrouter_anthropic_claude-haiku-5.5_RT-012_OS_s1.json`

```json
{
 "research_concepts": [
  "teammate DRIVE preceding PNR as a sequence context",
  "pick-and-roll ball-handler points per possession (PPP)",
  "play-type labels derived from NBA play-by-play",
  "derived possession records (initiator, play type, points) in the graph database",
  "foul-ending leakage in play-type PPP"
 ],
 "methodological_questions": [
  "Does a teammate DRIVE immediately preceding a PNR change the PNR possession's PPP, compared with PNR possessions without that preceding DRIVE?",
  "Are the DRIVE and PNR labels reliable enough to define the sequence and the outcome?",
  "Do outcome-derived labels (points used to build the possession records) and foul endings make the PPP comparison circular or biased?",
  "Which confounders (lineup, shot quality, defense, fouls, time in game) must be controlled before attributing any PPP difference to the sequence?"
 ],
 "historical_evidence": [
  {
   "id": "FAM:SF-APPA-030",
   "status_as_recorded": "inconclusive",
   "finding": "Backfilled play-type labels (921,514 possessions) failed verification against league bands and team identities: PNR share 28.7% vs band 20-28% (FAIL), PULL_UP 7.9% (FAIL), 2024-25 PULL_UP about 0-1% for many teams, 82.8% of PNR labels proxy-calibrated, 3100 games with team PNR >33% (FAIL). PNR PPP 0.948 was recorded as PASS. Final verdict: FAIL."
  },
  {
   "id": "FAM:SF-CHT-025",
   "status_as_recorded": "artifact",
   "finding": "Play-type labeling audit found OTHER possessions with 36% ending in fouls, which inflates OTHER PPP; DRIVE sits 12 points below the foul benchmark; PNR shows a 22% foul rate; initiation_type maps only 335 of 50,668 possessions (0.7%) to a play type. Verdict: artifact_found."
  },
  {
   "id": "FAM:SF-APPA-005",
   "status_as_recorded": "untestable",
   "finding": "Scheme labels inferred backwards from opponent play-type PPP (523 within-game cells, 440 game pairs) gave near-uniform transition matrices, consistent with label noise. The record notes that outcome-inferred labels cannot separate a defensive change from the offense executing differently. No error rate was recorded for directly observed labels."
  },
  {
   "id": "FAM:SF-APPS-058",
   "status_as_recorded": "untestable",
   "finding": "On one game (0042500101), matchup and play-by-play fields gave confident on-ball coverage labels for only 14.9% (DET, 10 of 67) and 3.3% (ORL, 2 of 60) of possessions. The switches_on field was not populated. Verdict: failed_gate."
  }
 ],
 "failed_approaches": [
  {
   "id": "FAM:SF-APPA-030",
   "what_failed": "Using backfilled play-type labels from play-by-play as the basis for play-type analyses (PNR and PULL_UP most directly)",
   "why": "Failed league-band and team-identity checks; 82.8% of PNR labels were proxy-calibrated; 2024-25 PULL_UP near 0% for many teams. The record does not quantify how much these failures bias any estimate."
  },
  {
   "id": "FAM:SF-CHT-025",
   "what_failed": "Comparing PPP across play types (OTHER and DRIVE in particular) with the initiation_type mapping as the play-type source",
   "why": "Foul endings inflate OTHER PPP (36% foul endings); DRIVE is 12 points below the foul benchmark; initiation_type maps only 0.7% of possessions. The record does not measure bias in downstream estimates."
  },
  {
   "id": "FAM:SF-APPS-058",
   "what_failed": "Deriving observed on-ball coverage labels from the NBA matchup and play-by-play feeds",
   "why": "Confident label rates of 14.9% and 3.3% on one game; switches_on not populated; small sample (n=67/60)."
  },
  {
   "id": "FAM:SF-APPA-005",
   "what_failed": "Inferring defensive scheme labels from outcome (opponent play-type PPP)",
   "why": "Outcome-inferred labels cannot separate defensive adjustment from offensive execution; near-uniform transition matrices are consistent with label noise."
  }
 ],
 "evidence_establishes": [
  "The project's play-type labels from play-by-play have failed validation: league-band and team-identity checks failed for PNR and PULL_UP (FAM:SF-APPA-030).",
  "Foul endings contaminate PPP comparisons across play types, and the DRIVE label sits well below the foul benchmark (FAM:SF-CHT-025).",
  "Direct labels for on-ball coverage were rarely obtainable from these feeds in the one game examined (FAM:SF-APPS-058).",
  "Outcome-inferred labels are not a valid basis for testing defensive or offensive sequence effects (FAM:SF-APPA-005)."
 ],
 "evidence_does_not_establish": [
  "Whether the DRIVE-to-PNR sequence effect on PNR PPP is real or null, since no retrieved record tests this sequence.",
  "The size of label bias in the DRIVE or PNR categories on the specific sequence subset.",
  "The number of DRIVE-then-PNR sequences in the data, or the power to detect an effect.",
  "Whether the 82.8% proxy-calibrated PNR labels also affect the sequence (preceding-action) field.",
  "Any result from tracking data or from more than one game for sequence labels."
 ],
 "own_inferences": [
  "The question is testable in principle only if the DRIVE and PNR labels are validated against an independent source (for example, a hand-coded sample of sequences) before any PPP comparison.",
  "Because the PNR PPP is computed from the same points that define the derived possession records, a PPP comparison on labels partly built from outcomes risks circularity.",
  "Teammate DRIVE-to-PNR sequences are a subset of PNR possessions, so exposure may be sparse at team-game level; the count must be checked before any power claim.",
  "Lineup, shot quality, defensive matchup, and foul-ending differences could all move PNR PPP with or without the preceding DRIVE, so a raw comparison would be confounded."
 ],
 "uncertainties": [
  "The records do not say what share of the DRIVE-to-PNR sequence subset carries proxy-calibrated labels.",
  "The records do not give an error rate for directly observed DRIVE or PNR labels.",
  "Data version: the 2025-26 playoff file is partial before 2026-06-21, and the regular-season file is partial before 2026-04-13; the sample depends on which version is used.",
  "No follow-up tool was called to check sequence counts or label coverage for DRIVE-to-PNR pairs; those facts are unknown here."
 ],
 "historical_effect": {
  "changed_decision": "yes",
  "explanation": "Retrieved records show that play-type labels from these feeds failed validation (FAM:SF-APPA-030), that PPP comparisons across play types are contaminated by foul endings (FAM:SF-CHT-025), and that outcome-inferred or sparsely labeled categories are not testable (FAM:SF-APPA-005, FAM:SF-APPS-058). Given these, a direct test of the DRIVE-to-PNR PPP effect on the current labels would be built on unvalidated and outcome-contaminated inputs. The decision therefore moves from a proceed-as-posed plan to do_not_proceed until labels are validated."
 },
 "testability": {
  "p_testable": 0.2,
  "blocking_constraints": [
   {
    "code": "LABEL_ERROR",
    "text": "PNR labels are 82.8% proxy-calibrated and the backfilled labels failed league-band and team-identity checks (FAM:SF-APPA-030); DRIVE is 12 points below the foul benchmark (FAM:SF-CHT-025)."
   },
   {
    "code": "OUTCOME_DERIVED_LABEL",
    "text": "The derived possession records use points as part of their construction, so a PNR PPP comparison on those records may be partly circular with the labels."
   },
   {
    "code": "CONFOUNDING",
    "text": "Lineup, shot quality, defensive matchup and foul endings can move PNR PPP independently of any preceding DRIVE; the question as posed has no control for these."
   },
   {
    "code": "EXPOSURE_SPARSITY",
    "text": "The count of teammate DRIVE-then-PNR sequences is not recorded in the retrieved evidence; if sparse, the test has little power (own inference)."
   }
  ]
 },
 "prior_work": {
  "already_answered": "no",
  "cited": [
   "FAM:SF-APPA-030",
   "FAM:SF-CHT-025",
   "FAM:SF-APPA-005",
   "FAM:SF-APPS-058"
  ],
  "summary": "No retrieved record tests the teammate DRIVE-to-PNR sequence effect on PNR PPP. The cited records concern label validity (play-type backfill, foul leakage in PPP, outcome-inferred scheme labels, on-ball coverage labels). They bear on whether the sequence can be measured reliably, not on whether the effect exists."
 },
 "risks": [
  {
   "code": "LABEL_ERROR",
   "text": "Backfilled PNR and PULL_UP labels failed validation; 82.8% of PNR labels proxy-calibrated (FAM:SF-APPA-030)."
  },
  {
   "code": "BASE_RATE",
   "text": "Foul endings (22% of PNR, 36% of OTHER) distort PPP, and the base rate of points per possession may differ between sequence and non-sequence PNRs (FAM:SF-CHT-025; own inference on the sequence subset)."
  },
  {
   "code": "OUTCOME_DERIVED_LABEL",
   "text": "Possession records carry points, so the sequence label and the PPP outcome share a source, creating circularity risk."
  },
  {
   "code": "LEAKAGE_LOOKAHEAD",
   "text": "If the sequence label is assigned using information from after the PNR begins (for example, a play later coded as a DRIVE), the preceding-action condition may leak the outcome; own inference."
  },
  {
   "code": "CONFOUNDING",
   "text": "Lineup, defensive matchup, shot quality and fouls can affect PNR PPP without any DRIVE; a raw comparison is confounded."
  },
  {
   "code": "SAMPLE_SIZE_POWER",
   "text": "The DRIVE-then-PNR subset size is unknown; a small subset gives little power to detect a modest PPP difference (own inference)."
  },
  {
   "code": "MEASURE_RELIABILITY",
   "text": "No reliability estimate for DRIVE or PNR labels is recorded; the test-retest or inter-coder reliability of the play-type labels is unknown."
  },
  {
   "code": "MULTIPLE_TESTING",
   "text": "If the test is run across many teammate-action pairs or play types, the number of comparisons must be controlled (own inference)."
  },
  {
   "code": "DRIFT_NONSTATIONARITY",
   "text": "The data span 2022-23 to 2025-26, and the 2025-26 files are partial before their completion dates; labeling practice may differ across seasons (own inference)."
  }
 ],
 "predicted_outcome": {
  "supported": 0.1,
  "rejected": 0.15,
  "untestable": 0.25,
  "artifact": 0.3,
  "uncertain": 0.2
 },
 "decision": "do_not_proceed",
 "design": {
  "estimand": "Minimum viable test: the difference in PNR PPP between PNR possessions preceded by a teammate DRIVE and PNR possessions not preceded by one, after label validation and adjustment for confounders. Not to be run until the preconditions below are met.",
  "unit": "Ball-handler PNR possession (one row per PNR possession), with the preceding teammate action identified from the ordered play-by-play.",
  "sample": "Only after label validation: a hand-coded sample of PNR and DRIVE labels, checked against play-by-play action types, from the regular seasons 2022-23 to 2024-25 (complete files). Exclude partial 2025-26 files. Report the number of DRIVE-then-PNR sequences before any power claim; if too few, stop.",
  "power": "Not computed; to be set from the observed count of DRIVE-then-PNR sequences and a pre-specified minimum detectable PPP difference. Do not claim power without that count.",
  "controls": "Adjust for lineup and player fixed effects, defensive matchup, shot distance and result (excluded from the outcome if derived from points), game clock and score state, and foul endings (analyse with and without foul-ending possessions). Use only pre-PNR information for the sequence label to avoid lookahead.",
  "falsification": "A placebo sequence (a teammate SPOT-UP or other non-DRIVE action preceding PNR) should show no PPP difference; a PNR preceded by a non-teammate action should show none either. A material difference on the placebo would indicate label or confounding artifact.",
  "multiplicity": "Single pre-registered primary contrast (DRIVE-then-PNR vs. no DRIVE); any other play-type pairs are exploratory and corrected for multiple comparisons.",
  "decision_rule": "Conclude the effect is supported only if the adjusted PPP difference is positive, its interval excludes zero, the placebo sequences show no difference, and label-validation agreement meets a threshold fixed before analysis. Otherwise report uncertain or artifact; do not report a rejection without adequate power.",
  "data_version": "Regular seasons 2022-23, 2023-24 and 2024-25 (complete). 2025-26 regular season excluded until complete (from 2026-04-13); 2025-26 playoffs excluded until complete (from 2026-06-21). Label version and backfill status must be recorded and fixed before analysis."
 }
}
```

## RT-012 O seed 1

File: `runs\study1b_smoke_v1\raw\study1b_smoke_v1_openrouter_anthropic_claude-haiku-5.5_RT-012_O_s1.json`

```json
{
 "research_concepts": [
  "teammate DRIVE preceding a pick-and-roll (PNR)",
  "pick-and-roll possession points (PPP)",
  "play-type sequencing and downstream efficiency",
  "derived play-type labels from play-by-play (initiation_type, proxy calibration)",
  "foul-ending leakage into possession points"
 ],
 "methodological_questions": [
  "Are PNR and DRIVE labels valid enough that a sequencing effect on PPP can be measured?",
  "Does a prior teammate DRIVE raise PNR PPP after adjusting for shot quality, matchups and possession context?",
  "Do foul endings or outcome-derived labels mechanically inflate PPP differences between play types?",
  "What sample and label-validation standard is needed before a sequencing test is meaningful?"
 ],
 "historical_evidence": [
  {
   "id": "FAM:SF-APPA-030",
   "status_as_recorded": "inconclusive",
   "finding": "Play-type label backfill verification on 921,514 possessions. PNR share 28.7% failed its 20-28% band; PULL_UP 7.9% failed; 3100 games with team PNR above 33% failed; PNR PPP 0.948 passed; temporal check passed; team identity failed. 2024-25 PULL_UP was roughly 0-1% for many teams. 82.8% of PNR labels were proxy_calibrated. Final result recorded as FAIL."
  },
  {
   "id": "FAM:SF-CHT-025",
   "status_as_recorded": "artifact",
   "finding": "Play-type labeling audit found OTHER possessions ending in fouls about 36% of the time, with inflated PPP (FOUL_BUCKET). DRIVE was 12 percentage points below the foul benchmark (FOUL_LEAK). PNR showed a 22% foul rate. Only 335 of 50,668 possessions (0.7%) mapped to a real play type via initiation_type. Verdict: artifact_found."
  },
  {
   "id": "FAM:SF-APPA-005",
   "status_as_recorded": "untestable",
   "finding": "Defensive scheme change analysis using inferred labels, 523 within-game cells and 440 cross-game pairs. Within-game change was 61.0% and cross-game change 67.7%; 99% of units changed. Transition matrices were near-uniform. The record states the inferred label cannot separate real defensive adjustment from offense executing differently."
  },
  {
   "id": "FAM:SF-APPS-058",
   "status_as_recorded": "untestable",
   "finding": "On-ball defensive coverage labels (DROP/ICE/SWITCH) on ORL-DET G1. Confident labels covered 10 of 67 DET possessions (14.9%) and 2 of 60 ORL possessions (3.3%). switches_on was not populated by the NBA matchups feed. Verdict recorded as failed_gate."
  }
 ],
 "failed_approaches": [
  {
   "id": "FAM:SF-APPA-030",
   "what_failed": "Using backfilled, largely proxy-calibrated play-type labels as the basis for play-type and PPP analysis",
   "why": "Band checks on PNR and PULL_UP shares failed, team identity failed, and most PNR labels were proxy-calibrated (82.8%). The record's auto mechanism is C_artifact with LABEL_ERROR. Only the PNR PPP level passed, and the overall verdict was FAIL."
  },
  {
   "id": "FAM:SF-CHT-025",
   "what_failed": "Comparing PPP across play types derived from initiation_type, without controlling for foul endings",
   "why": "OTHER PPP was inflated by foul endings (about 36%), DRIVE was 12 pp below the foul benchmark, and initiation_type mapped only 0.7% of possessions. The recorded mechanism is C_artifact."
  },
  {
   "id": "FAM:SF-APPS-058",
   "what_failed": "Inferring on-ball coverage type from NBA matchup and play-by-play fields",
   "why": "Confident label rates were 14.9% and 3.3%, and the switches_on field was not populated. The record is A_unanswerable with LABEL_ERROR and SAMPLE_SIZE_POWER."
  },
  {
   "id": "FAM:SF-APPA-005",
   "what_failed": "Inferred scheme labels used to detect defensive adjustment across units and games",
   "why": "The change rates were near-saturated and the transition matrices near-uniform, consistent with label noise. The record states the label cannot separate defensive adjustment from offense differences. The auto mechanism is A_unanswerable."
  }
 ],
 "evidence_establishes": [
  "No retrieved record tests the teammate DRIVE to PNR PPP hypothesis directly. The retrieved evidence is about labeling quality and does not estimate the effect.",
  "This project's play-type labels have failed validation in several ways. These include band and team-identity failures, a 0.7% initiation_type mapping rate, heavy proxy calibration of PNR labels, and foul-ending contamination of PPP.",
  "Foul endings systematically distort PPP across play-type buckets, which is a direct threat to any PPP comparison.",
  "Inferred on-ball labels were sparse in the one game examined, so label-based sequencing or coverage analyses were not feasible as built."
 ],
 "evidence_does_not_establish": [
  "The size or direction of any DRIVE-to-PNR PPP effect.",
  "Whether the PNR label is accurate enough at the individual-possession level, since the PNR PPP level passed one check (SF-APPA-030) but the labels were mostly proxy-calibrated.",
  "Whether the teammate DRIVE label itself is valid, because no retrieved record evaluates DRIVE labels beyond foul leakage.",
  "Whether the 2025-26 data, which is partial before 2026-04-13 and before 2026-06-21 for playoffs, behaves like earlier seasons.",
  "Anything about the related family FAM:SF-APPA-001 that is referenced in SF-APPA-030: it was not returned and is not described here."
 ],
 "own_inferences": [
  "The historical records concern label validity, not the sequencing hypothesis, so they block a test rather than answer the question.",
  "A valid test would need DRIVE and PNR labels that are not derived from the outcome (points or possession end), otherwise the estimate could be circular.",
  "Teammate actions before a PNR may be correlated with spacing, pace, and player quality. Without controls, a positive association could reflect those and not the sequencing itself.",
  "Rough scale: the mapped initiation_type sample (335 possessions in the audit) is far too small for a sequencing contrast, so exposure would have to come from a different labeling route."
 ],
 "uncertainties": [
  "The retrieval returned only four records, and the search may have missed relevant sequencing studies.",
  "The 82.8% proxy-calibration figure and the foul-leak estimate come from single-audit records with no recorded validation (no_validation_recorded).",
  "How the FAM:SF-APPA-030 PNR-PPP pass (0.948) was produced, and whether it can be trusted given the failed checks around it.",
  "Sample counts for teammate DRIVE to PNR pairs in the graph database are unknown.",
  "The data description does not say whether the graph's possession records are built independently of the PPP outcome."
 ],
 "historical_effect": {
  "changed_decision": "yes",
  "explanation": "Without the history, the question might have looked testable from the per-game play-by-play and the derived graph. The four records show that this project's play-type and coverage labels failed validation gates (SF-APPA-030 FAIL, SF-CHT-025 artifact_found, SF-APPS-058 failed_gate). Foul-ending contamination inflates PPP in the same family of labels. Together these establish that the sequencing estimate would not be interpretable without new label validation, which moved the decision to do_not_proceed as posed."
 },
 "testability": {
  "p_testable": 0.1,
  "blocking_constraints": [
   {
    "code": "LABEL_ERROR",
    "text": "Play-type labels failed validation (SF-APPA-030 FAIL, SF-CHT-025 artifact, SF-APPS-058 failed_gate); PNR labels are mostly proxy-calibrated and initiation_type maps only 0.7% of possessions."
   },
   {
    "code": "OUTCOME_DERIVED_LABEL",
    "text": "Labels and PPP may be derived from the same play-by-play outcome, so the association could be partly definitional."
   },
   {
    "code": "CONFOUNDING",
    "text": "Shot quality, matchups, spacing and possession context are not controlled in any retrieved design, and teammate actions are correlated with lineup and style."
   },
   {
    "code": "EXPOSURE_SPARSITY",
    "text": "Validated teammate-DRIVE-before-PNR pairs are not counted anywhere in the retrieved records; the mapped label sample is very small."
   }
  ]
 },
 "prior_work": {
  "already_answered": "no",
  "cited": [
   "FAM:SF-APPA-030",
   "FAM:SF-CHT-025",
   "FAM:SF-APPS-058",
   "FAM:SF-APPA-005"
  ],
  "summary": "No retrieved record estimates the effect of a teammate DRIVE before a PNR on PNR PPP. The cited records audit the labels and related defensive-scheme and coverage labels, and each either failed or was untestable. They are relevant because they show the label pipeline is not yet valid for this question."
 },
 "risks": [
  {
   "code": "LABEL_ERROR",
   "text": "PNR, DRIVE and other play-type labels are proxy-calibrated or mis-mapped; band and identity checks failed."
  },
  {
   "code": "OUTCOME_DERIVED_LABEL",
   "text": "Possession labels and points may come from the same play-by-play record, so the sequencing estimate could be circular."
  },
  {
   "code": "CONFOUNDING",
   "text": "Shot quality, matchup, lineup and pace differences can produce a PPP gap without any sequencing effect."
  },
  {
   "code": "MEASURE_RELIABILITY",
   "text": "No reliability check on DRIVE or PNR labels is recorded; the PNR PPP pass in SF-APPA-030 does not establish label accuracy."
  },
  {
   "code": "MECHANICAL_FLOOR",
   "text": "Foul endings and free-throw trips can mechanically raise PPP for some play types, as SF-CHT-025 shows, which could be mistaken for a sequencing effect."
  },
  {
   "code": "LEAKAGE_LOOKAHEAD",
   "text": "If the teammate-action window is defined using events at or after the PNR, the design would leak future information into the predictor."
  },
  {
   "code": "SAMPLE_SIZE_POWER",
   "text": "No power calculation exists; validated pairs are likely far fewer than needed for a PPP contrast."
  },
  {
   "code": "PLACEBO_DEPENDENCE",
   "text": "Without a placebo action, a positive result cannot be distinguished from a generic teammate-action or pace effect."
  },
  {
   "code": "DRIFT_NONSTATIONARITY",
   "text": "2025-26 data is partial before the cutoffs and label quality may shift across seasons."
  }
 ],
 "predicted_outcome": {
  "supported": 0.03,
  "rejected": 0.02,
  "untestable": 0.4,
  "artifact": 0.35,
  "uncertain": 0.2
 },
 "decision": "do_not_proceed",
 "design": {
  "estimand": "Within PNR possessions, the difference in PPP between those preceded by a teammate DRIVE within a defined window and those without, after adjustment. Fallback estimand, if labels fail: none; report label validity instead.",
  "unit": "Ball-handler PNR possession, using only pre-PNR events for the predictor.",
  "sample": "Stage 0 (required first): hand-check a stratified random sample of PNR and DRIVE labels against video or raw event sequences, drawn from 2022-23 to 2024-25 regular season and playoffs. Stage 1 (only if Stage 0 passes): the same seasons, with 2025-26 regular season used only after its completion on 2026-04-13 and playoffs only after 2026-06-21.",
  "power": "Not computed. Must be done with the validated label error rate and the number of eligible pairs before any run; the current records do not supply either number.",
  "controls": "Shot distance and quality, defender matchup, lineup and substitution state, score and clock context, pace, and foul-ending indicator. Predictor window restricted to events before the PNR initiation to avoid lookahead.",
  "falsification": "Placebo predictor: teammate non-DRIVE actions (e.g., catch-and-shoot) before PNR should show no PPP lift. Negative-control outcome: PPP on possessions with a foul ending should be analysed separately. Lookahead check: window must not include post-PNR events.",
  "multiplicity": "One pre-specified primary contrast. Placebo and control contrasts reported as secondary and not used for claims.",
  "decision_rule": "Proceed to the main test only if Stage 0 hand-check meets pre-specified label-accuracy thresholds for PNR and DRIVE, foul-ending and PPP leakage are handled, and the expected power is adequate. Otherwise report the question as untestable with current labels.",
  "data_version": "NBA stats API per-game play-by-play, substitution intervals and matchup files for 2022-23 to 2024-25 (regular and playoffs); 2025-26 regular season only after 2026-04-13 completion and playoffs only after 2026-06-21. Graph-derived play-type records not used as the primary label source until validated."
 }
}
```

## RT-147 OS seed 1

File: `runs\study1b_smoke_v1\raw\study1b_smoke_v1_openrouter_anthropic_claude-haiku-5.5_RT-147_OS_s1.json`

```json
{
 "research_concepts": [
  "opponent next-possession points per possession (PPP) after a play type X",
  "AVOID label thresholds for play types",
  "own-sequence lagged effects on possession outcomes",
  "play-type labeling from play-by-play data",
  "defensive aftershock after opponent success",
  "initiation_type mapping of play-type possessions"
 ],
 "methodological_questions": [
  "Can opponent next-possession PPP after play X be estimated reliably enough to drive AVOID labels?",
  "Is the play-type labeling valid enough that PPP differences between play types reflect efficiency rather than labeling or foul artifacts?",
  "Do own-sequence lagged effects survive controls for selection, base rates and regression to the mean?",
  "What sample sizes and exposure counts are needed for play-type-level PPP estimates, especially for small team-level cells?",
  "Does the opponent aftershock reflect play-type-specific disruption or a generic dead-ball/score effect?"
 ],
 "historical_evidence": [
  {
   "id": "FAM:SF07",
   "status_as_recorded": "supported",
   "finding": "Family-level record (auto_outcome_status supported; auto_members_disagree yes; adjudicated by automated rule-based R1 rule, not human review). Member APPA-049 (verdict supported) reports the defensive aftershock replicating for 8/8 play types in all games and playoffs (e.g., CUT +0.119 n=21,398; PO +0.131 n=1,145; TRANSITION +0.135 n=26,262), on 458,604 opponent possessions, with the sequential pair premium as Y PPP after X minus Y's H2 baseline. APPA-049 notes team-level 1-2 punch cells with tiny n (BKN n=16, CHI n=18) marked significant at |t|>=2.0. Member APPS-037 (verdict descriptive) reports all-games aftershock by play type (e.g., DRIVE +0.123 n=57,621; PNR +0.127; TRANSITION +0.135), with opponent-next baseline 1.206 and own-next baseline 0.975; it treats own-next A1 as exploratory (~4% of pairs). APPS-037 notes the aftershock is uniformly positive across play types and may be a generic dead-ball/score effect rather than play-type-specific. APPS-037 also notes that the sign convention is opposite to a 52-series net-swing table. Limit recorded: LIM:small_sample (level unclear)."
  },
  {
   "id": "FAM:SF-CHT-025",
   "status_as_recorded": "artifact",
   "finding": "Play-type labeling audit (verdict artifact_found; no_validation_recorded). OTHER possessions: 36% end in fouls, inflating OTHER PPP. DRIVE sits 12 points below the foul benchmark (FOUL_LEAK). PNR shows a 22% foul rate. initiation_type maps only 335 of 50,668 possessions (0.7%) to a real play type. The record's scope states it applies to analyses whose result depends on PPP differences between play types (OTHER and DRIVE most directly) or on initiation_type, and that it does not record label error for other categories or the bias in any downstream estimate."
  }
 ],
 "failed_approaches": [
  {
   "id": "FAM:SF-CHT-025",
   "what_failed": "Treating play-type PPP differences, especially OTHER and DRIVE versus other types, and initiation_type-based labels, as real efficiency differences.",
   "why": "Recorded failure type C_artifact: foul endings inflate OTHER PPP (36% of OTHER possessions end in fouls), DRIVE PPP sits 12 points below the foul benchmark, PNR has a 22% foul rate, and initiation_type covers only 0.7% of possessions. Labelling flaw, not validated (no_validation_recorded)."
  },
  {
   "id": "FAM:SF07",
   "what_failed": "Interpreting the defensive aftershock as play-type-specific disruption.",
   "why": "Recorded as uniformly positive across all 8 play types (opponent next PPP ~1.07-1.09 vs baseline 1.206); APPS-037 notes it may be a generic dead-ball/score effect. The record's failure mechanism is D_positive (no failure), and the auto_limited_by tag is LIM:small_sample, so this specificity concern is open in the record. Auto-validation is same_pipeline_validation only. Team-level cells include tiny n (e.g., n=16, n=18)."
  }
 ],
 "evidence_establishes": [
  "Across 458,604 opponent possessions in the recorded pipeline, opponent next-possession PPP after each of 8 play types is below the 1.206 opponent baseline, and this pattern is recorded as replicating in the playoffs (APPA-049, APPS-037).",
  "Sequential pair premiums are reported as positive for several pairs (e.g., PUTBACK->TRANSITION +0.084 n=565; CUT->PULL_UP +0.065 n=2,620), but these are descriptive records in one pipeline.",
  "The play-type labels used in at least some earlier analyses have a documented foul-leakage problem that biases OTHER and DRIVE PPP and PNR interpretation, and initiation_type coverage is very low (SF-CHT-025).",
  "Own-next (own-sequence) baseline PPP of 0.975 (n=18,943) is recorded in APPS-037, and own-next A1 is flagged as exploratory (~4% of pairs)."
 ],
 "evidence_does_not_establish": [
  "That the aftershock is specific to each play type X rather than a generic post-score or dead-ball effect; no record isolates it from score state, possession context, or time-of-game.",
  "That opponent next-PPP differences are large enough, or stable enough, to drive AVOID labels; no AVOID threshold, decision rule, or label-stability test is recorded.",
  "That own-sequence lagged effects survive controls for selection, base rates, or regression to the mean; the only own-sequence evidence is an exploratory A1 result on ~4% of pairs.",
  "That play-type PPP differences are free of labeling artifacts after the foul leakage fix; SF-CHT-025 records the artifact but not a corrected estimate or bias magnitude.",
  "Any estimate for small team-level cells, since sample sizes (e.g., n=16, n=18) are too small for reliable inference and no power analysis is recorded.",
  "Whether the recorded sign conventions across APPS-037 and the 52-series net-swing table are consistent; the record notes they are opposite."
 ],
 "own_inferences": [
  "The question as posed bundles three claims (opponent next-PPP drives AVOID labels, play-type specificity, and own-sequence lag effects). Each needs a separate test; the historical records address only the first and the labeling input to it.",
  "Because the aftershock is uniformly positive across all 8 play types, a play-type-specific AVOID label would require a contrast between play types, not a comparison to a common baseline. Such a contrast is not established by the records.",
  "The foul-leakage artifact in OTHER and DRIVE directly contaminates any PPP-difference-based AVOID rule that uses those categories, so labels must be re-audited before any AVOID label is assigned.",
  "The historical records do not show whether the AVOID threshold itself was pre-specified, so any threshold chosen after seeing these PPP values would be subject to multiplicity and selection risk."
 ],
 "uncertainties": [
  "Full text of APPA-049 and APPS-037 was not read in full; the retrieved summaries are the recorded findings, and the APPA-049 entry was truncated in the first retrieval.",
  "auto_members_disagree is yes for SF07, and the adjudication was automated rule-based rather than human, so the supported status may not reflect independent validation.",
  "The 2025-26 playoff data is partial until 2026-06-21 and the regular season is complete only from 2026-04-13; the records do not state which season data versions they used.",
  "No record quantifies the foul-leakage bias on opponent next-PPP itself, so the magnitude of artifact in the aftershock estimates is unknown.",
  "The auto_related_family links (SF-APPA-050, SF-APPS-049, SF40) were not retrieved, so their findings are unknown."
 ],
 "historical_effect": {
  "changed_decision": "yes",
  "explanation": "The retrieved records show that the opponent aftershock is uniformly positive and possibly generic (SF07), and that the play-type labels used for PPP comparisons contain a documented foul-leakage artifact with very low initiation_type coverage (SF-CHT-025). Together these mean the question as posed cannot be answered by directly using play-type PPP differences to drive AVOID labels. The decision moves from a direct test to proceed_with_changes: first audit and correct the labels, then test specificity against score/context controls, and treat own-sequence effects as a separate exploratory question."
 },
 "testability": {
  "p_testable": 0.45,
  "blocking_constraints": [
   {
    "code": "LABEL_ERROR",
    "text": "Play-type labels have documented foul leakage (OTHER 36% foul endings, DRIVE 12pp below foul benchmark, PNR 22% foul rate) and initiation_type maps only 0.7% of possessions, so PPP differences between types are not yet valid efficiency measures."
   },
   {
    "code": "CONFOUNDING",
    "text": "The uniform positive aftershock across all 8 play types may reflect a generic score or dead-ball effect; it is not separated from play-type-specific disruption."
   },
   {
    "code": "SAMPLE_SIZE_POWER",
    "text": "Team-level and own-next cells are small (e.g., n=16, n=18; own-next ~4% of pairs), so AVOID thresholds at team level lack power without pooling."
   },
   {
    "code": "OUTCOME_DERIVED_LABEL",
    "text": "Play-type labels are derived from the same play-by-play outcomes (points, fouls) used as the PPP outcome, creating circularity in PPP differences between types."
   }
  ]
 },
 "prior_work": {
  "already_answered": "partly",
  "cited": [
   "FAM:SF07",
   "FAM:SF-CHT-025"
  ],
  "summary": "SF07 records a supported, replicated aftershock and positive sequential pair premiums across all 8 play types in all games and playoffs, but its own notes flag a possible generic dead-ball/score effect and tiny team-level cells, and its adjudication was automated with members disagreeing. SF-CHT-025 records an artifact: foul leakage inflates OTHER PPP and depresses DRIVE PPP, and initiation_type coverage is 0.7%. Neither record answers whether opponent next-PPP is large enough, and specific to play type, to drive AVOID labels, nor whether own-sequence lag effects survive proper controls."
 },
 "risks": [
  {
   "code": "LABEL_ERROR",
   "text": "Foul-ending possessions are mislabelled as play-type efficiency (OTHER 36%, DRIVE 12pp below benchmark, PNR 22%); initiation_type covers 0.7% of possessions."
  },
  {
   "code": "OUTCOME_DERIVED_LABEL",
   "text": "Play-type labels and the PPP outcome come from the same play-by-play events, so PPP differences between types can be partly mechanical."
  },
  {
   "code": "CONFOUNDING",
   "text": "The aftershock may reflect score state, dead-ball timing, or garbage time rather than play-type disruption; no control for score margin, clock, or period is recorded."
  },
  {
   "code": "SAMPLE_SIZE_POWER",
   "text": "Team-level and own-next cells are small (n=16, n=18, ~4% of pairs); tiny-n cells marked significant at |t|>=2.0 are at risk of false positives."
  },
  {
   "code": "MULTIPLE_TESTING",
   "text": "Eight play types, pairwise sequences, team-level 1-2 punch tables, and multiple playoff/regular-season splits are tested without a recorded correction."
  },
  {
   "code": "BASE_RATE",
   "text": "Opponent baseline PPP (1.206) and the aftershock contrast against it depend on the base rate of possessions; the own-next baseline (0.975) differs widely, so the reference group choice changes the estimate."
  },
  {
   "code": "RTM_SELECTION",
   "text": "Play types and sequences are chosen after observing high or low PPP; selecting on extreme values inflates premiums and aftershocks (e.g., top pair premiums are reported as selected maxima)."
  },
  {
   "code": "PLACEBO_DEPENDENCE",
   "text": "No placebo or random-label check is recorded for the aftershock or premium estimates, so the generic-effect explanation cannot be ruled out from the existing records."
  },
  {
   "code": "DRIFT_NONSTATIONARITY",
   "text": "Data spans 2022-23 to 2025-26, with 2025-26 regular season and playoffs partial at retrieval date; pooling across seasons without a stability check may mix pace and rule-change effects."
  },
  {
   "code": "IMPLEMENTATION_BUG",
   "text": "Sign convention is recorded as opposite between APPS-037 and the 52-series net-swing table, so the direction of effects may be misreported."
  }
 ],
 "predicted_outcome": {
  "supported": 0.2,
  "rejected": 0.15,
  "untestable": 0.1,
  "artifact": 0.3,
  "uncertain": 0.25
 },
 "decision": "proceed_with_changes",
 "design": {
  "estimand": "Difference in opponent next-possession PPP after the opponent runs play type X (versus a matched score/clock/period baseline), by play type, and whether this difference exceeds a pre-specified AVOID threshold; secondary estimand: own-sequence lag effect after the same controls, reported as exploratory.",
  "unit": "Opponent possession (the possession immediately after a play-type possession by the opposing team), with the originating possession as the conditioning event.",
  "sample": "NBA 2022-23 to 2024-25 regular seasons and playoffs as the primary sample (complete data); 2025-26 regular season only from 2026-04-13 onward and 2025-26 playoffs only from 2026-06-21 onward, or as a held-out check. Exclude possessions with no initiation_type mapping or with foul-ending labels until the label audit is complete.",
  "power": "Pre-register minimum cell size (e.g., n>=5,000 opponent possessions per play type and n>=500 per own-next cell) and report power for the smallest pre-specified AVOID effect; team-level tables are descriptive only unless pooled to reach that size.",
  "controls": "Score margin, clock, period, garbage-time flag, possession count in the game, opponent identity, and team pace; foul-ending possessions removed or recoded using the play-by-play foul events; play-type labels re-audited against the foul benchmark before use; regression to the mean handled by splitting the sample (estimate the play-type set on one half, test on the other).",
  "falsification": "Random-label or shuffled play-type placebo should produce no aftershock; if the aftershock is equal across all 8 types after score-state controls, the play-type-specific AVOID rule is rejected and the effect is treated as generic. Own-sequence lag must also be null on the placebo pairs.",
  "multiplicity": "Pre-register the 8 play types as the primary family with Holm or Benjamini-Hochberg correction; team-level and own-next results are exploratory and reported without inferential claims.",
  "decision_rule": "Support an AVOID label for play X only if (a) the foul-corrected opponent next-PPP reduction exceeds the pre-specified threshold with the lower confidence bound above it, (b) the effect survives score-state controls and the random-label placebo, and (c) it replicates in the held-out season or playoff split. Otherwise report as rejected, artifact, or uncertain; own-sequence effects are reported only as exploratory.",
  "data_version": "Play-by-play data as of 2026-06-19; 2025-26 regular season complete from 2026-04-13 and playoffs partial until 2026-06-21; record the exact data pull and the label-audit version used."
 }
}
```

## RT-147 O seed 1

File: `runs\study1b_smoke_v1\raw\study1b_smoke_v1_openrouter_anthropic_claude-haiku-5.5_RT-147_O_s1.json`

```json
{
 "research_concepts": [
  "opponent next-possession PPP after play type X",
  "AVOID label derivation from opponent next-possession outcome",
  "own-sequence lagged play-type effects",
  "play-type initiation labeling from play-by-play",
  "defensive aftershock / sequential pair premium"
 ],
 "methodological_questions": [
  "Is the opponent next-possession PPP deviation after play X large enough to drive AVOID labels, relative to a proper baseline?",
  "Does the aftershock reflect play-type-specific disruption or a generic dead-ball/score-state effect?",
  "Are play-type labels reliable enough (initiation_type coverage, foul-ending contamination) for outcome-conditioned labels?",
  "Do own-sequence lagged play types matter once base rates and score state are controlled?",
  "Does outcome-derived labeling introduce leakage or selection bias?"
 ],
 "historical_evidence": [
  {
   "id": "FAM:SF07",
   "status_as_recorded": "supported",
   "finding": "Records that after opponent play type X, the next offensive play type Y scores above Y's unconditional H2 baseline, and every play type shows a defensive aftershock; 8/8 play types replicate in all-games and playoffs (APPA-049, n=458,604 opponent possessions). Aftershock magnitudes listed in APPS-037 are roughly +0.119 to +0.135 PPP (opponent next PPP about 1.07-1.09 vs baseline 1.206). Own-next A1 is recorded as exploratory (about 4% of pairs). The record notes the uniform positive result may be a generic dead-ball/score effect rather than play-type-specific disruption, and flags tiny-n team cells marked significant (e.g. BKN n=16, CHI n=18). Auto-adjudication was rule-based, and the record notes members disagree on sign convention relative to a 52-series net-swing table."
  },
  {
   "id": "FAM:SF-CHT-025",
   "status_as_recorded": "artifact",
   "finding": "Play-type labeling audit found OTHER possessions end in fouls about 36% of the time with inflated PPP (FOUL_BUCKET); DRIVE sits 12pp below the foul benchmark (FOUL_LEAK); PNR shows a 22% foul rate; only 335 of 50,668 possessions (0.7%) map to a real play type via initiation_type. Verdict: artifact_found; validation not recorded."
  }
 ],
 "failed_approaches": [
  {
   "id": "FAM:SF-CHT-025",
   "what_failed": "Treating per-play-type PPP differences as real efficiency using initiation_type-based play-type labels",
   "why": "Recorded failure mechanism C_artifact: foul-ending possessions inflate OTHER PPP, DRIVE is depressed by foul leakage, and initiation_type maps only 0.7% of possessions to a real play type, so labels are largely unreliable."
  }
 ],
 "evidence_establishes": [
  "In the project's earlier sequential-pair analysis (FAM:SF07), opponent next-possession PPP after a play type is below the unconditional baseline in every play type examined, with a consistent magnitude (about 0.12-0.14 PPP) across all-games and playoff samples.",
  "The earlier aftershock result is reproducible within that pipeline, with large n for most play types.",
  "Play-type labels derived from initiation_type are a known reliability problem in this project's data: coverage is very low and foul endings contaminate PPP by play type."
 ],
 "evidence_does_not_establish": [
  "That the aftershock is specific to play type X rather than a generic dead-ball or score-state effect; the record itself raises this and no control for score state, time, or garbage time is recorded.",
  "That opponent next-PPP deviations are large enough to drive AVOID labels; no AVOID-label threshold, decision rule, or label-to-outcome validation is recorded.",
  "Any causal reading of own-sequence lag effects: own-next is exploratory with about 4% of pairs and no recorded test of its magnitude.",
  "Out-of-sample or cross-season stability: the record uses 2026-05-31 analysis on pooled H2 data and does not report held-out validation (validation status is same_pipeline_validation).",
  "Whether the 0.7% initiation_type coverage problem has been fixed in the current data version."
 ],
 "own_inferences": [
  "Because the aftershock is positive for all play types, it cannot discriminate play X from other play types, which undercuts using it as a play-specific AVOID signal.",
  "An AVOID label defined by opponent next-PPP after X would be partly defined by the outcome it aims to explain, creating circularity and leakage risk unless labels are built from pre-outcome information only.",
  "Foul-ending contamination and the score-state dependence of opponent next-possession scoring mean raw PPP thresholds would likely flag play types for reasons unrelated to play design.",
  "Small per-team cells (tens of possessions) cannot support team-level AVOID labels without shrinkage."
 ],
 "uncertainties": [
  "The retrieval output truncated several records; the full text was read only for FAM:SF07, and FAM:SF-CHT-025 was used from the truncated retrieval excerpt.",
  "The sign convention conflicts across records (positive aftershock means opponent scores less in APPS-037, while a 52-series table shows the opposite net-swing sign), so the direction of the effect is ambiguous in the record.",
  "No AVOID-label definition, threshold, or downstream validation against outcomes was retrieved.",
  "Whether the 2025-26 regular season (partial before 2026-04-13) and playoffs (partial before 2026-06-21) are included in the historical records is unclear; the records are dated 2026-05-31, before the 2025-26 playoffs were complete.",
  "Statistical power of the own-sequence lag effects and the actual foul-ending rate after the labelling fix are unknown."
 ],
 "historical_effect": {
  "changed_decision": "yes",
  "explanation": "The earlier positive aftershock result (SF07) might suggest a testable and already-supported effect, which could have favored proceeding. However, the labelling audit (SF-CHT-025) found that play-type labels are mostly unavailable (0.7% coverage) and foul-contaminated, and SF07 itself flags a possible generic score/dead-ball explanation and sign inconsistencies. Together these show the labels that an AVOID rule would depend on are not validated, and the effect may not be play-specific. That moves the decision from proceeding toward proceed_with_changes, with label validation and controls as preconditions rather than a straight test of the stated question."
 },
 "testability": {
  "p_testable": 0.35,
  "blocking_constraints": [
   {
    "code": "OUTCOME_DERIVED_LABEL",
    "text": "AVOID labels would be defined from opponent next-possession PPP, the same outcome they are meant to explain; labels must be built from information available before the outcome."
   },
   {
    "code": "LABEL_ERROR",
    "text": "initiation_type maps only 0.7% of possessions to a real play type and OTHER/PNR/DRIVE PPP are contaminated by foul endings (FAM:SF-CHT-025)."
   },
   {
    "code": "CONFOUNDING",
    "text": "The uniform positive aftershock across play types is consistent with a generic dead-ball or score-state effect (FAM:SF07 notes this), so play-type-specific effects are not identified without controls."
   },
   {
    "code": "SAMPLE_SIZE_POWER",
    "text": "Own-sequence lag (about 4% of pairs) and small team-level cells (BKN n=16, CHI n=18 marked significant) cannot support reliable AVOID labels."
   }
  ]
 },
 "prior_work": {
  "already_answered": "partly",
  "cited": [
   "FAM:SF07",
   "FAM:SF-CHT-025"
  ],
  "summary": "The earlier sequential-pair work (FAM:SF07, supported) found an opponent next-PPP aftershock after every play type examined, replicated in playoffs, but flagged that it may reflect a generic dead-ball or score effect, and that own-next effects are exploratory. The labelling audit (FAM:SF-CHT-025, artifact) found play-type labels from initiation_type largely absent and foul-contaminated. Neither record answers whether opponent next-PPP after X specifically drives AVOID labels, nor whether own-sequence lags matter after controls."
 },
 "risks": [
  {
   "code": "OUTCOME_DERIVED_LABEL",
   "text": "Defining AVOID from the outcome (opponent next PPP) is circular; the label and the target are the same quantity."
  },
  {
   "code": "LABEL_ERROR",
   "text": "Play-type coverage is 0.7% via initiation_type; foul endings inflate OTHER PPP and depress DRIVE PPP."
  },
  {
   "code": "LEAKAGE_LOOKAHEAD",
   "text": "Any label or baseline computed using the full season or playoff sample includes future possessions relative to the decision point."
  },
  {
   "code": "CONFOUNDING",
   "text": "Score state, garbage time, dead-ball and substitution effects can produce a uniform opponent-next PPP drop unrelated to play type X."
  },
  {
   "code": "BASE_RATE",
   "text": "Opponent next PPP baseline (1.206) and the play-type-specific baselines drive the aftershock magnitude; small changes in baseline choice shift results."
  },
  {
   "code": "SAMPLE_SIZE_POWER",
   "text": "Own-sequence lag cells are small (about 4% of pairs) and some team-level cells have n of 16-18."
  },
  {
   "code": "MULTIPLE_TESTING",
   "text": "Testing 8 play types across two samples and many team cells, with |t|>=2.0 flags, inflates false positives."
  },
  {
   "code": "PLACEBO_DEPENDENCE",
   "text": "No placebo or non-play-type baseline (e.g. random non-X possession) is recorded to show the aftershock is specific to X."
  },
  {
   "code": "MEASURE_RELIABILITY",
   "text": "Sign convention and net-swing tables disagree across records, so the direction of the effect is not reliably measured."
  },
  {
   "code": "DRIFT_NONSTATIONARITY",
   "text": "Records are pooled across seasons; the 2025-26 partial/complete timing and rule or pace changes may shift baselines."
  }
 ],
 "predicted_outcome": {
  "supported": 0.25,
  "rejected": 0.15,
  "untestable": 0.2,
  "artifact": 0.25,
  "uncertain": 0.15
 },
 "decision": "proceed_with_changes",
 "design": {
  "estimand": "Difference in opponent next-possession PPP after opponent play type X versus a matched non-X baseline, conditional on score state, period, and time remaining; and the own-sequence lag effect from the prior own possession, with AVOID defined only from pre-outcome information.",
  "unit": "Opponent possession pair (play X by the offense, next opponent possession), with own-sequence pairs as a secondary unit.",
  "sample": "NBA 2022-23 to 2024-25 regular seasons and playoffs, plus 2025-26 regular season restricted to games completed by 2026-04-13 and playoffs restricted to games completed by 2026-06-21. Exclude possessions with unresolved play-type labels. Do not use partial-season files.",
  "power": "Pre-specify minimum n per play type (for example n>=5,000 for the primary test) and a minimum detectable effect; report power for the own-sequence lag separately, acknowledging about 4% of pairs.",
  "controls": "Score differential, period, time remaining, garbage-time exclusion, lineup/substitution indicators, and a placebo set of random non-X possessions; baselines computed on training seasons only, not on the evaluation season.",
  "falsification": "Placebo play labels (shuffled initiation types) and a non-play-type baseline should show no aftershock; if the aftershock appears equally after non-X possessions, the play-type claim is rejected.",
  "multiplicity": "Bonferroni or Holm correction across play types and team-level cells; team cells reported only as descriptive with shrinkage.",
  "decision_rule": "Supported only if the play-specific aftershock exceeds the matched non-X placebo at the pre-registered threshold in a held-out season and survives label-error sensitivity checks; AVOID labels may be built only from pre-outcome information. Otherwise report as rejected, artifact, or uncertain.",
  "data_version": "Per-game NBA stats API play-by-play files and Neo4j initiation records as of the 2026-06-19 snapshot; regular seasons 2022-23 to 2025-26 and playoffs 2022-23 to 2025-26 with completion dates as stated; the pre-registered labelling fix must be recorded as a separate version."
 }
}
```
