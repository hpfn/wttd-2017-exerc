# coding=utf-8
def centered_average(nums):
    nums.sort()
    nums = nums[1:-1]

    return int(sum(nums) / len(nums))