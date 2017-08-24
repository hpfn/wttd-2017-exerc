# coding=utf-8
def solution(s):
    if len(s) % 2 != 0:
        s += '_'

    return [s[x-1]+char
            for x, char in enumerate(s)
            if x % 2 != 0]
