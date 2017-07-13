# coding=utf-8
def date_fashion(you, date):
    if (you > 7 or date > 7) and (you > 2 and date > 2):
        result = 2
    elif you < 3 or date < 3:
        result = 0
    else:
        result = 1

    return result