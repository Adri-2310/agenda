"""
__author__ = 'Mertens Adrien'
__version__ = '1.0'
"""
# assign and input
day = int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))

#
flag = False

# add a day relative to the date given by the user
if month != 2: # all other months without february
    if month != 12 : # the december month
        if month in (1, 3, 5, 7, 8, 10): # the months of 31 days
            if day >= 30 : # traite le cas du 31 jour
                day = 1
                month += 1
                flag = True
            else: # traite le cas des jours en desous de 30
                pass
        else: # the months of 30 days
            pass
    else: # all other months without December
        pass
else: # the february month
    pass

if flag : print(f"demain, il sera {day}/{month}/{year}")