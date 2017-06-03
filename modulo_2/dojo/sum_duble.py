def sum_double(x, y):
    """
    website solution:
    first do the math
    then if the args are the same
    multiply by 2
    """
    if x == y:
        return (x * 2) + (y * 2)
    return x + y




assert sum_double(1, 2) == 3
assert sum_double(3, 2) == 5
assert sum_double(2, 2) == 8