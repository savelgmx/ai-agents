import json
from llm_client import call_llm

def load_system_prompt():
    with open("architect/system_prompt.txt", "r", encoding="utf-8") as f:
        return f.read()

def extract_json(text: str):
    try:
        return json.loads(text)
    except:
        start = text.find("{")
        end = text.rfind("}") + 1
        return json.loads(text[start:end])

def run_architect(feature: str):

    system = load_system_prompt()

    prompt = f"""
{system}

Feature:
{feature}
"""

    response = call_llm(prompt, model="qwen2.5-coder:3b")

    parsed = extract_json(response)

    with open("pipeline/plan.json", "w", encoding="utf-8") as f:
        json.dump(parsed, f, indent=2)

    print("✅ Architect done")

if __name__ == "__main__":
    feature = input("Feature:\n")
    run_architect(feature)
