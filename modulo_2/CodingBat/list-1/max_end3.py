# coding=utf-8
def max_end3(nums):
    tam = len(nums)
    border = [nums[0], nums[-1]]
    lager = max(border)

    return [lager for i in range(tam)]