r"""Build the experiment inventory, both memory conditions, and the audit tables from the research ledger.

Inputs (read-only):
  memory\ledger_merged.jsonl          merged records (built by 00_merge_ledger.py from Research Ledger\raw\*.jsonl)
  Research Ledger\raw\*.jsonl         slice files, for provenance and superseded versions
  Research Ledger\scratch\chats\*.txt condensed chat transcripts (number checks for chat-sourced records)
Outputs (all inside Research Harness Benchmark):
  experiment_inventory.csv
  memory\documents\<id>.md            condition B: one searchable document per experiment
  memory\graph_nodes.jsonl, memory\graph_edges.jsonl   condition C
  audit\*.csv, audit\tables.md
Every derived value is produced by a keyword rule listed in this file; rule names are stored with the value.
"""
import collections
import csv
import glob
import json
import os
import re

BB = r"C:\Users\lisas\OneDrive\Documents\Basketball"
LEDGER = os.path.join(BB, "Research Ledger")
OUT = os.path.join(BB, "Research Harness Benchmark")
for d in ("memory", os.path.join("memory", "documents"), "audit"):
    os.makedirs(os.path.join(OUT, d), exist_ok=True)

rows = [json.loads(l) for l in open(os.path.join(OUT, "memory", "ledger_merged.jsonl"), encoding="utf-8") if l.strip()]
raw = {}
slice_of = {}
for f in sorted(glob.glob(os.path.join(LEDGER, "raw", "*.jsonl"))):
    for l in open(f, encoding="utf-8"):
        if l.strip():
            r = json.loads(l)
            raw.setdefault(r["id"], []).append(r)
            slice_of.setdefault(r["id"], os.path.basename(f))
for r in rows:
    slice_of[r["id"]] = r.get("slice_file", slice_of.get(r["id"], ""))

# Study families: records that describe one study (duplicates) or reruns of one design, from manual review.
SLICE_RANK = {"PAP": 0, "TMP": 1, "APPA": 2, "APPM": 3, "APPS": 4, "CHT": 5}
family_of, family_kind, family_members, family_note = {}, {}, {}, {}
for fr in csv.DictReader(open(os.path.join(OUT, "audit", "study_family_review.csv"), encoding="utf-8")):
    members = [m.strip() for m in fr["members"].split(";")]
    family_members[fr["family_id"]] = members
    family_kind[fr["family_id"]] = fr["kind"]
    family_note[fr["family_id"]] = (fr["evidence"] + (" | " + fr["note"] if fr["note"] else "")).strip()
    for m in members:
        family_of[m] = fr["family_id"]
for r in rows:
    if r["id"] not in family_of:
        family_of[r["id"]] = "SF-" + r["id"]
        family_members["SF-" + r["id"]] = [r["id"]]
        family_kind["SF-" + r["id"]] = "single_record"
by_rec = {r["id"]: r for r in rows}
unknown = [m for ms in family_members.values() for m in ms if m not in by_rec]
assert not unknown, f"family members not in ledger: {unknown}"
family_rep = {f: min(ms, key=lambda i: (SLICE_RANK[i.split('-')[0]], i)) for f, ms in family_members.items()}

FAILED = {"null", "artifact_found", "failed_gate", "abandoned", "reversed", "tool_eval_fail"}
PAPERS = {"Structural Influence (Paper 1)": "Structural Influence (published)",
          "When a Hub Sits (Paper 2)": "When a Hub Sits (manuscript)",
          "Defensive Suppression": "Detecting Defensive Suppression (published)",
          "Halftime Minutes": "Halftime Minutes (manuscript)"}


def text(r, *fields):
    return " ".join(str(r.get(f) or "") for f in fields).lower()


# ---------------------------------------------------------------- keyword rules
TOPIC_RULES = [
    ("NCAA tournament prediction", r"march madness|ncaa|kenpom|brier|\bseed|538|women'?s|men'?s 2025|bracket"),
    ("Play-type labeling and data quality", r"label|backfill|classifier|accuracy audit|distribution audit|insuff_evidence|patternquerylayer|pattern audit"),
    ("Playing time and luck response", r"luck|halftime minute|playing.time"),
    ("Strategy engine and AI agent evaluation", r"\bagent|llm|langgraph|debate|gemini|ablation|playsheet|engine|optimizer|blog replay|template|calibrat|shrinkage|alpha blend|feature stacking|residual feature|opener|conformance|routing|net-swing|training seasons|equilibrium|retrospective|backtest|app report"),
    ("Player absence and offensive reorganization", r"restor|absence|absorb|\bhub|spell|injur|scout|displacement|reorganiz"),
    ("Structural roles and influence", r"structural|load|influence|fragility|portability|coverage|connector|shaper|hasconn|concentration|wiring|role|identity|margbig|pci|gravity"),
    ("Defensive suppression and counter strategy (BEST/AVOID)", r"suppress|best vs avoid|best-avoid|avoid|counter|aftershock"),
    ("Lineup and matchup effects", r"lineup|substitution|five-|5-on-5|rapm|stint|matchup|synergy|kernel|on/off|onoff"),
    ("Possession sequences and transitions", r"sequence|sequential|transition matrix|8x8|8×8|chain|markov|brown|tatum|lag-1|lags|state persistence|epv"),
    ("In-game and series adaptation", r"within-game|within-series|series|adapt|\bh1\b|\bh2\b|crunch|clutch|run|pivot|trigger|playoff|halves"),
    ("Shot selection and shot quality", r"shot|xfg|pull_up|pull-up|three|3pa|rim"),
]
DATASET_RULES = [
    ("Play-type initiation records (Neo4j INITIATED edges / play-type possessions)", r"play.type|play-type|\bpt\b|pnr|\bcut\b|drive|post_up|spot_up|putback|initiat|neo4j|fingerprint|edges|transition"),
    ("NBA play-by-play possessions and reconstructed lineups", r"possession|play-by-play|pbp|stint|lineup|substitution|five"),
    ("Shot-level data with expected FG", r"\bshot|xfg|fga"),
    ("Box score and traditional stats", r"box|minutes|net rating|traditional|usage|ortg"),
    ("Player absence spells", r"absence|spell|injur"),
    ("Playoff series outcomes", r"series|playoff|upset"),
    ("NCAA tournament and ratings data", r"ncaa|kenpom|march madness|seed|538|elo|bracket"),
    ("LLM or agent outputs", r"\bagent|llm|gemini|langgraph|debate"),
]
METHOD_RULES = [
    ("difference-in-differences", r"\bdid\b|difference-in-difference"),
    ("placebo or permutation test", r"placebo|shuffle|permut"),
    ("split-half reliability", r"split-half|reliab|spearman-brown"),
    ("bootstrap interval", r"bootstrap"),
    ("matched control", r"matched|caliper|\bmatch"),
    ("regression", r"regression|\bols\b|r2\b|r²|logit|logistic|\blpm\b|lasso"),
    ("ridge or RAPM ratings", r"ridge|rapm"),
    ("holdout, backtest or replay", r"holdout|backtest|out-of-sample|\boos\b|loso|replay|retro|prospective|held-out"),
    ("ablation", r"ablation"),
    ("LLM agent run", r"\bagent|llm|langgraph|gemini|debate"),
    ("correlation", r"spearman|pearson|ρ|\brho\b|\br\s?=|correlat"),
    ("simulation", r"simulat|monte carlo|\bmc\b"),
    ("event study", r"event study|event-study"),
    ("case study", r"case stud"),
    ("calibration scoring", r"brier|calibrat"),
]
LIMIT_RULES = [
    ("small sample", r"\bn\s?=\s?\d{1,2}\b|small[- ]n|small sample|few |only \d+|underpowered"),
    ("low measurement reliability", r"reliab|split-half|spearman-brown|noisy"),
    ("insufficient exposure", r"exposure|median \d+ possessions|per pair|sparse"),
    ("low power / large MDE", r"\bmde\b|power"),
    ("selection or regression to the mean", r"regression to (the )?mean|\brtm\b|selection"),
    ("leakage", r"leak"),
    ("label or classification error", r"label|misclass|classifier"),
    ("drift", r"drift"),
    ("multiple testing", r"multiple test|holm|bonferroni|\bfdr\b|benjamini"),
    ("confounding", r"confound"),
    ("implementation bug", r"\bbug|error in|wrong sign|miscod"),
]
VARIABLE_RULES = [
    ("PPP (points per possession)", r"\bppp\b|points per possession"),
    ("play-type share / mix", r"share|mix"),
    ("structural influence / load (L)", r"\bload\b|influence|\bl_pre|\bl\(p\)|l_pred"),
    ("restoration R / reorganization", r"restor|reorgani"),
    ("expected FG / shot value", r"xfg|expected (shot|fg|points)"),
    ("three-point attempts or luck", r"three|3pa|3p\b|luck"),
    ("minutes / playing time", r"minutes|playing time"),
    ("net rating / ORtg", r"net rating|ortg|drtg"),
    ("win probability / series outcome", r"win%|win pct|series win|upset|outcome"),
    ("Brier score", r"brier"),
    ("turnovers", r"\btov|turnover"),
    ("free throws / fouls", r"foul|free throw"),
]


def tags(rules, s):
    return [name for name, pat in rules if re.search(pat, s)]


def topic_of(r):
    s = text(r, "title", "hypothesis", "project")
    for name, pat in TOPIC_RULES:
        if re.search(pat, s):
            return name
    return "Other / unclassified"


def epistemic(r):
    v, ft, pw = r.get("verdict"), r.get("failure_type"), (r.get("power_info") or "").strip()
    if v == "artifact_found" or ft == "C_artifact":
        return "artifact"
    if ft == "A_unanswerable":
        return "cannot be tested with available data"
    if v in ("null", "failed_gate", "reversed") and ft == "B_powered_null" and pw:
        return "adequately rejected (as specified)"
    if v in ("null", "failed_gate", "reversed", "abandoned") or (ft == "B_powered_null" and not pw):
        return "not tested adequately"
    if v == "inconclusive":
        return "genuinely uncertain"
    if v == "supported" and ft == "D_positive":
        return "supported"
    if v in ("tool_eval_pass", "tool_eval_fail"):
        return "tool evaluation"
    if v == "descriptive":
        return "no hypothesis test (descriptive)"
    return "ambiguous classification"


# ---------------------------------------------------------------- source checks
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
READABLE = (".md", ".tex", ".py", ".log", ".json", ".csv", ".txt", ".jsonl")
_cache = {}


def clean_path(s):
    m = re.search(r"[A-Za-z]:\\[^\n\"'<>|]*", s)
    if not m:
        return None
    p = m.group(0).strip().rstrip(").,;")
    p = re.split(r"\s+\(|\s+-\s+|:\d+$|#", p)[0].strip()
    p = os.path.expandvars(p.replace("%TEMP%", os.environ.get("TEMP", "")))
    return p


# The strategy-app folder was moved after some chats cited it.
RENAMED = [(r"C:\Users\lisas\OneDrive\Documents\Basketball Strategy", r"C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy")]


def resolve(p):
    if os.path.exists(p) or glob.glob(p):
        return p, False
    for old, new in RENAMED:
        if p.lower().startswith(old.lower()):
            q = new + p[len(old):]
            if os.path.exists(q) or glob.glob(q):
                return q, True
            ext = glob.glob(q + ".*")
            if len(ext) == 1:
                return ext[0], True
    return p, False


def read_text(p):
    p, _ = resolve(p)
    if p in _cache:
        return _cache[p]
    t = ""
    try:
        if os.path.isfile(p) and p.lower().endswith(READABLE) and os.path.getsize(p) < 8_000_000:
            b = open(p, "rb").read()
            if b[:2] in (b"\xff\xfe", b"\xfe\xff"):
                t = b.decode("utf-16", errors="ignore")
            else:
                t = b.decode("utf-8", errors="ignore")
    except OSError:
        pass
    _cache[p] = t
    return t


NUM = re.compile(r"(?<![\w.])[-+−]?\d*\.\d+")


def number_check(r):
    nums = []
    for n in NUM.findall(r.get("primary_result") or ""):
        n = n.replace("−", "-").lstrip("+-")
        if n.startswith("."):
            n = "0" + n
        if n not in nums:
            nums.append(n)
    if not nums:
        return "", 0, 0
    corpus = ""
    for s in r.get("sources") or []:
        s = str(s)
        p = clean_path(s)
        if p:
            corpus += read_text(p)
        for u in UUID.findall(s):
            corpus += read_text(os.path.join(LEDGER, "scratch", "chats", u + ".txt"))
    if not corpus:
        return "no readable source", len(nums), 0
    found = sum(1 for n in nums if n in corpus or n.lstrip("0") in corpus)
    return "checked", len(nums), found


def source_status(r):
    paths, missing, transcripts, remapped = 0, 0, 0, []
    for s in r.get("sources") or []:
        s = str(s)
        p = clean_path(s)
        if p:
            paths += 1
            q, moved = resolve(p)
            if moved:
                remapped.append(q)
            elif not (os.path.exists(q) or glob.glob(q)):
                missing += 1
        transcripts += len(UUID.findall(s))
    return paths, missing, transcripts, remapped


# ---------------------------------------------------------------- inventory
def extract_sizes(r):
    s = " ".join([r.get("design") or "", r.get("power_info") or ""])
    pats = [r"\bn\s?=\s?[\d,]+(?:\s+[a-z-]+){0,2}", r"[\d,]{2,}\s+(?:team-seasons|spells|series|games|possessions|players|pairs|stoppages|events|windows|matches|teams|seasons|units|lineups|stints|shots|cases)"]
    hits = []
    for p in pats:
        for m in re.findall(p, s, re.I):
            m = m.strip()
            if m not in hits:
                hits.append(m)
    return "; ".join(hits[:4])


NR = "NOT RECORDED"
inv = []
for r in rows:
    design = r.get("design") or ""
    topic = topic_of(r)
    datasets = tags(DATASET_RULES, text(r, "title", "hypothesis", "design", "project"))
    methods = tags(METHOD_RULES, text(r, "title", "hypothesis", "design", "primary_result"))
    limits = tags(LIMIT_RULES, text(r, "power_info", "failure_evidence", "notes"))
    probs = ""
    if r.get("failure_type") == "C_artifact" or r.get("verdict") == "artifact_found":
        probs = r.get("failure_evidence") or NR
    elif re.search(r"leak|confound|bug|artifact|regression to (the )?mean", text(r, "notes", "failure_evidence")):
        probs = "mentioned: " + (r.get("notes") or r.get("failure_evidence") or "")
    repl = "mentioned (see notes)" if re.search(r"replicat", text(r, "notes", "primary_result", "failure_evidence")) else NR
    n_chk, n_nums, n_found = number_check(r)
    paths, missing, transcripts, remapped = source_status(r)
    fam = family_of[r["id"]]
    fam_verdicts = sorted({by_rec[m].get("verdict", "") for m in family_members[fam]})
    inv.append({
        "experiment_id": r["id"],
        "title": r.get("title", ""),
        "study_family_id": fam,
        "study_family_kind": family_kind[fam],
        "study_family_representative": family_rep[fam],
        "study_family_members": "; ".join(family_members[fam]),
        "study_family_verdicts": "; ".join(fam_verdicts),
        "study_family_verdict_conflict": "yes" if len(fam_verdicts) > 1 else "no",
        "research_question": r.get("hypothesis") or NR,
        "original_hypothesis": r.get("hypothesis") or NR,
        "domain_topic": topic,
        "project": r.get("project", ""),
        "datasets_and_fields": "; ".join(datasets) or NR,
        "sample_size_and_unit": extract_sizes(r) or NR,
        "design_as_recorded": design or NR,
        "experimental_method": "; ".join(methods) or NR,
        "primary_outcome": NR,
        "result_classification": r.get("verdict", ""),
        "primary_result": r.get("primary_result") or NR,
        "failure_mechanism": r.get("failure_type", "") if r.get("verdict") not in ("supported", "tool_eval_pass") else "n/a (not a failure)",
        "failure_type_as_recorded": r.get("failure_type", ""),
        "failure_evidence": r.get("failure_evidence") or NR,
        "power_or_reliability_limitations": (r.get("power_info") or NR) + (" | categories: " + "; ".join(limits) if limits else ""),
        "confounds_leakage_or_implementation_problems": probs or "none recorded",
        "preregistered": r.get("prespecified") or NR,
        "independently_replicated": repl,
        "what_was_learned": NR,
        "ruled_out_directions": NR,
        "viable_directions": NR,
        "epistemic_status_derived": epistemic(r),
        "knowable_in_advance": r.get("knowable_in_advance") or NR,
        "n_runs": int(r.get("n_runs") or 1),
        "n_runs_as_extracted": int(r.get("n_runs_recorded") or r.get("n_runs") or 1),
        "n_runs_note": r.get("n_runs_note", ""),
        "date": r.get("date") or NR,
        "date_basis": r.get("date_basis") or NR,
        "related_as_recorded": r.get("related") or "",
        "notes": r.get("notes") or "",
        "duplicate_records_merged": "; ".join(r.get("also_recorded_as") or []),
        "supersedes": "; ".join(r.get("supersedes_ids") or []),
        "slice_file": slice_of.get(r["id"], ""),
        "source_files_and_provenance": " | ".join(str(s) for s in r.get("sources") or []),
        "source_paths_cited": paths,
        "source_paths_missing": missing,
        "source_paths_resolved_after_folder_move": " | ".join(remapped),
        "source_transcripts_cited": transcripts,
        "numbers_check": n_chk,
        "numbers_in_result": n_nums,
        "numbers_found_in_sources": n_found,
    })

with open(os.path.join(OUT, "experiment_inventory.csv"), "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, fieldnames=list(inv[0].keys()))
    w.writeheader()
    w.writerows(inv)

# ---------------------------------------------------------------- condition B: documents
ids = {r["id"] for r in rows}
alias = {a: r["id"] for r in rows for a in r.get("also_recorded_as") or []}
for r, e in zip(rows, inv):
    body = [f"# {r['id']}: {r.get('title','')}", "",
            f"- Project: {r.get('project','')}", f"- Date: {r.get('date','')} ({r.get('date_basis','')})",
            f"- Topic: {e['domain_topic']}", f"- Pre-specified: {r.get('prespecified','')}",
            f"- Verdict: {r.get('verdict','')}", f"- Failure type: {r.get('failure_type','')}",
            f"- Knowable in advance: {r.get('knowable_in_advance','')}", f"- Runs: {e['n_runs']}",
            f"- Dataset tags: {'; '.join(tags(DATASET_RULES, text(r, 'title', 'hypothesis', 'design', 'project')))}",
            f"- Method tags: {'; '.join(tags(METHOD_RULES, text(r, 'title', 'hypothesis', 'design', 'primary_result')))}",
            f"- Limitation tags: {'; '.join(tags(LIMIT_RULES, text(r, 'power_info', 'failure_evidence', 'notes')))}",
            f"- Variable tags: {'; '.join(tags(VARIABLE_RULES, text(r, 'title', 'hypothesis', 'design', 'primary_result')))}",
            f"- Paper: {PAPERS.get(r.get('project'), '')}", "",
            "## Hypothesis", r.get("hypothesis", ""), "", "## Design", r.get("design", ""), "",
            "## Result", r.get("primary_result", ""), "", "## Failure evidence", r.get("failure_evidence", ""), "",
            "## Power and reliability", r.get("power_info", ""), "", "## Related", str(r.get("related", "")), "",
            "## Notes", r.get("notes", ""), "", "## Sources"] + [f"- {s}" for s in r.get("sources") or []]
    if r.get("verdict") == "supported":
        body += ["", "## Finding status", "supported in source; independent replication not recorded"]
    refs = [alias.get(x, x) for x in re.findall(r"\b(?:APPA|APPM|APPS|PAP|TMP|CHT)-\d{3}\b", str(r.get("related") or ""))]
    refs = [x for x in dict.fromkeys(refs) if x in ids and x != r["id"]]
    if refs:
        body += ["", "## Related records (ids resolved to merged records)", ", ".join(refs)]
    if re.search(r"motivat|follow-?up|next step|led to", text(r, "notes", "related", "failure_evidence")):
        body += ["", "## Follow-on candidate", "candidate, needs curation (see Notes)"]
    if r.get("also_recorded_as"):
        body += ["", "## Also recorded as", ", ".join(r["also_recorded_as"])]
    fam = family_of[r["id"]]
    if len(family_members[fam]) > 1:
        others = [m for m in family_members[fam] if m != r["id"]]
        body += ["", "## Same study family", f"{fam} ({family_kind[fam]}): " + ", ".join(others), family_note[fam]]
    open(os.path.join(OUT, "memory", "documents", r["id"] + ".md"), "w", encoding="utf-8").write("\n".join(body) + "\n")

# ---------------------------------------------------------------- condition C: graph
nodes, edges = {}, []


def node(nid, ntype, **props):
    if nid not in nodes:
        nodes[nid] = {"id": nid, "type": ntype, **props}
    return nid


def edge(src, rel, dst, provenance, **props):
    edges.append({"src": src, "rel": rel, "dst": dst, "provenance": provenance, **props})


ids = {r["id"] for r in rows}
alias = {a: r["id"] for r in rows for a in r.get("also_recorded_as") or []}
for fm in ("A_unanswerable", "B_powered_null", "C_artifact", "D_positive", "E_unclear"):
    node("FM:" + fm, "FailureMechanism", label=fm)
for r, e in zip(rows, inv):
    x = node("EXP:" + r["id"], "Experiment", title=r.get("title", ""), project=r.get("project", ""), date=r.get("date", ""),
             date_basis=r.get("date_basis", ""), prespecified=r.get("prespecified", ""), n_runs=e["n_runs"],
             sources=r.get("sources") or [], knowable_in_advance=r.get("knowable_in_advance", ""),
             design=r.get("design", ""), power_info=r.get("power_info", ""), related=str(r.get("related", "")),
             notes=r.get("notes", ""))
    h = node("HYP:" + r["id"], "Hypothesis", text=r.get("hypothesis", ""), source_record=r["id"])
    q = node("RQ:" + e["domain_topic"], "ResearchQuestion", label=e["domain_topic"], provenance="rule:TOPIC_RULES (topic-level grouping)")
    res = node("RES:" + r["id"], "Result", verdict=r.get("verdict", ""), primary_result=r.get("primary_result", ""),
               failure_evidence=r.get("failure_evidence", ""), source_record=r["id"])
    prov = {"record": r["id"], "sources": r.get("sources") or []}
    edge(h, "tested_by", x, prov)
    edge(h, "addresses", q, {"rule": "TOPIC_RULES", "record": r["id"]})
    edge(x, "produced", res, prov)
    edge(res, "has_mechanism", "FM:" + r.get("failure_type", "E_unclear"), prov)
    v = r.get("verdict")
    if v == "supported":
        edge(h, "supported_by", x, prov)
        f = node("FIND:" + r["id"], "Finding", statement=r.get("primary_result", ""), status="supported in source; independent replication not recorded", source_record=r["id"])
        edge(f, "derived_from", x, prov)
    elif v in ("null", "failed_gate", "reversed"):
        edge(h, "contradicted_by", x, prov)
    elif v == "artifact_found":
        edge(h, "invalidated_by", x, prov)
    for d in tags(DATASET_RULES, text(r, "title", "hypothesis", "design", "project")):
        edge(x, "uses_dataset", node("DS:" + d, "Dataset", label=d), {"rule": "DATASET_RULES", "record": r["id"]})
    for m in tags(METHOD_RULES, text(r, "title", "hypothesis", "design", "primary_result")):
        edge(x, "uses_method", node("METH:" + m, "Method", label=m), {"rule": "METHOD_RULES", "record": r["id"]})
    for l in tags(LIMIT_RULES, text(r, "power_info", "failure_evidence", "notes")):
        edge(x, "limited_by", node("LIM:" + l, "StatisticalLimitation", label=l), {"rule": "LIMIT_RULES", "record": r["id"]})
    for var in tags(VARIABLE_RULES, text(r, "title", "hypothesis", "design", "primary_result")):
        edge(x, "measures", node("VAR:" + var, "Variable", label=var), {"rule": "VARIABLE_RULES", "record": r["id"]})
    if r.get("project") in PAPERS:
        edge(x, "reported_in", node("PAPER:" + PAPERS[r["project"]], "Paper", label=PAPERS[r["project"]]), {"rule": "project field", "record": r["id"]})
    for a in r.get("also_recorded_as") or []:
        edge(x, "duplicates", node("ALIAS:" + a, "DuplicateRecord", label=a, slice_file=slice_of.get(a, "")), {"rule": "dedupe merge", "record": r["id"]})
    fam = family_of[r["id"]]
    if len(family_members[fam]) > 1 and r["id"] != family_rep[fam]:
        rel = "extends" if family_kind[fam] == "repeat_runs_or_robustness" else "duplicates"
        edge(x, rel, "EXP:" + family_rep[fam], {"rule": "audit/study_family_review.csv (manual review)", "record": r["id"],
                                                "family": fam, "family_kind": family_kind[fam],
                                                "family_members": family_members[fam], "evidence": family_note[fam]}, needs_review=False)
    for s_id in r.get("supersedes_ids") or []:
        edge(x, "supersedes_version", node("ALIAS:" + s_id + "(earlier)", "DuplicateRecord", label=s_id), {"rule": "supersedes field", "record": r["id"]})
    for ref in re.findall(r"\b(?:APPA|APPM|APPS|PAP|TMP|CHT)-\d{3}\b", str(r.get("related") or "")):
        ref = alias.get(ref, ref)
        if ref in ids and ref != r["id"]:
            edge(x, "extends", "EXP:" + ref, {"rule": "related field id reference (direction not verified)", "record": r["id"]}, needs_review=True)
    rel_text = text(r, "notes", "related", "failure_evidence")
    if re.search(r"rul(ed|es) out|rules-out", rel_text):
        edge(x, "rules_out", "UNRESOLVED", {"rule": "text pattern 'ruled out'", "record": r["id"], "text": r.get("notes", "")}, needs_review=True)
    if re.search(r"motivat|follow-?up|next step|led to", rel_text):
        fo = node("FOLLOW:" + r["id"], "FollowOnHypothesis", text="see notes of " + r["id"], status="candidate, needs curation", source_record=r["id"])
        edge(x, "motivates", fo, {"rule": "text pattern motivate/follow-up", "record": r["id"], "text": r.get("notes", "")}, needs_review=True)

with open(os.path.join(OUT, "memory", "graph_nodes.jsonl"), "w", encoding="utf-8") as fh:
    for n in nodes.values():
        fh.write(json.dumps(n, ensure_ascii=False) + "\n")
with open(os.path.join(OUT, "memory", "graph_edges.jsonl"), "w", encoding="utf-8") as fh:
    for e_ in edges:
        fh.write(json.dumps(e_, ensure_ascii=False) + "\n")

# ---------------------------------------------------------------- audit tables
T = []


def table(title, counter_rows, header):
    T.append(f"\n## {title}\n")
    T.append("| " + " | ".join(header) + " |")
    T.append("|" + "---|" * len(header))
    for row in counter_rows:
        T.append("| " + " | ".join(str(c) for c in row) + " |")


V = collections.Counter(e["result_classification"] for e in inv)
table("Verdict counts (unique designs)", [(k, c, sum(x["n_runs"] for x in inv if x["result_classification"] == k)) for k, c in V.most_common()], ["verdict", "designs", "runs (sum n_runs)"])
F = collections.Counter(e["failure_type_as_recorded"] for e in inv)
table("Failure type counts", F.most_common(), ["failure_type", "designs"])
vs = sorted(V)
fs = sorted(F)
ct = collections.Counter((e["result_classification"], e["failure_type_as_recorded"]) for e in inv)
table("Verdict x failure type", [[v] + [ct[(v, f)] for f in fs] + [V[v]] for v in vs], ["verdict"] + fs + ["total"])
ES = collections.Counter(e["epistemic_status_derived"] for e in inv)
table("Derived epistemic status", ES.most_common(), ["status", "designs"])
TP = collections.Counter(e["domain_topic"] for e in inv)
topics = [t for t, _ in TP.most_common()]
table("Topic x verdict", [[t, TP[t]] + [sum(1 for e in inv if e["domain_topic"] == t and e["result_classification"] == v) for v in ("supported", "null", "artifact_found", "failed_gate", "inconclusive", "descriptive")] + [sum(1 for e in inv if e["domain_topic"] == t and e["failure_type_as_recorded"] == "A_unanswerable")] for t in topics],
      ["topic", "designs", "supported", "null", "artifact", "failed_gate", "inconclusive", "descriptive", "A_unanswerable"])
PR = collections.Counter((e["preregistered"], e["result_classification"] in FAILED) for e in inv)
table("Pre-specification x failed", [(p, PR[(p, True)], PR[(p, False)]) for p in ("yes", "partial", "no", "unknown")], ["prespecified", "failed", "not failed"])
KA = collections.Counter((e["knowable_in_advance"], e["failure_type_as_recorded"]) for e in inv)
table("Knowable in advance x failure type", [[k] + [KA[(k, f)] for f in fs] for k in ("yes", "no", "unclear", NR)], ["knowable"] + fs)
table("Projects", collections.Counter(e["project"] for e in inv).most_common(), ["project", "designs"])
runs = sorted(inv, key=lambda e: -e["n_runs"])[:15]
table("Largest n_runs", [(e["experiment_id"], e["n_runs"], e["title"][:70]) for e in runs], ["id", "n_runs", "title"])
lim = collections.Counter(l for r in rows for l in tags(LIMIT_RULES, text(r, "power_info", "failure_evidence", "notes")))
table("Limitation categories (rule-tagged)", lim.most_common(), ["limitation", "designs"])
meth_art = collections.Counter()
meth_all = collections.Counter()
for r, e in zip(rows, inv):
    for m in tags(METHOD_RULES, text(r, "title", "hypothesis", "design", "primary_result")):
        meth_all[m] += 1
        if e["epistemic_status_derived"] == "artifact":
            meth_art[m] += 1
table("Method x artifact rate", [(m, meth_all[m], meth_art[m], f"{meth_art[m]/meth_all[m]:.2f}") for m, _ in meth_all.most_common()], ["method", "designs", "artifacts", "rate"])

# QA flags
flags = []
for r, e in zip(rows, inv):
    v, ft = e["result_classification"], e["failure_type_as_recorded"]
    f = []
    if v == "supported" and ft != "D_positive":
        f.append("supported but failure_type " + ft)
    if ft == "D_positive" and v in FAILED:
        f.append("D_positive but verdict " + v)
    if v == "descriptive" and ft in ("A_unanswerable", "B_powered_null", "C_artifact", "D_positive"):
        f.append("descriptive with failure_type " + ft)
    if v == "artifact_found" and ft != "C_artifact":
        f.append("artifact_found but failure_type " + ft)
    if ft == "C_artifact" and v not in ("artifact_found",):
        f.append("C_artifact but verdict " + v)
    if ft == "B_powered_null" and not (r.get("power_info") or "").strip():
        f.append("B_powered_null without power_info")
    if ft == "E_unclear":
        f.append("failure_type unclear")
    if e["epistemic_status_derived"] == "ambiguous classification":
        f.append("ambiguous epistemic status")
    if not (r.get("primary_result") or "").strip():
        f.append("no primary_result")
    if e["source_paths_missing"]:
        f.append(f"{e['source_paths_missing']} cited path(s) not found")
    if e["numbers_check"] == "checked" and e["numbers_in_result"] >= 2 and e["numbers_found_in_sources"] / e["numbers_in_result"] < 0.5:
        f.append(f"only {e['numbers_found_in_sources']}/{e['numbers_in_result']} result numbers found in sources")
    if e["numbers_check"] == "no readable source":
        f.append("numbers not checkable (no readable source)")
    if e["n_runs"] >= 50:
        f.append(f"n_runs {e['n_runs']} (check whether runs are independent)")
    if e["date"] == NR:
        f.append("no date")
    flags.append({"experiment_id": r["id"], "verdict": v, "failure_type": ft, "flags": "; ".join(f)})
with open(os.path.join(OUT, "audit", "classification_flags.csv"), "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, fieldnames=["experiment_id", "verdict", "failure_type", "flags"])
    w.writeheader()
    w.writerows(flags)
fc = collections.Counter()
for fl in flags:
    for x in fl["flags"].split("; "):
        if x:
            fc[re.sub(r"\d+", "#", x)] += 1
table("Audit flag counts", fc.most_common(), ["flag", "designs"])
chk = [e for e in inv if e["numbers_check"] == "checked"]
tot_n = sum(e["numbers_in_result"] for e in chk)
tot_f = sum(e["numbers_found_in_sources"] for e in chk)
T.append(f"\nNumber verification: {len(chk)} records checkable, {tot_n} decimal numbers, {tot_f} found verbatim in cited sources ({tot_f/max(tot_n,1):.1%}). "
         f"Not checkable: {sum(1 for e in inv if e['numbers_check']=='no readable source')}. No decimals in result: {sum(1 for e in inv if e['numbers_check']=='')}.")
T.append(f"\nGraph: {len(nodes)} nodes, {len(edges)} edges. Node types: {dict(collections.Counter(n['type'] for n in nodes.values()))}. "
         f"Edge types: {dict(collections.Counter(e_['rel'] for e_ in edges))}. Edges needing review: {sum(1 for e_ in edges if e_.get('needs_review'))}.")
reps = [e for e in inv if e["experiment_id"] == e["study_family_representative"]]
table("Study-family level: verdict of representative record", collections.Counter(e["result_classification"] for e in reps).most_common(), ["verdict", "study families"])
table("Study-family level: derived epistemic status of representative record", collections.Counter(e["epistemic_status_derived"] for e in reps).most_common(), ["status", "study families"])
table("Study-family level: topic", collections.Counter(e["domain_topic"] for e in reps).most_common(), ["topic", "study families"])
multi = [f for f, ms in family_members.items() if len(ms) > 1]
table("Multi-record study families", [(f, family_kind[f], "; ".join(family_members[f]),
                                       "; ".join(f"{m}={by_rec[m].get('verdict')}" for m in family_members[f]),
                                       "yes" if len({by_rec[m].get('verdict') for m in family_members[f]}) > 1 else "no") for f in multi],
      ["family", "kind", "members", "verdicts", "conflict"])
run_lo = sum(max(next(e["n_runs"] for e in inv if e["experiment_id"] == m) for m in ms) for ms in family_members.values())
T.append(f"\nStudy families: {len(family_members)} (from {len(inv)} merged records; {len(multi)} multi-record families covering "
         f"{sum(len(family_members[f]) for f in multi)} records; {sum(1 for f in multi if len({by_rec[m].get('verdict') for m in family_members[f]}) > 1)} with conflicting verdicts). "
         f"Runs: lower bound {run_lo} (largest n_runs within each family), upper bound {sum(e['n_runs'] for e in inv)} (sum over merged records).")
T.append(f"\nTotals: designs {len(inv)}, runs {sum(e['n_runs'] for e in inv)}, failed {sum(1 for e in inv if e['result_classification'] in FAILED)}, raw slice records {sum(len(v) for v in raw.values())}.")
open(os.path.join(OUT, "audit", "tables.md"), "w", encoding="utf-8").write("# Audit tables (generated)\n" + "\n".join(T) + "\n")
print("\n".join(T))
