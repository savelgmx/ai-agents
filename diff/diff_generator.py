import difflib
from diff.ast_diff import compute_diff


def generate_diff(old_code: str, new_code: str):

    # 1. Пытаемся AST diff (умный)
    ast = compute_diff(old_code, new_code)

    if ast:
        return {
            "type": "ast",
            "content": str(ast)
        }

    # 2. fallback → unified diff (как git)
    text_diff = difflib.unified_diff(
        old_code.splitlines(),
        new_code.splitlines(),
        lineterm=""
    )

    return {
        "type": "text",
        "content": "\n".join(text_diff)
    }
