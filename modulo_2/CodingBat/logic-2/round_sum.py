# coding=utf-8
def round_sum(a, b, c):
    a = ugly_round(a)
    b = ugly_round(b)
    c = ugly_round(c)

    return int(a) + int(b) + int(c)

def ugly_round(x):

    if x >= 10:
        x = str(x)
        y = x[0] + '0'
        if x[-1] >= '5':
            y = (int(x[0]) + 1) * 10
    else:
        y = 0
        if x >= 5:
            y = 10

    return y



