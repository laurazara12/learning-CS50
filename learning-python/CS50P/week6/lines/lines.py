import sys

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]

            non_comment_lines = [line for line in lines if line and not (line.startswith('#') and not line.startswith('"""'))]

            print(f"Lines of code in {file_path}: {len(non_comment_lines)}")
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Too few or too many command-line arguments")
        sys.exit(1)

    file_path = sys.argv[1]

    if not file_path.endswith('.py'):
        print("Not a Python file")
        sys.exit(1)

    count_lines(file_path)

if __name__ == "__main__":
    main()
