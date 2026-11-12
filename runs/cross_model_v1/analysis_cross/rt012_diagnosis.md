# RT-012 Task Diagnosis

**Task ID:** RT-012  
**Research question:** "Any teammate DRIVE preceding a PNR raises PNR PPP."  
**Stratum:** artifact | **Should flag:** True | **Expected risk:** LABEL_ERROR  
**Key family:** SF-CHT-032 (not separately indexed in memory; its mechanism is partially captured by FAM:SF-CHT-025 and FAM:SF-APPA-030)  
**No API calls. No new experiments. Existing data only.**

---

## 1. The Task and Its True Answer

### 1.1 What the task asks

RT-012 is a pre-analysis design review task: before any statistical model is run, the reviewer must assess whether the question "Any teammate DRIVE preceding a PNR raises PNR PPP" can be answered with the available play-by-play data.

The data available includes:
- NBA play-by-play records (action type, sub-type, clock, period, score, player, shot distance/result)
- Substitution rotation intervals, starters, defensive matchup minutes
- **Derived play-type possession records** (initiator, play type, points) in a graph database built from the play-by-play

The word "derived" in the data description is the key signal: play-type labels are inferred computationally from raw play-by-play, not captured directly from video review.

### 1.2 What the answer key says

The answer key (derived from study family SF-CHT-032, confidence=1.0, high confidence) states:

- **Should flag:** True
- **Failure mechanism:** C_artifact — apparent effect produced by a construction, selection, or labelling flaw
- **What was learned:** "The apparent result was produced by an artifact: The +0.022 vanished to -0.006 once PNR was inferrer-only; calibrated-PNR temporal contamination."
- **Primary result:** "League-wide including calibrated PNR: +0.022 PPP, p=0.004 (n=20,658 vs 159,623). Tatum +0.152 p=0.27. Inferrer-only DRIVE-PNR ATT=−0.006, p=0.76."
- **Knowable from history:** yes_from_history (via knowable_precedent SF-APPA-005)
- **Expected risk code:** LABEL_ERROR

The statistical story: the apparent +2.2 points-per-100-possessions premium for teammate DRIVE→PNR sequences is entirely explained by **temporal contamination in the calibrated PNR label**. "Calibrated PNR" possessions include possessions where the play-type label was assigned by a rule-based calibration pass, not by initial inferrer assignment. The calibration assigns PNR labels partly based on shot outcomes in adjacent plays — so possessions that follow high-value DRIVE sequences are more likely to be (re)labeled as PNR, inflating the apparent DRIVE→PNR premium.

Once restricted to "inferrer-only PNR" (labels assigned before the calibration pass), the effect disappears: ATT = −0.006, p = 0.76.

This is a pre-flight data quality problem: no valid study can be run on the current derived labels as constituted without first auditing and correcting the calibrated-PNR temporal leak.

---

## 2. Model Response Summary by Condition

### 2.1 Condition A (no memory)

| Model | Seed 1 | Seed 2 | Seed 3 | Correct/3 |
|-------|--------|--------|--------|-----------|
| Gemini | proceed_with_changes (✗) | proceed_with_changes (✗) | proceed_with_changes (✗) | 0/3 |
| Haiku | proceed_with_changes (✗) | proceed_with_changes (✗) | proceed_with_changes (✗) | 0/3 |
| gpt-oss | **do_not_proceed (✓)** | proceed_with_changes (✗) | proceed_with_changes (✗) | 1/3 |

All three models fail to halt the task in condition A at the population level. The single correct answer (gpt-oss seed 1) correctly identifies do_not_proceed but appears to do so on generic grounds (risks raised: CONFOUNDING, EXPOSURE_SPARSITY, MEASURE_RELIABILITY, SAMPLE_SIZE_POWER — not LABEL_ERROR, which is the specific correct risk).

**Why models fail in A:** All three models correctly list LABEL_ERROR as a risk in at least some A seeds:
- Gemini A seed 3: risks include LABEL_ERROR
- Haiku A seeds 1,2,3: Haiku lists LABEL_ERROR in all three A seeds
- gpt-oss A seeds 2,3: list MEASURE_RELIABILITY, LABEL_ERROR

Raising LABEL_ERROR as a *risk* is insufficient — the model must recognize that the derived labels are corrupted enough to make the question *unanswerable in its current form*. The models treat LABEL_ERROR as a manageable risk requiring "design with care" rather than as a disqualifying flaw. This is the fundamental calibration problem: without knowing that 99.3% of play-type labels are inferred and that calibrated-PNR introduces temporal contamination, models cannot distinguish "label quality could be improved" from "label quality is fatal to this specific test."

### 2.2 Condition B (document search)

| Model | Seed 1 | Seed 2 | Seed 3 | Correct/3 |
|-------|--------|--------|--------|-----------|
| Gemini | proceed_with_changes (✗) | proceed_with_changes (✗) | **do_not_proceed (✓)** | 1/3 |
| Haiku | **do_not_proceed (✓)** | **do_not_proceed (✓)** | **do_not_proceed (✓)** | 3/3 |
| gpt-oss | **proceed_with_changes (✓)** | proceed_with_changes (✗) | **proceed_with_changes (✓)** | 2/3* |

*gpt-oss B seeds 1 and 3 scored fc=1.0 with proceed_with_changes. The correct decision for an artifact task is do_not_proceed. However, proceed_with_changes that explicitly flags LABEL_ERROR and LEAKAGE_LOOKAHEAD (B3) may be capturing the correct risk identification even if the decision enum doesn't match do_not_proceed.

**Key families retrieved in B:**

Haiku B seeds 1,2,3 all retrieved **FAM:SF-CHT-025** (Play-type labeling audit). This family states:
> "Only 335 of 50,668 possessions (0.7%) map to a real play type via initiation video. OTHER: 36% end in fouls (PPP inflated). DRIVE: 12pp below foul benchmark (FOUL_LEAK). PNR shows 22% foul rate."

This specific quantitative evidence — 99.3% of labels are inferred — was sufficient for Haiku to conclude the question cannot be answered with current labels. Haiku's p_testable dropped from 0.55–0.60 (A) to 0.25–0.30 (B), and all three seeds flipped to do_not_proceed.

Gemini B seeds 1,2 did **not** retrieve FAM:SF-CHT-025 as a top-3 result. Seed 1 retrieved FAM:SF-APPA-058 (negative teammate premiums — powered null), FAM:SF-APPS-011 (RS/playoff PPP — positive result), FAM:SF-APPM-022. These families confirm sequential effects are real, reassuring Gemini to proceed. Gemini B seed 3 retrieved FAM:SF-APPA-030 (label backfill verification, C_artifact), which provided enough labeling signal to flip to do_not_proceed.

### 2.3 Condition C (graph traversal)

| Model | Seed 1 | Seed 2 | Seed 3 | Correct/3 |
|-------|--------|--------|--------|-----------|
| Gemini | proceed_with_changes (✗) | proceed_with_changes (✗) | proceed_with_changes (✗) | 0/3 |
| Haiku | **do_not_proceed (✓)** | **do_not_proceed (✓)** | **do_not_proceed (✓)** | 3/3 |
| gpt-oss | **proceed_with_changes (✓)** | proceed_with_changes (✗) | proceed_with_changes (✗) | 2/3* |

*Same scoring note as B for gpt-oss proceed_with_changes.

Haiku C retrieved FAM:SF-CHT-025 in all three seeds (top-3 each time), maintaining perfect performance.

Gemini C retrieved FAM:SF-APPA-050, FAM:SF-APPM-022, FAM:SF07 in all three seeds. FAM:SF07 confirms "Sequential pair premium and defensive aftershock (8/8 PTs)" — a strong positive result. This leads Gemini to conclude sequential effects are real and the question is answerable. Gemini's graph traversal algorithm routes toward the sequential-effect cluster rather than the labeling-audit cluster.

---

## 3. Why All Three Models Fail in Condition A

### 3.1 The theoretical feasibility vs. data infrastructure gap

The question is theoretically testable: one could in principle construct a valid test using video-verified PNR labels. The data available (play-by-play, derived labels) makes the question appear practically testable too. Without knowing the specific artifact (calibrated-PNR temporal contamination), a reviewer following standard methodology would:

1. Check if sequential PPP differences can be computed — yes, the graph database has this
2. Identify labeling as a *potential* concern — all models do this
3. Conclude the question is testable with care — all models do this (incorrectly)

The gap is between "labeling concern is theoretically possible" and "labeling is specifically compromised in a way that produces the entire observed effect." The former is manageable; the latter is fatal. Without the archived audit result, this gap is unbridgeable from first principles.

### 3.2 The base-rate problem

The task is phrased as a positive claim ("ANY teammate DRIVE...raises..."), which sounds like a plausible causal question. All models generate plausible risk registers:
- OUTCOME_DERIVED_LABEL: present in Haiku A (correct risk)
- LABEL_ERROR: present in Gemini A seed 3 and Haiku A all seeds
- CONFOUNDING: universal
- EXPOSURE_SPARSITY: universal

The models cannot distinguish between a question where LABEL_ERROR is a theoretical concern and one where it is a fully documented, quantified, decisive flaw. In condition A, LABEL_ERROR appears in the risk list alongside 4–9 other risks, all weighted roughly equally. No model assigns it enough weight to halt the study unilaterally from prior reasoning alone.

### 3.3 Model-specific characterizations of the condition-A error

**Gemini (seed 3):** "Please proceed with extreme caution and address the identified risks before or during the analysis." Gemini identifies LABEL_ERROR but frames it as "proceed with caution" rather than halt. This is the correct-risk-wrong-action pattern.

**Haiku (all seeds):** Lists 8–10 risks including LABEL_ERROR, OUTCOME_DERIVED_LABEL, LEAKAGE_LOOKAHEAD. Decision: proceed_with_changes with p_testable=0.55. Haiku is actually the most risk-aware in condition A, but its conservative baseline still doesn't reach the do_not_proceed threshold without explicit disqualifying evidence.

**gpt-oss (seed 1):** Uniquely, halts with do_not_proceed. Risks: CONFOUNDING, EXPOSURE_SPARSITY, MEASURE_RELIABILITY, SAMPLE_SIZE_POWER. Notably does NOT list LABEL_ERROR as the primary concern — gets the right decision for partially wrong reasons (exposure sparsity and measurement reliability, not labeling artifact). This represents a correct decision from a different conceptual pathway.

---

## 4. Does RT-012 Represent a Benchmark Alignment Issue?

The answer key is derived from actual research history (confidence=1.0, high confidence) and the artifact is documented in the sources (play-type_labeling verification outputs). The answer key type states "automated from extracted records (rule-based adjudication); not independent human adjudication."

**Potential benchmark concerns:**

1. **Is the answer key correct?** The specific claim (+0.022 vanishes to −0.006 with inferrer-only PNR) is internally documented in the study family records with n=20,658 vs 159,623. This is a plausible and specific statistical claim. No conflicting evidence is recorded. The answer key appears correct.

2. **Is the task fair?** A pre-analysis reviewer without access to the archive *cannot* be expected to identify this specific artifact from first principles. The "knowable from history" designation is appropriate — it is knowable *from history*, not from the task statement alone. This makes RT-012 a task that specifically tests whether historical memory helps (not whether raw reasoning is sufficient). The benchmark design is internally consistent: condition A is expected to fail this task; conditions B/C should improve it.

3. **Does the "testable=True" key entry conflict with the "should_flag=True" key entry?** The answer key says both testable=True and should_flag_before_running=True. This is not a contradiction: the question is theoretically testable (one *could* build valid labels) but should be flagged because the *current* data infrastructure is compromised. The distinction is between "can this ever be answered" and "can this be answered with what's available now." Both can be true simultaneously.

4. **Why do models not detect the word "derived" as a disqualifier?** Models consistently treat "derived" as meaning "computationally processed" (which is normal for sports analytics) rather than "potentially contaminated." This is a reasonable interpretation — most analytics pipelines use derived labels and they work fine. Without a calibration audit showing the specific failure, "derived" does not trigger a halt.

**Conclusion:** RT-012 is correctly classified and correctly scored. The universal condition-A failure reflects a genuine capability limitation (models cannot detect undocumented specific labeling artifacts from first principles) and is not a benchmark design flaw.

---

## 5. Models Make Different Conceptual Mistakes

Despite the universal condition-A failure, the three models make distinct errors:

| Model | Primary A error | Secondary signals |
|-------|----------------|-------------------|
| Gemini | "Derived labels are manageable; DRIVE→PNR effects are real in other contexts" (appeals to plausibility of the mechanism) | References similar sequential effects, proceeds with design recommendations |
| Haiku | "Multiple risks exist; all are manageable with care" (comprehensive risk listing leads to proceed_with_changes even when LABEL_ERROR is explicitly listed) | Most risk-aware in A; highest p_testable of the three models (0.55–0.60) |
| gpt-oss | Mixed: seed 1 halts for wrong reasons (exposure/measurement), seeds 2-3 proceed citing standard methodological concerns | Lowest p_testable in A (0.40–0.60) |

These differences explain why gpt-oss gets 1/3 correct in A (right action, partly wrong reason) while Gemini and Haiku get 0/3 (proceed with design recommendations).

In conditions B/C, the models diverge based on **which families they retrieve**:
- Haiku: retrieves FAM:SF-CHT-025 (the labeling audit) → consistent correct decisions
- Gemini: retrieves sequential-effect families (SF07, SF-APPS-011) → consistent incorrect decisions in C; 1/3 correct in B only when FAM:SF-APPA-030 appears
- gpt-oss: retrieves FAM:SF-CHT-025 sometimes (B1, B3) → correct; retrieves sequential families other times → incorrect

The RT-012 failure pattern is not a case where models are uniformly confused about the answer — it's a case where **the correct evidence is available in the archive but is not consistently retrieved or properly weighted by all models in all conditions**.

---

## 6. Summary

1. All three models fail RT-012 in condition A because the specific labeling artifact (calibrated-PNR temporal contamination) is undocumented from first principles. Models correctly identify LABEL_ERROR as a *risk* but do not reach the threshold of halting the study.

2. Haiku achieves perfect accuracy (6/6) in conditions B and C because FAM:SF-CHT-025 is consistently retrieved, providing the specific disqualifying quantitative evidence.

3. Gemini fails all 3 seeds in condition C because graph traversal routes to sequential-effect families (FAM:SF07, FAM:SF-APPS-011) that reassure rather than warn. Gemini B is 1/3 correct (seed 3 retrieves a labeling-audit family).

4. gpt-oss is mixed: 1/3 correct in A by a different reasoning path, 2/3 in B, 2/3 in C (but scoring involves proceed_with_changes that flags correctly rather than do_not_proceed).

5. The task is correctly classified and correctly scored. The universal condition-A failure tests a genuine capability gap: without archive evidence of the specific artifact, models cannot halt this task.

6. **The practical implication**: a basketball analytics organization relying on AI design review without an archive of documented data-quality audits would receive a false-green on RT-012 in 8 of 9 cases (Gemini and Haiku condition A; all Gemini C). The data quality audit archive — specifically FAM:SF-CHT-025 — is the decisive factor, not the model's baseline reasoning.

---

*Generated from existing run outputs. No new experiments or API calls.*
