# coding=utf-8
def extra_end(str):
    if len(str) < 2:
        return False

    return str[-2:] + str[-2:] + str[-2:]