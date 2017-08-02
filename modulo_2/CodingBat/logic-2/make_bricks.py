# coding=utf-8
# the author do not want loops
def make_bricks(small, big, goal):

    if (big * 5) == goal or small == goal:
        return True

    total = small
    for i in range(big):
        total += 5
        if total == goal:
            return True


    total = big * 5
    for i in range(small):
        total += 1
        if total == goal:
            return True

    return False
