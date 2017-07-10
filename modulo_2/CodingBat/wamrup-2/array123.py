# coding=utf-8
def array123(nums):
    str_nums = ''
    for i in nums:
        str_nums += str(i)

    return str_nums.count('123') > 0