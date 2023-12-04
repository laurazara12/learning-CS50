import sys
from um import count

def test():
    try:
        assert count("...um") == "1"
    except AssertionError:
        print("Error")
    try:
        assert count("yummy") == "0"
    except AssertionError:
        print("Error")
    try:
        assert count("um ummmm") == "2"
    except AssertionError:
        print("Error")
    try:
        assert count("Um...") == "1"
    except AssertionError:
        print("Error")

def main():
    test()

if __name__ == "__main__":
    main()