import subprocess


def run_build():

    print("🔧 Running Gradle build...")

    result = subprocess.run(
        ["./gradlew", "assembleDebug"],
        capture_output=True,
        text=True
    )

    success = result.returncode == 0

    return {
        "success": success,
        "output": result.stdout + result.stderr
    }
