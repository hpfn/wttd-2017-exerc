# coding=utf-8
# not pythonic
def title_case(title, minor_words=''):
    if len(title) == 0:
        return ''

    new_title = []
    minor_words = minor_words.lower().split()

    for word in title.capitalize().split():
        if word in minor_words:
            new_title.append(word)
        else:
            new_title.append(word.capitalize())

    return ' '.join(new_title)
