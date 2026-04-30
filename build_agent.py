import subprocess
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

PROJECT_DIR = config.get("project", "path", fallback="app")


def run_gradle_build():

    print("🔨 Running Gradle build...")

    result = subprocess.run(
        ["gradlew.bat", "build"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )

    success = result.returncode == 0

    return {
        "success": success,
        "output": result.stdout + result.stderr
    }
