# coding=utf-8
def caught_speeding(speed, is_birthday):

    limit_1 = 60
    limit_2 = 80
    result = 0

    if is_birthday:
        limit_1 = 65
        limit_2 = 85

    if limit_1 < speed <= limit_2:
        result = 1
    elif speed > limit_2:
        result = 2


    return result