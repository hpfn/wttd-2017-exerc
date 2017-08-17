# coding=utf-8
def sum13(nums):
    count_13 = nums.count(13)
    # author wants this 'try/except'
    try:
        for x in range(count_13):
            location = nums.index(13)
            nums.pop(location)
            if location + 1 <= len(nums):
                nums.pop(location)
    except ValueError:
        print('not in list')

    return sum(nums)
