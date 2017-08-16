# coding=utf-8
def xyz_there(string):
    occur = string.count('xyz')
    notval = string.count('.xyz')

    return occur > notval

