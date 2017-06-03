"""
como saber se o número é feliz ou triste ?

1. dado um número inteiro positivo
2. substitua o número pela soma dos quadrados dos seus dígitos
3. se o resultado for 1, o número é feliz
4. caso contrário, repita o processo indefinidamente

Os números que resultarem em 1, são felizes.
Os que não resultarem em 1 são tristes.

Número 7:

7² = 49
4² + 9² = 16 + 81 = 97
9² + 7² = 81 + 49 = 130
1² + 3² + 0² = 1 + 9 + 0 = 10
1² + 0² = 1

    7 é feliz

Número 4:

4² = 16
1² + 6² = 1 + 36 = 37
3² + 7² = 9 + 49 = 58
5² + 8² = 25 + 64 = 89
8² + 9² = 64 + 81 = 145
1² + 4² + 5² = 1 + 16 + 25 = 42
4² + 2² = 16 + 4 = 20
2² + 0² = 4 + 0 = 4

    4 não é feliz
"""

def sum_squares(number):
    digits = ((int(x) ** 2) for x in str(number))
    return sum(digits)

def happy(number):
    box = []
    n = number
    while n != 1 and n not in box:
        box.append(n)
        n = sum_squares(n)

    return n == 1


for x in (2, 3, 4, 5, 6, 8, 9, 11, 12, 14, 15, 16):
    #print(x)
    assert not happy(x) == 1
assert all(happy(n) for n in (1, 7, 10, 13, 100, 97, 130))
#for i in (1, 7, 10, 13, 100, 97, 130):
#    # print(i)
#    assert happy(i) == 1

