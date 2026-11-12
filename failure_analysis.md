# What the research history teaches

This document reads the 319 study families in `experiment_inventory.csv` for patterns that a research agent could use.

**How to read it:**
- **Labels.** Each statement is marked as a **fact** (from records, with ids) or an **interpretation** (a judgment that a reviewer may reject). Proposed tests appear only in `benchmark_design.md`.
- **Lists.** Complete lists by status and topic are in `audit\status_lists.md`. Family-level tables are in `audit\family_crosstabs.md`.

**Two cautions apply throughout:**
1. **The labels are not ground truth yet.** Verdicts and mechanisms were assigned by single extraction passes, and the same study received conflicting verdicts in 20 of 40 multi-record families (`data_quality_and_classification_audit.md`, section 4). Counts below are best estimates.
2. **A null is narrow.** A null result rejects one estimand, measured one way, in one population, at the power the test had. It does not show that related hypotheses are false. Each rejection below states its scope.

## 1. The five-way distinction

| class | families | operational rule | caveat |
|---|---|---|---|
| False as specified (adequately rejected) | 62 | null, failed gate or reversed, with mechanism B_powered_null and some power information | Upper bound: "power information" is often only a sample size |
| Untestable with available data | 58 | mechanism A_unanswerable | 53 of 58 judged knowable in advance, in hindsight |
| Not tested adequately | 32 | null, failed or abandoned without evidence of an adequate test | 27 of 32 have no recorded reason; mixes "known inadequate" with "adequacy never recorded" |
| Artifact | 50 | verdict artifact_found or mechanism C_artifact | Includes 21 families whose verdict is not artifact_found |
| Genuinely uncertain | 14 | inconclusive, mechanism not A or C | Small because most inconclusive results were judged untestable (18 families) |
| *Outside the five classes:* supported | 55 | supported with D_positive | None independently replicated (section 6) |
| *Outside the five classes:* descriptive, tool evaluation, ambiguous | 37, 8, 3 | no hypothesis test, software checks, conflicting labels | |

**Interpretation.**
- **Unusable for inference:** 108 families (58 untestable plus 50 artifacts, 34% of the history) failed for reasons other than the hypothesis being false. That is the share of effort a memory-equipped agent could in principle save or redirect.
- **Clean rejections:** only 62 families (19%) are candidate clean rejections, and that figure is an upper bound.

## 2. Repeated questions

**Fact.** The history asks a small number of questions many times. The largest clusters, grouped by reading the records:

| question cluster | families (examples) | pattern of results |
|---|---|---|
| Do teams adapt within or between games, and does adapting pay off? | about 35, e.g. SF02, SF05, SF12, SF13, SF14, PAP-042, APPS-025, APPS-027, APPS-030, APPS-049, APPM-019, APPM-054, CHT-020, CHT-039, CHT-072, TMP-014/015 (SF33), TMP-016, TMP-018, TMP-019 (SF39), PAP-078 to PAP-084 | Descriptive behavior holds up: offenses keep running suppressed plays in 93% of events (SF02, PAP-039), and own-team substitutions change shot mix (PAP-080). Every test of payoff from adapting, or of a stable team adaptation trait, is null, an artifact or untestable (SF13, CHT-072, CHT-064, TMP-016, APPS-027) |
| Do matchup-ranked BEST counters beat AVOID or continuing? | about 15, e.g. SF03, APPM-026, APPA-052, APPS-018, APPS-023, APPS-024, APPS-036, APPM-034, CHT-063 | The BEST minus AVOID gap is large and replicated across seasons (SF03: +0.375 PO, +0.422 RS). Tests of matchup specificity are null (APPS-023: non-CUT gap +0.010, p=0.17; APPM-034), and the gap is reproduced by a fixed league-wide ranking with no game information (CHT-063: +0.238 vs +0.248) |
| Does a pre-absence structural load predict reorganization when a player sits? | about 12, e.g. SF20, SF21, SF22, SF23, SF24, PAP-053, PAP-054, CHT-079 (SF26), PAP-058 | Displacement beyond sampling noise and its ranking by L_pre are supported in the 148-spell and 986-spell pools (SF21, SF22). The mechanical-floor check (SF23, PAP-048) attributes the ranking to deleting the player's own initiations (+0.432) rather than to teammate change beyond that (+0.082, CI [-0.104, +0.251]). Scouting forecasts from the same signal are null (SF26: 0.08% gap closure vs a 10% bar) |
| Does adding a model component improve the strategy engine? | about 25, e.g. APPA-011 to APPA-019, APPA-021, APPA-023, APPM-002, APPM-005 to APPM-009, SF11, CHT-006 | Mostly null or reversed. Several holdout R-squared values are negative (APPA-021: full-equilibrium R2 -0.1981; APPM-009: more training seasons worse on 5/5 metrics). Small gains for residual calibration (APPM-003) and starter-share features (APPM-006) |
| Is there possession-to-possession memory (sequences, aftershocks, gravity)? | about 15, e.g. APPS-059, APPS-060, APPS-067, APPS-069, APPS-073, APPS-074, APPS-079, CHT-029, CHT-037, SF07, SF15, SF30 | A small lag-1 signal (APPS-059: AUC +0.024; APPS-067: 3 of 64 cells). Larger apparent sequence premiums were artifacts (SF15: free-throw share 41.8% vs 9.9%; APPS-066 placebo) or null (SF30, APPS-074) |
| Do presence of structural roles (shapers, connectors, hubs) raise efficiency? | about 15, e.g. PAP-010 (SF29), PAP-011, SF28, CHT-058, APPS-086 to APPS-093 | Null on PPP throughout (PAP-010: +0.42 pts/100, CI [-1.15, +1.90], MDE80 2.19). Portability of the structural signature is supported (SF19) |
| NCAA tournament model additions | 14, PAP-086 to PAP-095, CHT-001 to CHT-003 | Sequential feature and architecture additions on the same folds, with Brier changes in the third or fourth decimal place |

**Interpretation.**
- **Adaptation cluster.** This is the clearest case of a question pursued past the point of diminishing returns: about 35 families asked whether teams adapt and whether it helps.
  - **What the evidence shows:** a stable picture. Behavior is persistent, the payoffs of adapting cannot be detected at available sample sizes, and team-level adaptation traits are unreliable (section 5).
  - **Benchmark implication:** an agent that proposes another variant should be scored as redundant unless it brings new data or a new measure. Following the task constraint, no further lineup-adaptation variants are proposed here.
- **Counter and absence clusters.** These show a different pattern: a robust positive followed by evidence that it may be a base-rate or mechanical effect (sections 4 and 6).

## 3. Data limitations that made questions untestable

**Fact.** The reason categories for the 58 untestable families (keyword rules, with several possible per family; `audit\family_crosstabs.md`):

| reason | families |
|---|---|
| sample or exposure too small | 37 |
| measure unreliable | 7 |
| power or MDE too large | 5 |
| label or classifier problem | 4 |
| confounded by team quality | 3 |
| other or no category matched | 9 or more |

The limits that recur, with the records that measured them:

| limitation | measured value | records |
|---|---|---|
| Five-on-five lineup matchup exposure | median 3 possessions per lineup pair; median lineup-game offensive possessions 4; single-possession PPP SD 1.147 | CHT-083, PAP-077 |
| Shot-mix difference-in-differences after lineup changes | MDE 3.2 to 3.6 percentage points | PAP-078 |
| Response repeatability across repeat meetings | MDE r = 0.36 with n = 63 | PAP-081 |
| Playoff series as the unit | 50 to 55 series; about 80 needed for p < 0.05 on the observed effect; talent confounds adaptation (talent p = 0.02, adaptation p = 0.28) | CHT-039, APPS-027 |
| Agent and LLM evaluations | 0 to 8 scoreable cases per test | APPA-026 (0 pairs), APPA-027 (3), APPA-028 (5), APPS-009 (0 scoreable) |
| Observed defensive scheme labels | 14.9% and 3.3% of on-ball possessions labelled; SWITCH feed empty | APPS-058, APPM-053 |
| Older seasons | 2020-22 rotation data about 15% retrievable | TMP-038 |
| Restoration measure | split-half 0.32 overall, 0.01 among 53 high-load spells (gate 0.40) | PAP-054 |

**Interpretation.**
- **The limits are general.** Possession-level outcomes are noisy (SD of about 1.15 points per possession). Lineup-pair, team-trait and series-level units do not accumulate enough possessions in a season to detect effects of the size these hypotheses imply.
- **They apply forward.** These constraints carry over to any future question that uses the same units. They are the most transferable knowledge in the history.
- **They were often visible in advance.** For most of the 58 families the limitation could be read from counts available before any outcome was examined (53 judged knowable in advance). That judgment needs blinded re-rating (`data_quality_and_classification_audit.md`, section 4.4).

## 4. Artifact-prone designs

**Fact.** The 50 artifact families fall into recurring mechanisms (the categories overlap):

| mechanism | records | example |
|---|---|---|
| Selection on early performance, then measuring later performance (regression to the mean) | SF13 (APPA-003, CHT-018), APPA-001, TMP-001, TMP-012, CHT-086 | The adapter PPP lift (+0.058) disappeared under the RTM falsification (CHT-018) |
| Outcome information leaking into labels or features | PAP-096, TMP-007, CHT-025, CHT-032, CHT-045, APPS-068 | The assisted flag existed only on made shots, giving SPOT_UP 2.83 PPP (PAP-096). 53.7% of labels were relabelled by an outcome-aware calibration (TMP-007). A leaky win gap of +11.5% became -2.7% ex ante (CHT-045) |
| Post-hoc calibration evaluated in sample | APPS-003, APPS-004, APPS-005, APPS-057 | Hit rate 51.7% before vs 96.2% after post-hoc calibration (APPS-004). The holdout protocol was specified but never scored (APPS-057) |
| Ranking small cells | SF31 (APPM-015, CHT-017), CHT-068, APPA-008 | Low-n "leaders" were role players at 3.00 PPP on 5 to 7 possessions (CHT-017) |
| Mechanical construction or shared noise | SF24 (PAP-052), SF23 (TMP-028), SF15, CHT-076 | A placebo sharing noise with the statistic (PAP-052); bonus FTA increase that is mechanical (CHT-076) |
| Implementation bugs | CHT-013, APPM-023, TMP-024 | The pipeline read `team_profiles` while the writer used `by_team` (CHT-013) |
| Unverified LLM analysis | APPA-008, CHT-086 | 706 findings with n < 5, a tool never called, an invented game score (APPA-008) |

**Fact.** Artifact rates by method tag (record level, `audit\tables.md`):
- ablation 0.29;
- LLM agent run 0.21;
- placebo or permutation 0.20;
- calibration scoring 0.20;
- matched control 0.18.

**Interpretation.**
- **Placebo and permutation designs** show high artifact rates because they are how artifacts get detected, not because they produce them.
- **Designs that need an extra check:** H1-to-H2 designs that select on first-half performance, labels inferred from possession outcomes, and calibration evaluated on the data it was fitted to. In this history these are the designs that most reliably produced false positives. Each needs a specific defensive check written into the design before results are seen.

## 5. Measures with poor and good reliability

**Fact.**

| measure | reliability | record |
|---|---|---|
| Team defensive second-half adjustment trait | r = -0.001 | CHT-064 |
| Team adaptation slope (usage vs first-half PPP) | odd-even r = -0.03; season-to-season -0.17, +0.25, +0.06 | CHT-072 |
| Team heterogeneity in halftime adaptation | split-half r = -0.026 | TMP-016 |
| Crunch-time identity, year over year | r = -0.023 | APPA-029 |
| Top suppressor per star, season to season | 2 of 30 stable | APPA-058 |
| Defensive PPP allowed by play type | Spearman-Brown 0.17 (PULL_UP) to 0.60 (DRIVE) | TMP-017 |
| Teammate restoration R | Spearman-Brown 0.32; 0.01 in high-load spells | PAP-054 |
| Connector teammate-path quality Q_p | Spearman-Brown 0.355 | APPS-085 |
| action_sequences pattern | CV 0.612, stability CV 0.919 | CHT-028 |
| *For contrast:* offensive play-type shares | Spearman-Brown 0.947 to 0.982 | TMP-017 |
| *For contrast:* team-season substitution timing | r = 0.59 | PAP-084 |
| *For contrast:* structural fingerprint persistence | P1a S = 0.352 [0.327, 0.378] | SF17 |
| *For contrast:* F1b split-half | rho = +0.670 | SF18 |

**Interpretation.**
- **The pattern:** in this data, what teams do (shares, timing, structure) is measured reliably, and how well it works (efficiency by play type, adaptation payoffs, team traits defined from efficiency) is not.
- **The consequence:** most failed hypotheses tried to relate a reliable behavior measure to an unreliable efficiency measure at a unit too small to average out the noise.

## 6. Surviving positives

**Fact.**
- **Count:** 55 families are supported with mechanism D (list in `audit\status_lists.md`).
- **Replication:** none is recorded as independently replicated by a different analyst or on independent data.
- **Validation types used:** several have out-of-sample checks within the same pipeline, such as two playoff seasons (APPM-026), a regular-season holdout (APPS-020) and leave-one-season-out folds (PAP-086).
- **Novelty:** not assessed against published sports research for any of them.

The main clusters and the later evidence that qualifies each:

| positive | records | later qualifying evidence | status |
|---|---|---|---|
| Suppression exceeds regression to the mean (published excess +0.408) | SF01 (PAP-036 to PAP-038), APPS-072 | TMP-012: a within-unit permutation null reproduces the excess (0.3798 vs 0.3744, z 0.40). TMP-001: null simulation expectation about 0.440 (from script text, no log). Both are dated October 2026, after APPS-072 (July 2026, memoryless simulation could not reproduce the excess) | **Contested.** Two null models disagree; the later audit is the more severe test but has no saved log for TMP-001 |
| Offenses continue suppressed plays, at a cost | SF02, SF05, PAP-040 | none recorded | Descriptive behavior, supported |
| BEST beats AVOID and continuing | SF03, APPM-026, APPA-036 | CHT-063 and APPS-023: the gap is reproduced by a fixed ranking dominated by CUT, and non-CUT matchup specificity is null | **Supported as a play-type base-rate gap; not supported as matchup intelligence** |
| Structural fingerprint persistence, fragility, portability | SF17, SF18, SF19, PAP-001, PAP-009, PAP-016 | none recorded; presence effects on PPP are null (section 2) | Supported as measurement properties |
| Absence displacement beyond noise; L_pre ranks it | SF21, SF22 | SF23: ranking accounted for by the mechanical floor | **Supported but largely mechanical** |
| Teammate restoration beyond placebo | PAP-053 (+0.173 [0.085, 0.262]), PAP-067 | SF24: an earlier placebo shared noise. PAP-054: the restoration measure failed its reliability gate | **Qualified** |
| Halftime minutes respond to opponent three-point luck | SF36 (opp3 0.131 to 0.134), PAP-068 | The next-game carryover is explained by the game-N role (SF35, CHT-070: +0.063 falls to +0.002 holding game-N role) | Supported for the within-game response |
| Own substitutions change shot mix; foul-trouble exploitation | PAP-080, TMP-022 | none recorded | Supported as benchmarks |
| Lag-1 possession memory | APPS-059, APPS-067 | Effect sizes small (AUC +0.024) | Supported, small |
| NCAA pipeline improvements | PAP-086, PAP-088 to PAP-090, PAP-094, PAP-095 | Gains in the third and fourth Brier decimal on the same folds used for selection | Supported in sample; selection risk |
| Engine calibration components | APPM-003, APPM-006, APPM-010, APPM-032, APPA-063 | APPA-063 also tagged C_artifact | Supported within the engine's own evaluation |

**Interpretation.**
- **Counter and absence clusters:** in both, the most replicated positives in the history may be measuring a base rate (CUT is the best play type) or a mechanical consequence of the measure (deleting a player's initiations changes the fingerprint).
- **Benchmark implication:** an agent that accepts these as substantive discoveries without checking those alternatives should score lower on validation risk.
- **Outside this benchmark:** whether these results are already known in the sports analytics literature has not been checked.

## 7. Failures that do and do not generalize

**Interpretation.** Not every failure carries reusable knowledge. Roughly three levels:

| level | examples | value to a future agent |
|---|---|---|
| Data-level constraints | exposure per lineup pair, efficiency-trait reliability, series counts, label leakage from outcomes, RTM in H1-to-H2 designs (sections 3 to 5) | High: they apply to any future question using the same data or design |
| Design-level lessons | post-hoc calibration evaluated in sample; ranking small cells; placebos that share noise with the statistic | Moderate: they apply to similar designs |
| Project-specific failures | engine variants A2 to A5 (APPA-011 to APPA-019), pipeline key mismatch (CHT-013), unpopulated template (APPA-068), individual NCAA feature additions (PAP-087, PAP-093) | Low: they show that one implementation choice did not help, and little beyond that |

**Fact.** Keyword rules found the following among the 50 artifact families:
- 3 implementation-bug families;
- at least 9 label-problem families;
- at least 4 selection or regression-to-the-mean families.

The project-specific engine-variant nulls form about 25 families (section 2).

## 8. Open items inside the history

**Fact.** Tests that were specified but never run or never scored, kept as recorded:

| record | what is open |
|---|---|
| APPS-057 | The SQ2 holdout protocol is specified. The 69.8% hit rate is in sample until the holdout is run. |
| PAP-085 and the Restoration Timing study | Timing of teammate restoration across 5-game bins: specified, deliberately not run |
| PAP-055 | Prespecified predictors of restoration, not evaluated after the reliability gate failed |
| PAP-031, PAP-034, PAP-025 | Abandoned or unrecorded analyses with no result |
| TMP-003, TMP-005 | Inconclusive designs with no result recorded |
| APPA-068 | Retrospective template never populated |

**Fact.** No record uses 2026-27 data. Topics with few families:

| topic | families |
|---|---|
| Shot selection and shot quality | 1 |
| Playing time and luck response | 3 |
| Possession sequences | 10 |
| In-game and series adaptation | 12 |

**Interpretation.**
- **Thin topics:** a small count marks where the history is thin, not where promising questions lie. Whether a thin area is worth pursuing depends on the published literature, which has not been reviewed here.
- **Following the task constraint:** no new hypotheses are proposed. The open items above are the only untested work the history itself defines.

## 9. Summary for the benchmark

| lesson | evidence | use in the benchmark |
|---|---|---|
| Questions at the lineup-pair, team-trait and series level are mostly untestable with one league's play-by-play data | sections 3 and 5 | early identification of unanswerable questions (criterion 1) |
| The adaptation question has been asked about 35 times with a stable answer | section 2 | redundancy avoidance (criterion 2) |
| Selection on H1 performance, outcome-derived labels, and in-sample calibration repeatedly produced false positives | section 4 | methodological risk detection (criterion 3) |
| The strongest positives have base-rate or mechanical alternatives that were found late | section 6 | survival under validation (criterion 6) |
| Labels conflict within 20 of 40 families | audit, section 4 | answer keys need adjudication before scoring |
