# coding=utf-8
def lone_sum(a, b, c):
    # this is not necessary
    nums = set([a, b, c])
    tam = len(nums)
    if tam == 1:
        result = 0
    elif tam == 2:
        if b == c:
            result = a
        elif a == c:
            result = b
        else:
            result = c
    else:
        result = a + b + c

    return result
