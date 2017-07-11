# coding=utf-8
def sum2(nums):
    result = 0

    if len(nums) == 0:
        result = 0
    elif len(nums) < 2:
        result = nums[0]
    else:
         result = nums[0] + nums[1]

    return result