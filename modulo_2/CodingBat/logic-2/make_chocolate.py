# coding=utf-8

def make_chocolate(small, big, goal):
    # CodingBat does not want a loop
    # big_bar = 0
    #
    # for x in range(big):
    #    big_bar += 5
    #    if big_bar == goal:
    #        return 0
    #    elif goal - big_bar < 5:
    #        break
    #
    # bars_missing = goal - big_bar
    # check_small_bars = small - bars_missing
    #
    # if check_small_bars >= 0:
    #     return bars_missing
    #
    # return -1
    how_many_big_bars = int(goal / 5)
    num_big_bars = big - how_many_big_bars

    result = -1

    if goal % 5 == 0 and num_big_bars > 0:
        result = 0

    if big < how_many_big_bars:
        has_big_bars = big * 5
    else:
        has_big_bars = how_many_big_bars * 5

    bars_missing = goal - has_big_bars
    check_small_bars = small - bars_missing
    if check_small_bars >= 0:
        result = bars_missing

    return result



