from datetime import date, datetime
import sys
import inflect

def calculate_age_in_minutes(user_input):
    try:
        birth_date = datetime.strptime(user_input, "%Y-%m-%d").date()
        current_date = date.today()
    except ValueError:
        print("Invalid date format.")
        sys.exit(1)
    age_in_minutes = calculate_total_minutes(birth_date, current_date)
    print_age_in_words(age_in_minutes)


def calculate_total_minutes(start_date, end_date):
    total_days = (end_date - start_date).days
    total_years = total_days / 365

    leap_years = count_leap_years(start_date.year, end_date.year)
    total_minutes = total_years * 365 * 24 * 60 + leap_years * 24 * 60

    return int(total_minutes)

def count_leap_years(start_year, end_year):
    return sum(1 for year in range(start_year, end_year) if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0)

def print_age_in_words(age_in_minutes):
    p = inflect.engine()
    age_words = p.number_to_words(age_in_minutes, andword='', zero='zero')
    print(age_words.capitalize() + " minutes")

def main():
    user_input = input("Please enter your date of birth in YYYY-MM-DD format: ")
    calculate_age_in_minutes(user_input)

if __name__ == "__main__":
    main()
