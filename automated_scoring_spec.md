# Automated scoring specification

Code: `bench\scoring.py`, `bench\stats.py`, `bench\claims.py`, `bench\redact.py`, `runner\experiment.py` (score and analyze phases). Tests: `tests\test_evaluation.py`.

All replay scores compare an agent's structured output with `benchmark_answer_key.jsonl`. The key is automated adjudication, so every score below measures agreement with provisional labels, not with an independent ground truth.

## 1. Agent output schema

Each run must end with one JSON object:

| field | content |
|---|---|
| `testability.p_testable` | probability in [0, 1] that the question can be answered with the stated data at useful power |
| `testability.blocking_constraints` | list of {code, text}, codes from the 14-code risk taxonomy |
| `prior_work.already_answered` | yes, partly, no or unknown |
| `prior_work.cited` | identifiers of prior work relied on |
| `risks` | list of {code, text} |
| `predicted_outcome` | probabilities for supported, rejected, untestable, artifact, uncertain |
| `decision` | proceed, proceed_with_changes or do_not_proceed |
| `design` | estimand, unit, sample, power, controls, falsification, multiplicity, decision_rule, data_version |

`scoring.validate_output` lists schema problems. Invalid outputs are scored where possible and counted in `valid_outputs`.

## 2. Replay scores per run

| score | definition | answer-key field |
|---|---|---|
| **flagged** | decision is do_not_proceed, or p_testable < 0.5, or predicted untestable + artifact > 0.5 | |
| **P1 (primary)** | balanced flag accuracy: mean of the share of should-flag tasks flagged and the share of other tasks not flagged; computed across tasks with class weights so the paired task-level contrast equals the difference in balanced accuracy | `should_flag_before_running` (untestable or artifact) |
| testability Brier | (p_testable minus truth)^2; truth = 0 for untestable, 1 otherwise | `testable` |
| testability AUC | Mann-Whitney AUC of p_testable against truth, per condition | `testable` |
| outcome log loss | minus log of the probability given to the key's stratum (floored at 0.01, probabilities renormalised) | `stratum` |
| risk recall | share of the key's expected risk codes that the agent raised (risks plus blocking constraints) | `expected_risk_codes` |
| risk codes not in key | count, reported but not penalised: the key's codes come from keyword rules and are incomplete | |
| prior work recognised | on tasks whose memory contains a family asking the same question, already_answered is yes or partly | `prior_same_question_families_in_memory` |
| false prior claim | on other tasks, in conditions B and C, already_answered is yes or partly | |
| pre-registration quality | rubric below, 0 to 1 | |
| proposal overlap | maximum TF-IDF similarity of the proposed design to the permitted memory records; repeats memory when at or above the repeat threshold 0.344 | |
| cost | input tokens, output tokens, USD where the provider reports it, tool calls, memory tool calls, wall-clock seconds | |

### Pre-registration rubric (deterministic)

Each of the nine design fields scores:

- **0** if empty or under 15 characters;
- **1** if present;
- **2** if present and specific by a fixed pattern.

| field | counts as specific when it contains |
|---|---|
| estimand | an estimand word (difference, ratio, rate, PPP, ...) |
| unit | an analysis unit |
| sample | a number |
| power | a number and a power or detectable-effect term |
| controls | a control or matching term |
| falsification | a placebo, permutation, holdout or similar term |
| multiplicity | a correction or a single primary test |
| decision_rule | a threshold with a number |
| data_version | a season, snapshot or cutoff |

Quality is the total divided by 18. The rubric measures completeness and specificity, not whether the design is good. A design can score 1.0 and still be wrong.

## 3. Redundancy detection

Redundancy uses the same TF-IDF representation and thresholds as the question clusters, calibrated on known same-study pairs (AUC 0.993):

- **Merge threshold, 0.231:** the 25th percentile of similarity within a study.
- **Repeat threshold, 0.344:** the median.

Redundancy is used in three places:

- **Task generation:** a task is excluded when an earlier family is near-identical (similarity 0.60 or more).
- **Challenge screening:** a candidate is redundant when its similarity to a historical record reaches 0.344.
- **Proposals:** a proposed design is flagged as repeating memory when its similarity reaches 0.344.

Lexical similarity misses paraphrase, so this is a screen, not a judgment.

## 4. Risk checklist scoring

The 14 codes are: SAMPLE_SIZE_POWER, EXPOSURE_SPARSITY, MEASURE_RELIABILITY, RTM_SELECTION, OUTCOME_DERIVED_LABEL, LEAKAGE_LOOKAHEAD, MECHANICAL_FLOOR, BASE_RATE, CONFOUNDING, LABEL_ERROR, PLACEBO_DEPENDENCE, MULTIPLE_TESTING, IMPLEMENTATION_BUG and DRIFT_NONSTATIONARITY.

The answer key's expected codes come from `common.RISK_RULES` applied to the family's failure evidence, power information and notes. Recall is the main score. Precision is not used, because the key under-lists risks; a raised code that is absent from the key is often still a real risk.

## 5. Claims, timestamps and validation (prospective arm)

`bench\claims.py`:

- **Register.** Appends a claim to `claims.jsonl` with the previous entry's SHA-256. Required fields are the estimand, direction, test, pass rule and analysis script. The script's own SHA-256 is stored with the claim.
- **Verify.** Fails when any entry's content no longer matches its hash, when the chain is broken, or when a registered script has changed since registration.
- **Close.** Appends a closing entry; later registrations are refused.
- **Release gate.** `release_allowed` requires the registry to verify and be closed, and the date to be after D2 (2027-04-12). The fetcher (`scripts\14_fetch_2026_27.py`) calls this gate before it requests any validation-period game.
- **Validate.** Re-runs each registered script on development data (reproducibility) and on validation data (survival). Each script prints `{"estimate", "ci_low", "ci_high"}`. A claim passes when its interval excludes 0 in the registered direction and the estimate reaches the registered minimum effect.

The hash chain proves internal order and integrity, not wall-clock time. For an external timestamp, publish the closing hash before D2, for example by e-mail to oneself or in a commit.

## 6. Comparison of conditions A, B and C

`bench\stats.py`, applied in `runner\experiment.analyze`:

- **Unit of analysis:** the task. Seeds and models are averaged within task and condition, then paired across conditions.
- **Interval:** the 95% bootstrap interval of the mean paired difference, resampling tasks (10,000 resamples).
- **Test:** a two-sided sign-flip permutation test, exact up to 16 tasks.
- **Multiplicity:** Holm adjustment across the three P1 contrasts (B minus A, C minus A, C minus B). Secondary contrasts are descriptive and uncorrected.
- **Equivalence of C and B:** two one-sided tests via the 90% bootstrap interval of C minus B on P1 inside plus or minus 0.10.

The decision rules from `benchmark_design.md` are unchanged.

**What the pilot can show.** With 10 tasks, the smallest exact two-sided sign-flip p-value is 2/1024. In practice, though, a P1 difference must be large and consistent to reach significance. The pilot estimates effect size and checks the pipeline; it is not a confirmatory test.

## 7. Blinding and redaction

`bench\redact.py` replaces:

- record, family, cluster and task identifiers;
- memory node identifiers;
- file paths;
- tool names;
- phrases that reveal a memory source ("the research history", "the graph", "graph node", ...).

Blinded IDs are an HMAC of the run ID with a per-experiment secret. The map is stored under `runs\<experiment>\sealed\`, and it must not be given to anyone scoring blinded outputs.

**Redaction cannot remove style.** An output from a memory condition may still reveal itself by referring to specific past results. Blinding therefore protects against casual bias only.

## 8. Which evaluations need a genuinely independent reviewer

| evaluation | automated now | independent reviewer needed? |
|---|---|---|
| schema validity, cost, tool use | yes | no |
| flag accuracy, Brier, AUC, log loss, risk recall | yes, against automated labels | **yes, for the labels**: a human check of a sample of answer-key strata (see `remaining_human_requirements.md`) |
| pre-registration completeness | yes (rubric) | no for completeness; yes if design quality is to be claimed |
| redundancy and overlap | yes (lexical screen) | only to estimate the screen's miss rate |
| prospective claim survival | yes (registered script on sealed data) | no, provided the script, data and pass rule were registered before release |
| novelty against the published literature | not automated | **yes** |
| usefulness of a validated discovery | not automated | **yes** |

**On LLM reviewers.** A different model is not an independent reviewer: it shares training data, conventions and blind spots with the agents being scored, and may recognise their phrasing. An LLM may be used to screen, for example to flag answer-key entries that look inconsistent. It must not relabel the key or produce a score that is reported as independent.
