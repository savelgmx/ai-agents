from llm_client import call_llm
from utilty.prompt_builder import build_prompt
from utilty.json_utils import extract_json
from memory.memory_agent import load_stage, save_stage, get_full_context


def load_system():
    return open("pipeline/system_prompt.txt").read()


def run_planner():

    system = load_system()
    architecture = load_stage("architecture")
    context = get_full_context()

    task = f"""
Based on architecture:
{architecture}

Return JSON file structure.
"""

    prompt = build_prompt(system, context, task)

    result = call_llm(prompt)
    parsed = extract_json(result)

    save_stage("plan", parsed)
    print("✅ Planner done")
    return parsed
