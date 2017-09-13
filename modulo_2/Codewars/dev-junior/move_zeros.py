# coding=utf-8
def move_zeros(array):
    zero_r = []
    others_r = []
    for i in array:
        if i is 0 or str(i) == '0.0':
            zero_r.append(0)
        else:
            others_r.append(i)

    return array + zero_r

