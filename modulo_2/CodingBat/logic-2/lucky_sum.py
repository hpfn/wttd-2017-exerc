# coding=utf-8
def lucky_sum(a, b, c):

    nums = [a, b, c]
    result = sum(nums)

    if 13 in nums:
        if a == 13:
            result = 0
        elif b == 13:
            result = a
        else:
            result = a + b

    return result