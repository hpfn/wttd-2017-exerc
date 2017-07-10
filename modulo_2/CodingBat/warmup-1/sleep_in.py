# coding=utf-8
def sleep_in(a_cond, b_cond):
    if not a_cond and b_cond:
        return True
    return a_cond == b_cond
