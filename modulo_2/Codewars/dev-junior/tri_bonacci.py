# coding=utf-8
# not smart today
def tri_bonacci(signature, n):

    if n == 0:
        signature = []
    elif n == 1:
        signature = [signature[0]]
    elif n == 2:
        signature = [signature[0], signature[1]]
    else:
        tam_n = len(signature)

        for x in range(tam_n, n):
            signature.append(signature[x-3]+signature[x-2]+signature[x-1])

    return signature

    """ Codewars guy
    res = signature[:n]
    for i in range(n - 3): res.append(sum(res[-3:]))
    return res
    """