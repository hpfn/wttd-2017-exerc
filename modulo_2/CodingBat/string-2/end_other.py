# coding=utf-8
def end_other(a, b):
    tam_a = len(a)
    tam_b = len(b)

    a = a.lower()
    b = b.lower()

    if tam_a > tam_b:
        return b in a[tam_b*-1:]

    return a in b[tam_a*-1:]
