# coding=utf-8
from re import search, fullmatch

def regex_passwd_val(str_pass):
    return search(r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?!.*[\W_]).{6,}$', str_pass)
