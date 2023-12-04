import re
import sys


def main():
    print(count(input("Text: ").strip()))


def count(s):
    a = []
    count = 0
    a = s.split(" ")
    for word in a:
        if re.search(r"^\W*um\W*$", word, re.IGNORECASE):
            count += 1
    return count


if __name__ == "__main__":
    main()