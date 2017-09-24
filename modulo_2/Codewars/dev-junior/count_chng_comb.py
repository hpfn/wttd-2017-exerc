# coding=utf-8

# Fails at '5 should equal 1022'
#
def count_chng_comb(money, coins):
    many_diff = 0

    if coins.count(1):
        many_diff = 1
        coins.remove(1)

    for i in coins:
        if one_at_time(i, money) == money:
            many_diff += 1

    return many_diff + combine(coins, money)


def one_at_time(number, total):
    count = 0
    while count < total:
        count += number

    return count


def combine(numbers, total):
    count_1 = 0
    for x in numbers:
        for i in numbers:
            x += i
            if x == total:
                count_1 += 1

    return count_1


if __name__ == '__main__':
    count_chng_comb(4, [1, 2])
