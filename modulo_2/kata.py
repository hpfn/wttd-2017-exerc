"""
 Regras do FizzBuzz

 1. Se a posição for múltipla de 3: fizz
 2. Se a posição for múltipla de 5: buzz
 3. Se a posição for múltipla de 3 e 5: fizzbuzz
 4. Para qualquer outra posição fale o próprio nº
"""
# tip from Henrique Bastos
from functools import partial
# import unittest

# lambda argumentos: retorno da expressão
#def multiple_of_X(base, number):
#    return number % base == 0
multiple_of_X = lambda base, number: number % base == 0
multiple_of_5 = partial(multiple_of_X, 5)
multiple_of_3 = partial(multiple_of_X, 3)

def robot(number):
    say = str(number)

    if multiple_of_3(number) and multiple_of_5(number):
        say = 'fizzbuzz'
    elif multiple_of_3(number):
        say = 'fizz'
    elif multiple_of_5(number):
        say = 'buzz'

    return say



""""
def assert_equal(result, expected):
    from sys import _getframe
    msg = 'Fail: Line {} got {} expecting {}'

    if not result == expected:
        current = _getframe()
        caller = current.f_back
        line_no = caller.f_lineno
        print(msg.format(line_no, result, expected))


if __name__ == '__main__':
    # Faltou:
    #     - consolidar cada caso de cada vez.
    #     - forma pythônica durante refatorar.
    #     - babysteps.
    # Passos bagunçados.
    assert_equal(robot(1), '1')
    assert_equal(robot(2), '2')
    assert_equal(robot(7), '7')

    assert_equal(robot(3), 'fizz')
    assert_equal(robot(6), 'fizz')
    assert_equal(robot(9), 'fizz')

    assert_equal(robot(5), 'buzz')
    assert_equal(robot(10), 'buzz')
    assert_equal(robot(20), 'buzz')

    assert_equal(robot(15), 'fizzbuzz')
    assert_equal(robot(30), 'fizzbuzz')
    assert_equal(robot(45), 'fizzbuzz')
"""
