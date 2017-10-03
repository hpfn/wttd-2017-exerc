# coding=utf-8
from collections import deque

def josephus_survivor(n, k):
    n = deque(range(1, n+1))
    while len(n) != 1:
        to_rotate = len(n) - k
        n.rotate(to_rotate)
        n.pop()

    return n[0]

# Codewars
# result = 0
# for i in range(1, n + 1):
#     result = (result + k) % i
#
# return result + 1