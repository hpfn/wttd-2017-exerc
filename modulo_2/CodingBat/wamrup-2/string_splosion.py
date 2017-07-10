# coding=utf-8
def string_splosion(str):
    #l = str[0]
    #for x in range(2, len(str)+1):
    #    l = l + str[0] + str[1:x]
    l = ''
    for x in range(len(str)):
        l += str[:x+1]
    return l
