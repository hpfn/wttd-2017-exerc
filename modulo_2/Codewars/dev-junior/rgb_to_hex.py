# coding=utf-8
def rgb_to_hex(r, g, b):
    num_received = [r, g, b]
    rgb_list = [fix_rgb(num) for num in num_received]

    return ''.join(rgb_list)

def fix_rgb(z):
    if z < 0:
        z = 0
    elif z > 255:
        z = 255

    return format(z, '02x').upper()

# to me a better solution - from Codewars
#def limit(num):
#    if num < 0:
#        return 0
#    if num > 255:
#        return 255
#    return num
#
#
#def rgb(r, g, b):
#    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))