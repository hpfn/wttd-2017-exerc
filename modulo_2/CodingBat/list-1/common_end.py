# coding=utf-8
def common_end(a, b):
    return (a[0] == b[0] or a[-1] == b[-1])
    if a[0] == b[0]:
        return True
    elif a[-1] == b[-1]:
        return True
    else:
        return False