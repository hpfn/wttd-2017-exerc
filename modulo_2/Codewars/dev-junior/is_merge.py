# coding=utf-8


def is_merge(s, part1, part2):
    if len(part1) + len(part2) != len(s):
        return False
        
    result = ['1' for x in range(len(s))]
    check_str(s, part1, result)
    check_str(s, part2, result)

    return ''.join(result) == s


def check_str(main_s, str_x, final):
    tmp = -1
    for x in str_x:
        for y, char in enumerate(main_s):
            if x == char and y > tmp:
                final[y] = x
                tmp = final.index(x)


if __name__ == '__main__':
    print(is_merge('codewars', 'code', 'wasr'))

