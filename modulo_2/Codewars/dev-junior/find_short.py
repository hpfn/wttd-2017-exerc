# coding=utf-8
def find_short(s):
    min_s = s.split(' ')
    min_s = min(min_s, key=len)
    return len(min_s)


