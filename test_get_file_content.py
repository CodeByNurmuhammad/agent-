
from functions.get_file_content import get_file_content


def main():
    print("Reading main.py:")
    print(get_file_content("calculator", "main.py"))

    print("\nReading calculator.py:")
    print(get_file_content("calculator", "pkg/calculator.py"))

    print("\nReading outside file:")
    print(get_file_content("calculator", "/bin/cat"))

    print("\nReading nonexistent file:")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

    print("\nTesting lorem.txt:")
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")


if __name__ == "__main__":
    main()

