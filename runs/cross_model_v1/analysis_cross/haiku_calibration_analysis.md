# Haiku 5.5 Calibration Degradation Analysis

**Scope:** Haiku 5.5 only. 90 runs (10 tasks × 3 conditions × 3 seeds). Testability calibration = whether p_testable scores correctly rank tasks by their actual testability.  
**Background:** Cross-model report recorded Haiku testability AUC: A = 0.79, B = 0.62, C = 0.69.  
**No API calls. No new experiments. Existing data only.**

---

## 1. Framing: What "Testability Calibration" Means Here

In protocol 3, the model returns a `testability` block containing `p_testable` (a 0–1 probability). A perfectly calibrated model would assign high p_testable to genuinely testable tasks (strata: rejected, supported, uncertain — these should proceed) and low p_testable to tasks that should be halted (strata: artifact, untestable — these should not proceed, flag=True).

AUC measures how well p_testable discriminates between the two classes. An AUC of 0.79 in condition A means Haiku's prior p_testable scores correctly rank 79% of task pairs. The drop to 0.62 in B and 0.69 in C means memory degrades this discrimination.

This analysis asks: **which tasks and seeds drive the degradation, and through what mechanism?**

---

## 2. Haiku p_testable by Task, Condition, and Seed

### 2.1 Should-flag tasks (correct p_testable is LOW)

| Task | Stratum | A seeds 1,2,3 | B seeds 1,2,3 | C seeds 1,2,3 |
|------|---------|--------------|--------------|--------------|
| RT-012 | artifact | 0.60, 0.55, 0.55 | 0.30, 0.25, 0.30 | 0.25, 0.25, 0.35 |
| RT-014 | artifact | 0.30, 0.20, 0.20 | 0.10, 0.15, 0.20 | 0.12, 0.20, 0.35 |
| RT-179 | untestable | 0.30, 0.35, 0.45 | 0.30, 0.20, 0.40 | 0.55, 0.50, 0.35 |
| RT-183 | untestable | 0.12, 0.15, 0.10 | 0.15, 0.30, 0.20 | 0.20, 0.10, 0.20 |

**Correct direction for flag tasks: memory keeps p_testable low or pushes it lower.** RT-012 and RT-014 improve dramatically (0.55 → 0.25; 0.25 → 0.12). RT-183 is already very low in A and stays low. RT-179 is mostly stable except C seed 1 drifts up to 0.55 (2 incorrect C runs).

### 2.2 Should-proceed tasks (correct p_testable is HIGH)

| Task | Stratum | A seeds 1,2,3 | B seeds 1,2,3 | C seeds 1,2,3 |
|------|---------|--------------|--------------|--------------|
| RT-065 | rejected | 0.12, 0.15, 0.12 | 0.15, 0.20, 0.15 | 0.15, 0.30, 0.20 |
| RT-066 | rejected | 0.35, 0.45*, 0.30 | 0.35, 0.30, 0.35 | 0.55, 0.45, 0.55 |
| RT-101 | supported | 0.45, 0.45, 0.45 | 0.45, 0.40, 0.45 | 0.30, 0.40, 0.40 |
| RT-112 | supported | 0.50, 0.60, 0.50 | 0.60, 0.45, 0.45 | 0.60, 0.50, 0.50 |
| RT-146 | uncertain | 0.50, 0.60, 0.60 | 0.50, 0.45, 0.50 | 0.55, 0.50, 0.50 |
| RT-147 | uncertain | 0.60, 0.50, 0.65 | 0.25, 0.20, 0.20 | 0.45, 0.35, 0.35 |

*\* RT-066 seed 2 condition A was invalid output.*

**Key observations:**
1. **RT-065:** p_testable is extremely low (0.12–0.15) in condition A and remains low across B/C. This represents *persistent miscalibration from baseline*, not memory-induced degradation.
2. **RT-147:** p_testable drops dramatically from A (0.50–0.65) to B (0.20–0.25) → **this is the primary calibration degradation**. Condition C partially recovers (0.35–0.45) but does not return to A levels.
3. **RT-066:** Slight recovery in C (0.45–0.55), suggesting graph traversal helps more than document search.
4. **RT-101:** Mild downward drift in C seed 1 (0.45 → 0.30), contributing minor degradation.
5. **RT-112, RT-146:** Mostly stable; memory neither helps nor hurts.

---

## 3. Mechanism: Why Does B Degrade RT-147 Calibration?

### 3.1 What Haiku sees in condition B for RT-147

Haiku B retrieves (across all 3 seeds):
- **FAM:SF-APPA-050**: Superstar sequential suppression — not a hypothesis test (E_unclear)
- **FAM:SF-CHT-039**: Series-level AVOID share vs winning — **untestable (A_unanswerable)**, talent confound
- **FAM:SF-APPM-022**: Superstar suppression profiles — inconclusive (E_unclear)
- **FAM:SF-APPS-075**: Extended Possession Value (opponent T+1 suppression) — not a hypothesis test (E_unclear)
- **FAM:SF-APPS-015**: Player BEST/AVOID tier tendency — not a hypothesis test (E_unclear)

### 3.2 The conflation error

RT-147 asks whether **opponent next-possession PPP after you run play X is large enough to drive AVOID labels.** This is a measurement/effect-size question about a short-window sequential effect.

FAM:SF-CHT-039 asks whether **series-level AVOID share predicts winning**. This is labeled untestable due to talent confound — high-talent teams can afford to run AVOID plays less often. This is a completely different question about a different time horizon, but Haiku appears to interpret "the AVOID → winning link is untestable" as evidence that "AVOID-related questions are generally untestable."

**Effect in Haiku B RT-147:**
- Seed 1: p_testable 0.60 → 0.25; decision flips from proceed_with_changes to do_not_proceed (wrong)
- Seed 2: p_testable 0.50 → 0.20; same flip (wrong)
- Seed 3: p_testable 0.65 → 0.20; same flip (wrong)

All three seeds produce the same wrong decision in B. The retrieval pool includes FAM:SF-CHT-039 in all three B seeds (confirmed from retrieved_ids). In condition C (graph traversal), the AVOID-winning family is less prominent; the retrieved pool favors FAM:SF07 (D_positive sequential premium confirmation) more, explaining partial recovery to 0.35–0.45.

### 3.3 The "contamination by adjacent untestable family" pattern

This is a general failure mode, not just RT-147. When the archive contains a family that:
1. Shares topical vocabulary (AVOID, suppression, sequential, reliability)
2. Has a high-salience failure label (A_unanswerable, C_artifact)
3. Was classified as untestable for a reason that does NOT apply to the current task

…Haiku reduces its p_testable score for the current task, even when the retrieved family's failure mechanism is different. This is a calibration error: models should update p_testable based on *whether the retrieved family's failure applies here*, not simply *whether a failure occurred in the same domain*.

---

## 4. Distinguishing Calibration from Classification Accuracy

These are related but different:

**Calibration:** Does p_testable correctly rank tasks on a continuous scale? (AUC measure.)

**Classification accuracy:** Does the binary decision (do_not_proceed = flag) match the correct answer? (flag_correct measure.)

For Haiku these diverge in important ways:

| Condition | AUC (testability) | Flag accuracy (BA) |
|-----------|------------------|--------------------|
| A | 0.79 | 0.659 (high baseline) |
| B | 0.62 | 0.559 (drops) |
| C | 0.69 | 0.655 (partially recovers) |

The calibration degradation explains the classification drop: when Haiku incorrectly assigns low p_testable to testable tasks (RT-147 in B), those tasks flip from correct-proceed to incorrect-do_not_proceed, harming BA.

**Critically:** Haiku's calibration degradation is not symmetric. It improves substantially for should-flag tasks (especially RT-012) but degrades for should-proceed tasks (RT-147, RT-065 stays bad). The net effect is negative because the benchmark has 6 should-proceed tasks and 4 should-flag tasks — the improvements are numerically outweighed.

---

## 5. Task-Level Summary of Calibration Direction

| Task | Flag | Memory direction | Net effect on Haiku accuracy |
|------|------|-----------------|------------------------------|
| RT-012 | ✓ flag | **Improves** (p_testable drops from 0.55 to 0.25) | Positive: Haiku B/C 3/3 correct |
| RT-014 | ✓ flag | **Improves** (p_testable already low, stays low) | Neutral (already correct in A) |
| RT-179 | ✓ flag | **Mostly stable** (one C drift to 0.55) | Minor negative in C |
| RT-183 | ✓ flag | **Stable** (very low throughout) | Neutral |
| RT-065 | ✗ proceed | **No help** (p_testable stays ~0.12–0.20) | Neutral (already wrong in A) |
| RT-066 | ✗ proceed | **Mixed** (B stays low, C improves slightly) | Minor positive in C only |
| RT-101 | ✗ proceed | **Slight degradation** (C seed 1 drops to 0.30) | Minor negative |
| RT-112 | ✗ proceed | **Stable** (0.50–0.60 throughout) | Neutral |
| RT-146 | ✗ proceed | **Slight degradation** (B drops to 0.45–0.50) | Minor negative |
| RT-147 | ✗ proceed | **Large degradation** (B drops to 0.20–0.25) | Major negative: all 3 B seeds flip wrong |

---

## 6. Seed Consistency Assessment

RT-147 B degradation is fully seed-consistent: all 3 seeds degrade in exactly the same direction. This rules out a single-seed artifact. The same retrieved families appear in all three B seeds because the retrieval router returns the same top-k documents regardless of seed (seeds only affect the LLM's response, not the document retrieval). This means the calibration failure is **structural, not stochastic** — any Haiku run in condition B on RT-147 would likely produce the same miscalibration.

In contrast, RT-179 C seed 1 (p_testable 0.30 → 0.55) is seed-inconsistent: seeds 2 and 3 maintain correct low p_testable. This likely reflects a particular graph neighborhood traversal that returned FAM:SF18 (D_positive stability) prominently in seed 1.

---

## 7. Practical Implication

The degradation is not random — it follows a predictable pattern:

> **Haiku applies a "domain-level caution transfer": if any family in a retrieved set is labeled untestable, artifact, or inconclusive for reasons related to the query's domain, Haiku reduces p_testable for the current task, regardless of whether the retrieved family's failure mechanism applies here.**

For a basketball analytics organization using this benchmark:
- Haiku would be well-suited to screening tasks with known labeling problems (RT-012, RT-014) after document retrieval — it responds correctly to explicit audit evidence.
- Haiku would be poorly suited for tasks in well-studied domains where the archive contains older failed-for-different-reasons studies: it would over-flag testable questions, generating false-positive halts that block valid analyses.
- The condition B vs C difference (B=0.62, C=0.69) suggests graph traversal is somewhat better calibrated for Haiku, likely because the graph returns more direct mechanistic neighbors and fewer thematically-adjacent but mechanistically-unrelated families.

---

## 8. Summary

1. Haiku's testability AUC drops from 0.79 (A) to 0.62 (B) to 0.69 (C).
2. The primary driver is **RT-147 in condition B**: a systematic, seed-consistent miscalibration caused by the presence of FAM:SF-CHT-039 (AVOID-share vs winning, untestable due to talent confound) in the retrieval set. This unrelated untestable family causes Haiku to misclassify a testable sequential-effects question as untestable.
3. A secondary driver is **RT-065's persistent low p_testable** — this is not memory-induced but reflects an unresolved baseline miscalibration on this task across all conditions.
4. Memory *improves* calibration for should-flag tasks (RT-012, RT-014) but *degrades* it for should-proceed tasks (RT-147, mildly RT-101, RT-146).
5. Because the 10-task pilot has 6 should-proceed tasks and 4 should-flag tasks, the net calibration effect is negative.
6. This is a **calibration error, not a classification error at the individual-family level**: Haiku correctly identifies that FAM:SF-CHT-039 is untestable. The error is applying that finding to a different question in the same domain.

---

*Generated from existing run outputs. No new experiments or API calls.*
