# coding=utf-8
def make_out_word(out, word):
    if len(out) != 4:
        return False

    return out[:2] + word + out[2:]