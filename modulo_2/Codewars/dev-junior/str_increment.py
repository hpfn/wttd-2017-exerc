# coding=utf-8
def str_increment(string):
    count = 0
    new_str = ''
    while abs(count) < len(string):
        try:
            count -= 1
            if isinstance(int(string[count]), int):
                new_str = string[count:]
        except ValueError:
            count += 1
            break

    if new_str:
        tam_new_str = len(new_str)
        new_str = str(int(new_str) + 1)
        string = string[:count]
        string += '0' * (tam_new_str - len(new_str))
        string += new_str
    else:
        string += '1'

    return string

# I do not know python yet - Codewars
# I did not remember rstrip()
# I did not know about zfill()
#
# def increment_string(strng):
    # head = strng.rstrip('0123456789')
    # tail = strng[len(head):]
    # if tail == "": return strng+"1"
    # return head + str(int(tail) + 1).zfill(len(tail))
