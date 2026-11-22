
from functions.write_file import write_file


def main():
    print("Test 1: Overwrite existing file")
    print(write_file(
        "calculator",
        "lorem.txt",
        "wait, this isn't lorem ipsum"
    ))

    print("\nTest 2: Create file in nested directory")
    print(write_file(
        "calculator",
        "pkg/morelorem.txt",
        "lorem ipsum dolor sit amet"
    ))

    print("\nTest 3: Reject outside path")
    print(write_file(
        "calculator",
        "/tmp/temp.txt",
        "this should not be allowed"
    ))


if __name__ == "__main__":
    main()
