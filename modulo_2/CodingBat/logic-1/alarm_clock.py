# coding=utf-8
def alarm_clock(day, vacation):

    result = ''

    if 0 < day < 6:
        if not vacation:
            result = '7:00'
        else:
            result = '10:00'
    else:
        if not vacation:
            result = '10:00'
        else:
            result = 'off'

    return result