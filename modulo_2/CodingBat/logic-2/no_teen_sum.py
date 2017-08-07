# coding=utf-8
def no_teen_sum(a, b, c):
    teen_range = teen_range_fix()

    if a in teen_range:
        a = 0

    if b in teen_range:
        b = 0

    if c in teen_range:
        c = 0

    return a + b + c

def teen_range_fix():
    t_r = [i for i in range(13, 20)]
    t_r.remove(15)
    t_r.remove(16)
    return t_r