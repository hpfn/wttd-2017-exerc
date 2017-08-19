# coding=utf-8
def descending_order(nums):
    nums = [x for x in str(nums)]
    nums.sort()
    nums = ''.join(nums[::-1])
    return int(nums)

