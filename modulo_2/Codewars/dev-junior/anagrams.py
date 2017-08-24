# coding=utf-8
def anagrams(word, words):

    return [letters for letters in words
            if sorted(letters) == sorted(word)]
