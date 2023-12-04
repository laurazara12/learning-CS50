import sys
from numb3rs import validate

def test():
    try:
        assert validate("...") == False
    except AssertionError:
        print("Error")
    try:
        assert validate(".1.32.0") == False
    except AssertionError:
        print("Error")
    try:
        assert validate("193.256.22.1") == False
    except AssertionError:
        print("Error")
    try:
        assert validate("0.0.0.0") == True
    except AssertionError:
        print("Error")
    try:
        assert validate("1.2.2.1") == True
    except AssertionError:
        print("Error")

def main():
    test()

if __name__ == "__main__":
    main()