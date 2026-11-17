#!/usr/bin/env python3
"""Offline defensive audit of workflow configuration. Never runs a workflow."""
import argparse
import hashlib
import json
import re
from pathlib import Path

SOURCE_COMMIT = "eff19e436f8a6a7f7b019a2ab846a8e4c1355d9c"
STRATEGY = "Insert Custom Strategy PDF"
CUSTOM = "Use Custom Strategy Namespace"
DEFAULT = "Use Default Northstar Namespace"
RET = "Pinecone Vector Store"
START = "Start Parallel Research"
ROUTE = [
    "Check research availability", "AI Agent", "Convert Report to HTML", "Send a message"
]


def projection(raw):
    """Extract relevant configuration and redact the default email value."""
    raw_workflow = json.loads(raw)
    params = {n["name"]: n["parameters"] for n in raw_workflow["nodes"]}
    write = params[STRATEGY]
    read = params[RET]
    email = params[ROUTE[-1]]["sendTo"]
    # Preserve the expression syntax and fallback existence, not the address.
    email = re.sub(r"(['\"])[^'\"\s]+@[^'\"\s]+\1", r"\1[REDACTED_EMAIL]\1", email)
    successors = {}
    for src in ROUTE[:-1]:
        successors[src] = [
            target["node"]
            for branch in raw_workflow["connections"][src]["main"]
            for target in branch
        ]

    def assignment(node, field):
        return next(row["value"] for row in params[node]["assignments"]["assignments"]
                    if row["name"] == field)

    return {
        "source_commit": SOURCE_COMMIT,
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "source_node_count": len(raw_workflow["nodes"]),
        "vector_write": {
            "index": write["pineconeIndex"]["value"],
            "namespace": write["options"]["pineconeNamespace"],
            "clear_namespace": write["options"]["clearNamespace"],
        },
        "routing": {
            "custom_namespace": assignment(CUSTOM, "strategyNamespace"),
            "default_namespace": assignment(DEFAULT, "strategyNamespace"),
            "parallel_namespace": assignment(START, "strategyNamespace"),
        },
        "vector_read": {
            "index": read["pineconeIndex"]["value"],
            "namespace_expression": read["options"]["pineconeNamespace"],
        },
        "report_main_successors": successors,
        "recipient_expression": email,
    }


def assess(snap):
    writer, route, reader = (snap[k] for k in ("vector_write", "routing", "vector_read"))
    static_custom = writer["namespace"] == route["custom_namespace"] and not writer["namespace"].startswith("=")
    linked_read = (
        writer["index"] == reader["index"]
        and START in reader["namespace_expression"]
        and "strategyNamespace" in reader["namespace_expression"]
        and "strategyNamespace" in route["parallel_namespace"]
    )
    route_to_mail = all(dst in snap["report_main_successors"][src] for src, dst in zip(ROUTE, ROUTE[1:]))
    fallback = "customerEmail" in snap["recipient_expression"] and bool(
        re.search(r"""\|\|\s*['"]\[REDACTED_EMAIL\]['"]""", snap["recipient_expression"])
    )
    return {
        "source_commit": snap["source_commit"],
        "method": "Static configuration query against a redacted workflow excerpt",
        "external_requests_made": 0,
        "checks": {
            "custom_upload_uses_fixed_namespace": static_custom,
            "upload_clears_namespace": writer["clear_namespace"] is True,
            "read_uses_same_index_and_routed_namespace": linked_read,
            "direct_generation_to_mail_path_present": route_to_mail,
            "recipient_expression_has_fixed_mailbox_fallback": fallback,
        },
        "decision": "HOLD_LIVE_CUSTOM_UPLOADS_AND_DELIVERY" if static_custom and linked_read and fallback else "REVIEW_CONFIGURATION",
        "limitation": "No deployment status, concurrent execution, actual retrieval, delivery or disclosure tested.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--extract", action="store_true",
                        help="Project a local copy of the pinned raw workflow; do not commit the raw export")
    args = parser.parse_args()
    raw = args.input.read_bytes()
    result = projection(raw) if args.extract else assess(json.loads(raw))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
