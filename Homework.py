import random
from datetime import datetime, timedelta

# Function to check if the format is consistent
def check_format(date, date_format):
    for date_char, format_char in zip(date, date_format):
        if format_char in 'YMD':
            if not date_char.isdigit():
                return False
        elif date_char != format_char:
            return False
    return True

# Function to check if the date is valid
def check_valid_date(date, date_format):
    year = int(date[date_format.index('Y'):date_format.index('Y')+4])
    month = int(date[date_format.index('M'):date_format.index('M')+2])
    day = int(date[date_format.index('D'):date_format.index('D')+2])

    if month < 1 or month > 12:
        return False

    if month % 2 == 1:
        if day < 1 or day > 31:
            return False
    elif month == 2:
        if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) and (day < 1 or day > 29):
            return False
        elif day < 1 or day > 28:
            return False
    else:
        if day < 1 or day > 30:
            return False

    return True

# Function to get the weekday name
def get_weekday_name(date):
    weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekday_names[datetime.strptime(date, "%Y-%m-%d").weekday()]

from datetime import datetime, timedelta

# Function to choose a date format
def choose_date_format():
    while True:
        print("Choose a date format:")
        print("1. YYYY-MM-DD")
        print("2. MM/DD/YYYY")
        choice = input("Enter the order number (1 or 2): ")
        if choice in ["1", "2"]:
            return choice

# Function to get a date from the user
def get_user_date(date_format_choice):
    date_format = "%Y-%m-%d" if date_format_choice == "1" else "%m/%d/%Y"
    while True:
        user_date = input(f"Enter a date in the format {date_format}: ")
        if check_format(user_date, date_format):
            if check_valid_date(user_date, date_format):
                return user_date
            else:
                print("Invalid date. Please enter a valid date.")
        else:
            print("Date format inconsistency. Please enter a date in the correct format.")

# Function to display the weekday and one year later
def display_weekday_and_one_year_later(user_date):
    print(f"The weekday of {user_date} is {get_weekday_name(user_date)}.")
    one_year_later = datetime.strptime(user_date, "%Y-%m-%d") + timedelta(days=365)
    one_year_later_str = one_year_later.strftime("%Y-%m-%d")
    print(f"A year later, it will be {get_weekday_name(one_year_later_str)} on {one_year_later_str}.")

# Main program
while True:
    date_format_choice = choose_date_format()
    user_date = get_user_date(date_format_choice)
    display_weekday_and_one_year_later(user_date)

    another_date = input("Do you want to test another date? (y/n): ")
    if another_date.lower() != 'y':
        print("The random auto-testing is starting...")
        break

# Define a function to return a randomly composed date
def generate_random_date():
    year = random.randint(2000, 2020)
    month = f"{random.randint(1, 12):02d}"
    if month == "02":
        day = f"{random.randint(1, 28):02d}"
    elif month in ["04", "06", "09", "11"]:
        day = f"{random.randint(1, 30):02d}"
    else:
        day = f"{random.randint(1, 31):02d}"

    date_format_choice = random.choice(["1", "2"])
    if date_format_choice == "1":
        return f"{year}-{month}-{day}"
    else:
        return f"{month}/{day}/{year}"

# Compose and test 10 random dates
for _ in range(10):
    random_date = generate_random_date()
    random_format_choice = random.choice(["1", "2"])
    date_format = "%Y-%m-%d" if random_format_choice == "1" else "%m/%d/%Y"
    
    print(f"Generated date: {random_date} Format: {'YYYY-MM-DD' if random_format_choice == '1' else 'MM/DD/YYYY'}")
    
    if check_format(random_date, date_format):
        if check_valid_date(random_date, date_format):
            print("Date format consistency: True")
            print("Date validity: True")
            print(f"The weekday of {random_date} is {get_weekday_name(random_date)}.")
        else:
            print("Date format consistency: True")
            print("Date validity: False")
    else:
        print("Date format consistency: False")

