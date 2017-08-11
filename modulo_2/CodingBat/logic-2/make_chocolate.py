# coding=utf-8
def make_chocolate(small, big, goal):
    # CodingBat does not want a loop
    big_bar = 0
    for x in range(big):
        big_bar += 5
        if big_bar == goal:
            return 0
        elif goal - big_bar < 5:
            break

    bars_missing = goal - big_bar
    check_small_bars = small - bars_missing

    if check_small_bars >= 0:
        return bars_missing

    return -1


