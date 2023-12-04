import seasons
import sys

def main():
    test_seasons()

def test_seasons():
    try:
        output = seasons.calculate_age_in_minutes("2022-10-29")
        assert output == "Five hundred twenty-five thousand, six hundred minutes", f"Expected output: 'Five hundred twenty-five thousand, six hundred minutes', Actual output: '{output}'"
    except AssertionError:
        print("Error")

if __name__ == "__main__":
    main()
