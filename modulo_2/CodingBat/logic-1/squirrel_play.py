# coding=utf-8
def squirrel_play(temp, is_summer):
    if not is_summer and 60 <= temp <= 90:
        result = True
    elif is_summer and 60 <= temp <= 100:
        result = True
    else:
        result = False

    return result