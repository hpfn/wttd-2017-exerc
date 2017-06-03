def diff21(number):
    """
    absolute diff between number and 21
    except return double the absolute diff if n is over 21
    """
    if number > 21:
        return (number - 21) * 2
    return 21 - number

assert diff21(19) == 2
assert diff21(10) == 11
assert diff21(21) == 0
assert diff21(22) == 2