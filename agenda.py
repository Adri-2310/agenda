"""
__author__ = 'Mertens Adrien'
__version__ = '1.0'
"""

# Assign and input values
day = int(input("Entrez un jour : "))
month = int(input("Entrez un mois : "))
year = int(input("Entrez une année : "))

# Boolean flags to track errors
flag_end: bool = False
flag_day: bool = False
flag_month: bool = False
flag_year: bool = False

# Add a day relative to the user-provided date
if month != 2:  # All months except February
    if month != 12:  # All months except December
        if month in (1, 3, 5, 7, 8, 10):  # Months with 31 days
            if 0 < day < 31:  # Valid days (1-30)
                day += 1
                flag_end = True
            elif day == 31:  # Case where day is 31
                day = 1
                month += 1
                flag_end = True
            else:  # Invalid day input
                flag_end = False  # Stop execution
                flag_day = True  # Invalid day flag
        elif month in (4, 6, 9, 11):  # Months with 30 days
            if 0 < day < 30:  # Valid days (1-29)
                day += 1
                flag_end = True
            elif day == 30:  # Case where day is 30
                day = 1
                month += 1
                flag_end = True
            else:  # Invalid day input
                flag_end = False  # Stop execution
                flag_day = True  # Invalid day flag
        else:
            flag_end = False  # Invalid month input
            flag_month = True  # Invalid month flag

    elif month == 12:  # Special case: December
        if 0 < day < 31:  # Valid days (1-30)
            day += 1
            flag_end = True
        elif day == 31:  # Case where day is 31
            day = 1
            month = 1
            year += 1  # Move to the next year
            flag_end = True
        else:
            flag_end = False  # Stop execution
            flag_day = True  # Invalid day flag
    else:
        flag_end = False  # Stop execution
        flag_month = True  # Invalid month flag

elif month == 2:  # Special case: February
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:  # Leap year condition
        if 0 < day < 29:  # Valid days (1-28)
            day += 1
            flag_end = True
        elif day == 29:  # Last day of February in a leap year
            day = 1
            month += 1
            flag_end = True
        else:
            flag_end = False  # Stop execution
            flag_day = True  # Invalid day flag
    else:  # Non-leap year
        if 0 < day < 28:  # Valid days (1-27)
            day += 1
            flag_end = True
        elif day == 28:  # Last day of February in a non-leap year
            day = 1
            month += 1
            flag_end = True
        else:
            flag_end = False  # Stop execution
            flag_day = True  # Invalid day flag
else:
    flag_end = False  # Stop execution
    flag_day = True  # Invalid month flag

# display results or errors
if flag_end:
    print(f"La date de demain sera : {day}/{month}/{year}")
else:
    if flag_day:
        print("Vous avez entré une mauvaise donnée pour le jour")
    elif flag_month:
        print("Vous avez entré une mauvaise donnée pour le mois")
    else:
        print("Vous avez entré une mauvaise donnée pour l'année")
