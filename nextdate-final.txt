#!/usr/bin/python

var = 1


def get_date():

    try:
        year = int(input("Input a year [1900-2099]: "))
        int(year)
    except ValueError:
        print ("Enter Valid Number")
    year_range = range(1900, 2099)
    if year not in year_range:
        print("The Value of the year should be in range 1900 - 2099 ")
        return
    if (year % 400 == 0):
        leap_year = True
    elif (year % 100 == 0):
        leap_year = False
    elif (year % 4 == 0):
        leap_year = True
    else:
        leap_year = False

    month = int(input("Input a month [1-12]: "))

    try:
        int(month)
    except ValueError:
        print ("Enter Valid Number")
    month_range = range(1, 12)
    if month not in month_range:
        print("The Value of the month should be in range 1 - 12 ")
        return
    if month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif month == 2:
        if leap_year:
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30

    day = int(input("Input a day [1-31]: "))
    try:
        int(day)
    except ValueError:
        print ("Enter Valid Number")
    day_range = range(1, 31)
    if day not in day_range:
        print("The Value of the day should be in range 1 - 31 ")

    if day < month_length:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))


if __name__ == '__main__':
    while var == 1:
        get_date()