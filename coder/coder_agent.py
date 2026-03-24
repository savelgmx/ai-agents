import json
from llm_client import call_llm

def run_coder():

    with open("pipeline/plan.json", "r", encoding="utf-8") as f:
        plan = json.load(f)

    prompt = f"""
You are a Senior Android Kotlin developer.

Follow Clean Architecture strictly.

Architecture:
{json.dumps(plan, indent=2)}

Generate Kotlin code.

Return JSON:
[
  {{
    "path": "",
    "code": ""
  }}
]
"""

    response = call_llm(prompt, model="deepseek-coder:1.3b")

    with open("pipeline/code.json", "w", encoding="utf-8") as f:
        f.write(response)

    print("✅ Code generated")

if __name__ == "__main__":
    run_coder()
