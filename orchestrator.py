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
from scanner.scanner_agent import scan_project

def run_full_pipeline(feature):

    create_branch(feature)

    # 1. SCAN
    project_code = scan_project()

    # 2. DESIGN
    run_architect(feature)
    run_planner()

    # 3. CODE
    changes = run_coder()

    # 4. APPROVAL (ВАЖНО)
    if not approve_changes(changes):
        print("❌ Cancelled")
        return

    # 5. REVIEW LOOP
    for _ in range(2):
        run_reviewer()

    # 6. WRITE (AST patch)
    run_writer()

    # 7. BUILD
    build = run_build()

    if not build["success"]:
        print("❌ Build failed → retry loop")

    # 8. TEST
    run_tests()

    # 9. COMMIT
    commit_all("AI update")
