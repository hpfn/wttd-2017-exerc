#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises


# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
    # endswith() could be used
    if len(s) > 2 and s[-3:] in 'ing':
        s = s + 'ly'
    elif len(s) > 2:
        s = s + 'ing'
    else:
        pass
    # +++your code here+++
    return s


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    # +++your code here+++
    import re
    result = re.sub(r'not.*bad', r'good', s)
    return result


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

# import math (ceil) and lambda could be used
def div_even(x, lst_x):
    divisor = int(lst_x / 2)
    return x[:-divisor], x[divisor:]

def div_odd(y, lst_y):
    divisor = int(lst_y / 2)
    return y[:-divisor], y[divisor+1:]

def send_to_odd_or_even(the_str, len_str):
    if len_str % 2 == 0:
        front_x, back_x = div_even(the_str, len_str)
    else:
        front_x, back_x = div_odd(the_str, len_str)

    return front_x, back_x

def front_back(a, b):
    tam_a = len(a)
    tam_b = len(b)

    front_a, back_a = send_to_odd_or_even(a, tam_a)
    front_b, back_b = send_to_odd_or_even(b, tam_b)

    return front_a + front_b + back_a + back_b

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
    main()
