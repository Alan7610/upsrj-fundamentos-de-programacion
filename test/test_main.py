import subprocess
import sys
import os

SOURCE_FILE = "../src/main.c"
EXECUTABLE = "./a.out"


def compile_program():
    """
    Compiles the student's C program.
    Returns 0 on success, 1 on failure.
    """
    result = subprocess.run(
        ["gcc", SOURCE_FILE],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        print("COMPILATION FAILED")
        print(result.stderr)
        return 1

    if not os.path.exists(EXECUTABLE):
        print("COMPILATION FAILED: executable not generated")
        return 1

    return 0


def run_test(input_value, expected_keyword: str):
    """
    Runs the executable, sends input, and checks output.
    """
    process = subprocess.Popen(
        [EXECUTABLE],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = process.communicate(input_value)

    print('----------------------------------------')
    if process.returncode != 0:
        print("RUNTIME ERROR")
        print(stderr)
        return 1

    if expected_keyword.lower() not in stdout.lower():
        print("TEST FAILED")
        print("Input:", input_value.strip())
        print("Expected output to contain:", expected_keyword)
        print("Actual output:", stdout)
        return 1
    else: 
        print("TEST PASSED")
        print("Input:", input_value.strip())
        print("Expected output to contain:", expected_keyword)
        print("Actual output:", stdout)
        return 0


def main():
    errors = 0

    errors += compile_program()
    if errors != 0:
        sys.exit(1)

    errors += run_test("6\n", "El numero es par")
    errors += run_test("9\n", "El numero es impar")
    errors += run_test("0\n", "El numero es par")
    errors += run_test("-4\n", "El numero es par")
    errors += run_test("-3\n", "El numero es impar")

    if errors == 0:
        print("ALL TESTS PASSED")
        sys.exit(0)

    print(f"{errors} TEST(S) FAILED")
    sys.exit(1)


if __name__ == "__main__":
    main()
