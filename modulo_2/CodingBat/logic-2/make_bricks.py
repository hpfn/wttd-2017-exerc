# coding=utf-8
def make_bricks(small, big, goal):

    # it is not what CodingBat wants
    total = small + (big * 5) + 1
    if goal in (i for i in range(total)):
        return True

    return False
