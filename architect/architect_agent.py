from llm_client import call_llm
from utils.prompt_builder import build_prompt
from utils.json_utils import extract_json
from memory.memory_agent import save_stage, get_full_context
from memory.context_loader import load_relevant_code


def load_system():
    return open("architect/system_prompt.txt").read()


def run_architect(feature: str):

    system = load_system()
    context = get_full_context() + load_relevant_code()

    task = f"""
Design architecture for:
{feature}

Return JSON:
{{}}
"""

    prompt = build_prompt(system, context, task)

    result = call_llm(prompt, model="mistral:7b")
    parsed = extract_json(result)

    save_stage("architecture", parsed)
    print("✅ Architect done")
    return parsed
