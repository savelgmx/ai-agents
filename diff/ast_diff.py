import code_diff as cd
# РЕАЛИЗАЦИЯ AST DIFF (ПРАКТИЧЕСКАЯ)

def compute_diff(old_code: str, new_code: str):

    try:
        diff = cd.difference(
            old_code,
            new_code,
            lang="java"  # Kotlin близок к Java
        )

        return diff.edit_script()

    except Exception as e:
        print("AST diff failed:", e)
        return None
