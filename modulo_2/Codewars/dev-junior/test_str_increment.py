# coding=utf-8
from unittest import TestCase
from str_increment import str_increment


class StrIncrementTest(TestCase):
    def test_str_increment(self):
        self.assertEqual(str_increment('foo'), 'foo1')

    def test_str_increment_1(self):
        self.assertEqual(str_increment('foo9'), 'foo10')

    def test_str_increment_2(self):
        self.assertEqual(str_increment('foo099'), 'foo100')

    def test_str_increment_3(self):
        self.assertEqual(str_increment('foo0042'), 'foo0043')

    def test_str_increment_4(self):
        self.assertEqual(str_increment(''), '1')

    def test_str_increment_5(self):
        self.assertEqual(str_increment('11'), '12')

