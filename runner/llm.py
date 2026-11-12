"""Model clients. All return (text, usage) where usage has input_tokens, output_tokens, cost_usd (None if unknown).

API keys come from the process environment or from the .env file named in the config. Key values are never logged.
"""
import hashlib
import json
import os
import random
import re
import time

DEFAULT_ENV = r"C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\.env"


def load_key(name, env_path=DEFAULT_ENV):
    """First of the names (one name or a tuple) found in the process environment, then in the .env file."""
    names = (name,) if isinstance(name, str) else tuple(name)
    for n in names:
        if os.environ.get(n):
            return os.environ[n]
    if env_path and os.path.exists(env_path):
        found = {}
        for line in open(env_path, encoding="utf-8"):
            m = re.match(r"\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)\s*$", line)
            if m and m.group(1) in names:
                found[m.group(1)] = m.group(2).strip().strip('"').strip("'")
        for n in names:
            if found.get(n):
                return found[n]
    raise KeyError(f"{' or '.join(names)} not found in environment or {env_path}")


def _post(url, headers, body, timeout=180, retries=6):
    import requests
    for attempt in range(retries):
        try:
            r = requests.post(url, headers=headers, json=body, timeout=timeout)
        except requests.RequestException:
            if attempt < retries - 1:
                time.sleep(min(60, 2 ** attempt * 3))
                continue
            raise
        if r.status_code in (429, 500, 502, 503, 504) and attempt < retries - 1:
            time.sleep(min(60, 2 ** attempt * 3))
            continue
        if r.status_code >= 400:
            raise RuntimeError(f"HTTP {r.status_code}: {r.text[:500]}")
        return r.json()


class OpenAICompatible:
    """OpenAI chat completions protocol (OpenAI, OpenRouter)."""

    def __init__(self, model, base_url, key_name, env_path=DEFAULT_ENV, temperature=0.7, max_tokens=4000, extra=None):
        self.model, self.base_url, self.key_name, self.env_path = model, base_url.rstrip("/"), key_name, env_path
        self.temperature, self.max_tokens, self.extra = temperature, max_tokens, extra or {}
        self.name = f"{base_url.split('//')[-1].split('/')[0]}:{model}"

    def chat(self, system, messages, seed=None):
        body = {"model": self.model, "messages": [{"role": "system", "content": system}] + messages,
                "temperature": self.temperature, "max_tokens": self.max_tokens, **self.extra}
        if seed is not None:
            body["seed"] = seed
        if "openrouter" in self.base_url:
            body["usage"] = {"include": True}
        j = _post(self.base_url + "/chat/completions", {"Authorization": "Bearer " + load_key(self.key_name, self.env_path)}, body)
        u = j.get("usage") or {}
        msg = j["choices"][0]["message"]
        # OpenRouter reports the routed model id in the top-level "model" field
        model_version = j.get("model") if "openrouter" in self.base_url else None
        # reasoning_details: returned by Claude extended-thinking via OpenRouter; must be
        # passed back unchanged in subsequent turns of a multi-turn conversation.
        reasoning_details = msg.get("reasoning_details")
        return msg.get("content") or "", {
            "input_tokens": u.get("prompt_tokens", 0), "output_tokens": u.get("completion_tokens", 0),
            "cost_usd": u.get("cost"), "model_version": model_version,
            "reasoning_details": reasoning_details}


class Anthropic:
    def __init__(self, model, key_name="ANTHROPIC_API_KEY", env_path=DEFAULT_ENV, temperature=0.7, max_tokens=4000):
        self.model, self.key_name, self.env_path, self.temperature, self.max_tokens = model, key_name, env_path, temperature, max_tokens
        self.name = f"anthropic:{model}"

    def chat(self, system, messages, seed=None):
        body = {"model": self.model, "system": system, "messages": messages, "temperature": self.temperature, "max_tokens": self.max_tokens}
        j = _post("https://api.anthropic.com/v1/messages",
                  {"x-api-key": load_key(self.key_name, self.env_path), "anthropic-version": "2023-06-01"}, body)
        u = j.get("usage") or {}
        text = "".join(b.get("text", "") for b in j.get("content", []) if b.get("type") == "text")
        return text, {"input_tokens": u.get("input_tokens", 0), "output_tokens": u.get("output_tokens", 0), "cost_usd": None}


GEMINI_KEY_NAMES = ("GEMINI_API_KEY", "GOOGLE_API_KEY")
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"


class Gemini:
    """Google Gemini API (generateContent). The key is sent in a header, never in the URL.

    Cost is computed from token counts and the configured list price, because the API does not report cost.
    Thinking tokens are billed as output tokens and are counted in output_tokens.
    """

    def __init__(self, model, env_path=DEFAULT_ENV, temperature=0.7, max_tokens=8192, thinking_budget=None,
                 price_per_million=None, json_mode=True):
        self.model, self.env_path, self.temperature, self.max_tokens = model, env_path, temperature, max_tokens
        self.thinking_budget, self.price, self.json_mode = thinking_budget, price_per_million, json_mode
        self.name = f"gemini:{model}"

    def body(self, system, messages, seed=None):
        cfg = {"temperature": self.temperature, "maxOutputTokens": self.max_tokens}
        if self.json_mode:
            cfg["responseMimeType"] = "application/json"
        if self.thinking_budget is not None:
            cfg["thinkingConfig"] = {"thinkingBudget": self.thinking_budget}
        if seed is not None:
            cfg["seed"] = seed
        return {"systemInstruction": {"parts": [{"text": system}]},
                "contents": [{"role": "model" if m["role"] == "assistant" else "user", "parts": [{"text": m["content"]}]} for m in messages],
                "generationConfig": cfg}

    def parse(self, j):
        cands = j.get("candidates") or [{}]
        parts = (cands[0].get("content") or {}).get("parts") or []
        text = "".join(p.get("text", "") for p in parts if not p.get("thought"))
        u = j.get("usageMetadata") or {}
        tin = u.get("promptTokenCount", 0) or 0
        tout = (u.get("candidatesTokenCount", 0) or 0) + (u.get("thoughtsTokenCount", 0) or 0)
        cost = (tin * self.price["input"] + tout * self.price["output"]) / 1e6 if self.price else None
        return text, {"input_tokens": tin, "output_tokens": tout, "thinking_tokens": u.get("thoughtsTokenCount", 0) or 0,
                      "cost_usd": cost, "model_version": j.get("modelVersion"), "finish_reason": cands[0].get("finishReason"),
                      "response_id": j.get("responseId")}

    def chat(self, system, messages, seed=None):
        j = _post(GEMINI_URL.format(model=self.model), {"x-goog-api-key": load_key(GEMINI_KEY_NAMES, self.env_path)},
                  self.body(system, messages, seed))
        return self.parse(j)


RISK_HINTS = [("LABEL_ERROR", r"play[- ]type|label"), ("RTM_SELECTION", r"slump|after|trigger|extreme"),
              ("EXPOSURE_SPARSITY", r"lineup|pair|stint|matchup"), ("MEASURE_RELIABILITY", r"trait|stable|signature"),
              ("SAMPLE_SIZE_POWER", r"playoff|series|rare"), ("CONFOUNDING", r"opponent|context")]


class Mock:
    """Deterministic scripted agent for dry runs. It exercises every code path; its outputs carry no research value."""

    name = "mock:scripted"

    def __init__(self, **_):
        pass

    def chat(self, system, messages, seed=None):
        first = messages[0]["content"]
        tools_seen = sum(1 for m in messages if m["role"] == "user" and m["content"].startswith("TOOL_RESULT"))
        q = re.search(r"\n(.+)\n\nData available", first)
        question = q.group(1) if q else first[:200]
        rng = random.Random(int(hashlib.sha256((question + str(seed)).encode()).hexdigest()[:8], 16))
        v2 = "retrieve_history(" in system
        if "Stage 1. Reply only" in first:
            return self._v3(system, question, messages, rng)
        if tools_seen == 0 and v2:
            act = {"action": "tool", "tool": "retrieve_history", "args": {"research_question": question, "query": question[:120]}}
        elif tools_seen == 0 and "query_graph" in system:
            act = {"action": "tool", "tool": "query_graph", "args": {"op": "find", "type": "Hypothesis", "text": question, "limit": 5}}
        elif tools_seen == 0 and "search_documents" in system:
            act = {"action": "tool", "tool": "search_documents", "args": {"query": question, "k": 5}}
        elif tools_seen == 0:
            act = {"action": "tool", "tool": "glossary", "args": {}}
        else:
            ctx = " ".join(m["content"] for m in messages).lower()
            art = 0.35 if "artifact" in ctx and tools_seen else 0.15
            unt = 0.30 if "untestable" in ctx else 0.15
            probs = {"supported": 0.2, "rejected": 0.2, "untestable": unt, "artifact": art, "uncertain": 0.15}
            risks = [{"code": c, "text": "scripted"} for c, pat in RISK_HINTS if re.search(pat, question.lower())]
            act = {"action": "final", "output": {
                "testability": {"p_testable": round(0.4 + 0.4 * rng.random(), 2), "blocking_constraints": []},
                "prior_work": {"already_answered": "partly" if "fam:" in ctx or "sf-" in ctx else "unknown", "cited": [], "summary": "scripted"},
                "risks": risks, "predicted_outcome": probs,
                "decision": "proceed_with_changes" if art + unt > 0.5 else "proceed",
                "design": {"estimand": "difference in PPP between conditions", "unit": "possession, clustered by game",
                           "sample": "about 1200 games from 2022-23 to 2024-25", "power": "power 0.8 for an MDE of 0.03 PPP",
                           "controls": "opponent and season fixed effects, matched baseline", "falsification": "placebo permutation of labels",
                           "multiplicity": "single primary test; Holm for secondary", "decision_rule": "proceed if the 95% CI excludes 0 and effect > 0.02",
                           "data_version": "frozen snapshot of seasons 2022-23 to 2024-25"}}}
            if v2:
                got = re.findall(r'"id": "([^"]+)"', next((m["content"] for m in messages if m["content"].startswith("TOOL_RESULT retrieve_history")), ""))
                act["output"] = {"research_question": question, "retrieval_summary": {
                    "prior_findings": [{"id": i, "status": "uncertain", "summary": "scripted"} for i in got[:2]],
                    "failed_experiments": [], "limitations": [], "unresolved": []},
                    "evidence_use": "scripted: prior records retrieved" if got else "scripted: nothing retrieved", **act["output"]}
                act["output"]["prior_work"]["cited"] = got[:2]
        text = json.dumps(act)
        if v2 and act["action"] == "final" and rng.random() < 0.3:
            text = text[:-1]
        return text, {"input_tokens": (len(system) + sum(len(m["content"]) for m in messages)) // 4,
                      "output_tokens": len(text) // 4, "cost_usd": 0.0}

    def _v3(self, system, question, messages, rng):
        """Protocol 3: retrieval request, then a final answer citing the first returned family. The first final
        states a fixed status, so the citation check and correction turn are exercised when it is wrong."""
        results = [m["content"] for m in messages if m["role"] == "user" and m["content"].startswith("TOOL_RESULT retrieve_history")]
        if not results:
            act = {"action": "tool", "tool": "retrieve_history", "args": {
                "research_concepts": [question[:60]], "methodological_questions": ["is the sample large enough"], "query": question[:120]}}
        else:
            ids = re.findall(r'"id": "(FAM:[^"]+)"', results[0])
            st = re.findall(r'auto_outcome_status(?:": "|: )([a-z ]+)', results[0])
            fix = messages[-1]["content"].startswith("Citation check failed")
            ev = [{"id": ids[0], "status_as_recorded": st[0] if fix and st else "inconclusive", "finding": "scripted"}] if ids else []
            ctx = results[0].lower()
            probs = {"supported": 0.2, "rejected": 0.2, "untestable": 0.3 if "untestable" in ctx else 0.15,
                     "artifact": 0.35 if "artifact" in ctx else 0.15, "uncertain": 0.15}
            act = {"action": "final", "output": {
                "research_concepts": [question[:60]], "methodological_questions": ["sample size"],
                "historical_evidence": ev, "failed_approaches": [], "evidence_establishes": [], "evidence_does_not_establish": [],
                "own_inferences": ["scripted"], "uncertainties": ["scripted"],
                "historical_effect": {"changed_decision": "no" if ids else "no_historical_evidence", "explanation": "scripted"},
                "testability": {"p_testable": round(0.4 + 0.4 * rng.random(), 2), "blocking_constraints": []},
                "prior_work": {"already_answered": "partly" if ids else "unknown", "cited": ids[:1], "summary": "scripted"},
                "risks": [{"code": c, "text": "scripted"} for c, pat in RISK_HINTS if re.search(pat, question.lower())],
                "predicted_outcome": probs, "decision": "proceed_with_changes" if probs["artifact"] + probs["untestable"] > 0.5 else "proceed",
                "design": {"estimand": "difference in PPP between conditions", "unit": "possession, clustered by game",
                           "sample": "about 1200 games from 2022-23 to 2024-25", "power": "power 0.8 for an MDE of 0.03 PPP",
                           "controls": "opponent and season fixed effects, matched baseline", "falsification": "placebo permutation of labels",
                           "multiplicity": "single primary test; Holm for secondary", "decision_rule": "proceed if the 95% CI excludes 0 and effect > 0.02",
                           "data_version": "frozen snapshot of seasons 2022-23 to 2024-25"}}}
        text = json.dumps(act)
        return text, {"input_tokens": (len(system) + sum(len(m["content"]) for m in messages)) // 4,
                      "output_tokens": len(text) // 4, "cost_usd": 0.0}


def make(spec, env_path=DEFAULT_ENV):
    p = spec["provider"]
    if p == "mock":
        return Mock()
    if p == "openrouter":
        return OpenAICompatible(spec["model"], "https://openrouter.ai/api/v1", "OPENROUTER_API_KEY", env_path,
                                spec.get("temperature", 0.7), spec.get("max_tokens", 4000), spec.get("extra"))
    if p == "openai":
        return OpenAICompatible(spec["model"], "https://api.openai.com/v1", "OPENAI_API_KEY", env_path,
                                spec.get("temperature", 0.7), spec.get("max_tokens", 4000), spec.get("extra"))
    if p == "gemini":
        return Gemini(spec["model"], env_path, spec.get("temperature", 0.7), spec.get("max_tokens", 8192),
                      spec.get("thinking_budget"), spec.get("price_per_million"), spec.get("json_mode", True))
    if p == "anthropic":
        return Anthropic(spec["model"], env_path=env_path, temperature=spec.get("temperature", 0.7), max_tokens=spec.get("max_tokens", 4000))
    raise ValueError(f"unknown provider {p}")
