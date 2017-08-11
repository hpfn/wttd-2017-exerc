# coding=utf-8
def make_chocolate(small, big, goal):
    # CodingBat does not want a loop
    keep_goal = 0
    for x in range(big):
        keep_goal += 5
        if keep_goal == goal:
            return 0
        elif goal - keep_goal < 5:
            break

    bars_missing = goal - keep_goal
    check_small_bars = small - bars_missing

    if check_small_bars >= 0:
        return bars_missing


    return -1
