from architect.architect_agent import run_architect
from memory.memory_agent import save_stage
from pipeline.planner_agent import run_planner
from coder.coder_agent import run_coder
from reviewer.reviewer_agent import run_reviewer
from writer.writer_agent import run_writer
from git_agent import create_branch, commit_all

logs = []


def log(message: str):
    print(message)
    logs.append(message)


def get_logs():
    return logs


def clear_logs():
    global logs
    logs = []


# -------------------------
# MAIN PIPELINE
# -------------------------

def run_full_pipeline(feature, preview_only=False):

    clear_logs()

    log(f"🚀 Starting pipeline for: {feature}")

    try:
        # --- GIT ---
        log("🌿 Creating git branch...")
        create_branch(feature)
        log("✅ Branch created")

        # --- ARCHITECT ---
        log("🧠 Architect running...")
        run_architect(feature)
        log("✅ Architect done")

        # --- PLANNER ---
        log("📐 Planner running...")
        run_planner()
        log("✅ Planner done")

        # --- CODER ---
        log("💻 Coder running...")
        changes = run_coder()
        log(f"✅ Coder done ({len(changes)} files)")

        if preview_only:
            log("👀 Preview mode enabled (no changes applied)")
            return changes

        # --- REVIEW LOOP ---
        log("🔍 Reviewer running...")
        for i in range(2):
            log(f"   ↪ Review iteration {i+1}")
            run_reviewer()
        log("✅ Review done")

        # --- WRITE ---
        log("✍️ Writing changes...")
        run_writer()
        log("✅ Files updated")

        return changes

    except Exception as e:
        log(f"❌ Pipeline error: {str(e)}")
        raise


# -------------------------
# APPLY APPROVED CHANGES
# -------------------------

def apply_approved_changes(changes):

    clear_logs()

    log("✅ Applying approved changes...")

    try:
        save_stage("code_raw", changes)

        # --- REVIEW ---
        log("🔍 Reviewer running...")
        run_reviewer()

        # --- WRITE ---
        log("✍️ Writing changes...")
        run_writer()

        # --- COMMIT ---
        log("📦 Committing to git...")
        commit_all("AI approved changes")

        log("🎉 Done")

    except Exception as e:
        log(f"❌ Apply failed: {str(e)}")
        raise
