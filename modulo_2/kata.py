"""
 Regras do FizzBuzz

 1. Se a posição for múltipla de 3: fizz
 2. Se a posição for múltipla de 5: buzz
 3. Se a posição for múltipla de 3 e 5: fizzbuzz
 4. Para qualquer outra posição fale o próprio nº
"""
# tip from Henrique Bastos
from functools import partial
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


if __name__ == '__main__':
    # Faltou:
    #     - consolidar cada caso de cada vez.
    #     - forma pythônica durante refatorar.
    #     - babysteps.
    # Passos bagunçados.
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(3) == 'fizz'
    assert robot(5) == 'buzz'
    assert robot(6) == 'fizz'
    assert robot(7) == '7'
    assert robot(9) == 'fizz'
    assert robot(10) == 'buzz'
    assert robot(11) == '11'
    assert robot(12) == 'fizz'
    assert robot(14) == '14'
    assert robot(15) == 'fizzbuzz'
    assert robot(20) == 'buzz'
    assert robot(21) == 'fizz'
    assert robot(24) == 'fizz'
    assert robot(25) == 'buzz'
    assert robot(34) == '34'
    assert robot(55) == 'buzz'