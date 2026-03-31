# SAFE PATCHER (НЕ ПЕРЕЗАПИСЫВАЕМ ФАЙЛ)

def apply_patch(original: str, updated: str):

    # MVP версия (safe fallback)
    # позже заменим на AST-level patch

    if len(updated) < len(original) * 0.3:
        raise Exception("⚠️ Suspicious patch (too small)")

    return updated