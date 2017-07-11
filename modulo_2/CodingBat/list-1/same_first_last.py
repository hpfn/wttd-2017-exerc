# coding=utf-8
def same_first_last(nums):
    return (len(nums) > 0 and (nums[0] == nums[-1]))

    if len(nums) > 0:
        if nums[0] == nums[-1]:
            return True

    return False