# coding=utf-8
from unittest import TestCase
from regex_passwd_val import regex_passwd_val


class RegexPaswdValTest(TestCase):
    def test_regexpasswdval(self):
        content = ['fjd3IR9', '4fdg5Fj3'
                   'djI38D55', '123abcABC',
                   'ABC123abc', 'Password123']

        for t in content:
            with self.subTest():
                self.assertTrue(regex_passwd_val(t))

    def test_regexpasswdval_1(self):
        content = ['DSJKHD23', 'jfkdfj3j',
                   '!fdjn345', 'JHD5FJ53',
                   'a2.d412', 'fjd3  IR9',
                   'fjd3IR9.;', '12we_5tg']

        for t in content:
            with self.subTest():
                self.assertFalse(regex_passwd_val(t))



