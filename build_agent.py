import subprocess
import os

from config_loader import get_project_path


# ==========================================
# BUILD
# ==========================================

def run_gradle_build():

    PROJECT_DIR = get_project_path()

    if not os.path.exists(PROJECT_DIR):
        raise Exception(
            f"❌ PROJECT_DIR not found: {PROJECT_DIR}"
        )

    GRADLEW_PATH = os.path.join(
        PROJECT_DIR,
        "gradlew.bat"
    )

    if not os.path.exists(GRADLEW_PATH):
        raise Exception(
            f"❌ gradlew.bat not found: {GRADLEW_PATH}"
        )

    print("🔨 Running Gradle build...")
    print(f"📂 PROJECT_DIR: {PROJECT_DIR}")

    result = subprocess.run(
        [GRADLEW_PATH, "assembleDebug"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )

    success = result.returncode == 0

    output = (
        result.stdout +
        "\n" +
        result.stderr
    )

    if success:
        print("✅ Build successful")
    else:
        print("❌ Build failed")

    return {
        "success": success,
        "output": output
    }