from llm_client import call_llm
from memory.memory_agent import load_stage


def generate_pr_summary():

    changes = load_stage("code_raw")
    review = load_stage("ai_review")

    prompt = f"""
Write a professional GitHub Pull Request.

Include:
- Title
- Summary
- Changes
- Risks
- Review notes

Changes:
{changes}

Review:
{review}
"""

    return call_llm(prompt)
