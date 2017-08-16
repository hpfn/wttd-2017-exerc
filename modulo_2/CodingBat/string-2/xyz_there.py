# coding=utf-8
def xyz_there(string):
    occur = string.count('xyz')
    notval = string.count('.xyz')

    if occur > notval:
        return True

    return False
