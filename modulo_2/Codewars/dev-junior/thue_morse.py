# coding=utf-8
def thue_morse(n):
    # From Codewars.
    # To me the best answer
    #out = "0"
    #while len(out) < n:
    #    out += out.replace('1', '2').replace('0', '1').replace('2', '0')
    #
    #return out[:n]

    result = '0'

    for num in range(n - 1):
        for x in result:
            if x == '0':
                result += '1'
            else:
                result += '0'
            if len(result) == n:
                return result

    return result
