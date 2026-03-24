import json
from llm_client import call_llm

def run_reviewer():

    with open("pipeline/code.json", "r", encoding="utf-8") as f:
        code = f.read()

    prompt = f"""
You are a strict Android reviewer.

Fix:
- architecture violations
- bad Kotlin practices
- coroutine misuse

Improve this code:

{code}

Return same JSON format.
"""

    response = call_llm(prompt, model="qwen2.5-coder:3b")

    with open("pipeline/code_reviewed.json", "w", encoding="utf-8") as f:
        f.write(response)

    print("✅ Review done")

if __name__ == "__main__":
    run_reviewer()
