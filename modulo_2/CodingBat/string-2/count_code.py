# coding=utf-8
def count_code(string):
    if string.count('co'):
        count = 0
        for char in range(len(string)-3):
            if (string[char] == 'c' and
                    string[char+1] == 'o' and
                    string[char+3] == 'e'):
                count += 1

        return count

    return 0
