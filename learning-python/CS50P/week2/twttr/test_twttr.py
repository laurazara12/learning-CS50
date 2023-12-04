from twttr import shorten
import sys

def test_twttr():
    try:
        result = shorten("What's your name?")
        assert result == "Wht's yr nm?"

        result = shorten("Twitter")
        assert result == "Twttr"

        result = shorten("CS50")
        assert result == "CS50"
    except ValueError as e :
        print(f"Error {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

def main():
    test_twttr()

if __name__ == "__main__":
    main()
