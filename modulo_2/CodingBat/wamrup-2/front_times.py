# coding=utf-8
def front_times(str, n):
    if n < 0:
        return 'not a valid number'
    if len(str) > 2:
        str = str[:3]

    return str * n