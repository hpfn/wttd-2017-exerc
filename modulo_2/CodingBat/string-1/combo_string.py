# coding=utf-8
def combo_string(a, b):
    tam_a = len(a)
    tam_b = len(b)
    str_ = ''
    if tam_a == tam_b:
        str_ = False
    elif tam_a > tam_b:
        str_ = b + a + b
    else:
        str_ = a + b + a

    return str_
