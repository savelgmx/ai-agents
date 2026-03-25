from llm_client import call_llm
from utilty.prompt_builder import build_prompt
from utilty.json_utils import extract_json
from memory.memory_agent import load_stage, save_stage, get_full_context
from scanner.scanner_agent import scan_project


def load_system():
    return open("coder/system_prompt.txt").read()


def run_coder():

    system = load_system()
    plan = load_stage("plan")

    context = get_full_context() + scan_project()

    task = f"""
Generate FULL Kotlin implementation for:
{plan}

Return JSON:
[
  {{
    "file": "",
    "code": ""
  }}
]
"""

    prompt = build_prompt(system, context, task)

    result = call_llm(prompt)
    parsed = extract_json(result)

    save_stage("code_raw", parsed)
    print("✅ Coder done")
    return parsed
