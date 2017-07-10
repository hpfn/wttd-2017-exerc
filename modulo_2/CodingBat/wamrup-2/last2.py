# coding=utf-8
def last2(str):
    #if len(str) < 4:
    #    return 0

    sub_str = str[-2:]

    count = 0
    index = 0

    while index < len(str) - 2:
        if str[index] + str[index+1] == sub_str:
            count += 1

        index += 1

    return count