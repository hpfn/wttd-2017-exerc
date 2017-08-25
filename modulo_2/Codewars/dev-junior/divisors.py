# coding=utf-8
def divisors(integer):
    limit = int(integer / 2) + 1
    result = [i for i in range(2, limit)
              if integer % i == 0]

    if len(result) > 0:
        return result

    return '%s is prime' % integer


