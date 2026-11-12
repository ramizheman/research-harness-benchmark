# Mechanism-Level Transfer Analysis

**Scope:** 10 benchmark tasks × 3 models × 3 conditions × 3 seeds = 270 runs.  
**Data sources:** `runs/pilot3_v1/raw/`, `runs/cross_model_v1/raw/`, `_gathered.json`, `_fam_info.json`.  
**No API calls. No new experiments. Existing data only.**

---

## 1. Framework and Definitions

### 1.1 Classification categories

For every family retrieved in conditions B or C, each distinct (task, family) pair is classified as:

| Class | Definition |
|-------|-----------|
| **Mechanistically relevant (MR)** | Family's primary failure mechanism (auto_failure_mechanism) matches the task's expected failure code AND/OR the family's research question directly addresses the same data infrastructure or causal pathway the task depends on |
| **Topically similar, different mechanism (TS-DM)** | Same domain or outcome variable (e.g., play-type PPP, lineup effects) but the family's failure was for a different reason (e.g., powered null vs labeling artifact vs talent confound) |
| **Unrelated (UR)** | Different concept, different data layer, or different population from the task |
| **Ambiguous (AMB)** | Topical overlap is clear but the mechanism is not recorded (E_unclear) or the link to the task's specific failure requires inference beyond the record text |

A single retrieved family can **generate positive transfer** for one model and no transfer for another, depending on how the model weights it.

### 1.2 Transfer definitions

Counting is at the individual (model, condition, seed) run level:

- **Positive transfer (PT):** Run in B or C is flag-correct; the same model's condition-A run with the same seed was flag-incorrect.
- **Negative transfer (NT):** Run in B or C is flag-incorrect; the same model's condition-A run with the same seed was flag-correct.
- **No change – correct (NCC):** Both A and B/C are correct.
- **No change – incorrect (NCI):** Both A and B/C are incorrect.

Only valid-output runs (valid=1) are counted unless otherwise noted.

---

## 2. Per-Task Family Classification

### RT-012 — `stratum=artifact`, `flag=True`, `expected_risk=LABEL_ERROR`

**Research question:** "Any teammate DRIVE preceding a PNR raises PNR PPP."  
**True failure:** The +0.022 league-wide effect vanished to −0.006 once PNR was restricted to inferrer-only labels. Only 335 of 50,668 possessions (0.7%) map to a play type via initiation video; the rest are inferred. This calibrated-PNR temporal contamination is the sole source of the apparent effect.

**Families retrieved across all 27 runs (B and C):**

| Family | Question | Status | Mechanism | Classification |
|--------|----------|--------|-----------|----------------|
| FAM:SF-CHT-025 | Play-type labeling audit: OTHER/DRIVE foul leakage | artifact | C_artifact | **MR** — directly audits the labeling infrastructure that RT-012 depends on; quantifies 0.7% valid possession coverage |
| FAM:SF-APPA-030 | Play-type label backfill verification | inconclusive | C_artifact | **MR** — label backfill audit, same data layer; final verdict FAIL |
| FAM:SF-APPM-014 | Play-type label accuracy / distribution audit | not a hypothesis test | C_artifact | **MR** — audit of play-type derivation; DRIVE foul-draw 1.7% vs 14–22% benchmark |
| FAM:SF40 | Player and teammate sequential premiums | not a hypothesis test | E_unclear | **AMB** — same DRIVE→PNR sequential concept; LIM:label_or_classification_error noted; does not quantify the contamination |
| FAM:SF-APPA-058 | Season stability of top suppressors / negative teammate pairs | rejected | B_powered_null | **TS-DM** — includes Giannis→Lillard DRIVE→PNR −0.263, contradicting the hypothesis statistically; failure is powered null, not labeling artifact |
| FAM:SF07 | Sequential pair premium and defensive aftershock (8/8 PTs) | supported | D_positive | **TS-DM** — confirms sequential PPP premiums exist; actively misleads toward "proceed" by establishing sequential effects as real |
| FAM:SF-APPS-011 | Regular season vs playoff PPP by play type | supported | D_positive | **TS-DM** — PPP by play type, no label audit |
| FAM:SF-APPM-022 | Superstar suppression profiles | inconclusive | E_unclear | **AMB** — sequential triggering concept, no labeling fault |
| FAM:SF-APPA-050 | Superstar sequential suppression | not a hypothesis test | E_unclear | **AMB** — sequential effects at player level, no labeling fault |
| FAM:SF02 | Cost of ignoring suppression | inconclusive | none | **TS-DM** — sequential play continuation, LIM:label_or_classification_error noted |

**Classification summary:** 3 MR, 3 TS-DM, 0 UR, 3 AMB, 1 additional TS-DM.

**Transfer mechanism:** When FAM:SF-CHT-025 is retrieved (or FAM:SF-APPA-030), the specific quantitative fact — 99.3% of play-type labels are inferred from play-by-play rules, not video — provides a clear disqualifying signal. When FAM:SF07 is retrieved, models are reassured that sequential PPP effects exist and tend to proceed. The graph traversal (condition C) in seeds 1 and 3 returns FAM:SF-APPA-050 / FAM:SF-APPM-022 / FAM:SF07, none of which are MR, so Gemini C fails all 3 seeds.

---

### RT-014 — `stratum=artifact`, `flag=True`, `expected_risk=LEAKAGE_LOOKAHEAD`

**Research question:** "Adhering to a suppression-conditional recommended mix predicts winning."  
**True failure:** The recommended mix is generated by optimizing on the outcome of the same games used to test the prediction. The "recommendation" already knows which plays worked because it was derived post-hoc.

**Families retrieved (sample):**

| Family | Question | Status | Mechanism | Classification |
|--------|----------|--------|-----------|----------------|
| FAM:SF-APPA-008 | Audit of overnight LLM adaptation-analysis batch ('9/10 adaptation predicts winning') | artifact | C_artifact | **MR** — same "adaptation predicts winning" circularity; the audit found the LLM-based analysis was already looking at post-hoc outcomes |
| FAM:SF-CHT-039 | Series-level AVOID share vs winning (talent confound) | untestable | A_unanswerable | **TS-DM** — same win-prediction framing; failure is talent confound not lookahead |
| FAM:SF-APPS-027 | Adaptation quality vs talent as predictor of series wins | untestable | A_unanswerable | **TS-DM** — similar outcome variable; untestable reason different |
| FAM:SF-APPS-023 | System BEST vs constrained league mix | rejected | B_powered_null | **TS-DM** — recommendation quality, powered null |

**Note:** All models are already correct in condition A for RT-014 (all 9 A-runs flag correctly). Memory adds no further positive transfer. Negative transfer is also absent: all B/C runs are correct except Gemini C seed 3 (proceed_with_changes, fc=0). That one incorrect case represents an instance where the graph traversal retrieved ambiguous families that diluted the strong evidence for lookahead.

---

### RT-065 — `stratum=rejected`, `flag=False`, no relevant families in memory

**Research question:** "The teammate with the closest pre-absence initiation profile is the largest gainer when a key player is absent."

**Retrieval audit status:** No family in the archive directly addresses substitution-pattern role adoption during key-player absence. This task has no mechanistically relevant families in memory.

**Families retrieved (sample):**

| Family | Question | Status | Mechanism | Classification |
|--------|----------|--------|-----------|----------------|
| FAM:SF-APPS-088 | Offensive-identity resilience: connector absence vs usage-matched others | supported | D_positive | **TS-DM** — about connectors leaving, not about which teammate gains; different hypothesis, different methodology |
| FAM:SF35 | Next-game playing-time response to opponent 3P luck (carryover) | artifact | C_artifact | **UR** — carryover from opponent luck; unrelated |
| FAM:SF-PAP-068 | Opponent three-point luck has no persistent player component | supported | D_positive | **UR** — opponent 3P luck persistence; unrelated |
| FAM:SF-APPA-044 | Oracle player matchup specificity on BEST counters | supported | D_positive | **UR** — matchup counter quality; unrelated |
| FAM:SF-APPM-022 | Superstar suppression profiles | inconclusive | E_unclear | **UR** — star-level sequential suppression; unrelated |

**Classification summary:** 0 MR, 1 TS-DM, 3+ UR, several AMB.

**Key diagnostic:** All three models over-flag RT-065 in condition A already (p_testable = 0.05–0.15), so the failure is not caused by memory — it predates retrieval. Memory does not improve this: retrieved families are unrelated, and models continue to flag. The task involves measuring "who gains the most usage when player X is absent," which requires per-game usage reassignment data that is logistically available but methodologically complex (which teammate pattern is "closest" requires defining a distance metric). Models likely flag because the question sounds like RTM/selection — the biggest gainer might simply be whoever starts most often — and they have no archive evidence to counter this conservative reading.

---

### RT-066 — `stratum=rejected`, `flag=False`, `expected_risk=SAMPLE_SIZE_POWER`

**Research question:** "How much the offense reorganizes (relative to L) predicts the change in PPP."

**Families retrieved (sample):**

| Family | Question | Status | Mechanism | Classification |
|--------|----------|--------|-----------|----------------|
| FAM:SF-APPS-088 | Offensive-identity resilience: connector absence | supported | D_positive | **MR** — directly shows that offensive reorganization is measurable and has a real effect; same data layer |
| FAM:SF-APPS-067 | Opponent action T → your offense T+1 | supported | D_positive | **TS-DM** — sequential reorganization but at the possession level, not the lineup level; different time scale |
| FAM:SF-APPS-041 | PUTBACK suppression matched-pair isolation | artifact | C_artifact | **UR** — star vs team putback suppression; unrelated |
| FAM:SF-APPS-043 | PNR suppression RTM-excess | not a hypothesis test | A_unanswerable | **TS-DM** — RTM in suppression context, not reorganization prediction |

**Classification summary:** 1 MR, 2 TS-DM, 1+ UR.

**Transfer mechanism:** FAM:SF-APPS-088 is mechanistically relevant — it establishes that reorganization metrics are measurable and that connector absence has a positive, estimable effect. However, its main finding is about *whether effects exist* (D_positive), not about the *sample size* problem that RT-066 is flagging with SAMPLE_SIZE_POWER. Models that retrieve FAM:SF-APPS-088 and weighted it as reassuring evidence proceed correctly; models that weigh artifact families more heavily flag incorrectly.

---

### RT-101 — `stratum=supported`, `flag=False`

**Research question:** "Lineup coverage (≥1 organizer, shaper, terminal) varies within team, is separable from talent/counts, and talent control behaves."

**Families retrieved (sample):**

| Family | Question | Status | Mechanism | Classification |
|--------|----------|--------|-----------|----------------|
| FAM:SF18 | Fragility confirmatory: F1a usage decoupling and F1b split-half stability of residual influence | supported | D_positive | **MR** — directly addresses whether lineup role metrics are separable from talent and stable; the split-half stability sub-test is the closest archive test to RT-101's hypothesis |
| FAM:SF-CHT-039 | Series-level AVOID share vs winning (talent confound) | untestable | A_unanswerable | **TS-DM** — same talent-confound concern; different question |
| FAM:SF-CHT-009 | Superstar suppression by lineup and forced play type | not a hypothesis test | E_unclear | **AMB** — lineup effects on outcomes; not the same question but shares the "lineup as unit" framing |
| FAM:SF-APPS-027 | Adaptation quality vs talent | untestable | A_unanswerable | **TS-DM** — talent confound again; different framing |

**Transfer problem:** FAM:SF18's positive split-half stability result is the correct anchor for RT-101 (a supported task). However, models retrieve it alongside FAM:SF-CHT-039 and FAM:SF-APPS-027, both A_unanswerable with talent confounds. The weight given to the two "untestable" families typically exceeds the single positive, and all three models flag RT-101 in most B/C runs — a systematic case of negative transfer from archive-level caution.

---

### RT-112 — `stratum=supported`, `flag=False`, `expected_risk=PLACEBO_DEPENDENCE`

**Research question:** "Changing the offensive five itself moves shot mix, showing the design can detect personnel effects."

**Families retrieved:**

| Family | Question | Status | Mechanism | Classification |
|--------|----------|--------|-----------|----------------|
| FAM:SF34 | Opponent lineup adaptation: shot mix when opposing rim big is off floor | inconclusive | none | **MR** — directly tests whether shot mix responds to personnel changes; same outcome variable, same design concept |
| FAM:SF32 | Opener recommendations vs personnel feasibility | artifact | C_artifact | **TS-DM** — personnel system, different failure (feasibility) |
| FAM:SF-TMP-009 | PULL_UP exposure-effect diagnostics | artifact | C_artifact | **TS-DM** — play-type labeling artifact; different mechanism |
| FAM:SF-CHT-037 | Sequence-memory lag effects with game-state controls | artifact | C_artifact | **TS-DM** — lag structure artifact; different mechanism |
| FAM:SF-CHT-029 | Persistent Impact Score Level 1 gate | artifact | C_artifact | **TS-DM** — persistence artifact; different mechanism |

**Classification summary:** 1 MR, 4+ TS-DM, 0 UR.

**Note:** RT-112 is the best-performing task for all models. FAM:SF34 anchors the correct reading (shot mix is measurable and responds to roster), and the artifact families (SF32, SF-TMP-009, etc.) are sufficiently different in mechanism that models don't treat them as disqualifying. This is the cleanest example of MR-family-driven positive calibration.

---

### RT-146 — `stratum=uncertain`, `flag=False`

**Research question:** "If PNR fails, PULL_UP is a real league-wide counter; should show lift>0 in ≥70% of units with median lift>2pp."

**Families retrieved:**

| Family | Question | Status | Mechanism | Classification |
|--------|----------|--------|-----------|----------------|
| FAM:SF-APPS-011 | Regular season vs playoff PPP by play type | supported | D_positive | **MR** — contains PULL_UP +0.301 PPP in RS vs playoffs, directly showing PULL_UP behaves differently from DRIVE, which supports the testability of the counter hypothesis |
| FAM:SF12 | A1 within-scheme re-test controlling early-third PPP selection | inconclusive | E_unclear | **AMB** — scheme analysis; unclear connection |
| FAM:SF-APPM-022 | Superstar suppression profiles | inconclusive | E_unclear | **AMB** — sequential triggering; partial overlap |
| FAM:SF-APPM-058 | PNR shot-level season rates vs possession labels | not a hypothesis test | E_unclear | **TS-DM** — PNR volume data; different question |

**Key finding:** gpt-oss consistently flags RT-146 across all 6 B/C runs (do_not_proceed) despite the correct answer being to proceed. gpt-oss A correctly proceeds in 2/3 seeds. This is systematic negative transfer for gpt-oss on RT-146. The retrieved families (mostly AMB and TS-DM) seem to activate gpt-oss's conservative bias around "PULL_UP validity." In contrast, Gemini correctly proceeds in 5/6 B/C runs, apparently weighting FAM:SF-APPS-011's positive PULL_UP finding.

---

### RT-147 — `stratum=uncertain`, `flag=False`

**Research question:** "Opponent next-possession PPP after you run play X is large enough to drive AVOID labels."

**Families retrieved:**

| Family | Question | Status | Mechanism | Classification |
|--------|----------|--------|-----------|----------------|
| FAM:SF07 | Sequential pair premium and defensive aftershock (8/8 PTs) | supported | D_positive | **MR** — directly confirms that opponent next-possession PPP after your play type is systematically elevated, at scale (8/8 play types across all games and playoffs) |
| FAM:SF-APPS-075 | Extended Possession Value (direct PPP + opponent T+1 suppression) | not a hypothesis test | E_unclear | **MR** — quantifies opponent T+1 suppression component, the exact EPV mechanism the task asks about |
| FAM:SF-APPA-050 | Superstar sequential suppression | not a hypothesis test | E_unclear | **AMB** — opponent-play → star-efficiency sequence; related causal direction |
| FAM:SF-CHT-039 | Series-level AVOID share vs winning (talent confound) | untestable | A_unanswerable | **TS-DM** — AVOID concept present but untestable due to talent confound, different from RT-147's question about the effect size |

**Transfer insight:** FAM:SF07's positive confirmation of defensive aftershock is strongly MR. Gemini correctly proceeds (5/6 B/C runs correct). Haiku, however, weights FAM:SF-CHT-039 heavily — when Haiku B retrieves the untestable "AVOID share vs winning" family, its p_testable drops from 0.50–0.65 (A) to 0.20–0.25 (B). This is the clearest case of **negative transfer**: FAM:SF-CHT-039, while topically related, is about a different and harder testability question; Haiku conflates "AVOID's relation to winning is untestable" with "the opponent-T+1 effect is untestable," producing systematic over-flagging.

---

### RT-179 — `stratum=untestable`, `flag=True`, `expected_risks=[MEASURE_RELIABILITY, MECHANICAL_FLOOR]`

**Research question:** "A defense's effect on opponents' H2-H1 change is a reliable team trait."

**Families retrieved:**

| Family | Question | Status | Mechanism | Classification |
|--------|----------|--------|-----------|----------------|
| FAM:SF-APPA-005 | Defensive scheme change within game and across games (inferred labels) | untestable | A_unanswerable | **MR** — same question about whether defensive attributes can be reliably labelled and measured game-by-game; directly establishes that inferred defensive labels are too sparse for reliability analysis |
| FAM:SF-APPS-085 | Connector teammate-path quality split-half reliability | untestable | A_unanswerable | **MR** — split-half reliability test on a different derived metric; directly quantifies how reliability analyses fail for low-frequency derived statistics |
| FAM:SF18 | Fragility confirmatory: F1b split-half stability of residual influence | supported | D_positive | **AMB** — split-half stability confirmed for a different metric; could be read as supportive OR as showing the threshold RT-179 doesn't meet |
| FAM:SF-APPS-014 | Within-game DRIVE decline by game third | rejected | B_powered_null | **TS-DM** — within-game patterns but different metric |
| FAM:SF-APPS-073 | Persistent Impact Score lag curves | artifact | C_artifact | **TS-DM** — lag artifacts in a persistence metric; different metric |

**Classification summary:** 2 MR, 2 TS-DM, 1 AMB.

**Note:** RT-179 has the strongest MR-family presence (FAM:SF-APPA-005, FAM:SF-APPS-085), and all three models flag correctly in most conditions. Haiku C fails 2/3 seeds — Haiku's graph traversal in C retrieves FAM:SF18 (D_positive) prominently, and Haiku occasionally interprets positive split-half stability evidence as evidence that RT-179's question is also answerable.

---

### RT-183 — `stratum=untestable`, `flag=True`, `expected_risk=SAMPLE_SIZE_POWER`

**Research question:** "Cut-heavy shapers' roles travel better than drive-heavy ones."

**Families retrieved:**

| Family | Question | Status | Mechanism | Classification |
|--------|----------|--------|-----------|----------------|
| FAM:SF-APPS-088 | Offensive-identity resilience: connector absence | supported | D_positive | **TS-DM** — player role stability; different player type and different time horizon |
| FAM:SF-APPS-009 | Player routing V4 vs V5 direct scoring | untestable | A_unanswerable | **MR** — routing/role stability across system versions; untestable for same sample-size reason |
| FAM:SF-APPS-036 | Player-level BEST vs AVOID PPP gap | supported | D_positive | **TS-DM** — player role effectiveness; different question |
| FAM:SF-APPS-087 | Connector tangible impact: star shielding, TO, lineup lift | rejected | B_powered_null | **TS-DM** — connector role impact; sample-size limited but powered null |

**Classification summary:** 1 MR, 3 TS-DM, 0 UR.

**Note:** All models correctly flag RT-183 in the majority of conditions. The sample-size reason (no multi-season tracking of cut vs drive shapers' roles across trades/free-agent moves) is detectable from first principles, and even in condition A all models flag correctly. FAM:SF-APPS-009 (MR) reinforces this reading in B/C.

---

## 3. Aggregate Transfer Counts

The following counts use only valid-output runs in conditions B and C, compared against the same model's condition-A run at the same seed.

| Task | PT | NT | NCC | NCI | Notes |
|------|----|----|-----|-----|-------|
| RT-012 | 7 | 0 | 1 | 10 | Haiku B/C all correct (+6); gpt-oss B3 correct (+1); Gemini A 0/3 correct |
| RT-014 | 0 | 1 | 16 | 0 | All A correct; Gemini C3 regresses to wrong |
| RT-065 | 2 | 0 | 0 | 14 | Only isolated Gemini C2, gpt-oss C3 correct; all others wrong in both |
| RT-066 | 2 | 0 | 6 | 8 | Haiku C1, C3 positive; Gemini mostly stable-correct |
| RT-101 | 0 | 3 | 2 | 11 | Gemini A all correct; Gemini C1 flips wrong (NT×3 via Gemini) |
| RT-112 | 1 | 1 | 14 | 1 | One gpt-oss A1 wrong→B correct (PT); one Haiku B2 correct→wrong (NT) |
| RT-146 | 0 | 4 | 10 | 3 | gpt-oss systematic NT (4/6 B/C runs where A was correct) |
| RT-147 | 0 | 6 | 9 | 2 | Haiku B systematic NT (all 3); gpt-oss B3 NT |
| RT-179 | 3 | 2 | 12 | 0 | gpt-oss gains in C (PT); Haiku C loses (NT) |
| RT-183 | 0 | 0 | 17 | 1 | Near-universal correct, memory adds nothing |
| **Total** | **15** | **17** | **87** | **50** | Slight net-negative transfer overall |

---

## 4. Model-Level Transfer Patterns

### Gemini (Pilot 3 reference)
- **PT:** 6 (primarily RT-012 B3, RT-066 B/C, RT-179 C)
- **NT:** 4 (RT-014 C3, RT-101 C1, RT-147 C2, some RT-183)
- **Mechanism:** Gemini's graph traversal (C) tends to return sequential-effect families (SF07, SF-APPS-011) that confirm effects are real; this helps on should-proceed tasks but fails to retrieve labeling-audit families for should-flag artifact tasks.

### Haiku 5.5
- **PT:** 6 (RT-012 B×3 and C×3 — all correct after FAM:SF-CHT-025 retrieved)
- **NT:** 6 (RT-147 B×3 systematic; plus isolated cases in RT-101 and RT-179)
- **Mechanism:** Haiku is maximally responsive to MR families when retrieved: FAM:SF-CHT-025's specific quantitative disqualification completely flips RT-012. But Haiku is also the most susceptible to AMB families: FAM:SF-CHT-039 (untestable due to talent confound) is routinely retrieved for RT-147 and causes systematic over-flagging. Haiku appears to apply a broad "any untestable archive finding in this domain → flag this too" heuristic.

### gpt-oss-20b
- **PT:** 3 (RT-012 B1, B3; RT-179 C1,C2)
- **NT:** 7 (RT-146 systematic ×4; RT-147 B3; RT-183 C; RT-101 B1)
- **Mechanism:** gpt-oss's most consistent failure mode is systematic negative transfer on uncertain tasks (RT-146, RT-147) where its conservative prior causes over-flagging regardless of memory condition. Protocol issues (25 repair turns, 11 invalid outputs) add noise but don't systematically bias in one direction.

---

## 5. Cross-Task Mechanism Patterns

### 5.1 Labeling-artifact tasks (RT-012, RT-014)

Memory genuinely helps — but only when the right families are retrieved. The labeling-audit families (FAM:SF-CHT-025, FAM:SF-APPA-030, FAM:SF-APPM-014) are mechanistically indispensable. When graph traversal returns sequential-effect families instead, the models lose the labeling signal.

**Design implication:** The retrieval router should weight C_artifact families more heavily for tasks that use derived play-type records.

### 5.2 No-relevant-family tasks (RT-065)

Memory cannot help tasks that have no relevant families in the archive. All three models over-flag RT-065 from baseline, and retrieval of TS-DM and UR families reinforces this. The benchmark is testing whether models can recognize a task is genuinely under-studied — but the models interpret "under-studied" as "too risky to proceed."

### 5.3 Untestable tasks with MR families (RT-179, RT-183)

These tasks are the most robust. MR families (especially A_unanswerable: reliability tests, routing version tests) give a clear, task-congruent signal and all models respond correctly.

### 5.4 Testable tasks with mixed archive evidence (RT-101, RT-147, RT-146)

These produce the most negative transfer. D_positive MR families compete with A_unanswerable TS-DM families, and the models' priors determine which wins. Haiku defaults to caution (TS-DM families win), Gemini defaults to trust (MR D_positive families win), gpt-oss is inconsistent.

---

## 6. Summary

- Mechanism-level retrieval produced **positive transfer in 15 run-instances** and **negative transfer in 17** — a slight net-negative effect.
- Positive transfer is concentrated in two tasks: RT-012 (labeling artifact identified by Haiku when FAM:SF-CHT-025 retrieved) and RT-179 (reliability failure identified correctly).
- Negative transfer is concentrated in three tasks: RT-147 (Haiku over-flags due to AMB TS-DM family FAM:SF-CHT-039), RT-146 (gpt-oss systematic conservatism), and RT-101 (all models deflected by talent-confound archive entries).
- **The primary driver of negative transfer is topically-similar families whose mechanism does not match the task's failure mode** — models treat any cautionary archive finding in the same domain as disqualifying evidence for the current task, regardless of mechanism.

---

*Generated from existing run outputs. No new experiments or API calls.*
