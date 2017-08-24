# coding=utf-8
def comp(array1, array2):
    if (not isinstance(array1, list)
            or not isinstance(array2, list)):
        return False

    array1 = [x ** 2 for x in array1]

    array1.sort()
    array2.sort()

    return array1 == array2



