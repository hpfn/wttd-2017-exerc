# coding=utf-8
def in1to10(n, outside_mode):

    result = False

    if not outside_mode and 1 <= n <= 10:
        result = True
    elif outside_mode and (n <= 1 or n >= 10):
        result = True

    return result
