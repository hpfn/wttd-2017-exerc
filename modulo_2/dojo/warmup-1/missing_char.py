def missing_char(str, n):
    str_l = list(str)
    # if you need a return. remember collections.deque
    #str_l.pop(n)
    del str_l[n]
    return ''.join(str_l)