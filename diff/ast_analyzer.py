from diff.diff_generator import generate_diff
from llm_client import call_llm

# ast_analyzer.py (УРОВЕНЬ SENIOR)
#
# Теперь он:
#
# использует diff
# прогоняет через LLM
# возвращает семантику изменений

def analyze_changes(old_code: str, new_code: str):

    diff = generate_diff(old_code, new_code)

    prompt = f"""
You are a Senior Android Reviewer.

Analyze the following code diff.

Return JSON:
{{
  "summary": "what changed",
  "risk_level": "low|medium|high",
  "breaking_changes": true/false,
  "improvements": ["list of improvements"],
  "issues": ["potential problems"]
}}

DIFF:
{diff["content"][:1500]}
"""

    result = call_llm(prompt)

    try:
        import json
        parsed = json.loads(result)
    except:
        parsed = {
            "summary": "Failed to analyze",
            "risk_level": "unknown",
            "breaking_changes": False,
            "improvements": [],
            "issues": []
        }

    return {
        "diff_type": diff["type"],
        "analysis": parsed
    }
