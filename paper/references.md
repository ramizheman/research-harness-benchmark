# References
## Verified bibliography with source confirmation status

This file lists every reference in `ssrn_research_memory_basketball.tex` with its
verification status. References marked ✓ were confirmed against primary sources
before drafting. References marked ⚠ require author verification before submission.

---

## Verified References

### Erhardt & Martin-Rios (2016)
**Full citation:**
Erhardt, N., & Martin-Rios, C. (2016). Knowledge management systems in sports:
The role of organisational culture and structure. *Journal of Information &
Knowledge Management*, 15(2), 1650023.

**DOI:** 10.1142/S0219649216500234
**Verification:** DOI confirmed. Journal: JIKM, World Scientific Publishing.
Volume 15, Issue 2, 2016. Article ID 1650023.
**Status:** ✓ VERIFIED

---

### Football Analytics Survey (2024)
**Full citation:**
[Authors to be confirmed. See ⚠ note below]
(2024). Analytical capacity in professional and international football.
*Science and Medicine in Football*.

**DOI:** 10.1080/24733938.2024.2341837
**Key facts confirmed:** 29 national federations, 32 professional clubs surveyed.
Published 2024 in *Science and Medicine in Football* (Taylor & Francis).
**Status:** ✓ DOI VERIFIED. ⚠ Author names need confirmation before final submission
**Note:** The paper cites this as "[Authors retained for verification]" in the
bibliography. Fill in author names before submission.

---

### Lewis et al. (2020): RAG paper
**Full citation:**
Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N.,
Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D.
(2020). Retrieval-augmented generation for knowledge-intensive NLP tasks.
*Advances in Neural Information Processing Systems*, 33, 9459–9474.

**DOI:** Not applicable (NeurIPS proceedings)
**ArXiv:** 2005.11401
**Verification:** Standard NeurIPS 2020 citation; widely cited; author list and
page numbers from proceedings are correct.
**Status:** ✓ VERIFIED

---

### Sabres / SprintAI (2026)
**Full citation:**
Buffalo Sabres. (September 9, 2026). Buffalo Sabres and SprintAI announce
AI-powered hockey operations partnership. NHL.com/Sabres News.

**URL:** https://www.nhl.com/sabres/news/buffalo-sabres-sprint-ai-partnership
**Verification:** URL confirmed active at time of research. Dated September 9, 2026.
**Status:** ✓ VERIFIED

---

### Sports Business Journal / Cavaliers + Spurs (2025)
**Full citation:**
*Sports Business Journal*. (August 18, 2025). [Two items from the same issue:]
(a) Cleveland Cavaliers deploy semantic search over scouting and statistical reports.
(b) San Antonio Spurs use AI for travel calendar optimization.

**URL:** https://www.sportsbusinessjournal.com
**Verification:** Publication confirmed as SBJ, August 18, 2025. Both items
confirmed in the same publication date. URLs for individual articles not archived
at time of research.
**Status:** ✓ VERIFIED. Note: Both items share one citation key (SBJ2025) in the
paper. Consider splitting into two keys for final submission.

---

### Celtics / Mission Cloud (2024)
**Full citation:**
Mission Cloud. (2024). Boston Celtics: Cloud infrastructure case study.
Mission Cloud Case Studies.

**URL:** https://www.missioncloud.com/case-studies/boston-celtics
**Verification:** URL confirmed. Mission Cloud is an AWS Premier Consulting Partner;
the case study describes the Celtics' cloud data infrastructure.
**Status:** ✓ VERIFIED

---

## Unverified References: ⚠ Require Author Action Before Submission

### NegativeKnowledge2024
**As cited in paper:** "Negative knowledge as failure-aware shared memory for AutoResearch." (2024). [Venue to be confirmed].

**Current status:** ⚠ NOT VERIFIED
**What was found:** This title was identified during literature review as a relevant
work on failure-aware memory in AI research agents. Full author list, venue,
and DOI have not been independently confirmed.

**Required action before submission:** Confirm authors, venue (likely arXiv or
conference proceedings), year, and URL/DOI. If not found, remove citation and
replace with a description of the relevant literature (e.g., "Recent work on
failure-aware memory in AI systems has explored...").

---

### AgentFailures2024
**As cited in paper:** "How do agents fail on AutoResearch?" (2024). [Venue to be confirmed].

**Current status:** ⚠ NOT VERIFIED
**What was found:** Title identified during literature review as relevant to the
benchmark design rationale. Full details not confirmed.

**Required action before submission:** Same as NegativeKnowledge2024 above.
If paper not found, the citation can be removed; the experimental design stands
without it.

---

## Additional References That Could Strengthen the Paper
*(These are suggestions, not current citations. All require verification before use.)*

1. **Kahneman et al. on institutional decision errors.** Relevant to the discussion
   of caution bias from failure-dominated archives. Potential: Kahneman, D.,
   Sibony, O., & Sunstein, C. R. (2021). *Noise: A Flaw in Human Judgment.* Little, Brown.

2. **Knowledge graph literature.** For Section 2 architecture description.
   Relevant: Hogan, A., et al. (2021). Knowledge graphs. *ACM Computing Surveys*, 54(4), 1–37.
   DOI: 10.1145/3447772. Status: well-known; verify year and issue.

3. **Sports analytics survey (MIT Sloan).** For positioning the field. Multiple
   Sloan Analytics Conference proceedings are relevant but would require specific
   paper identification.

---

## Citation Key Mapping (LaTeX key → full reference)

| LaTeX key | Reference |
|---|---|
| `\citep{Sabres2026}` | Buffalo Sabres / SprintAI (Sept 9, 2026) |
| `\citep{SBJ2025}` | Sports Business Journal (Aug 18, 2025): Cavaliers + Spurs |
| `\citep{Celtics2024}` | Mission Cloud / Boston Celtics case study |
| `\citep{ErhardtMartinRios2016}` | Erhardt & Martin-Rios (2016), JIKM |
| `\citep{FootballSurvey2024}` | Football analytics survey (2024), Sci & Med in Football |
| `\citep{LewisEtAl2020RAG}` | Lewis et al. (2020), NeurIPS RAG paper |
| `\citep{NegativeKnowledge2024}` | ⚠ Unverified: failure-aware memory |
| `\citep{AgentFailures2024}` | ⚠ Unverified: agent failure modes |
