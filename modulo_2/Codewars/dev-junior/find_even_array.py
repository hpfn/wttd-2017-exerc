# coding=utf-8
def find_even_index(arr):
    tam_arr = len(arr)

    for x in range(tam_arr):
        if sum(arr[:x]) == sum(arr[x+1:]):
            return x

    return -1



