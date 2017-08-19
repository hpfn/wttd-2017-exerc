def square_digits(num):
    result = [str(int(x) ** 2) for x in str(num)]
    return int(''.join(result))

if __name__ == '__main__':
    assert square_digits(9119) == 811181