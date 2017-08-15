# coding=utf-8
from unittest import TestCase
from double_char import double_char


class DoubleCharTest(TestCase):
    def test_double_char(self):
        self.assertEqual(double_char('The'), 'TThhee')

    def test_double_char_1(self):
        self.assertEqual(double_char('AAbb'), 'AAAAbbbb')

    def test_double_char_2(self):
        self.assertEqual(double_char('Hi-There'), 'HHii--TThheerree')