# coding=utf-8
def first_half(str):
    tam = len(str)

    #if tam < 2:
    #    return False

    f_h = int(tam / 2)
    return str[:f_h]
