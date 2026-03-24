import json
from llm_client import call_llm

def run_planner():

    with open("pipeline/plan.json", "r", encoding="utf-8") as f:
        plan = json.load(f)

    prompt = f"""
You are a Senior Android Tech Lead.

Convert architecture into file plan.

Architecture:
{json.dumps(plan, indent=2)}

Return JSON:
[
  {{
    "path": "",
    "description": ""
  }}
]
"""

    response = call_llm(prompt)

    with open("pipeline/files.json", "w", encoding="utf-8") as f:
        f.write(response)

    print("✅ Planner done")

if __name__ == "__main__":
    run_planner()
