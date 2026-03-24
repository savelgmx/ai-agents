def build_prompt(system: str, context: str, task: str):

    CONSTRAINTS = """
OUTPUT RULES:
- ONLY valid JSON
- No markdown
- No explanations
- No comments outside JSON
- Follow schema strictly
- If unsure — proceed with best assumption
"""

    ROLE_ENFORCEMENT = f"""
IMPORTANT:
You MUST behave strictly as:
{system.splitlines()[0]}
Do NOT switch roles.
"""

    return f"""
{system}

{ROLE_ENFORCEMENT}

You are a Senior Android Engineer.

PROJECT CONTEXT:
{context}

STRICT RULES:
- MVVM
- Clean Architecture
- Repository pattern
- Kotlin Coroutines
- SOLID
- Production-ready code

{CONSTRAINTS}

TASK:
{task}
"""
