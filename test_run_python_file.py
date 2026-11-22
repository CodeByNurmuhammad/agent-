from functions.run_python_file import run_python_file


def main():
    print("Test 1: Run main.py")
    print(run_python_file("calculator", "main.py"))

    print("\nTest 2: Run main.py with arguments")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    print("\nTest 3: Run tests.py")
    print(run_python_file("calculator", "tests.py"))

    print("\nTest 4: Try to run outside working directory")
    print(run_python_file("calculator", "../main.py"))

    print("\nTest 5: Try nonexistent file")
    print(run_python_file("calculator", "nonexistent.py"))

    print("\nTest 6: Try a non-Python file")
    print(run_python_file("calculator", "lorem.txt"))


if __name__ == "__main__":
    main()