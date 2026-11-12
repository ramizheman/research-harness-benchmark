# Pilot 3: evidence-aware basketball research memory

Experiment `pilot3_v1`, run 2026-11-10. Model `gemini-2.5-flash` (listing version 001; every response reported
modelVersion `gemini-2.5-flash`). 10 tasks x 3 conditions x seeds 1, 2, 3 = 90 runs. Answer key: automated
adjudication, unchanged. Scoring: unchanged.

## Summary

* The protocol worked as intended. All 90 runs retrieved before any assessment, no preliminary answer was produced,
  no citation was invented, and every historical status claim in the final outputs matched the record (B 110 of 110,
  C 118 of 118 checked items; two wrong statuses in C were caught by the citation check and corrected).
* Consolidated family records reached the model in every memory run (4 families per run, 100% of retrieved items were
  family records, compared with 0 of 160 in Pilot 2).
* Memory now changes decisions: flags differed from condition A under the same seed in 10 of 30 B runs and 12 of 30
  C runs, against a seed-to-seed disagreement of 2 of 30 pairs within A.
* The changes do not improve decisions on balance. Primary balanced flag accuracy, task level: A 0.639, B 0.681,
  C 0.583. B minus A +0.042 (95% CI -0.264 to 0.389), C minus A -0.056 (-0.361 to 0.292). Relative to A, B moved
  5 flags from wrong to right and 5 from right to wrong; C moved 5 and 7.
* The mechanism is a shift toward caution rather than better discrimination. Retrieved history, which is dominated by
  failed, untestable and artifact studies, lowered the stated probability of testability on both kinds of task and
  raised the flag rate on tasks that should be flagged (B 0.50 to 0.75) and on tasks that should not (B 0.22 to 0.39).
* Three pilots, three designs, the same result: no measurable gain in research decisions from memory.
* Recommendation: stop investing in research memory for this question. Do not scale to 78 tasks as an expected
  improvement, and do not make a further targeted change. Details at the end.

## 1. What was run and what was preserved

* Pilot 1 and Pilot 2 configurations, raw outputs, reports, comparisons, the 10 tasks, the answer key, scoring and
  the v2 memory snapshots were not modified. Pilot 3 has its own configuration (`configs/pilot3.json`), memory
  (`memory_v3/snapshots/`), protocol code (`runner/tools_v3.py`, `run_v3` in `runner/agent.py`) and output
  (`runs/pilot3_v1/`).
* Same model and version, same generation settings (temperature 0.7, 8,192 output tokens, thinking budget 2,048,
  JSON mode), same budgets, order seed, cap and equivalence margin as Pilots 1 and 2 (checked by the preflight).
  Seeds 1, 2 and 3 are the only intended difference in settings.

### Memory v3: study-family records

One record per study family, rendered twice from the same canonical fact set: as a document per family (condition B)
and as a family node linked to concept nodes for research-question clusters, methods, datasets, measures,
limitations and risk codes, plus related-family edges (condition C). Each family carries the research question,
hypothesis, dataset and sample size, method and outcome measures, result, outcome status, failure mechanism,
confounders and limitations, validation status, related families and source references with provenance.
Fields copied from records are prefixed `observed_`; rule-based interpretations (outcome status, failure mechanism,
validation status, confidence) are prefixed `auto_`. Missing information is written `NOT_RECORDED`; no outcome was
inferred. Documents and graph were verified fact-for-fact equivalent for all 10 task snapshots (96 to 289 families,
2,943 to 9,419 facts), every family has every field, and each task's excluded record is absent.

### Retrieval

* A: `retrieve_history` executes and returns nothing.
* B: TF-IDF document search over family documents.
* C: graph traversal. The request is matched to concept nodes and to family question and hypothesis text; families
  are scored by following relationships from those nodes (and family-to-family links); each result lists the
  relationship paths that reached it.
* Same budget: 4 families per call, each shown through the same field selection under the same character limit, so a
  family retrieved in B and in C shows identical facts. First-retrieval size: B 4,511 characters, C 5,474 (the
  difference is JSON structure and relationship paths). C traversed 100 edges per run on average.
* B and C selected different families: 1.4 of 4 shared on average, never identical.

### Decision sequence (protocol 3)

Stage 1 shows the task and asks only for the retrieval call (research concepts, methodological questions, query);
the output schema is not shown. The stage-2 schema arrives with the retrieval result and requires, in order:
historical evidence (id, status as recorded, finding), failed approaches, what the evidence does and does not
establish, own inferences, uncertainties, testability, risks, decision, and whether the evidence changed the
decision. A final answer or assessment content in stage 1 would be rejected and counted. After the final answer,
cited identifiers must have been returned by a tool and stated statuses must match the record; one correction turn is
allowed and the pre-correction answer is kept and scored separately.

### Quality controls before spending

91 unit tests passed (including information equivalence, graph traversal, equal budgets, schema hidden before
retrieval, preliminary-answer rejection, citation correction). A 90-run mock dry run completed. The preflight passed
every check: 90 runs, identical settings to both earlier pilots apart from seeds, v3 equivalence for all tasks, A
retrieval empty, B and C returning 4 families under the cap with identical family views, C reaching families through
relationships, identical system instructions across conditions apart from the tool list, no mock client, cap 5.00 USD,
listing version 001. A paid stage-1 smoke test (3 calls, one per condition, 0.0099 USD) confirmed the real model
replied with the retrieval call only.

A pre-run diagnostic (no tuning followed) showed that with realistic queries the top 4 families included a family
the audit counts as relevant for only 3 of 10 tasks in B and 2 of 10 in C. Three tasks (RT-065, RT-101, RT-146) have
no relevant family in memory at all.

## 2. Protocol compliance

| | A | B | C |
|---|---|---|---|
| runs ending with a final answer | 30 | 30 | 30 |
| valid outputs | 30 | 29 | 29 |
| retrieval first | 30 | 30 | 30 |
| preliminary answers / gate turns | 0 / 0 | 0 / 0 | 0 / 0 |
| repair turns | 0 | 2 | 1 |
| citation correction turns | 0 | 0 | 2 |
| follow-up memory calls | 0 | 0 | 0 |

The two invalid outputs are memory-induced vocabulary leaks: one B run wrote risk codes as graph identifiers
(`RISK:SAMPLE_SIZE_POWER`), one C run used the failure-mechanism code `C_artifact` as a risk code. No run used the
optional follow-up tools; every run made exactly one retrieval.

## 3. Primary outcome: balanced flag accuracy

Seeds are averaged within task; the 10 tasks are the unit. Repeated seeds measure model variability on the same
tasks and do not add independent tasks.

| | A | B | C |
|---|---|---|---|
| task level (invalid outputs count as wrong) | 0.639 | 0.681 | 0.583 |
| valid outputs only | 0.639 | 0.669 | 0.574 |
| seed 1 / 2 / 3 | 0.583 / 0.667 / 0.667 | 0.583 / 0.667 / 0.750 | 0.775 / 0.500 / 0.458 |

| contrast | difference | 95% CI | sign-flip p | Holm p |
|---|---|---|---|---|
| B - A | +0.042 | -0.264 to 0.389 | 0.91 | 1.00 |
| C - A | -0.056 | -0.361 to 0.292 | 0.84 | 1.00 |
| C - B | -0.097 | -0.278 to 0.083 | 0.37 | 1.00 |

B and C are not equivalent within the 0.10 margin (90% CI of C - B: -0.250 to 0.056). With ten tasks the intervals
are about 0.6 wide; effects smaller than roughly 0.3 cannot be ruled out in either direction.

Seed variability: within A, flags changed between seeds in 2 of 30 seed pairs (0.07); within B in 0.21 and within C
in 0.39 of pairs. Memory makes the model less stable across seeds, especially graph memory.

## 4. Secondary outcomes

| | A | B | C |
|---|---|---|---|
| testability AUC (runs) | 0.653 | 0.679 | 0.804 |
| testability AUC by seed | 0.66 / 0.84 / 0.50 | 0.75 / 0.69 / 0.66 | 1.00 / 0.69 / 0.75 |
| testability Brier (lower is better) | 0.232 | 0.336 | 0.254 |
| outcome log loss (lower is better) | 1.879 | 1.757 | 1.567 |
| risk recall | 0.639 | 0.647 | 0.472 |
| pre-registration quality | 0.967 | 0.960 | 0.971 |
| prior work recognized (2 tasks with a prior same-question family) | 0.0 | 0.50 | 0.40 |
| false prior claim (8 tasks without one; claims "yes" or "partly" answered) | n/a | 0.26 | 0.54 |

Task-paired secondary contrasts against A all have intervals that include zero. Points worth noting:

* Testability: B worsened Brier (B - A -0.093, CI -0.245 to 0.071) because it lowered p_testable across the board.
  C's higher run-level AUC is driven by seed 1 (1.00) and is not stable across seeds.
* Outcome log loss improved in both memory conditions (C - A +0.324, CI -0.179 to 0.910), consistent with more
  probability on untestable and artifact outcomes. The interval includes zero.
* Prior work: recognition occurred on RT-147 only (6 of 6 memory runs); on RT-183 none of the 6 runs recognized the
  prior family. False prior claims were common, mostly "partly answered", and twice as frequent in C as in B
  (C - B -0.292, CI -0.542 to -0.042, sign-flip p 0.16).

## 5. Use of historical evidence

### Citation correctness and false claims

* Invented identifiers: 0 before and after correction, in all 90 runs.
* Status as recorded: before correction, B 110 of 110 and C 116 of 118 correct; after correction, 228 of 228.
  The separate retrieval audit (statuses checked against the v2 strata) agrees: B 70 of 70, C 97 of 97.
* Statuses cited by memory runs: "not a hypothesis test" 60, "supported" 45, "untestable" 39, "inconclusive" 33,
  "artifact" 30, "rejected" 20, "no result recorded" 1. In other words, about half of the cited history is failed or
  inconclusive work.
* Condition A runs stated "no historical evidence" in all 30 runs and made no claims about earlier studies.

Citations are now accurate. The remaining false-claim problem is interpretive: the model overstates how far adjacent
studies answer the current question.

### Relevance and meaningful use

| | B | C |
|---|---|---|
| runs where a relevant family was retrieved | 0.43 | 0.33 |
| runs citing a relevant retrieved family (meaningful use) | 0.20 | 0.27 |
| flag correct when citing relevant evidence | 0.83 (6 runs) | 0.75 (8 runs) |
| flag correct otherwise | 0.63 (24 runs) | 0.55 (22 runs) |

The association between citing relevant evidence and a correct flag is descriptive only; it is confounded by task
(relevant evidence exists only for some tasks).

### Did retrieved findings change research decisions?

* Self-report: 59 of 60 memory runs said the evidence changed the decision. This is not informative on its own.
* Against the control: flags differed from A under the same seed in 10 of 30 B runs and 12 of 30 C runs, well above
  the A seed-to-seed rate (0.07). Unlike Pilot 2, where the flag changed in 1 of 17 runs, memory now changes
  decisions.
* Direction of the changes: B 5 wrong to right, 5 right to wrong; C 5 and 7. By task class (task level, B - A flag
  accuracy): +0.250 on the 4 tasks that should be flagged, -0.167 on the 6 that should not; C: 0.000 and -0.111.
* Flag rate and stated testability:

| | A | B | C |
|---|---|---|---|
| flag rate, should-flag tasks | 0.50 | 0.75 | 0.50 |
| flag rate, should-not tasks | 0.22 | 0.39 | 0.33 |
| mean p_testable, should-flag tasks | 0.48 | 0.26 | 0.40 |
| mean p_testable, should-not tasks | 0.61 | 0.51 | 0.51 |

Two tasks show the mechanism.

* RT-179 (untestable, should flag). A proceeded in 3 of 3 seeds; B and C declined in 6 of 6 runs. The model cited
  an untestable within-game scheme study (SF-APPA-005) and a low-reliability trait study (SF-APPS-085) and reasoned
  that the new trait would face the same reliability and attribution problems. None of these families meets the
  audit's relevance definition, so the gain came from analogy to methodologically similar failures.
* RT-101 (supported, no relevant family in memory). A was correct in 3 of 3 seeds; B was wrong in 3 of 3 and C in
  2 of 3. The retrieved families (talent-confounded adaptation studies, team-quality artifacts) were unrelated to the
  question, but the model treated their failures as a warning and lowered p_testable or declined.

Memory acts mainly as a prior toward caution. It helps when the new question shares the failure mode of retrieved
studies and hurts when it does not, and the model does not distinguish the two cases reliably.

## 6. Document versus graph memory

* Retrieval differed by design and in practice (1.4 of 4 families shared per same-seed pair). Relevant-family
  retrieval: B 0.43, C 0.33 of runs (C - B -0.10, CI -0.27 to 0.07).
* Decisions: B 0.681, C 0.583 balanced accuracy (C - B -0.097, CI -0.278 to 0.083). Same-seed B and C flags differed
  in 10 of 30 pairs.
* C was less stable across seeds (0.39 vs 0.21 flag disagreement), made more false prior claims (0.54 vs 0.26) and
  raised fewer expected risks (0.47 vs 0.65). C had the better testability Brier (0.254 vs 0.336) and log loss
  (1.567 vs 1.757). No difference is statistically clear, and neither representation dominates.
* Cost: C used about 14% more input tokens than B (larger results with relationship paths).

## 7. Task-level comparison with Pilots 1 and 2 (not pooled)

Flag correctness per task. Pilot 1 (recovered outputs) and Pilot 2 used seed 1 only; Pilot 3 shows the mean of three
seeds. The pilots differ in memory content, retrieval and protocol, so differences between pilots are descriptive.

| task | stratum | should flag | relevant families | P1 A/B/C | P2 A/B/C | P3 A/B/C |
|---|---|---|---|---|---|---|
| RT-012 | artifact | yes | 4 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0.33 / 0 |
| RT-014 | artifact | yes | 6 | 1 / 1 / 1 | 1 / 0 / 1 | 1 / 1 / 0.67 |
| RT-065 | rejected | no | 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0.33 |
| RT-066 | rejected | no | 21 | 1 / 1 / 1 | 1 / 1 / 1 | 1 / 0.67 / 1 |
| RT-101 | supported | no | 0 | 1 / 1 / 1 | 1 / 1 / 1 | 1 / 0 / 0.33 |
| RT-112 | supported | no | 7 | 1 / 1 / 1 | 1 / 1 / 1 | 1 / 1 / 1 |
| RT-146 | uncertain | no | 0 | 1 / 0 / 1 | 0 / 1 / 1 | 1 / 1 / 0.67 |
| RT-147 | uncertain | no | 1 | 0 / 0 / 0 | 1 / 1 / 1 | 0.67 / 1 / 0.67 |
| RT-179 | untestable | yes | 6 | 0 / 1 / 0 | 0 / 0 / 0 | 0 / 1 / 1 |
| RT-183 | untestable | yes | 22 | 1 / 1 / 1 | 1 / 1 / 0 | 1 / 0.67 / 0.33 |

| balanced flag accuracy (task level) | A | B | C |
|---|---|---|---|
| Pilot 1 | 0.583 | 0.625 | 0.583 |
| Pilot 2 | 0.583 | 0.542 (0.583 valid only) | 0.542 |
| Pilot 3 | 0.639 | 0.681 | 0.583 |

Memory effect (memory minus A, balanced accuracy): B +0.042, -0.042, +0.042 in Pilots 1, 2, 3; C 0.000, -0.042,
-0.056. Change in the memory effect from Pilot 1 to Pilot 3, task-paired: B 0.000 (CI -0.264 to 0.264), C -0.056
(-0.361 to 0.292). From Pilot 2 to Pilot 3: B +0.083 (-0.347 to 0.542), C -0.014 (-0.375 to 0.347).

Pilot 2's strongest secondary result, B testability AUC 0.938, did not replicate: Pilot 3 B gave 0.75, 0.69 and
0.66 across seeds. Single-seed secondary results in the earlier pilots should be read with that variability in mind.
RT-012 and RT-065 are wrong in nearly every run of every pilot and condition.

## 8. Cost and tokens

| | A | B | C | total |
|---|---|---|---|---|
| cost (USD) | 0.377 | 0.510 | 0.547 | 1.434 |
| input tokens | 91,342 | 151,835 | 173,479 | 416,656 |
| output tokens (including thinking) | 139,830 | 185,790 | 198,154 | 523,774 |
| mean wall time per run (s) | 24.7 | 30.9 | 32.6 | |

Preflight smoke requests cost a further 0.0100 USD. Total Pilot 3 spend 1.44 USD, under the 5.00 USD cap. Memory
added about 35% (B) and 45% (C) to the cost of a run.

## 9. Limitations

* Ten tasks. Three seeds reduce model noise per task but do not add tasks; intervals remain wide.
* The answer key is automated adjudication, not expert judgement.
* Only 7 of 10 tasks have any relevant family in memory, and retrieval surfaced one in 33 to 43% of runs. The
  experiment measures memory as it exists in this archive, not an ideal archive.
* The archive is dominated by failed and inconclusive studies, which is the likely source of the caution shift.
* The model never used follow-up retrieval, so the evidence comes from one retrieval per run.
* The retrieval audit's relevance definition misses analogical relevance (RT-179), so "meaningful use" is a lower
  bound.

## 10. Recommendation

**Stop.** The evidence does not justify further investment in research memory for this model.

* The harness question is settled. Pilot 3 removed every process explanation left by the earlier pilots: retrieval
  happens first, the model receives consolidated family records with outcomes and failure mechanisms, it cites them
  accurately, and it does not invent prior studies.
* With those problems removed, memory changes decisions but does not improve them. Across three pilots and three
  designs, the memory effect on the primary metric stayed between -0.06 and +0.04.
* The mechanism found in Pilot 3 explains why: retrieved history moves the model toward caution regardless of
  whether it applies, gaining on should-flag tasks and losing on should-not tasks by similar amounts.
* Graph memory adds cost and instability without a clear benefit over document search.

**Why not scale to 78 tasks.** A 78-task run (one seed, about 234 runs, roughly 3.70 USD; three seeds about 11 USD,
above the cap) would narrow the interval enough to bound an effect near 0.1. The pilot evidence predicts a small
effect near zero, because the caution shift adds as many errors as it removes. Scaling would mainly confirm a null
result. It is worth doing only if a bounded null result is itself the goal. If so, it has to finish before
`gemini-2.5-flash` requests are rerouted to newer models on 2026-12-01.

**Why not one more targeted improvement.** The obvious candidates are retrieval relevance (relevant families reached
in under half the runs) and calibration of how failures transfer. Both amount to redesigning the intervention after
a null result, which the brief rules out. Neither is supported by an observed effect that a change would unlock.

## Files

* `configs/pilot3.json`, `configs/pilot3_mock.json`
* `bench/memory_v3.py`, `memory_v3/snapshots/RT-*/`
* `runner/tools_v3.py`, `runner/agent.py` (`run_v3`), `runner/llm.py` (mock protocol 3)
* `tests/test_pilot3.py`; `scripts/21_preflight.py` (protocol-3 checks); `scripts/24_pilot3_analysis.py`
* `runs/pilot3_v1/` raw, blinded and sealed outputs, `scores.csv`, `analysis.json`, `report.md`
* `runs/pilot3_v1/analysis_p3/` `per_run.csv`, `per_task.csv`, `contrasts.csv`, `citations.csv`,
  `retrieval_pairs.csv`, `summary.json`
* `runs/pilot3_mock/` mock dry run
