from working import convert
import sys

def test():
    try:
        assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    except ValueError:
        print("Error")
        sys.exit(1)
    try:
        assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    except ValueError:
        print("Error")
        sys.exit(1)
    try:
        assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    except ValueError:
        print("Error")
        sys.exit(1)
    try:
        assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    except ValueError:
        print("Error")
        sys.exit(1)
    try:
        assert convert("01:10 PM to 4 PM") == "13:10 to 16:00"
    except ValueError:
        print("Error")
        sys.exit(1)

def main():
    test()

if __name__ == "__main__":
    main()
