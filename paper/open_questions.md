# Open Questions
## Genuine unresolved issues requiring author review before submission

This file contains only items that require a decision or verification from the
author. It does not list solved issues, limitations that are already disclosed in
the paper, or stylistic preferences.

---

## 1. Two Unverified Citations: Must Resolve Before Submission

### NegativeKnowledge2024 and AgentFailures2024

The paper's related-work section cites two papers by title:
- "Negative knowledge as failure-aware shared memory for AutoResearch"
- "How do agents fail on AutoResearch?"

These titles were identified during the literature review as relevant, but their
authors, venues, DOIs, and publication years were not independently confirmed during
the experiment phase.

**Required action:**
- Search arXiv, Semantic Scholar, or Google Scholar for each title
- If found: add full citation to `references.md` and update `ssrn_research_memory_basketball.tex` bibliography entries
- If not found: remove the `\citep{}` references and replace the relevant paragraph in Section 3.3 with:

  > "Recent work on AI agent failure modes has begun to treat recorded failures as
  > first-class knowledge [CITE or rephrase without citation]. The argument is that
  > knowing what does not work, and understanding why, is as important as knowing
  > what does."

This is the most important open item. Do not submit with placeholder citations.

---

## 2. Football Survey Author Names

The citation `\citep{FootballSurvey2024}` in the paper reads:
> [Authors retained for verification; see paper/references.md]

The DOI (10.1080/24733938.2024.2341837) and the key facts (29 federations, 32
clubs, *Science and Medicine in Football*, 2024) are verified. The author names
were not confirmed during drafting.

**Required action:** Look up the paper at
https://doi.org/10.1080/24733938.2024.2341837 and fill in the author list in
the `\bibitem` entry in the .tex file.

---

## 3. RT-012 Haiku Condition A Discrepancy

The paper text (Section 7.2) states: "Without memory, this task is consistently
difficult: Gemini condition A is wrong in 3 of 3 seeds; Haiku is wrong in 3 of 3."

However:
- `cross_model_report.md` Section 4 task table shows Haiku A = 0.333 (implying 1/3 seeds correct)
- `rt012_diagnosis.md` states "A: Haiku 0/3 correct"
- The audit script (`verify_numbers.py`) returns Haiku A = 0.00 for RT-012

The most likely resolution: the cross_model_report.md table shows valid-output-only
rates, and one Haiku A seed may have been invalid. But this should be confirmed.

**Required action:**
```python
# Run in the project directory to verify:
import csv
rows = list(csv.DictReader(open('runs/cross_model_v1/scores.csv')))
rt012_haiku_a = [r for r in rows
                 if r['task_id']=='RT-012'
                 and 'haiku' in r['model']
                 and r['condition']=='A']
for r in rt012_haiku_a:
    print(r['seed'], r['valid_output'], r['flag_correct'])
```
If Haiku A has 1 valid correct run (not 0), revise the paper text accordingly.

---

## 4. SBJ2025 Citation: Consider Splitting

The paper cites both the Cavaliers semantic search story and the Spurs travel
calendar story under a single citation key (`SBJ2025`). Both appeared in the
*Sports Business Journal* on August 18, 2025.

**Required action:** Decide whether to split into two separate `\bibitem` entries
for clarity. If kept as one, confirm the footnote is sufficient to identify both
items. Neither item affects a quantitative claim.

---

## 5. Pilot 1 and Pilot 2 Exact Run Counts and Costs

The paper reports "~30 runs" for Pilot 1 and Pilot 2 and costs as "< $0.10 each."
These are estimates from the architecture description in the Pilot 3 report, which
compares against "Pilot 1 (recovered outputs) and Pilot 2 used seed 1 only" and
"30 B runs and 30 C runs" for pilot comparisons.

**Required action (low priority):** If exact numbers matter for the paper, run:
```
Get-ChildItem runs\pilot1_v1\*.json | Measure-Object
Get-ChildItem runs\pilot2_v1\*.json | Measure-Object
```
or check the relevant config files to confirm run counts.

---

## 6. Appendix A Table: Haiku A Row for RT-012

The Appendix A task table shows Haiku A = .00 for RT-012 (from the verify script).
If item #3 above resolves to Haiku A = 0.333, the table value should be updated
to .33. The table was drawn from SCORES-CM via the audit script.

---

## Items Confirmed NOT Open Questions

The following were considered but resolved:

- **Gemini B discrepancy (0.681 vs 0.669):** Resolved. 0.681 is the primary metric
  (invalids count as wrong); 0.669 is valid-only. Paper uses 0.681 with a footnote.
  Both numbers are disclosed.
- **Transfer count basis (169 vs 180):** The 169 figure in Section 7 refers to
  classified memory runs where both the treatment and control run were valid enough
  to classify. The 180 figure is total memory runs. Both are sourced from
  CM-INT sec.2.1. Resolved by saying "169 condition comparisons."
- **Citation fabrication in gpt-oss:** Confirmed as schema formatting artifacts
  (non-existent family IDs in structure fields), not hallucinated findings.
  Consistent with "zero fabricated citations" claim.
- **Haiku risk recall (0.90 vs 0.639 for Gemini):** These are different models.
  The 0.90 value is for Haiku; the 0.639 is for Gemini condition A.
  No inconsistency.
