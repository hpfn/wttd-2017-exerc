# coding=utf-8
def pos_neg(a, b, negative):
    if not negative:
        return (a > 0 > b) or (a < 0 < b)
        # if (a > 0 and b < 0) or (a < 0 and b > 0):
        #    return True
    else:
        return a < 0 and b < 0
        # if (a < 0 and b < 0):
        #    return True

    # return False
