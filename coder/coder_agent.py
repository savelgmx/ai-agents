from scanner.file_indexer import index_project
from scanner.file_targeting import map_targets_to_files
from scanner.context_loader import build_relevant_context
from utilty.prompt_builder import build_prompt
from utilty.json_utils import extract_json
from llm_client import call_llm
from memory.memory_agent import load_stage, save_stage
from scanner.scanner_agent import scan_project


def run_coder():

    plan = load_stage("plan")

    file_index = index_project()

    mapping = map_targets_to_files(plan, file_index)

    relevant_context = build_relevant_context(mapping)

    full_context = relevant_context + "\n\n" + scan_project()

    task = f"""
Apply changes safely to existing project.

PLAN:
{plan}

FILE MAPPING:
{mapping}

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

    prompt = build_prompt(load_system(), full_context, task)

    result = call_llm(prompt)

    parsed = extract_json(result)

    save_stage("code_raw", parsed)

    return parsed
