from datetime import datetime

def prompt_user():
    while True:
        user_input = input("Please enter a date (in month-day-year or Month Day, Year format): ")
        date_iso = convert_date_to_iso(user_input)
        if date_iso:
            print(date_iso)
            break
        else:
            print("Invalid date format. Please try again.")

def convert_date_to_iso(date_str):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    try:
        # Attempt to parse the date input
        date_obj = datetime.strptime(date_str, '%m/%d/%Y')
        return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        pass

    try:
        # Attempt to parse the date input with Month Day, Year format
        for month in months:
            if month in date_str:
                date_obj = datetime.strptime(date_str, f'%B %d, %Y')
                return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        pass

    return None

if __name__ == "__main__":
    prompt_user()
