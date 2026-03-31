import subprocess


def run_tests():

    print("🧪 Running tests...")

    result = subprocess.run(
        ["./gradlew", "test"],
        capture_output=True,
        text=True
    )

    return result.returncode == 0
