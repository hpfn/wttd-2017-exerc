# coding=utf-8
def centered_average(nums):
    nums.sort()

    return int(sum(nums[1:-1]) / len(nums[1:-1]))