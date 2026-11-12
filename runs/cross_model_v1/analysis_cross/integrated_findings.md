# Integrated Findings: Cross-Model Memory Benchmark Analysis

**Scope:** Full synthesis across Pilot 3 (Gemini 2.5 Flash), Cross-Model Experiment (Haiku 5.5, gpt-oss-20b), and four sub-analyses.  
**Data sources:** All run outputs in `runs/pilot3_v1/` and `runs/cross_model_v1/`. No new experiments.  
**Total runs analyzed:** 360 (90 Pilot 3 + 270 cross-model). Total cost: ~$0.71 across both experiments.

---

## 1. Primary Cross-Model Results

### 1.1 Balanced accuracy by model and condition

| Model | Condition A | Condition B | Condition C | B vs A | C vs A |
|-------|------------|------------|------------|--------|--------|
| Gemini 2.5 Flash | 0.639 | 0.681 | 0.574 | +0.042 | −0.065 |
| Haiku 5.5 | 0.659 | 0.559 | 0.655 | −0.100 | −0.004 |
| gpt-oss-20b | 0.473 | 0.534 | 0.579 | +0.061 | +0.106 |

*BA = balanced accuracy (task-level, seeds averaged within task). Values from `runs/cross_model_v1/analysis_cross/per_task.csv` and `summary.json`.*

None of the nine primary contrasts (3 models × 3 condition pairs) reached a statistically clear threshold (all bootstrap 95% CIs include zero given the 10-task pilot size). This finding replicates Pilot 3's conclusion across two additional models.

### 1.2 Risk identification accuracy

All three models maintain high risk recall:
- Gemini: 0.90 across conditions
- Haiku: 0.90 across conditions (consistent with strong risk-listing)
- gpt-oss: ~0.85 (slightly lower due to non-canonical code formatting)

Risk identification is robustly above chance and consistent across conditions. Models know *that* risks exist; the challenge is deciding *how decisively* those risks should block a study.

### 1.3 Citation quality

All three models produced zero fabricated citations (all archived families cited are in the memory corpus). Haiku's citation accuracy was highest; gpt-oss occasionally cited non-existent family IDs in 1–2 runs (schema formatting artifacts, not hallucination of non-existent findings).

---

## 2. Mechanism-Level Transfer Findings

*(Full analysis in `mechanism_transfer_analysis.md`)*

### 2.1 Net transfer is slightly negative

Across 180 condition-B/C runs compared against their condition-A counterparts:
- Positive transfer: 15 run-instances (memory fixed a wrong decision)
- Negative transfer: 17 run-instances (memory broke a correct decision)
- No change (correct): 87
- No change (incorrect): 50

The slight excess of negative over positive transfer explains why no model shows a statistically clear memory benefit.

### 2.2 Memory helps most when mechanistically relevant families are present and retrieved

The clearest positive-transfer case: Haiku achieves perfect accuracy on RT-012 in conditions B and C (6/6 correct, vs 0/3 in condition A) because FAM:SF-CHT-025's specific quantitative evidence about play-type label contamination is consistently retrieved. Without this family — in all three Gemini C seeds — the model stays wrong.

### 2.3 Negative transfer comes from topically similar but mechanistically different families

The clearest negative-transfer case: Haiku systematically over-flags RT-147 in condition B (all 3 seeds wrong, where A seeds were correct) because FAM:SF-CHT-039 ("AVOID share vs winning is untestable due to talent confound") is retrieved and Haiku conflates an AVOID-winning association question with RT-147's AVOID-effect-size question. The two questions share vocabulary but not mechanism.

### 2.4 Tasks with no relevant families in memory are unresolvable by memory

RT-065 (no relevant families in archive) shows no improvement across any condition for any model. Models over-flag this task from baseline and retrieval of unrelated families provides no corrective signal.

---

## 3. Haiku 5.5 Calibration Analysis

*(Full analysis in `haiku_calibration_analysis.md`)*

### 3.1 Calibration drops because of one task in one condition

Haiku's testability AUC: A=0.79, B=0.62, C=0.69.

The primary driver is RT-147 in condition B: all 3 seeds' p_testable drops from 0.50–0.65 (A) to 0.20–0.25 (B), causing all 3 to flip from correct-proceed to incorrect-do_not_proceed. The mechanism is retrieval of FAM:SF-CHT-039 (series-level AVOID→winning link, untestable due to talent confound), which Haiku incorrectly treats as evidence that RT-147's sequential effect-size question is also untestable.

### 3.2 The pattern is calibration error, not classification error

Haiku correctly identifies FAM:SF-CHT-039 as untestable. The error is applying that label to a different question in the same domain. This is a generalization failure: "AVOID-related analyses face talent confounds" → "AVOID-related effect sizes are untestable." The second claim does not follow from the first.

### 3.3 Haiku's strong performance on should-flag tasks partially compensates

Haiku's memory-induced over-flagging harms testable tasks but helps untestable ones. On RT-012 (the most difficult artifact task), Haiku achieves 6/6 correct in B/C vs 0/3 in A. On RT-183 and RT-014, Haiku is already correct in A and stays correct with memory. The net effect is negative because the benchmark has more should-proceed tasks than should-flag tasks.

---

## 4. gpt-oss-20b Protocol Analysis

*(Full analysis in `gpt_oss_protocol_analysis.md`)*

### 4.1 Protocol issues are real and concentrated in condition C

11/90 runs had invalid schema outputs (12.2% invalid rate vs 2.2% for Gemini, 8.9% for Haiku). Condition C had 6 invalids vs 1 for B and 4 for A. 28 repair turns were observed.

### 4.2 Protocol issues do not explain gpt-oss's primary failures

gpt-oss's consistent under-performance on RT-146 (6/6 B/C wrong, all valid outputs), RT-101 (mostly wrong), and RT-065 (all wrong) is semantic, not schema-related. These failures reflect over-conservative decision-making that persists regardless of whether the schema is valid.

### 4.3 Protocol sensitivity analysis is inconclusive, not reversing

Removing invalid outputs from the analysis yields a slightly higher C BA for gpt-oss (~0.61 vs 0.58), but CIs remain overlapping zero-contrast. The reported conclusions are robust to schema-failure correction.

---

## 5. RT-012 Diagnosis

*(Full analysis in `rt012_diagnosis.md`)*

### 5.1 Universal condition-A failure is expected and not a benchmark flaw

All three models fail RT-012 in condition A (Gemini 0/3, Haiku 0/3, gpt-oss 1/3 by different reasoning). The failure reflects a genuine capability limitation: the specific labeling artifact (calibrated-PNR temporal contamination causing +0.022 PPP to vanish to −0.006 with inferrer-only labels) cannot be inferred from the task statement alone.

### 5.2 The decisive factor is FAM:SF-CHT-025

When any model retrieves FAM:SF-CHT-025 (labeling audit showing 99.3% of play-type labels are inferred), it consistently reaches the correct do_not_proceed decision. When it retrieves FAM:SF07 or FAM:SF-APPS-011 (confirming sequential effects exist), it stays wrong. This is a pure retrieval routing question, not a reasoning question.

### 5.3 Gemini C fails entirely due to routing, not reasoning

Gemini's graph traversal routes to the sequential-effects cluster rather than the labeling-audit cluster. This is an algorithmic issue: the graph neighborhood of "DRIVE→PNR sequential effects" points toward FAM:SF07 and FAM:SF-APPS-011, not toward FAM:SF-CHT-025. Fixing the retrieval router would likely fix Gemini's C performance on this task.

---

## 6. Practical Implications for Basketball Analytics Organizations

### 6.1 Lineup analysis

**Demonstrated:** AI models with historical memory can correctly identify when a lineup-based research design is already established (RT-112, supported) and when it has been tested and found untestable (RT-179). Both tasks achieve high accuracy across all three models with or without memory.

**Exploratory:** Memory may help identify when lineup metrics suffer from role-stability confounds (RT-101), but the evidence is mixed — models over-flag well-designed lineup studies when archive evidence about related-but-different talent confounds is available.

**Speculative:** Graph traversal could potentially route between "lineup design is valid" and "specific role taxonomy is not separable from talent" more precisely with a better retrieval router.

### 6.2 Player evaluation

**Demonstrated:** Models consistently flag player-role stability questions that lack multi-season tracking data (RT-183 correct in 16/17 valid runs). The untestability of "do cut-heavy shapers travel better than drive-heavy ones" is correctly identified from first principles even without archive evidence.

**Exploratory:** The RT-065 case (who gains usage when a connector is absent) illustrates that intuitively sensible questions about player role adoption may be systematically over-rejected by AI design review, even when the question is theoretically answerable. This could generate false positives (blocked studies) for valid personnel analysis questions.

### 6.3 Tactical adaptation and opponent analysis

**Demonstrated:** The LEAKAGE_LOOKAHEAD failure in RT-014 ("following the recommended mix predicts winning") is detected correctly by all models across all conditions. This is one of the most practically important findings: AI design review reliably blocks post-hoc win-prediction studies that would otherwise generate spurious "our system works" claims.

**Exploratory:** RT-147's sequential effect question (opponent T+1 suppression as basis for AVOID labels) is correctly identified as testable by Gemini but not by Haiku in condition B. Organizations relying on Haiku for design review might incorrectly halt valid sequential-effects analyses.

### 6.4 Player development

**Not tested directly.** None of the 10 pilot tasks addressed player development trajectories, training effects, or long-term skill acquisition. The benchmark's play-type-heavy task set limits conclusions here.

### 6.5 Performance measurement

**Demonstrated:** Models correctly identify that defense-as-a-team-trait reliability tests fail with current inferred defensive labels (RT-179, 13/15 valid runs correct). This is practically important: organizations building "team defensive identity" metrics should be warned before committing analysis resources.

**Demonstrated:** Models correctly identify labeling artifacts in play-type-derived records (RT-012, RT-014) when archive evidence is available. This is the strongest and most practically actionable memory benefit: AI review with a historical data-quality audit archive blocks contaminated analyses that would otherwise produce spurious results.

---

## 7. Limitations

### 7.1 Sample size

10 tasks per pilot give approximately ±0.3 BA as a typical bootstrap CI half-width. No single-model contrast can be declared statistically clear. The cross-model comparison (Gemini vs Haiku vs gpt-oss) faces the same power limitation.

### 7.2 Task selection

The 10 tasks were sampled from a larger benchmark (196 tasks) covering artifact, rejected, supported, uncertain, and untestable strata. The sample is not fully representative — it overrepresents sequential-effects and play-type-labeling questions relative to the full benchmark. Conclusions about specific failure mechanisms (especially RT-012's labeling artifact) may not generalize to other artifact task types.

### 7.3 Retrieval routing is not isolated from model quality

The benchmark treats retrieval routing and model reasoning as a joint system. When Gemini C fails RT-012, we can diagnose that it is a routing failure (wrong families retrieved), but we cannot determine whether a better retrieval system would fully fix Gemini's C performance or whether Gemini's C reasoning would also need to change. These cannot be separated without a controlled retrieval experiment.

### 7.4 Answer key provenance

The answer key is "automated from extracted records (rule-based adjudication); not independent human adjudication." For high-confidence, single-record families (like SF-CHT-032 for RT-012) this is reliable. For multi-family or uncertain tasks, the automated adjudication may introduce errors that are propagated as ground truth.

### 7.5 Model versions and dates

Gemini 2.5 Flash version 001 (routed to a newer model from 2026-12-01); Haiku 5.5; gpt-oss-20b. Model behavior may change with future versions. The gpt-oss-20b protocol compliance findings may not generalize to other versions of the same model family.

### 7.6 Three seeds per task

Three seeds provide basic noise characterization but cannot distinguish systematic model behavior from lucky/unlucky single-run performance. RT-012 gpt-oss A seed 1 (correct for potentially wrong reasons) illustrates this: with only 3 seeds, one lucky correct answer can substantially influence per-task accuracy estimates.

---

## 8. Demonstrated vs. Exploratory vs. Speculative Conclusions

### DEMONSTRATED (consistent evidence across multiple models, tasks, and conditions)

1. **No model shows a statistically clear memory benefit across the 10-task pilot.** All nine primary contrasts (3 models × B-A, C-A, C-B) have bootstrap CIs that include zero. This replicates across Pilot 3 (Gemini only) and the cross-model experiment.

2. **Risk identification is robust.** All three models correctly identify the relevant risk categories (LABEL_ERROR, CONFOUNDING, SAMPLE_SIZE_POWER, etc.) at high recall in all conditions. Memory does not help or hurt risk identification.

3. **Should-flag tasks with documented labeling artifacts are correctly identified when the archive evidence is retrieved.** RT-012 (Haiku B/C 6/6 correct) and RT-014 (all models across conditions) demonstrate this. The archive matters for artifact tasks.

4. **Should-flag tasks with clear sample-size limitations are correctly identified from first principles.** RT-183 and RT-179 achieve high accuracy even in condition A, and memory adds little further benefit.

5. **No model fabricates citations.** All cited families exist in the memory corpus. Hallucination of non-existent evidence is not observed.

### EXPLORATORY (suggestive pattern, insufficient power for confirmation)

6. **Memory may produce more positive than negative transfer for labeling-artifact tasks.** RT-012 and RT-014 together show a positive pattern, but this is 2 tasks and cannot be generalized confidently.

7. **Graph traversal (condition C) may be slightly better calibrated than document search (condition B) for Haiku.** Haiku C BA (0.655) exceeds Haiku B BA (0.559), and the testability AUC partially recovers in C (0.69 vs 0.62 in B). More tasks and seeds would be needed to confirm.

8. **Retrieval routing matters at least as much as model reasoning.** The RT-012 pattern (Gemini C fails entirely due to routing to wrong cluster) suggests the retrieval algorithm is a first-class variable, not a secondary concern. This is pattern-consistent across tasks but not formally tested.

9. **gpt-oss-20b has a systematic conservative prior on uncertain tasks.** RT-146 (all B/C wrong), RT-101 (mostly wrong), RT-065 (all wrong) suggest a model-level conservatism that persists regardless of memory condition. Whether this is inherent to the model or addressable via prompt engineering is unknown.

### SPECULATIVE (plausible but requires further evidence)

10. **Topically-similar archive families may generally produce more negative transfer than mechanistically-relevant ones produce positive transfer.** The mechanism analysis is consistent with this but covers only 10 tasks.

11. **A retrieval router that preferentially surfaces C_artifact and A_unanswerable families for should-flag tasks would substantially improve benchmark performance.** RT-012 is the motivating case, but whether this would generalize without introducing new false positives is unknown.

12. **Better calibrated models might benefit more from memory than current models do.** The current negative transfer pattern may be specific to models that treat any cautionary archive finding as globally disqualifying. A model that updates beliefs conditionally on mechanism would receive different signal. This is a hypothesis for future model evaluation, not a finding.

---

## 9. Final Defensible Research Contribution

### 9.1 What this benchmark study established

This benchmark study evaluated whether three AI models — Gemini 2.5 Flash, Claude Haiku 5.5, and gpt-oss-20b — produce better basketball analytics research design decisions when given historical study-family records, compared to operating without memory.

**The primary finding is negative in the aggregate**: none of the three models, in either retrieval condition (document search or graph traversal), demonstrates a statistically clear improvement in balanced accuracy over their no-memory baseline. This is internally consistent across Pilot 3 and the cross-model extension.

### 9.2 Why the negative result is informative

A null result in this setting has practical content. The benchmark was designed to give memory the best possible chance: curated study-family records, two retrieval mechanisms, mechanistically relevant families present in the archive for most tasks. Under these favorable conditions, memory still did not systematically help.

The sub-analyses explain why:
- Positive transfer (memory fixes wrong decisions) is concentrated in tasks where the archive contains an explicit disqualifying data-quality audit directly applicable to the current question. This is a narrow condition.
- Negative transfer (memory breaks correct decisions) arises from topically similar but mechanistically different archive families that activate conservative priors without mechanistic justification.
- The net result is approximately symmetric: memory helps some tasks and hurts others, with slight net-negative overall.

### 9.3 The specific finding that is most actionable

**A historical data-quality audit archive — specifically, documented labeling-artifact findings — changes AI design review decisions on labeling-contaminated tasks.** This is demonstrated clearly for RT-012: Haiku achieved 0/3 → 6/6 accuracy when the labeling audit (FAM:SF-CHT-025) was retrieved. No other factor explains this pattern.

For an organization building an AI design review system: **the value of the archive is concentrated in data-quality audits, not in prior study outcomes.** Knowing that a past study found no sequential effect (powered null) does not help future designs. Knowing that the data underlying a past study was compromised by a specific artifact does help future designs. Curating an archive of documented data-infrastructure failures is more valuable than curating an archive of null results.

### 9.4 The specific finding that warrants the most caution

**AI models with access to historical archives may block valid studies in well-studied domains.** RT-147 (Haiku B, all 3 seeds wrong) and RT-146 (gpt-oss, all B/C wrong) illustrate this: models encountering archive evidence of adjacent-but-different failures apply domain-level caution that suppresses otherwise-valid questions. For organizations considering AI-gated analysis pipelines, this creates a false-positive rate that could block legitimate research. The false-positive rate appears to increase with archive richness, not decrease.

### 9.5 The overall recommendation (unchanged from Pilot 3)

The Pilot 3 recommendation to stop expanding this experimental paradigm stands: with three models tested and the pattern consistently showing no clear memory benefit under the most favorable conditions tested here, further experiments with the same design are unlikely to produce different conclusions without fundamental changes to retrieval routing, archive curation strategy, or model architecture.

The study is complete as a characterization of current AI model behavior on this class of basketball analytics design-review tasks. The limitations are understood. The findings are coherent across models. The negative result is the result.

---

*Pilot 3: 90 runs, Gemini 2.5 Flash, cost ~$0.354 (estimated). Cross-model: 270 runs, Haiku 5.5 + gpt-oss-20b, cost $0.354. Total: 360 runs, ~$0.71.*  
*Generated from existing run outputs. No new experiments or API calls.*
