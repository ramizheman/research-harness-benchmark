"""Offline retrieval test on saved Study 1 runs. Read-only on runs, snapshots and code; writes only to retrieval_test/.

Relevance follows analysis_fixes/recompute_retrieval_audit.py exactly (the source of the paper's figures):
question tier without the TF-IDF merge term (that script checks the tier sizes equal the saved columns), lesson
tier with the corrected risk-code parsing, both read from the memory_v2 snapshot graph as in the paper's audit.
Retrieval pools are the memory_v3 snapshots the runs actually searched.
"""
import csv, glob, json, os, re, sys
from collections import defaultdict

import numpy as np

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HB, "retrieval_test", "outputs")
os.makedirs(OUT, exist_ok=True)
sys.path.insert(0, HB)
from bench import common, retrieval_audit as ra  # noqa: E402
from runner import tools_v3  # noqa: E402
from runner.experiment import load_task, answer_key  # noqa: E402

TASKS = ["RT-012", "RT-014", "RT-065", "RT-066", "RT-101", "RT-112", "RT-146", "RT-147", "RT-179", "RT-183"]
KS = (4, 8, 10, 20)
MANUAL = {"RT-012": "SF-CHT-025", "RT-147": "SF-CHT-025"}
WATCH = {"RT-012": ["SF-CHT-025"], "RT-147": ["SF-CHT-025", "SF07"]}
MODELS = [("sentence-transformers/all-MiniLM-L6-v2", "", ""),
          ("BAAI/bge-small-en-v1.5", "Represent this sentence for searching relevant passages: ", ""),
          ("intfloat/e5-small-v2", "query: ", "passage: ")]
RRF_K = 60

# ------------------------------------------------------------------ relevance (as in recompute_retrieval_audit.py)
K = answer_key()
ORIG_LIST = ra._list


def fixed_list(v):
    x = ORIG_LIST(v)
    if x or v in (None, ""):
        return x
    s = str(v).strip()
    return [] if s.startswith("[") else [c.strip() for c in s.replace(";", ",").split(",") if c.strip()]


records = {r["id"]: r for r in common.load_records()}
ctx = object.__new__(ra.Context)
ctx.records = records
ctx.family_of, ctx.members, _, _ = common.load_families(list(records.values()))
ctx.cluster = {r["study_family_id"]: r["cluster_id"] for r in
               csv.DictReader(open(os.path.join(HB, "research_question_clusters.csv"), encoding="utf-8-sig"))}


def q_tier(task, key, snap_fams):
    fam = task["study_family_id"]
    rel = {f for f, c in ctx.cluster.items() if c == ctx.cluster.get(fam) and f != fam}
    rel |= {x.strip() for x in str(key.get("knowable_precedents") or "").split(";") if x.strip()}
    rel |= set(ORIG_LIST(key.get("prior_same_question_families_in_memory")))
    return rel & snap_fams


REL = {}
for t in TASKS:
    task, key = load_task(t), K[t]
    strata, risks, fg, rqc = ra.snapshot_info(os.path.join(HB, "memory_v2", "snapshots", t), with_risks=True)
    snap_fams = set(strata) | {ctx.family_of[p] for p in task["permitted_records"] if p in ctx.family_of}
    ra._list = fixed_list
    L = ra.lesson_families(key, risks, strata)
    ra._list = ORIG_LIST
    REL[t] = {"Q": q_tier(task, key, snap_fams), "L": L}

# ------------------------------------------------------------------ pools and saved queries
TB = {}
for t in TASKS:
    snap3 = os.path.join(HB, "memory_v3", "snapshots", t)
    TB[t] = {"B": tools_v3.Toolbox3("B", snap3), "C": tools_v3.Toolbox3("C", snap3)}


def joined(args):
    parts = [args.get("query", "")]
    for k in ("research_concepts", "methodological_questions"):
        v = args.get(k)
        parts += v if isinstance(v, list) else [v or ""]
    return " ".join(str(x) for x in parts).strip()


def clean_question(t):
    s = load_task(t)["statement"]
    lines = s.splitlines()
    i = next(n for n, l in enumerate(lines) if l.startswith("Research question (as posed"))
    out = []
    for l in lines[i + 1:]:
        if not l.strip():
            break
        out.append(l.strip())
    return " ".join(out)


saved = {}
for p in ("runs/pilot3_v1/analysis_p3/per_run.csv", "runs/cross_model_v1/analysis_cross/per_run.csv",
          "runs/reasoning_models_v1/analysis_rm/per_run.csv"):
    for r in csv.DictReader(open(os.path.join(HB, p), encoding="utf-8-sig")):
        saved[r["run_id"]] = r

queries = []
repro = defaultdict(lambda: [0, 0])
mismatches, order_swaps, no_search = [], [], []
for d in ("runs/pilot3_v1/raw", "runs/cross_model_v1/raw", "runs/reasoning_models_v1/raw"):
    for p in sorted(glob.glob(os.path.join(HB, d, "*.json"))):
        r = json.load(open(p, encoding="utf-8"))
        if r["run_id"] not in saved or r["condition"] not in ("B", "C"):
            continue
        calls = [l["tool"] for l in r.get("log", []) if "tool" in l]
        mem = [c for c in calls if c["name"] in tools_v3.MEMORY_TOOLS]
        first = next((c for c in calls if c["name"] == "retrieve_history"), None)
        if first is None:
            no_search.append(r["run_id"])
            continue
        tb = TB[r["task_id"]][r["condition"]]
        tb.returned = []
        got = tb.retrieve(first["args"])
        got_ids = [x["id"] for x in got["results"]]
        saved_ids = list(first.get("returned_ids") or [])
        order_ok = got_ids == saved_ids
        ok = order_ok or sorted(got_ids) == sorted(saved_ids)
        repro[r["condition"]][0] += ok
        repro[r["condition"]][1] += 1
        if ok and not order_ok:
            order_swaps.append((r["run_id"], f"saved {saved_ids} reproduced {got_ids}"))
        if not ok:
            mismatches.append((r["run_id"], f"saved {saved_ids} reproduced {got_ids}"))
        first_fams = {i[4:] for i in first.get("returned_ids") or [] if i.startswith("FAM:")}
        all_fams = set()
        for c in mem:
            for i in c.get("returned_ids") or []:
                all_fams |= ra.families_of_id(i, ctx, {}, {}) if not i.startswith("FAM:") else {i[4:]}
        queries.append({"run_id": r["run_id"], "model": r["model_name"], "task_id": r["task_id"], "condition": r["condition"],
                        "seed": r["seed"], "query": joined(first["args"]), "first_fams": first_fams, "all_fams": all_fams,
                        "saved_order": saved_ids if order_ok else None})

json.dump({"reproduction": {c: {"match": v[0], "n": v[1]} for c, v in repro.items()}, "mismatches": mismatches,
           "set_matched_order_differed": order_swaps, "no_search_made": no_search},
          open(os.path.join(OUT, "reproduction.json"), "w", encoding="utf-8"), indent=1)
print("reproduction", {c: f"{v[0]}/{v[1]}" for c, v in repro.items()}, "mismatches", len(mismatches),
      "order swaps", len(order_swaps), "no search", no_search)
if mismatches:
    for m in mismatches[:10]:
        print("  ", m)
    sys.exit("Reproduction failed; stopping as instructed.")

# ------------------------------------------------------------------ retrievers
import torch  # noqa: E402
from rank_bm25 import BM25Okapi  # noqa: E402
from sentence_transformers import SentenceTransformer  # noqa: E402

torch.manual_seed(0)
np.random.seed(0)
analyzer = tools_v3._tfidf().build_analyzer()
POOL, FULL, QH = {}, {}, {}
for t in TASKS:
    b = TB[t]["B"]
    POOL[t] = list(b.families)
    FULL[t] = [b.doc_text[f] for f in POOL[t]]
    QH[t] = [" ".join(o for p, o, _ in b.facts[f] if p in ("observed_research_question", "observed_hypothesis")) for f in POOL[t]]

model_info, ENC = {}, {}
for name, qpre, dpre in MODELS:
    try:
        m = SentenceTransformer(name, device="cpu")
    except Exception as e:  # noqa: BLE001
        model_info[name] = {"loaded": False, "error": str(e)[:200]}
        continue
    model_info[name] = {"loaded": True, "max_seq_length": m.max_seq_length,
                        "dim": m.get_sentence_embedding_dimension(), "query_prefix": qpre, "doc_prefix": dpre}
    ENC[name] = {"m": m, "q": qpre, "d": dpre, "full": {}, "qh": {}}
    for t in TASKS:
        ENC[name]["full"][t] = m.encode([dpre + x for x in FULL[t]], normalize_embeddings=True, batch_size=32)
        ENC[name]["qh"][t] = m.encode([dpre + x for x in QH[t]], normalize_embeddings=True, batch_size=32)
try:
    import importlib.metadata as md
    versions = {p: md.version(p) for p in ("sentence-transformers", "torch", "rank-bm25", "scikit-learn", "transformers")}
except Exception:  # noqa: BLE001
    versions = {}
BM = {t: BM25Okapi([analyzer(x) for x in FULL[t]]) for t in TASKS}


def ranked_tfidf(t, q):
    b = TB[t]["B"]
    s = (b.vec.transform([q]) @ b.X.T).toarray().ravel()
    return [b.families[i] for i in s.argsort()[::-1] if s[i] > 0]


def ranked_bm25(t, q):
    s = BM[t].get_scores(analyzer(q))
    return [POOL[t][i] for i in np.argsort(-s, kind="stable")]


def ranked_emb(t, q, name, field):
    e = ENC[name]
    qv = e["m"].encode([e["q"] + q], normalize_embeddings=True)[0]
    s = e[field][t] @ qv
    return [POOL[t][i] for i in np.argsort(-s, kind="stable")]


def rrf(*lists):
    sc = defaultdict(float)
    for L in lists:
        for r, f in enumerate(L):
            sc[f] += 1.0 / (RRF_K + r + 1)
    return [f for f, _ in sorted(sc.items(), key=lambda x: (-x[1], x[0]))]


def retrievers(t, q):
    out = {"tfidf_full": ranked_tfidf(t, q), "bm25_full": ranked_bm25(t, q)}
    for name in ENC:
        short = name.split("/")[-1]
        out[f"emb_full:{short}"] = ranked_emb(t, q, name, "full")
        out[f"emb_qh:{short}"] = ranked_emb(t, q, name, "qh")
        out[f"hybrid_rrf:{short}"] = rrf(out["tfidf_full"], out[f"emb_full:{short}"])
    return out


def first_rank(ranking, fams):
    return next((i + 1 for i, f in enumerate(ranking) if f[4:] in fams), None)


rows = []
cleans = {t: clean_question(t) for t in TASKS}
items = [dict(q, kind="model") for q in queries] + \
        [{"run_id": f"clean|{t}", "model": "clean", "task_id": t, "condition": "clean", "seed": "", "query": cleans[t],
          "first_fams": set(), "all_fams": set()} for t in TASKS]
for n, it in enumerate(items):
    t = it["task_id"]
    Q, L = REL[t]["Q"], REL[t]["L"]
    for rname, ranking in retrievers(t, it["query"]).items():
        row = {"run_id": it["run_id"], "model": it["model"], "task_id": t, "query_source": it["condition"],
               "retriever": rname, "n_ranked": len(ranking),
               "first_Q_rank": first_rank(ranking, Q), "first_L_rank": first_rank(ranking, L),
               "first_any_rank": first_rank(ranking, Q | L)}
        for f in WATCH.get(t, []):
            row[f"rank_{f}"] = first_rank(ranking, {f})
        if t in MANUAL:
            row["first_Q_or_manual_rank"] = first_rank(ranking, Q | {MANUAL[t]})
        for k in KS:
            top = {f[4:] for f in ranking[:k]}
            row[f"Q@{k}"] = int(bool(top & Q))
            row[f"L@{k}"] = int(bool(top & L))
            row[f"any@{k}"] = int(bool(top & (Q | L)))
            row[f"n@{k}"] = len(ranking[:k])
        rows.append(row)
    if it["condition"] != "clean":
        so = it.get("saved_order")
        rows.append({"run_id": it["run_id"], "model": it["model"], "task_id": t, "query_source": it["condition"],
                     "retriever": "as_run_first_call", "Q@4": int(bool(it["first_fams"] & Q)), "L@4": int(bool(it["first_fams"] & L)),
                     "any@4": int(bool(it["first_fams"] & (Q | L))),
                     "first_any_rank": first_rank(so, Q | L) if so else None, "order_matched": int(bool(so))})
        rows.append({"run_id": it["run_id"], "model": it["model"], "task_id": t, "query_source": it["condition"],
                     "retriever": "as_run_all_calls", "Q@4": int(bool(it["all_fams"] & Q)), "L@4": int(bool(it["all_fams"] & L)),
                     "any@4": int(bool(it["all_fams"] & (Q | L)))})
    if n % 50 == 0:
        print("queries done", n, "of", len(items))

fields = sorted({k for r in rows for k in r}, key=lambda k: (k not in ("run_id", "model", "task_id", "query_source", "retriever"), k))
with open(os.path.join(OUT, "per_query.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

# ------------------------------------------------------------------ summaries
QT = [t for t in TASKS if REL[t]["Q"]]
AT = [t for t in TASKS if REL[t]["Q"] or REL[t]["L"]]
LT = [t for t in TASKS if REL[t]["L"] and not REL[t]["Q"]]
NT = [t for t in TASKS if not (REL[t]["Q"] or REL[t]["L"])]
summ = {"relevance_sets": {t: {"Q": sorted(REL[t]["Q"]), "n_L": len(REL[t]["L"])} for t in TASKS},
        "pool_sizes": {t: len(POOL[t]) for t in TASKS}, "clean_queries": cleans, "models": model_info,
        "versions": versions, "tasks_Q": QT, "tasks_any": AT, "tasks_L_only": LT, "tasks_none": NT, "table": []}
rnames = sorted({r["retriever"] for r in rows})
for src in ("B", "C", "clean"):
    for rn in rnames:
        for k in KS:
            g = [r for r in rows if r["query_source"] == src and r["retriever"] == rn and f"Q@{k}" in r]
            if not g:
                continue
            gq = [r for r in g if r["task_id"] in QT]
            ga = [r for r in g if r["task_id"] in AT]
            gl = [r for r in g if r["task_id"] in LT]
            summ["table"].append({"query_source": src, "retriever": rn, "k": k,
                                  "Q_hits": sum(r[f"Q@{k}"] for r in gq), "Q_n": len(gq),
                                  "any_hits": sum(r[f"any@{k}"] for r in ga), "any_n": len(ga),
                                  "Lonly_hits": sum(r[f"L@{k}"] for r in gl), "Lonly_n": len(gl)})
            if rn.startswith("as_run"):
                break
watch = []
for t, fs in WATCH.items():
    for f in fs:
        for src in ("B", "C", "clean"):
            for rn in rnames:
                g = [r[f"rank_{f}"] for r in rows if r["task_id"] == t and r["query_source"] == src and r["retriever"] == rn and f"rank_{f}" in r]
                if g:
                    have = [x for x in g if x is not None]
                    watch.append({"task": t, "family": f, "query_source": src, "retriever": rn, "n": len(g),
                                  "median_rank": float(np.median(have)) if have else None, "best_rank": min(have) if have else None,
                                  "in_top4": sum(1 for x in have if x <= 4), "in_top20": sum(1 for x in have if x <= 20), "never_ranked": len(g) - len(have)})
summ["watch"] = watch
noise = []
for t in NT:
    for rn in rnames:
        g = [r for r in rows if r["task_id"] == t and r["retriever"] == rn and "n@4" in r and r["query_source"] in ("B", "C")]
        if g:
            noise.append({"task": t, "retriever": rn, "n_queries": len(g), "mean_returned_at_4": float(np.mean([r["n@4"] for r in g])),
                          "queries_returning_fewer_than_4": sum(1 for r in g if r["n@4"] < 4)})
summ["noise"] = noise

# vocabulary overlap between each query and each question-tier family's full text
overlap = []
for q in queries:
    t = q["task_id"]
    if t not in QT:
        continue
    qt = set(analyzer(q["query"]))
    for f in REL[t]["Q"] | ({MANUAL[t]} if t in MANUAL else set()):
        fid = "FAM:" + f
        if fid not in TB[t]["B"].doc_text:
            continue
        dt = set(analyzer(TB[t]["B"].doc_text[fid]))
        overlap.append({"run_id": q["run_id"], "task": t, "condition": q["condition"], "family": f,
                        "query_terms": len(qt), "shared_terms": len(qt & dt), "share_of_query_terms": len(qt & dt) / max(1, len(qt))})
summ["overlap"] = overlap
json.dump(summ, open(os.path.join(OUT, "summary.json"), "w", encoding="utf-8"), indent=1, default=list)
print("done", len(rows), "rows")
