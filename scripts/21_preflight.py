r"""Pre-flight check for a config: tasks, snapshots, conditions, retrieval ranking, run count, spend cap and the API key.

Usage: python scripts\21_preflight.py configs\pilot.json [--smoke]
Key checks use free model-listing endpoints. --smoke additionally sends one tiny request (a few hundred tokens,
well under 0.01 USD) to confirm that generation, JSON mode and the reported model version work.
Prints READY only if every check passes. Key values are never printed.
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from runner import experiment, llm, tools, tools_v3  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("config")
ap.add_argument("--smoke", action="store_true")
a = ap.parse_args()
cfg = experiment.load_config(a.config if os.path.isabs(a.config) else os.path.join(experiment.HB, a.config))
env = cfg.get("env_path", llm.DEFAULT_ENV)
ok = True


def check(name, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + (f": {detail}" if detail else ""))


# Study 1b: conditions O and OS, per-model condition lists, frozen gold families and scope annotations.
# Study 2 also loads an oracle file, but its conditions are A, B and O and its annotation file is empty.
oracle = experiment.oracle_inputs(cfg)
study2 = bool(oracle) and sorted(cfg.get("conditions", [])) == ["A", "B", "O"]


def toolbox3(cond, task):
    snap3 = None if cond == "A" else experiment.ensure_snapshot_v3(task)[0]
    extra = {"gold": oracle["gold"][task["task_id"]], "annotations": oracle["annotations"]} if cond in tools_v3.ORACLE_CONDITIONS else {}
    return tools_v3.Toolbox3(cond, snap3, cfg["budgets"]["max_tool_result_chars"], **extra)


# ------------------------------------------------------------------ design
runs = experiment.plan(cfg)
if study2:
    conds_of = {m["model"]: m.get("conditions", cfg["conditions"]) for m in cfg["models"]}
    n_expected = sum(len(cfg["tasks"]) * len(c) * len(cfg["seeds"]) for c in conds_of.values())
    check("run count", len(runs) == n_expected,
          f"{len(runs)} runs = {len(cfg['tasks'])} tasks x {len(cfg['seeds'])} seed(s) x conditions per model "
          + ", ".join(f"{m} {'/'.join(c)}" for m, c in conds_of.items()))
    check("conditions", sorted(cfg["conditions"]) == ["A", "B", "O"] and all(set(c) == {"A", "B", "O"} for c in conds_of.values()),
          ", ".join(cfg["conditions"]))
    check("every model runs exactly its listed conditions",
          all({r["condition"] for r in runs if r["model"]["model"] == m} == set(c) for m, c in conds_of.items()))
    check("gold families loaded for every task; scope annotations empty (OS is not a Study 2 condition)",
          set(oracle["gold"]) == set(cfg["tasks"]) and oracle["annotations"] == {},
          ", ".join(f"{k} {v[:12]}" for k, v in oracle["hashes"].items()))
    check("study budget stop", experiment.spend_cap(cfg) is not None and cfg.get("budget_usd") is not None
          and experiment.spend_cap(cfg) <= cfg["budget_usd"] * cfg.get("stop_fraction", 0.8),
          f"runs stop once recorded spend reaches {experiment.spend_cap(cfg)} USD (budget {cfg.get('budget_usd')} USD)")
elif oracle:
    conds_of = {m["model"]: m.get("conditions", cfg["conditions"]) for m in cfg["models"]}
    n_expected = sum(len(cfg["tasks"]) * len(c) * len(cfg["seeds"]) for c in conds_of.values())
    check("run count", len(runs) == n_expected,
          f"{len(runs)} runs = {len(cfg['tasks'])} tasks x {len(cfg['seeds'])} seed(s) x conditions per model "
          + ", ".join(f"{m} {'/'.join(c)}" for m, c in conds_of.items()))
    check("conditions", sorted(cfg["conditions"]) == ["O", "OS"] and all(set(c) <= {"O", "OS"} for c in conds_of.values()),
          ", ".join(cfg["conditions"]))
    check("every model runs exactly its listed conditions",
          all({r["condition"] for r in runs if r["model"]["model"] == m} == set(c) for m, c in conds_of.items()))
    check("gold families and scope annotations loaded for every task, every gold family annotated",
          set(oracle["gold"]) == set(cfg["tasks"]) and all(f in oracle["annotations"] for g in oracle["gold"].values() for f in g),
          ", ".join(f"{k} {v[:12]}" for k, v in oracle["hashes"].items()))
    check("study budget stop", experiment.spend_cap(cfg) is not None and cfg.get("budget_usd") is not None
          and experiment.spend_cap(cfg) <= cfg["budget_usd"] * cfg.get("stop_fraction", 0.8),
          f"runs stop once recorded spend reaches {experiment.spend_cap(cfg)} USD (budget {cfg.get('budget_usd')} USD)")
else:
    n_expected = len(cfg["models"]) * len(cfg["tasks"]) * len(cfg["conditions"]) * len(cfg["seeds"])
    check("run count", len(runs) == n_expected,
          f"{len(runs)} runs = {len(cfg['models'])} model(s) x {len(cfg['tasks'])} tasks x {len(cfg['conditions'])} conditions x {len(cfg['seeds'])} seed(s)")
    check("conditions", sorted(cfg["conditions"]) == ["A", "B", "C"], ", ".join(cfg["conditions"]))
specs = {json.dumps(r["model"], sort_keys=True) for r in runs}
by_cond = {c: {json.dumps(r["model"], sort_keys=True) for r in runs if r["condition"] == c} for c in cfg["conditions"]}
if oracle:
    pass  # per-model condition lists, checked above
elif len(cfg["models"]) == 1:
    check("one model, identical settings in every condition", len(specs) == 1 and all(v == specs for v in by_cond.values()),
          next(iter(specs)) if len(specs) == 1 else f"{len(specs)} distinct model specs")
else:
    # multi-model: each condition must see the same set of models, not just one
    check("all conditions see the same set of models", all(v == by_cond[cfg["conditions"][0]] for v in by_cond.values()),
          f"{len(cfg['models'])} models, conditions consistent: {all(v == by_cond[cfg['conditions'][0]] for v in by_cond.values())}")
check("no mock client", all(m["provider"] != "mock" for m in cfg["models"]))
check("spend cap", cfg.get("max_cost_usd", 0) >= 5.0, f"{cfg.get('max_cost_usd')} USD")
priced = all(m["provider"] == "openrouter" or m.get("price_per_million") for m in cfg["models"])
check("cost is computable for the cap", priced, "price_per_million set" if priced else "no price: the cap could not be enforced")

# ------------------------------------------------------------------ tasks, snapshots, exclusions
keys = experiment.answer_key()
for t in cfg["tasks"]:
    try:
        task = experiment.load_task(t)
        _, man = experiment.ensure_snapshot(task)
        excl = set(task.get("excluded_records", []))
        check(f"{t} frozen task, snapshot, exclusions, answer key", t in keys and not (excl & set(man["records"])),
              f"{man['n_records']} permitted records, {len(excl)} excluded and absent, {man['n_facts']} facts, documents = graph")
    except Exception as e:  # noqa: BLE001
        check(f"{t}", False, repr(e))

# ------------------------------------------------------------------ retrieval ranking
snap, _ = experiment.ensure_snapshot(experiment.load_task(cfg["tasks"][0]))
dm, gm = tools.DocumentMemory(os.path.join(snap, "documents")), tools.GraphMemory(os.path.join(snap, "graph"))
pd, pg = dm.vec.get_params(), gm.vec.get_params()
check("document and graph search use the same ranking (TF-IDF, identical settings)", pd == pg,
      "sublinear_tf={sublinear_tf}, token_pattern={token_pattern}".format(**pd))

# ------------------------------------------------------------------ protocol 2: controls against the comparator pilot
protocol = cfg.get("protocol", 1)
if protocol == 2:
    from runner import agent  # noqa: E402
    comp_id = cfg.get("comparator_experiment_id")
    if comp_id:
        cm = json.load(open(os.path.join(experiment.HB, "runs", comp_id, "manifest.json"), encoding="utf-8"))["config"]
        same = {k: cm.get(k) == cfg.get(k) for k in ("models", "tasks", "conditions", "seeds", "order_seed", "budgets", "max_cost_usd", "equivalence_margin")}
        check(f"identical to {comp_id} in model, generation settings, tasks, seed, order and budgets", all(same.values()),
              ", ".join(k for k, v in same.items() if not v) or "all equal")
        comp_raw = experiment.raw_runs({"_out": os.path.join(experiment.HB, "runs", comp_id)})
        cv = sorted({v for r in comp_raw for v in r.get("model_versions", [])})
        check(f"{comp_id} responses all report the expected model version", cv == [cfg.get("expected_response_model_version")], ", ".join(cv))
    prompts = {}
    for c in cfg["conditions"]:
        tb = tools.Toolbox(c, snap if c != "A" else None, cfg["budgets"]["max_tool_result_chars"], protocol)
        p = agent.system_prompt(tb, cfg["budgets"]["max_tool_calls"], protocol)
        prompts[c] = p.replace(tb.describe(), "<TOOLS>")
        check(f"{c} prompt lists retrieve_history first with the shared description", tb.describe().startswith("- " + tools.TOOL_DOCS["retrieve_history"]))
    check("protocol-2 instructions identical in every condition apart from the tool list", len(set(prompts.values())) == 1)
    for t in cfg["tasks"]:
        task = experiment.load_task(t)
        s, _ = experiment.ensure_snapshot(task)
        q = {"research_question": task["statement"][:400], "query": task["statement"][:200]}
        ra = json.loads(tools.Toolbox("A", None, 6000, protocol).call("retrieve_history", q))
        tb_b, tb_c = tools.Toolbox("B", s, 6000, protocol), tools.Toolbox("C", s, 6000, protocol)
        ib = [x["id"] for x in json.loads(tb_b.call("retrieve_history", q))["results"]]
        ic = [x["id"] for x in json.loads(tb_c.call("retrieve_history", q))["results"]]
        check(f"{t} retrieval: A executes and returns nothing; B and C return the same ranked items",
              ra == {"results": [], "n_results": 0} and ib == ic and len(ib) > 0, f"{len(ib)} items")

# ------------------------------------------------------------------ protocol 3: family memory, distinct retrieval, retrieval first
stage1_probe = []
if protocol >= 3 and study2:
    from runner import agent, tools_v3  # noqa: E402
    check("run count (4 models x 68 tasks x A, B, O x seed 1)",
          len(runs) == n_expected and len(cfg["tasks"]) == 68 and cfg["seeds"] == [1],
          f"{len(runs)} runs (expected {n_expected})")
    src = json.load(open(os.path.join(experiment.HB, "configs", "study1b.json"), encoding="utf-8"))
    src_models = {m["model"]: {k: v for k, v in m.items() if k != "conditions"} for m in src["models"]}
    for m in cfg["models"]:
        check(f"{m['model']} generation settings and price identical to configs/study1b.json", m == src_models.get(m["model"]))
    check("budgets identical to configs/study1b.json", cfg["budgets"] == src["budgets"])
    budget = cfg["budgets"]["max_tool_result_chars"]
    prompts = {}
    task0 = experiment.load_task(cfg["tasks"][0])
    for c in cfg["conditions"]:
        tb = toolbox3(c, task0)
        p = agent.system_prompt_v3(tb, cfg["budgets"]["max_tool_calls"])
        prompts[c] = p.replace(tb.describe(), "<TOOLS>")
        check(f"{c} prompt lists retrieve_history first with the shared description",
              tb.describe().startswith("- " + tools_v3.TOOL_DOCS["retrieve_history"]))
    check("protocol-3 system instructions identical in every condition apart from the tool list", len(set(prompts.values())) == 1)
    sp = next(iter(prompts.values()))
    check("output schema is not shown before retrieval (system prompt and stage-1 message)",
          not any(k in sp + agent.STAGE1 for k in ('"predicted_outcome"', '"historical_evidence"', '"p_testable"', "Output schema")))
    check("stage-2 schema contains the scored fields and the evidence fields",
          all(k in agent.stage2_text() for k in list(agent.scoring.OUTPUT_SCHEMA) + list(agent.EVIDENCE_SCHEMA)))
    n_empty_gold = 0
    q = {"query": "sample", "research_concepts": ["sample size and statistical power"], "methodological_questions": ["is the outcome measure reliable"]}
    for t in cfg["tasks"]:
        try:
            task = experiment.load_task(t)
            d, man = experiment.ensure_snapshot_v3(task)
            check(f"{t} v3 family memory: documents = graph, every family has every field, exclusions absent",
                  man["equivalent"] and man["every_family_has_all_fields"] and not (set(man["records"]) & set(task.get("excluded_records", []))),
                  f"{man['n_families']} families, {man['n_facts']} facts")
            ra = json.loads(tools_v3.Toolbox3("A", None, budget).call("retrieve_history", q))
            tb_b = tools_v3.Toolbox3("B", d, budget)
            sb = tb_b.call("retrieve_history", q)
            rb = json.loads(sb)["results"]
            want_b = min(tools_v3.RETRIEVE_K, len(tb_b.families))
            gold = oracle["gold"][t]
            so = toolbox3("O", task).call("retrieve_history", q)
            ro = json.loads(so)["results"]
            check(f"{t} retrieval: A empty; B returns {want_b} families uncut; O returns the {len(gold)} frozen gold families in order, uncut, with no annotation",
                  ra == {"results": [], "n_results": 0} and len(tb_b.families) > 0 and len(rb) == want_b
                  and "truncated" not in sb and len(sb) <= budget
                  and [x["id"] for x in ro] == ["FAM:" + f for f in gold]
                  and "truncated" not in so and len(so) <= budget
                  and not any("scope_annotation" in x for x in ro)
                  and all(x["document"] == tb_b.doc_text[x["id"]] for x in ro),
                  f"B {len(sb)} chars, O {len(so)} chars, {len(tb_b.families)} families in memory")
            if not gold:
                n_empty_gold += 1
        except Exception as e:  # noqa: BLE001
            check(f"{t} protocol 3", False, repr(e)[:300])
    check("tasks with no gold families return an empty oracle list", n_empty_gold > 0, f"{n_empty_gold} tasks")
elif protocol >= 3:
    from runner import agent, tools_v3  # noqa: E402
    n_models = len(cfg["models"])
    expected_p3 = n_expected if oracle else 10 * 3 * 3 * n_models
    check(f"run count ({n_models} model(s) x 10 tasks x {'conditions per model' if oracle else '3 conditions'} x seeds 1, 2, 3)",
          len(runs) == expected_p3 and len(cfg["tasks"]) == 10 and cfg["seeds"] == [1, 2, 3],
          f"{len(runs)} runs (expected {expected_p3})")
    comp_models = {}
    for comp_id in cfg.get("comparator_experiment_ids", []):
        try:
            cm = json.load(open(os.path.join(experiment.HB, "runs", comp_id, "manifest.json"), encoding="utf-8"))["config"]
        except FileNotFoundError:
            check(f"comparator {comp_id} manifest exists", False, f"runs/{comp_id}/manifest.json not found"); continue
        if oracle:
            # Study 1b runs new conditions (O, OS) in a new order; it shares tasks and budgets with the comparators,
            # and each of its models must have the comparator's generation settings and response version.
            same = {k: cm.get(k) == cfg.get(k) for k in ("tasks", "budgets")}
            check(f"identical to {comp_id} in tasks and budgets; {comp_id} ran A, B and C", all(same.values()) and sorted(cm.get("conditions", [])) == ["A", "B", "C"],
                  ", ".join(k for k, v in same.items() if not v) or f"all equal; {comp_id} conditions {', '.join(cm.get('conditions', []))}")
            comp_raw = experiment.raw_runs({"_out": os.path.join(experiment.HB, "runs", comp_id)})
            for s in cm["models"]:
                comp_models[s["model"]] = (comp_id, s, cm.get("expected_response_model_version"),
                                           sorted({v for r in comp_raw if r["model"]["model"] == s["model"] for v in r.get("model_versions", [])}))
            continue
        # cross-model and reasoning-model experiments may differ in 'models' and in 'max_cost_usd'
        # (reasoning models legitimately need a higher cap); compare only the core scientific design.
        design_keys = ("tasks", "conditions", "order_seed", "budgets", "equivalence_margin")
        same = {k: cm.get(k) == cfg.get(k) for k in design_keys}
        check(f"identical to {comp_id} in tasks, conditions, order, budgets, cap and margin (models and seeds may differ)",
              all(same.values()), ", ".join(k for k, v in same.items() if not v) or "all equal")
        if cfg.get("expected_response_model_version"):
            cv = sorted({v for r in experiment.raw_runs({"_out": os.path.join(experiment.HB, "runs", comp_id)}) for v in r.get("model_versions", [])})
            check(f"{comp_id} responses report the expected model version", cv == [cfg.get("expected_response_model_version")], ", ".join(cv))
    if oracle:
        added = ("conditions", "expected_response_model_version", "price_per_million")
        for m in cfg["models"]:
            comp_id, s, comp_ver, cv = comp_models.get(m["model"], (None, {}, None, []))
            check(f"{m['model']} generation settings and price identical to its Study 1 run ({comp_id})",
                  comp_id is not None and {k: v for k, v in m.items() if k not in added} == {k: v for k, v in s.items() if k not in added}
                  and {k: m["price_per_million"][k] for k in ("input", "output")} == {k: s.get("price_per_million", {}).get(k) for k in ("input", "output")})
            exp = m.get("expected_response_model_version")
            if exp:
                check(f"{m['model']}: {comp_id} responses report the expected model version {exp}", cv == [exp] and comp_ver in (None, exp), ", ".join(cv))
    budget = cfg["budgets"]["max_tool_result_chars"]
    prompts, stage1 = {}, set()
    task0 = experiment.load_task(cfg["tasks"][0])
    for c in (["A"] if oracle else []) + cfg["conditions"]:
        tb = toolbox3(c, task0)
        p = agent.system_prompt_v3(tb, cfg["budgets"]["max_tool_calls"])
        prompts[c] = p.replace(tb.describe(), "<TOOLS>")
        check(f"{c} prompt lists retrieve_history first with the shared description", tb.describe().startswith("- " + tools_v3.TOOL_DOCS["retrieve_history"]))
    check("protocol-3 system instructions identical in every condition apart from the tool list"
          + (" (O and OS compared with Study 1's A)" if oracle else ""), len(set(prompts.values())) == 1)
    sp = next(iter(prompts.values()))
    check("output schema is not shown before retrieval (system prompt and stage-1 message)",
          not any(k in sp + agent.STAGE1 for k in ('"predicted_outcome"', '"historical_evidence"', '"p_testable"', "Output schema")))
    check("stage-2 schema contains the scored fields and the evidence fields",
          all(k in agent.stage2_text() for k in list(agent.scoring.OUTPUT_SCHEMA) + list(agent.EVIDENCE_SCHEMA)))
    for t in cfg["tasks"]:
        try:
            task = experiment.load_task(t)
            d, man = experiment.ensure_snapshot_v3(task)
            check(f"{t} v3 family memory: documents = graph, every family has every field, exclusions absent",
                  man["equivalent"] and man["every_family_has_all_fields"], f"{man['n_families']} families, {man['n_facts']} facts")
            q = {"query": task["statement"].split("\n")[1][:300], "research_concepts": ["sample size and statistical power", "selection bias"],
                 "methodological_questions": ["is the outcome measure reliable enough to detect the effect"]}
            ra = json.loads(tools_v3.Toolbox3("A", None, budget).call("retrieve_history", q))
            tb_b, tb_c = tools_v3.Toolbox3("B", d, budget), tools_v3.Toolbox3("C", d, budget)
            sb, sc = tb_b.call("retrieve_history", q), tb_c.call("retrieve_history", q)
            rb, rc = json.loads(sb)["results"], json.loads(sc)["results"]
            tr = tb_c.last_trace
            views_equal = all(tools_v3.family_view(tb_b.facts[f]) == tools_v3.family_view(tb_c.facts[f]) for f in tb_b.families)
            check(f"{t} retrieval: A empty; B document search and C graph traversal return {tools_v3.RETRIEVE_K} families each under the cap; "
                  "identical family views; C reached families through relationships",
                  ra == {"results": [], "n_results": 0} and len(rb) == len(rc) == tools_v3.RETRIEVE_K and len(sb) <= budget and len(sc) <= budget
                  and "truncated" not in sb + sc and views_equal and tr["edges_traversed"] > 0
                  and any("; FAM:" in p or p.startswith("FAM:") for x in rc for p in x["reached_via"]),
                  f"B {len(sb)} chars, C {len(sc)} chars, {tr['edges_traversed']} edges traversed, "
                  f"{len({x['id'] for x in rb} & {x['id'] for x in rc})} of {tools_v3.RETRIEVE_K} families shared")
            if oracle:
                gold = oracle["gold"][t]
                so, ss = toolbox3("O", task).call("retrieve_history", q), toolbox3("OS", task).call("retrieve_history", q)
                ro, rs = json.loads(so)["results"], json.loads(ss)["results"]
                doc_b = {x["id"]: x["document"] for x in rb}
                check(f"{t} oracle: O and OS return the {len(gold)} frozen gold families in order, uncut; O documents are B's; "
                      "OS adds the frozen annotation to each family",
                      [x["id"] for x in ro] == [x["id"] for x in rs] == ["FAM:" + f for f in gold]
                      and "truncated" not in so + ss and len(so) <= budget
                      and all(x["document"] == doc_b[x["id"]] for x in ro if x["id"] in doc_b)
                      and [x["document"] for x in ro] == [x["document"] for x in rs]
                      and [x.get("scope_annotation") for x in rs] == [oracle["annotations"][f] for f in gold]
                      and not any("scope_annotation" in x for x in ro),
                      f"O {len(so)} chars, OS {len(ss)} chars in total")
        except Exception as e:  # noqa: BLE001
            check(f"{t} protocol 3", False, repr(e)[:300])
    stage1_probe = [(c, experiment.load_task(t)) for c, t in zip(cfg["conditions"], cfg["tasks"][:3])]

# ------------------------------------------------------------------ provider authentication
import requests  # noqa: E402

for m in cfg["models"]:
    if m["provider"] == "gemini":
        exp_ver = m.get("expected_response_model_version", cfg.get("expected_response_model_version"))
        try:
            key = llm.load_key(llm.GEMINI_KEY_NAMES, env)
            r = requests.get("https://generativelanguage.googleapis.com/v1beta/models?pageSize=1000", headers={"x-goog-api-key": key}, timeout=30)
            check("Gemini key accepted", r.ok, f"key read from {env} ({'GEMINI_API_KEY' if 'GEMINI_API_KEY' in open(env, encoding='utf-8').read() else 'GOOGLE_API_KEY'})" if r.ok else f"HTTP {r.status_code}")
            info = next((x for x in r.json().get("models", []) if x["name"] == "models/" + m["model"]), None) if r.ok else None
            check(f"model {m['model']} available for generateContent", info and "generateContent" in info.get("supportedGenerationMethods", []),
                  f"version {info.get('version')}, {info.get('displayName')}" if info else "")
            if cfg.get("expected_listing_version"):
                check(f"model version unchanged ({cfg['expected_listing_version']})", info and info.get("version") == cfg["expected_listing_version"],
                      f"listed version {info.get('version') if info else None}")
            if a.smoke and info:
                c = llm.make(m, env)
                text, u = c.chat('Reply with the JSON object {"ok": true} and nothing else.', [{"role": "user", "content": "ping"}], seed=1)
                good = json.loads(text or "{}").get("ok") is True
                check("smoke request (generation, JSON mode, seed, thinking budget)", good,
                      f"modelVersion={u.get('model_version')}, tokens {u['input_tokens']}+{u['output_tokens']}, cost {u['cost_usd']:.6f} USD")
                if exp_ver:
                    check("response model version matches the comparator pilot", u.get("model_version") == exp_ver,
                          f"{u.get('model_version')}")
            if a.smoke and info and stage1_probe:
                c = llm.make(m, env)
                for cond, task in stage1_probe:
                    tb = toolbox3(cond, task)
                    text, u = c.chat(agent.system_prompt_v3(tb, cfg["budgets"]["max_tool_calls"]),
                                     [{"role": "user", "content": task["statement"] + agent.STAGE1}], seed=1)
                    act, err, _ = agent.parse_action_lenient(text)
                    good = act is not None and act["action"] == "tool" and act.get("tool") == "retrieve_history" and not agent.has_assessment(act.get("args"))
                    check(f"stage-1 smoke {task['task_id']} condition {cond}: real model replies with the retrieval call only, no preliminary answer", good,
                          f"modelVersion={u.get('model_version')}, arg keys {sorted((act or {}).get('args', {}))}, cost {u['cost_usd']:.6f} USD" if act else err[:200])
                    check(f"stage-1 smoke {task['task_id']} response model version", u.get("model_version") == exp_ver,
                          f"{u.get('model_version')}")
        except Exception as e:  # noqa: BLE001
            check("Gemini key accepted", False, repr(e)[:300])
    elif m["provider"] == "openrouter":
        try:
            key = llm.load_key("OPENROUTER_API_KEY", env)
            # auth/key endpoint
            rk = requests.get("https://openrouter.ai/api/v1/auth/key",
                              headers={"Authorization": f"Bearer {key}"}, timeout=30)
            kd = rk.json().get("data", {}) if rk.ok else {}
            check("OpenRouter key accepted", rk.ok,
                  f"label={kd.get('label')} limit={kd.get('limit')} usage={kd.get('usage')} free_tier={kd.get('is_free_tier')}"
                  if rk.ok else f"HTTP {rk.status_code}")
            if rk.ok and kd.get("is_free_tier"):
                check("OpenRouter account is not free-tier (paid models require credits)", False,
                      "free-tier account cannot call gpt-oss-20b or claude-haiku-5.5")
            # model availability
            rm = requests.get("https://openrouter.ai/api/v1/models",
                              headers={"Authorization": f"Bearer {key}"}, timeout=30)
            or_models = {x["id"]: x for x in (rm.json().get("data", []) if rm.ok else [])}
            info = or_models.get(m["model"])
            check(f"OpenRouter model {m['model']} listed", info is not None,
                  f"pricing in=${float((info or {}).get('pricing', {}).get('prompt', 0))*1e6:.4f}/1M "
                  f"out=${float((info or {}).get('pricing', {}).get('completion', 0))*1e6:.4f}/1M ctx={info.get('context_length')}"
                  if info else "not found in model list")
            if a.smoke and info:
                client = llm.make(m, env)
                text, u = client.chat('Reply with the JSON object {"ok": true} and nothing else.',
                                      [{"role": "user", "content": "ping"}], seed=1)
                good = json.loads(text or "{}").get("ok") is True
                check(f"OpenRouter smoke {m['model']}", good,
                      f"model_version={u.get('model_version')} tokens {u['input_tokens']}+{u['output_tokens']} cost {u.get('cost_usd'):.6f} USD"
                      if good else f"bad reply: {text[:200]}")
            if a.smoke and info and stage1_probe:
                from runner import agent as _agent  # noqa: E402
                client = llm.make(m, env)
                for cond, task in stage1_probe[:1]:  # one stage-1 call per model
                    tb = toolbox3(cond, task)
                    text, u = client.chat(_agent.system_prompt_v3(tb, cfg["budgets"]["max_tool_calls"]),
                                         [{"role": "user", "content": task["statement"] + _agent.STAGE1}], seed=1)
                    act, err, _ = _agent.parse_action_lenient(text)
                    good = act is not None and act["action"] == "tool" and act.get("tool") == "retrieve_history" and not _agent.has_assessment(act.get("args"))
                    check(f"stage-1 smoke {m['model']} {task['task_id']} cond={cond}: retrieval call only, no preliminary answer", good,
                          f"model_version={u.get('model_version')} cost {u.get('cost_usd'):.6f} USD arg keys {sorted((act or {}).get('args', {}))}"
                          if act else err[:200])
        except Exception as e:  # noqa: BLE001
            check(f"OpenRouter {m['model']}", False, repr(e)[:300])
    elif m["provider"] in ("openai", "anthropic"):
        name, url, hdr = {"openai": ("OPENAI_API_KEY", "https://api.openai.com/v1/models", lambda k: {"Authorization": "Bearer " + k}),
                          "anthropic": ("ANTHROPIC_API_KEY", "https://api.anthropic.com/v1/models", lambda k: {"x-api-key": k, "anthropic-version": "2023-06-01"})}[m["provider"]]
        try:
            r = requests.get(url, headers=hdr(llm.load_key(name, env)), timeout=30)
            check(f"{m['provider']} key accepted", r.ok, "" if r.ok else f"HTTP {r.status_code}")
        except Exception as e:  # noqa: BLE001
            check(f"{m['provider']} key accepted", False, repr(e)[:300])

for m in cfg["models"]:
    p = m.get("price_per_million")
    if p:
        b = cfg["budgets"].get("max_total_tokens", 250000)
        print(f"INFO price per million tokens: input {p['input']} USD, output {p['output']} USD (thinking billed as output)")
        print(f"INFO bound if every run used its whole {b:,}-token budget at the input price: {len(runs) * b * p['input'] / 1e6:.2f} USD; "
              f"the runner stops starting new runs once recorded spend reaches {cfg.get('max_cost_usd')} USD")
print("READY" if ok else "NOT READY")
