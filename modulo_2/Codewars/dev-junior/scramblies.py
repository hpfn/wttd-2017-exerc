# coding=utf-8
def scramblies(str1, str2):
    str1 = set(str1)
    str2 = set(str2)
    return str2.issubset(str1)
