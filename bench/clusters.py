"""Research-question clusters: study families that ask substantially the same question.

Unit: the study family (members are already known to describe one study). Each family is embedded with TF-IDF
(unigrams; numbers, record ids and stop words removed) over the title, hypothesis and design of its members, and
families are grouped by average-linkage agglomerative clustering on cosine distance across all topics.

Calibration: same-family record pairs are pairs known to ask one question. The merge threshold is the 25th percentile
of their similarity (three quarters of known same-question pairs are at least this similar); the repeat threshold is
their median. Both are computed from the data on every run and reported, not fixed by hand.
"""
import collections

import numpy as np

from . import common


def record_texts(records):
    return [f"{r.get('title', '')}. {r.get('hypothesis', '')}. {r.get('design', '')}" for r in records]


def vectorizer(texts):
    from sklearn.feature_extraction.text import TfidfVectorizer
    vec = TfidfVectorizer(preprocessor=common.norm_text, ngram_range=(1, 1), sublinear_tf=True, min_df=1)
    return vec, vec.fit_transform(texts)


def cosine(X):
    S = (X @ X.T)
    S = S.toarray() if hasattr(S, "toarray") else np.asarray(S)
    np.fill_diagonal(S, 1.0)
    return S


def pair_separation(records, family_of):
    """Similarity of same-family record pairs versus pairs from different families (the calibration evidence)."""
    from sklearn.metrics import roc_auc_score
    _, X = vectorizer(record_texts(records))
    S = cosine(X)
    pos, neg = [], []
    for i in range(len(records)):
        for j in range(i + 1, len(records)):
            (pos if family_of[records[i]["id"]] == family_of[records[j]["id"]] else neg).append(S[i, j])
    y = [1] * len(pos) + [0] * len(neg)
    return {"same_family_pairs": len(pos), "other_pairs": len(neg),
            "auc": round(float(roc_auc_score(y, pos + neg)), 3) if pos else None,
            "same_family_median": round(float(np.median(pos)), 3) if pos else None,
            "same_family_p25": round(float(np.quantile(pos, 0.25)), 3) if pos else None,
            "other_p95": round(float(np.quantile(neg, 0.95)), 3), "other_p99": round(float(np.quantile(neg, 0.99)), 3)}


def family_matrix(records, family_of, members):
    by_id = {r["id"]: r for r in records}
    fams = sorted({family_of[r["id"]] for r in records})
    texts = [" ".join(record_texts([by_id[m] for m in members[f] if m in by_id])) for f in fams]
    vec, X = vectorizer(texts)
    return fams, vec, X


def agglomerate(S, threshold):
    from sklearn.cluster import AgglomerativeClustering
    if len(S) == 1:
        return np.array([0])
    D = np.clip(1.0 - S, 0.0, 1.0)
    return AgglomerativeClustering(n_clusters=None, metric="precomputed", linkage="average",
                                   distance_threshold=threshold).fit_predict(D)


def top_terms(vec, X, rows, k=6):
    sub = np.asarray(X[rows].sum(axis=0)).ravel()
    terms = np.array(vec.get_feature_names_out())
    picked = []
    for j in np.argsort(-sub):
        if sub[j] <= 0 or len(picked) == k:
            break
        t = terms[j]
        if not any(t in p or p in t for p in picked):
            picked.append(t)
    return picked


def family_order(fa, fb, members, by_id):
    """'before' if every record of fa certainly precedes every record of fb, 'after' for the reverse, else 'unknown'."""
    A = [by_id[m] for m in members[fa] if m in by_id]
    B = [by_id[m] for m in members[fb] if m in by_id]
    if all(common.strictly_before(a, b) for a in A for b in B):
        return "before"
    if all(common.strictly_before(b, a) for a in A for b in B):
        return "after"
    return "unknown"


def build(records, family_of, members, merge_sim=None, repeat_sim=None):
    """Return (family_rows, cluster_rows, calibration).

    family_rows: one row per study family with cluster id, nearest other family in the cluster, similarity and the
    relation to it: repeat_of_earlier_family, repeated_by_later_family, repeat_order_unknown, related_question,
    or distinct_question (alone in its cluster).
    """
    by_id = {r["id"]: r for r in records}
    cal = pair_separation(records, family_of)
    merge_sim = merge_sim if merge_sim is not None else (cal["same_family_p25"] or 0.22)
    repeat_sim = repeat_sim if repeat_sim is not None else (cal["same_family_median"] or 0.32)
    cal.update({"merge_similarity": merge_sim, "repeat_similarity": repeat_sim})
    fams, vec, X = family_matrix(records, family_of, members)
    S = cosine(X)
    lab = agglomerate(S, 1.0 - merge_sim)
    groups = collections.defaultdict(list)
    for i, l in enumerate(lab):
        groups[int(l)].append(i)
    ordered = sorted(groups.values(), key=lambda g: (-len(g), fams[g[0]]))
    cid = {}
    for n, g in enumerate(ordered):
        for i in g:
            cid[i] = f"RQC-{n + 1:03d}"
    fam_rows = []
    for i, f in enumerate(fams):
        g = next(g for g in ordered if i in g)
        others = [j for j in g if j != i]
        best = max(others, key=lambda j: S[i, j]) if others else None
        sim = float(S[i, best]) if best is not None else 0.0
        rel, o = "distinct_question", ""
        if best is not None:
            o = family_order(fams[best], f, members, by_id)
            if sim >= repeat_sim:
                rel = {"before": "repeat_of_earlier_family", "after": "repeated_by_later_family"}.get(o, "repeat_order_unknown")
            else:
                rel = "related_question"
        rep = common.representative([m for m in members[f] if m in by_id])
        fam_rows.append({"study_family_id": f, "cluster_id": cid[i], "cluster_size_families": len(g),
                         "topic": common.topic_of(by_id[rep]), "representative": rep,
                         "members": "; ".join(m for m in members[f] if m in by_id),
                         "nearest_family_in_cluster": fams[best] if best is not None else "",
                         "nearest_similarity": round(sim, 3), "nearest_order": o, "relation": rel})
    cl_rows = []
    for n, g in enumerate(ordered):
        within = [S[a, b] for x, a in enumerate(g) for b in g[x + 1:]]
        recs = sorted(m for i in g for m in members[fams[i]] if m in by_id)
        topics = collections.Counter(common.topic_of(by_id[m]) for m in recs)
        cl_rows.append({"cluster_id": f"RQC-{n + 1:03d}", "n_families": len(g), "n_records": len(recs),
                        "main_topic": topics.most_common(1)[0][0], "topics": "; ".join(f"{t} ({c})" for t, c in topics.most_common()),
                        "label_terms": "; ".join(top_terms(vec, X, g)),
                        "mean_within_similarity": round(float(np.mean(within)), 3) if within else "",
                        "families": "; ".join(fams[i] for i in g), "records": "; ".join(recs)})
    return fam_rows, cl_rows, cal


def related_field_agreement(records, family_rows, family_of):
    """Share of explicit related-field id references whose two families fall in one cluster (external sanity check)."""
    cl = {r["study_family_id"]: r["cluster_id"] for r in family_rows}
    ids = {r["id"] for r in records}
    tot = same = 0
    for r in records:
        for ref in common.ID_RE.findall(str(r.get("related") or "")):
            if ref in ids and family_of[ref] != family_of[r["id"]]:
                tot += 1
                same += cl[family_of[ref]] == cl[family_of[r["id"]]]
    return {"cross_family_references": tot, "same_cluster": same, "rate": round(same / tot, 3) if tot else None}
