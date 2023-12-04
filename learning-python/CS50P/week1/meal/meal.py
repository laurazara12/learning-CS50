def convert(time):
    hours, minutes = map(int, time.split(':'))
    return hours + (minutes / 60)

def main():
    time = input("Enter the time in 24-hour format (e.g., 07:00): ")

    meal_time = convert(time)

    breakfast_start = 7.0
    breakfast_end = 11.0
    lunch_start = 12.0
    lunch_end = 16.0
    dinner_start = 18.0
    dinner_end = 22.0

    if breakfast_start <= meal_time <= breakfast_end:
        print("breakfast time")
    elif lunch_start <= meal_time <= lunch_end:
        print("lunch time")
    elif dinner_start <= meal_time <= dinner_end:
        print("dinner time")

if __name__ == "__main__":
    main()
