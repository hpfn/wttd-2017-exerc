# coding=utf-8
def make_readable(seconds):
    if seconds == 0:
        result = '00:00:00'
    elif seconds < 60:
        result = '00:00:{:02}'.format(seconds)
    elif seconds < 3600:
        minutes = int(seconds / 60)
        secs = seconds - (60 * minutes)
        result = '00:{:02}:{:02}'.format(minutes, secs)
    else:
        hours = int(seconds / 3600)
        minutes = int((seconds / 3600 - hours) * 60)
        secs = round((((seconds / 3600 - hours) * 60) - minutes) * 60)
        result = '{:02}:{:02}:{:02}'.format(hours, minutes, int(secs))

    return result
