# coding=utf-8
def love6(a, b):

    if a == 6 or b == 6:
        result = True
    elif (a + b) == 6 or abs(a - b) == 6:
        result = True
    else:
        result = False

    return result
