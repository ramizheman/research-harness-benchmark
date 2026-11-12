# Data quality and classification audit

This audit covers the research-history inventory built in this folder: what was counted, how the counts reconcile, where the classifications are unreliable, and which sources are missing. Every number below is produced by the scripts in `scripts\` and can be regenerated; the generated tables are in `audit\`.

Labels used throughout:
- **Fact:** read directly from a record or a source file, or computed from them.
- **Interpretation:** a judgment about what the facts mean.
- **Proposed check:** work that has not been done.

## 1. Counting levels

| level | count | how it was obtained |
|---|---|---|
| Extraction lines in `Research Ledger\raw\*.jsonl` | 448 | 11 slice files written by 12 extraction passes |
| Unique record ids | 445 | 3 ids (APPA-009, APPA-031, APPA-037) were rewritten under the same id with more sources; the newer copy is kept |
| Records not replaced by a newer id | 440 | 5 records were replaced by records with new ids (APPM-024, 037, 038, 040, 041) |
| Merged records | 384 | `scripts\00_merge_ledger.py`: automatic merge of 56 duplicates by shared source file plus title overlap, or high title overlap, plus 17 manually confirmed pairs (`memory\merge_log.tsv`) |
| **Study families (unique designs)** | **319** | `audit\study_family_review.csv`: 40 manually reviewed families covering 105 merged records, each with the shared numbers that identify it |

**Fact.** The earlier `Research Ledger\ledger.jsonl` (381 records) dropped 8 records. When a record's `supersedes` field equalled its own id, the old merge script removed both copies. That file was not overwritten. Everything in this folder uses `memory\ledger_merged.jsonl` instead.

**Fact.** 319 is the best available count of unique experiment designs, not an exact one.
- **How the 40 families were found:** pairs of records whose results share distinctive numbers (`scripts\aux_number_duplicates.py`, 110 candidate pairs in `audit\duplicate_candidates_raw.tsv`), plus pairs seen while reading `audit\status_lists.md`.
- **Why more duplicates probably remain:** duplicates reported with rounded or different numbers, or described in different words, can still be in the inventory.
- **Proposed check:** a second reviewer reads the 384 merged records grouped by topic and confirms or splits the families.

**Definitions used for "design" and "run":**
- **Design (study family):** one hypothesis tested on one data source with one analysis plan.
- **Repeats inside one family:** robustness reruns (caliper sweeps, outlier filters), expanding-sample reruns, and the same result recorded by more than one extraction pass.
- **Bundles:** records that combine several prespecified tests (TMP-035 and TMP-036) are kept as families. The component tests that have their own records stay separate, so a few results are represented twice (see SF25 and SF26).

## 2. Runs

| quantity | value |
|---|---|
| Sum of `n_runs` as extracted over the 384 merged records | 1,578 |
| After correcting three resampling counts | 681 |
| Lower bound at study-family level (largest `n_runs` within each family) | 612 |
| Interim figure in the task brief | about 391, over 203 raw records |

**Corrections (fact).** Three records recorded resamples as runs:

| id | as extracted | used | reason |
|---|---|---|---|
| PAP-033 | 500 | 1 | split-half resamples |
| PAP-070 | 200 | 1 | shuffle placebo draws |
| PAP-083 | 200 | 1 | placebo permutations |

**Interpretation.** The per-record `n_runs` counts executions of one design on different games, series, teams, seasons or model versions, as judged by the extraction passes. These runs are not independent experiments. They share data, code and often the same hypothesis. The 612 to 681 range is a count of executions, not of evidence units. Large values need case-by-case reading:
- **APPM-046 (62):** generated matchup reports with no outcome evaluation.
- **APPS-056 (45):** series backtests.
- **PAP-087 (19):** sequential NCAA feature additions evaluated on the same folds, which carries selection risk.
- **APPS-002 (16):** agent pipeline runs.

The interim figures were 203 records, about 391 runs and 98 failures. They were reported while three extraction passes were still running and before any deduplication, so they are superseded by the counts above.

## 3. Reconciling result classifications and failure mechanisms

Two fields describe each record. `verdict` is the outcome of the test. `failure_type` is the mechanism behind a failure or a success:
- **A_unanswerable:** the data could not support the test.
- **B_powered_null:** an adequate test found no effect.
- **C_artifact:** the apparent result came from leakage, a confound, a bug or selection.
- **D_positive:** the result survived.
- **E_unclear:** the mechanism cannot be determined from the evidence.

The two fields overlap by construction and are not mutually exclusive. The crosstab below is at study-family level; the record-level version is in `audit\family_crosstabs.md`.

| verdict | A | B | C | D | E | families |
|---|---|---|---|---|---|---|
| null | 22 | 62 | 9 | 0 | 14 | 107 |
| artifact_found | 0 | 0 | 29 | 0 | 0 | 29 |
| failed_gate | 7 | 6 | 7 | 0 | 1 | 21 |
| abandoned | 5 | 0 | 0 | 0 | 5 | 10 |
| reversed | 0 | 5 | 0 | 0 | 1 | 6 |
| tool_eval_fail | 1 | 1 | 2 | 0 | 0 | 4 |
| **failed subtotal** | **35** | **74** | **47** | **0** | **21** | **177** |
| supported | 0 | 0 | 1 | 55 | 3 | 59 |
| inconclusive | 18 | 0 | 2 | 0 | 14 | 34 |
| descriptive | 4 | 0 | 0 | 3 | 34 | 41 |
| tool_eval_pass | 1 | 0 | 0 | 6 | 1 | 8 |
| **total** | **58** | **74** | **50** | **64** | **73** | **319** |

**Reconciliation (fact).**
- **Failed families:** 177 study families have a failed verdict (null, artifact_found, failed_gate, abandoned, reversed or tool_eval_fail). Within the failures the mechanisms sum exactly: 35 + 74 + 47 + 21 = 177.
- **Totals beyond the failures:** the mechanism totals (58 A, 74 B, 50 C) exceed their failed-only counts because 23 inconclusive, descriptive or tool-evaluation families also carry A, and 3 supported or inconclusive families carry C.
- **Brief vs current counts:** the brief's mechanism counts (40 A, 37 B, 26 C, summing to 103 against 98 failures) did not reconcile for the same reason. They were counted over all 203 interim records, not over the 98 failures.
- **Verdict artifact_found vs mechanism C:** the 29 artifact verdicts and the 50 C mechanisms are different counts. 21 families with a null, failed-gate, inconclusive, tool-failure or supported verdict were also judged to involve an artifact.

At record level (384 merged records) the same table gives:
- **Failed verdicts:** 199 records.
- **Failure types:** A 63, B 83, C 60, D 96, E 82.

## 4. Reliability of the classifications

### 4.1 Same study, different verdicts

**Fact.** In 20 of the 40 multi-record study families, the records give different verdicts for the same study. Examples:

| family | records and verdicts |
|---|---|
| SF20, 23-case absence validation | APPA-006 supported, APPA-007 failed_gate, APPS-081 inconclusive, CHT-051 failed_gate, PAP-023 null |
| SF23, mechanical floor | PAP-048 supported, TMP-028 artifact_found |
| SF24, restoration placebo | PAP-052 artifact_found, TMP-033 supported |
| SF27, linear vs kernel baseline | CHT-004 supported, PAP-097 null |
| SF13, within-game adapter lift | APPA-003 and CHT-018 artifact_found, APPM-013 supported |
| SF35, next-game luck carryover | CHT-070 failed_gate, TMP-011 artifact_found |

**Interpretation.** These conflicts have three causes:
1. **One record bundles several tests.** SF20 has a V1 that passed and a V2 that failed. A single verdict cannot describe both.
2. **The verdict depends on how the hypothesis is framed.** PAP-048 frames the mechanical floor as a supported finding ("L_pre tracks deletion"). TMP-028 frames the same numbers as an artifact of the displacement measure.
3. **Records were written at different stages.** APPM-013 records the first run, before the regression-to-the-mean falsification recorded in CHT-018.

The family representative (the paper record if there is one, then TMP, then the app slices, then chats) does not always carry the final verdict. A per-test verdict with an explicit hypothesis statement is needed before these labels can serve as an answer key.

### 4.2 Verdict and mechanism inconsistencies

**Fact.** 38 merged records have a verdict and failure type that disagree (listed in `audit\summaries.md`):

| combination | records |
|---|---|
| C_artifact with verdict null | 11 |
| C_artifact with verdict failed_gate | 9 |
| C_artifact with verdict inconclusive | 3 |
| C_artifact with verdict tool_eval_fail | 2 |
| C_artifact with verdict supported (APPA-063) | 1 |
| supported with E_unclear (APPA-031, APPA-054, PAP-028) | 3 |
| descriptive with D_positive | 5 |
| descriptive with A_unanswerable | 4 |

**Interpretation.** Most C-with-null cases record a positive result that turned out to be an artifact, followed by a null once it was corrected (for example CHT-030 and APPS-063). These cases are consistent, but they need two linked results rather than one label.

### 4.3 Unclear and unsupported mechanism labels

**Fact.**
- **Unclear mechanism:** 82 merged records (73 families) have failure_type E_unclear.
- **Powered nulls without power information:** 11 records labelled B_powered_null have no power information at all.
- **What "adequately rejected" requires:** the derived status (section 6) counts a record as adequately rejected when it is B_powered_null and has any non-empty `power_info`. That text is often only a sample size, not a power calculation or a minimum detectable effect.

**Interpretation.** The 62 families marked "adequately rejected (as specified)" are an upper bound on the nulls whose power was actually established.

### 4.4 Hindsight judgments

**Fact.**
- The `knowable_in_advance` field was filled by the extraction passes after the outcomes were known.
- **Untestable and artifact families:** the passes judged 53 of 58 untestable families and 34 of 50 artifact families knowable in advance.
- **Gaps:** 10 records have no value.

**Interpretation.** This is the field the benchmark most depends on: an agent with memory should flag these studies early. It is also the field most exposed to hindsight bias. It must be re-rated by reviewers who see only the pre-outcome information (`benchmark_design.md`, section 5.1).

### 4.5 Single extractor

**Fact.** Every record was written by one extraction pass. Some passes ran on a cheaper model (`cursor-grok-4.6-high-fast`) after the first round. No record was independently double-coded.

**Proposed check.** Two people independently code a random sample of at least 60 families for verdict and mechanism, and report Cohen's kappa. The labels should be used as benchmark ground truth only if kappa is at least 0.6 on both fields.

## 5. Number verification

**Fact.**
- **Coverage:** 356 merged records have decimal numbers in `primary_result`, 3,030 numbers in total.
- **Match rate:** 2,988 (98.6%) appear verbatim in the cited source files or, for records drawn from chats, in the condensed chat transcripts.
- **Records with no numbers to check:** 28 records have no decimals and 7 have no result.
- **Lowest match:** PAP-013, with 3 of 7 numbers found. Its source CSV stores unrounded values.

**Two problems fixed during the audit (fact):**
- **UTF-16 logs:** logs in `%TEMP%\supp_audit` written by PowerShell redirection are UTF-16. The first check read them as UTF-8 and found only 29 of 157 TMP numbers. They are now decoded correctly.
- **Renamed folder:** 22 records from chats cite `Documents\Basketball Strategy\`, which was later moved to `Documents\Basketball\App\Strategy\`. All 22 files exist at the new location. The inventory column `source_paths_resolved_after_folder_move` records each remap, and the cited path is left unchanged.

**Interpretation.** A verbatim match shows that a number exists in the source, not that the record attaches it to the right quantity. Chat-derived records were partly checked against the transcripts they were extracted from, which is a weaker check.

**Proposed check.** For a random sample of 40 records, a reviewer confirms that each number refers to the quantity the record says it does.

## 6. Derived epistemic status

The inventory adds `epistemic_status_derived`, computed by the rule `epistemic()` in `scripts\01_build_inventory_and_memory.py`. The rules are applied in order:

| status | rule | families |
|---|---|---|
| artifact | verdict artifact_found or mechanism C | 50 |
| cannot be tested with available data | mechanism A | 58 |
| adequately rejected (as specified) | null, failed_gate or reversed, with B and non-empty power_info | 62 |
| not tested adequately | null, failed_gate, reversed or abandoned otherwise, or B without power_info | 32 |
| genuinely uncertain | inconclusive, not A or C | 14 |
| supported | supported with D | 55 |
| no hypothesis test (descriptive) | descriptive, not A or C | 37 |
| tool evaluation | tool_eval_pass or tool_eval_fail, not A or C | 8 |
| ambiguous classification | anything else (APPA-031, APPA-054, PAP-028) | 3 |

**Interpretation.** "Not tested adequately" combines two groups: tests known to be inadequate, and nulls whose adequacy was never recorded. 27 of the 32 families have no reason recorded.

## 7. Fields marked NOT RECORDED

| inventory field | merged records with NOT RECORDED | reason |
|---|---|---|
| primary_outcome | 384 | The ledger schema has no primary-outcome field. The design and result text usually implies it, but naming it is a judgment. |
| what_was_learned, ruled_out_directions, viable_directions | 384 each | These are interpretive. They are the answer key for benchmark criteria 1 and 2, so they should be written by blinded human curators, not by the agent that built the inventory. |
| independently_replicated | 375 | No record states an independent replication. 9 records mention replication in some sense, marked "mentioned (see notes)". |
| sample_size_and_unit | 133 | Pulled by regex from the design and power text. Missing where the text gives no sample size. |
| experimental_method | 105 | Keyword rules matched nothing. |
| power_or_reliability_limitations | 56 | Empty `power_info`. |
| datasets_and_fields | 52 | Keyword rules matched nothing. Field-level detail (which columns) is not in the ledger. |
| failure_evidence | 15 | Empty in the record. |
| knowable_in_advance | 10 | Empty in the record. |
| primary_result | 7 | PAP-025, PAP-031, PAP-034, PAP-055, PAP-085, TMP-003, TMP-005 |

296 records say "none recorded" for confounds, leakage or implementation problems. That is the absence of a mention, not evidence that the study was clean.

## 8. Dates

**Fact.**

| date basis | records |
|---|---|
| file modification time | 205 |
| date in the document | 117 |
| chat transcript timestamp | 61 |
| none (PAP-025) | 1 |

**Interpretation.** Modification times on a synced OneDrive folder can postdate the work. They are not reliable enough to set the chronological memory cutoffs in the benchmark. Cutoffs should come from document dates, transcript timestamps or git history where available. Records dated only by modification time should be checked by hand before they are assigned to a "before" or "after" split.

## 9. Topic, dataset and method tags

**Fact.**
- **How tags are assigned:** topic, dataset, method, limitation and variable tags come from ordered keyword rules (`TOPIC_RULES` and the related lists in `scripts\01_build_inventory_and_memory.py`). The topic is the first rule that matches.
- **Unclassified:** 7 families have no topic.
- **Known misfits:** some engine-evaluation records are about suppression counters, and the "In-game and series adaptation" topic absorbs some playoff-series work.

**Interpretation.** The tags are fine for navigation and for the graph's grouping nodes. Topic-level counts are approximate. They are not suitable as benchmark labels without review.

## 10. Coverage of source material

`audit\coverage_check.md` lists each candidate source area, how many files it holds, and how many of those files any extraction record cites. An uncited file can still be covered if a record cites the summary write-up instead. Areas with low citation where the ledger text also shows no coverage:

| area | files | cited | what is missing |
|---|---|---|---|
| App top-level scripts | 635 | 67 | Script families with no matching record: `_knicks_*` (5, including a Dean Oliver analysis), `_connector_tier_ppp_*` (about 10 robustness variants), `run_proof_suite.py`, and the `clutch` family (8 scripts, 6 records) |
| App top-level logs | 14 | 1 | `_backtest_okc_phx_2526.log`, `_backtest_sas_por_2526.log`, shooter-coefficient runs |
| App `reports` | 41 | 0 | NYK vs SAS and SAS vs NYK context and pregame outputs (2026-06) |
| App `PREGAME_*` and `demo_reports` | 12 | 0 | Pregame predictions. Possibly scoreable against outcomes. |
| App `Chats` (exported chats 1 to 11) | 11 | 1 | Chats 1 to 5 and 7 to 11 |
| App `playsheet_validation` markdown | 219 | 51 | Per-team and per-play-type tables, clutch analyses |
| App `sequence_memory` outputs | 82 | 25 | EPV, channel 2 and distribution-shift tables |
| App `paper2_output` | 28 | 24 | `connector_positive_mechanism_report.md`, `hasconn_scoring_speed_report.md` |
| `Documents\March Madness` | 133 | 8 | Backtest and goto-conversion analyses beyond the 14 recorded families |
| `%TEMP%\supp_audit` subfolders | 1,909 | 11 | Mostly build logs. `historical_absence_extension` and `scout` are partly covered. |
| Downloads, basketball-related names | 79 | 2 | `adaptation_brief_LAL_HOU_2026_g1*.md` (5 copies) and `adaptation_presentation_8.29.26.pptx` |
| Published papers (PDFs) | n/a | n/a | The records cite the `.tex`, scripts and outputs rather than the PDFs. Covered through those. |

**Interpretation.**
- **Volume:** the missing material is mostly in the strategy app and its outputs, so the app-engine and suppression-counter topics are probably undercounted more than the paper projects.
- **Engineering scripts:** about 200 scripts (check, probe, debug, patch, fix and smoke prefixes) were skipped on purpose as engineering rather than experiments, following the ledger rule in `Research Ledger\SCHEMA.md`.
- **Where to look next:** the pregame reports and the 2026 backtest logs are the most useful gaps, because they contain predictions that could be scored against known outcomes.

## 11. Exclusions and constraints that affect use

- **2025-26 exclusion:** 2025-26 data was excluded from the lineup-adaptation analyses at the researcher's request. Other projects used 2025-26 data, and 23 records mention it. The benchmark must not treat those results as held-out (`benchmark_design.md`, section 4).
- **2026-27:** no record uses 2026-27 data.
- **Unchanged files:** no published paper, manuscript, source data, script or existing record was modified. All outputs are new files in this folder.

## 12. Readiness verdict for this layer

**Interpretation.** The inventory is ready to act as a document memory and a structured memory for a pilot, because the two conditions are built from the same records. It is not ready to provide ground-truth labels for scoring. Four steps come first:
1. Resolve the 20 within-family verdict conflicts.
2. Double-code a sample to measure agreement on verdict and mechanism.
3. Have reviewers blinded to outcomes re-rate `knowable_in_advance`.
4. Have human curators write the learned, ruled-out and viable fields.
