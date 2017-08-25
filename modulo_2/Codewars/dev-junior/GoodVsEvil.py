# coding=utf-8
def GoodVsEvil(good, evil):
    good_ones = [1, 2, 3, 3, 4, 10]
    bad_ones = [1, 2, 2, 2, 3, 5, 10]

    good_plus = sum([x * int(y) for x, y in zip(good_ones, good.split())])
    evil_plus = sum([x * int(y) for x, y in zip(bad_ones, evil.split())])

    if good_plus < evil_plus:
        return "Battle Result: Evil eradicates all trace of Good"
    elif good_plus > evil_plus:
        return "Battle Result: Good triumphs over Evil"
    else:
        return "Battle Result: No victor on this battle field"

