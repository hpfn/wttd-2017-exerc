# coding=utf-8
def sum67(nums):
    has_6 = nums.count(6)
    # ugly, and the except will happen
    # but passes the tests
    try:
        for x in range(has_6):
            location_6 = nums.index(6)
            str_1 = nums[:location_6]
            str_2 = nums[location_6:]
            location_7 = str_2.index(7) + 1
            nums = str_1 + str_2[location_7:]
    except ValueError:
        pass

    return sum(nums)
