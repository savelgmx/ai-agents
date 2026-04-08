from architect.architect_agent import run_architect
from memory.memory_agent import save_stage
from pipeline.planner_agent import run_planner
from coder.coder_agent import run_coder
from reviewer.reviewer_agent import run_reviewer
from writer.writer_agent import run_writer
from git_agent import create_branch, commit_all
from logs.logger import log, get_logs, clear_logs


# -------------------------
# MAIN PIPELINE
# -------------------------

def run_full_pipeline(feature, preview_only=False):

    clear_logs()

    log("SYSTEM", f"🚀 Start: {feature}")

    try:
        # --- GIT ---
        log("GIT", "🌿 Creating git branch...")
        create_branch(feature)
        log("GIT", "Branch created")

        # --- ARCHITECT ---
        log("ARCHITECT", "🧠 Architect running...")
        run_architect(feature)
        log("ARCHITECT", "Done")

        # --- PLANNER ---
        log("PLANNER", "📐 Planner running...")
        run_planner()
        log("PLANNER", "Done")

        # --- CODER ---
        log("CODER", "💻 Coder running...")
        changes = run_coder()
        log("CODER", f"Done ({len(changes)} files)")

        # --- PREVIEW MODE ---
        if preview_only:
            log("SYSTEM", "👀 Preview mode")
            return {
                "changes": changes,
                "logs": get_logs()
            }

        # --- REVIEW ---
        log("REVIEWER", "🔍 Reviewer running...")
        run_reviewer()
        log("REVIEWER", "Done")

        # --- WRITE ---
        log("WRITER", "✍️ Writing changes...")
        run_writer()
        log("WRITER", "Files written")

        # --- COMMIT ---
        log("GIT", "📦 Committing...")
        commit_all("AI update")
        log("GIT", "Committed")

        return {
            "changes": changes,
            "logs": get_logs()
        }

    except Exception as e:
        log("ERROR", str(e))
        raise


# -------------------------
# APPLY APPROVED CHANGES
# -------------------------

def apply_approved_changes(changes):

    clear_logs()

    log("SYSTEM", "✅ Applying approved changes...")

    try:
        save_stage("code_raw", changes)

        log("REVIEWER", "🔍 Reviewer running...")
        run_reviewer()

        log("WRITER", "✍️ Writing changes...")
        run_writer()

        log("GIT", "📦 Committing...")
        commit_all("AI approved changes")

        log("SYSTEM", "🎉 Done")

    except Exception as e:
        log("ERROR", str(e))
        raise
