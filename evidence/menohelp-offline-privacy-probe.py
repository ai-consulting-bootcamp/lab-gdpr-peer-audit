"""Offline, synthetic audit probe. Python 3.10+ standard library only.

Extracts selected functions and literal constants from an explicitly supplied,
read-only checkout. It does not import the app, read .env, or call a vendor.
Vendor clients are spies. This verifies local transformations, not deployment.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import types

EXPECTED_COMMIT = "89940e85b3f869b888e247a5b9651020b8d6c865"


def extract(path, functions, env):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    selected = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            try:
                ast.literal_eval(node.value)
            except (ValueError, TypeError):
                continue
            selected.append(node)
        elif isinstance(node, ast.FunctionDef) and node.name in functions:
            selected.append(node)
    future = ast.ImportFrom(module="__future__", names=[ast.alias(name="annotations")], level=0)
    module = ast.fix_missing_locations(ast.Module(body=[future] + selected, type_ignores=[]))
    exec(compile(module, str(path), "exec"), env)
    missing = set(functions) - env.keys()
    if missing:
        raise RuntimeError(f"Missing source functions: {sorted(missing)}")
    return {n.name: [n.lineno, n.end_lineno] for n in tree.body
            if isinstance(n, ast.FunctionDef) and n.name in functions}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.source.resolve()
    sha = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    if sha != EXPECTED_COMMIT:
        raise RuntimeError(f"Expected {EXPECTED_COMMIT}, received {sha}")
    source_files = ["app/agent/nodes.py", "app/agent/symptoms.py", "app/rag/retrieve.py", "app/rag/clients.py"]
    for name in source_files:
        if subprocess.check_output(["git", "-C", str(root), "diff", "HEAD", "--", name]):
            raise RuntimeError(f"Source has local modifications: {name}")

    # Reserved .invalid addresses and invented health statements: no real person.
    fixture = {
        "stats": {"dataset_id": "synthetic-audit-001", "user_id": "audit.person@example.invalid",
                  "age": 46, "n_cycles": 6, "mean_length": 32, "events": []},
        "intake": {"symptoms": {"sleep": 3},
                   "top_concern": "Synthetic case only: I am Alex Audit, alex.audit@example.invalid, with night sweats."},
    }
    env = {"json": json}
    extract(root / "app/agent/symptoms.py", ["rate_systems"], env)
    locators = extract(root / "app/agent/nodes.py",
                       ["summarise_symptoms", "_by", "_sections", "_labs_view", "_findings_view", "_prompt", "retrieve"], env)
    symptoms = env["summarise_symptoms"](fixture["intake"])
    state = {"stats": fixture["stats"], "context": [], "findings": {
        "symptoms": symptoms, "flags": [], "case_tags": [], "explanations": []}}
    prompt = env["_prompt"](state)

    embedding_calls, rpc_calls, selector_calls = [], [], []

    class Embeddings:
        def create(self, **kw):
            embedding_calls.append(kw)
            return types.SimpleNamespace(data=[types.SimpleNamespace(embedding=[0.11, 0.22, 0.33])])

    class Database:
        def rpc(self, name, params):
            rpc_calls.append({"method": name, "params": params})
            return self

        def table(self, name):
            return self

        def select(self, *a):
            return self

        def eq(self, *a):
            return self

        def in_(self, field, values):
            selector_calls.append({"field": field, "values": values})
            return self

        def execute(self):
            return types.SimpleNamespace(data=[])

    vendor_env = {"openai_client": lambda: types.SimpleNamespace(embeddings=Embeddings())}
    extract(root / "app/rag/clients.py", ["embed"], vendor_env)
    db = Database()
    retrieval_env = {"embed": vendor_env["embed"], "supabase_client": lambda: db}
    extract(root / "app/rag/retrieve.py", ["retrieve", "symptom_cards", "lab_cards"], retrieval_env)

    # Only import statements inside extracted functions resolve to these local spies.
    fake_retrieve = types.ModuleType("app.rag.retrieve")
    for name in ("retrieve", "symptom_cards", "lab_cards"):
        setattr(fake_retrieve, name, retrieval_env[name])
    fake_symptoms = types.ModuleType("app.agent.symptoms")
    fake_symptoms.SYSTEMS = env["SYSTEMS"]
    sys.modules["app.rag.retrieve"] = fake_retrieve
    sys.modules["app.agent.symptoms"] = fake_symptoms
    # No laboratory inputs in this fixture; suppress only the empty-lab helpers.
    env.update(lab_topics=lambda *a, **kw: [], lab_card_titles=lambda *a: [], norm_card=lambda *a: None)
    env["retrieve"](state)

    raw_concern = fixture["intake"]["top_concern"]
    checks = {
        "user_identifier_survives_generation_prompt": fixture["stats"]["user_id"] in prompt[1]["content"],
        "free_text_identifier_survives_generation_prompt": raw_concern in prompt[1]["content"],
        "raw_concern_reaches_embedding_client_spy": any(raw_concern in c["input"] for c in embedding_calls),
        "query_vector_reaches_supabase_rpc_spy": any(c["params"]["query_embedding"] == [0.11, 0.22, 0.33] for c in rpc_calls),
        "symptom_selector_reaches_supabase_spy": bool(selector_calls),
    }
    result = {
        "assessment_date": "2026-11-17", "source_commit": sha,
        "method": "Executed selected actual source functions with synthetic input and offline vendor spies; no app import or network calls.",
        "input": fixture, "observations": checks,
        "captured_generation_user_message": prompt[1]["content"],
        "captured_free_text_embedding_call": next(c for c in embedding_calls if raw_concern in c["input"]),
        "captured_supabase_rpc_example": rpc_calls[-1], "captured_symptom_selectors": selector_calls,
        "source_sha256": {name: hashlib.sha256((root / name).read_bytes()).hexdigest() for name in source_files},
        "source_function_lines": locators,
        "limitation": "No live requests, authentication tests, consent verification, vendor-region verification, retention measurement or actual anonymisation test. The three-number vector is a spy fixture, not a real embedding. No claim that these synthetic inputs were sent externally.",
    }
    assert all(checks.values()), checks
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(json.dumps({"checks_observed": sum(checks.values()), "total_checks": len(checks), "output": str(args.output)}))


if __name__ == "__main__":
    main()
