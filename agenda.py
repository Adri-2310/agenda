"""
__author__ = 'Mertens Adrien'
__version__ = '1.0'
"""

# assign and input
day = int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))

#
flag: bool = False

# add a day relative to the date given by the user
if month != 2:  # all other months without february
    if month != 12:  # all ohter months without december
        if month in (1, 3, 5, 7, 8, 10):  # the months of 31 days
            if day < 31 and day > 0:  # traite le cas en-desous de 31
                day += 1
                flag = True
            elif day == 31:  # traite le cas du 31 jour
                day = 1
                month += 1
                flag = True
            else:  # l'utilisateur a mis un mauvais jour
                flag = False  # to do mauvais jour entrez
        elif month in (4, 6, 9, 11):  # the months of 30 days
            if day < 30 and day > 0:  # traite le cas en-desous de 30
                day += 1
                flag = True
            elif day == 30:  # traite le cas du 30 jour
                day = 1
                month += 1
                flag = True
            else:  # l'utilisateur a mis un mauvais jour
                flag = False  # to do mauvais jour entrez
        else:
            flag = False  # l'utilisateur a mis un nombre trop grand pour le month

    elif month == 12:  # the december month
        if day < 31 and day > 0:  # traite le cas des jours en-desous de 31
            day += 1
            flag = True
        elif day == 31:  # traite le cas du 31
            day = 1
            month = 1
            year += 1
            flag = True
        else:
            flag = False  # utilisateur mauvais jour
    else:
        flag = False  # mauvais month entrez

elif month == 2:  # the february month
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:  # année bisextille
        if day < 29 and day > 0:  # jour entre 0 et 28
            day += 1
            flag = True
        elif day == 29:  # jour 28
            day = 1
            month += 1
            flag = True
        else:  # mauvais jour entrez
            flag = False
    else:  # année non bisextille
        if day < 28 and day > 0:  # jour entre 0 et 28
            day += 1
            flag = True
        elif day == 28:  # jour 28
            day = 1
            month += 1
            flag = True
        else:  # mauvais jour entrez
            flag = False
else:
    flag = False  # mauvais month entrez


if flag:
    print(f"demain, il sera {day}/{month}/{year}")
else:
    print(
        f"Vous avez entré de mauvais données, les données doivent être entré comme cela jour:30 / month:3 / year:2000"
    )
