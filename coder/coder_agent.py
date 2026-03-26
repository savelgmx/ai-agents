from llm_client import call_llm
from utilty.prompt_builder import build_prompt
from utilty.json_utils import extract_json
from memory.memory_agent import load_stage, save_stage, get_full_context
from scanner.scanner_agent import scan_project
from scanner.file_indexer import index_project
from scanner.file_targeting import map_targets_to_files

def load_system():
    return open("coder/system_prompt.txt").read()


def run_coder():

    plan = load_stage("plan")
    file_index = index_project()

    mapping = map_targets_to_files(plan, file_index)

    context = get_full_context() + scan_project()

    task = f"""
Apply these changes:

PLAN:
{plan}

FILE MAPPING:
{mapping}

Return JSON:
[
  {{
    "file": "",
    "action": "modify|create",
    "code": ""
  }}
]
"""

    prompt = build_prompt(load_system(), context, task)

    result = call_llm(prompt)
    parsed = extract_json(result)

    save_stage("code_raw", parsed)

    return parsed
