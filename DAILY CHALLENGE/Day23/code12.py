import calendar

def printMonth():
    try:
        year = int(input("Year: "))
    except Exception as err:
        print(f"An error is occur as {err}")
    try:
        month = int(input("Month: "))
    except Exception as err:
        print(f"An error is occur as {err}")

    print(calendar.month(year, month))


def printYear():
    try:
        year = int(input("Year: "))
    except Exception as err:
        print(f"An error is occur as {err}")

    print(calendar.calendar(year))


while True:
    print(f"Press 1 for specific month calender")
    print(f"Press 2 for whole year calender")

    response = int(input("Enter your choice: "))


    if response == 1:
        printMonth()

    if response == 2:
        printYear()

    else:
        raise Exception("ValueError => Invalid choice")
        print("")
