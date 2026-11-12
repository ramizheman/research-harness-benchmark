"""Statistics for comparing conditions: task-level paired contrasts, cluster bootstrap, sign-flip tests, Holm, TOST."""
import itertools
import math

import numpy as np


def auc(scores, labels):
    """Mann-Whitney AUC; None when one class is empty."""
    pos = [s for s, y in zip(scores, labels) if y == 1]
    neg = [s for s, y in zip(scores, labels) if y == 0]
    if not pos or not neg:
        return None
    wins = sum((p > n) + 0.5 * (p == n) for p in pos for n in neg)
    return wins / (len(pos) * len(neg))


def balanced_accuracy(pred, truth):
    pos = [p == t for p, t in zip(pred, truth) if t == 1]
    neg = [p == t for p, t in zip(pred, truth) if t == 0]
    parts = [np.mean(x) for x in (pos, neg) if x]
    return float(np.mean(parts)) if parts else None


def task_means(rows, metric, condition):
    """Mean of metric per task for one condition (averaging seeds and models), skipping missing values."""
    acc = {}
    for r in rows:
        v = r.get(metric)
        if r["condition"] != condition or v is None or (isinstance(v, float) and math.isnan(v)) or v == "":
            continue
        acc.setdefault(r["task_id"], []).append(float(v))
    return {t: float(np.mean(v)) for t, v in acc.items()}


def paired(rows, metric, a, b):
    """Per-task differences b minus a for tasks present in both conditions."""
    ma, mb = task_means(rows, metric, a), task_means(rows, metric, b)
    tasks = sorted(set(ma) & set(mb))
    return tasks, np.array([mb[t] - ma[t] for t in tasks])


def bootstrap_ci(d, n_boot=10000, alpha=0.05, seed=0):
    if len(d) == 0:
        return (None, None)
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(d), size=(n_boot, len(d)))
    means = d[idx].mean(axis=1)
    return float(np.quantile(means, alpha / 2)), float(np.quantile(means, 1 - alpha / 2))


def sign_flip_p(d, n_mc=20000, seed=0):
    """Two-sided sign-flip permutation p-value for mean(d) = 0 (exact up to 16 tasks)."""
    d = np.asarray(d, dtype=float)
    if len(d) == 0:
        return None
    obs = abs(d.mean())
    if len(d) <= 16:
        sums = [abs(np.dot(s, d) / len(d)) for s in itertools.product((-1, 1), repeat=len(d))]
        return float(np.mean([s >= obs - 1e-12 for s in sums]))
    rng = np.random.default_rng(seed)
    s = rng.choice((-1, 1), size=(n_mc, len(d)))
    return float((np.abs((s * d).mean(axis=1)) >= obs - 1e-12).mean())


def holm(pvals):
    """Holm-adjusted p-values in the input order."""
    order = sorted(range(len(pvals)), key=lambda i: pvals[i])
    adj, running = [0.0] * len(pvals), 0.0
    for k, i in enumerate(order):
        running = max(running, min(1.0, (len(pvals) - k) * pvals[i]))
        adj[i] = running
    return adj


def tost(d, margin, n_boot=10000, seed=0):
    """Equivalence by the 90% bootstrap interval lying inside (-margin, margin)."""
    lo, hi = bootstrap_ci(np.asarray(d, dtype=float), n_boot=n_boot, alpha=0.10, seed=seed)
    if lo is None:
        return {"ci90": (None, None), "equivalent": None}
    return {"ci90": (lo, hi), "equivalent": bool(lo > -margin and hi < margin)}


def contrast(rows, metric, a, b, higher_is_better=True):
    tasks, d = paired(rows, metric, a, b)
    if not higher_is_better:
        d = -d
    lo, hi = bootstrap_ci(d)
    return {"metric": metric, "contrast": f"{b} - {a}" + ("" if higher_is_better else " (sign flipped: positive = better)"),
            "n_tasks": len(tasks), "mean_difference": float(d.mean()) if len(d) else None, "ci95": (lo, hi),
            "p_sign_flip": sign_flip_p(d)}
