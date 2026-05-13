from llm_client import call_llm
from scanner.file_indexer import index_project
from scanner.file_targeting import map_targets_to_files
from utilty.prompt_builder import build_prompt
from utilty.json_utils import extract_json
from memory.context_builder import build_relevant_context
from memory.memory_agent import (
    load_stage,
    save_stage,
    get_full_context
)


def load_system():

    return open(
        "coder/system_prompt.txt",
        encoding="utf-8"
    ).read()


def run_coder():

    system = load_system()

    architecture = load_stage("architecture")
    plan = load_stage("plan")

    # -------------------------
    # PROJECT INDEX
    # -------------------------
    file_index = index_project()

    # -------------------------
    # TARGET MAPPING
    # -------------------------
    mapping = map_targets_to_files(
        plan,
        file_index
    )

    # -------------------------
    # RELEVANT CONTEXT
    # -------------------------
    relevant_context = build_relevant_context(
        mapping
    )

    # -------------------------
    # TASK
    # -------------------------
    task = f"""
Generate production-ready Kotlin code.

Architecture:
{architecture}

Plan:
{plan}

Relevant project context:
{relevant_context}

IMPORTANT:
- MODIFY existing files when possible
- DO NOT break existing code
- Keep architecture intact
- Return FULL updated files

Return JSON:
[
  {{
    "file": "",
    "action": "modify|create",
    "code": ""
  }}
]
"""

    prompt = build_prompt(
        system,
        get_full_context(),
        task
    )

    result = call_llm(prompt)

    parsed = extract_json(result)

    save_stage("code_raw", parsed)

    print("✅ Coder done")

    return parsed
