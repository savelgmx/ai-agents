from llm_client import call_llm
from utilty.prompt_builder import build_prompt
from utilty.json_utils import extract_json
from memory.memory_agent import load_stage, save_stage, get_full_context


def load_system():
    return open("reviewer/system_prompt.txt").read()


def run_reviewer():

    system = load_system()
    code = load_stage("code_raw")
    context = get_full_context()

    task = f"""
Fix and improve this code:
{code}

Return JSON.
"""

    prompt = build_prompt(system, context, task)

    result = call_llm(prompt)
    parsed = extract_json(result)

    save_stage("code_final", parsed)
    print("✅ Reviewer done")
    return parsed
