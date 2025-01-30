"""
__author__ = 'Mertens Adrien'
__version__ = '1.0'
"""

# assign and input
day = int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))

# bool flag
flag_end: bool = False
flag_day: bool = False
flag_month: bool = False
flag_year: bool = False

# add a day relative to the date given by the user
if month != 2:  # all other months without february
    if month != 12:  # all ohter months without december
        if month in (1, 3, 5, 7, 8, 10):  # the months of 31 days
            if day < 31 and day > 0:  # traite le cas en-desous de 31
                day += 1
                flag_end = True
            elif day == 31:  # traite le cas du 31 jour
                day = 1
                month += 1
                flag_end = True
            else:  # l'utilisateur a mis un mauvais jour
                flag_end = False  # stop
                flag_day = True  # mauvais jour entrez
        elif month in (4, 6, 9, 11):  # the months of 30 days
            if day < 30 and day > 0:  # traite le cas en-desous de 30
                day += 1
                flag_end = True
            elif day == 30:  # traite le cas du 30 jour
                day = 1
                month += 1
                flag_end = True
            else:  # l'utilisateur a mis un mauvais jour
                flag_end = False  # stop
                flag_day = True  # mauvais jour entrez
        else:
            flag_end = False  # l'utilisateur a mis un nombre trop grand pour le month
            flag_month = True  # mauvais mois entrez

    elif month == 12:  # the december month
        if day < 31 and day > 0:  # traite le cas des jours en-desous de 31
            day += 1
            flag_end = True
        elif day == 31:  # traite le cas du 31
            day = 1
            month = 1
            year += 1
            flag_end = True
        else:
            flag_end = False  # stop
            flag_day = True  # mauvais jour entrez
    else:
        flag_end = False  # stop
        flag_month = True  # mauvais mois entrez

elif month == 2:  # the february month
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:  # année bisextille
        if day < 29 and day > 0:  # jour entre 0 et 28
            day += 1
            flag_end = True
        elif day == 29:  # jour 28
            day = 1
            month += 1
            flag_end = True
        else:
            flag_end = False  # stop
            flag_day = True  # mauvais jour entrez
    else:  # année non bisextille
        if day < 28 and day > 0:  # jour entre 0 et 28
            day += 1
            flag_end = True
        elif day == 28:  # jour 28
            day = 1
            month += 1
            flag_end = True
        else:
            flag_end = False  # stop
            flag_day = True  # mauvais jour entrez
else:
    flag_end = False  # stop
    flag_day = True  # mauvais mois entrez


if flag_end:
    print(f"demain, il sera {day}/{month}/{year}")
else:
    if flag_day:
        print("Vous avez entrez une mauvais donnée pour le jour")
    elif flag_month:
        print("Vous avez entrez une mauvais donnée pour le mois")
    else:
        print("Vous avez entrez une mauvais donnée pour l'année")
