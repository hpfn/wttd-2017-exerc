def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile
    if a_smile and b_smile == False:
        return False
    elif a_smile == False and b_smile:
        return False

    return True



assert monkey_trouble(True, True) == True
assert monkey_trouble(False, False) == True
assert monkey_trouble(True, False) == False
assert monkey_trouble(False, True) == False