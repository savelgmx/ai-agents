from architect.architect_agent import run_architect
from pipeline.planner_agent import run_planner
from coder.coder_agent import run_coder
from reviewer.reviewer_agent import run_reviewer
from writer.writer_agent import run_writer
from git_agent import create_branch, commit_all
from logs.logger import log
from approval_agent import approve_changes
from build_agent import  run_build
from test_agent import run_tests

def run_full_pipeline(feature):

    create_branch(feature)

    run_architect(feature)
    run_planner()

    changes = run_coder()

    if not approve_changes(changes):
        print("❌ Cancelled")
        return

    run_reviewer()
    run_writer()

    build = run_build()

    if not build["success"]:
        print("❌ Build failed → fixing...")

        for _ in range(2):
            run_reviewer()
            run_coder()
            run_writer()

    run_tests()

    commit_all("AI feature update")


