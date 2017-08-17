# coding=utf-8
from unittest import TestCase
from sum13 import sum13


class Sum13Test(TestCase):
    def test_sum13(self):
        self.assertEqual(sum13([1, 2, 2, 1]), 6)

    def test_sum13_1(self):
        self.assertEqual(sum13([1, 1]), 2)

    def test_sum13_2(self):
        self.assertEqual(sum13([1, 2, 2, 1, 13]), 6)

    def test_sum13_3(self):
        self.assertEqual(sum13([1, 2, 2, 1, 13, 1]), 6)

    def test_sum13_4(self):
        self.assertEqual(sum13([]), 0)

    def test_sum13_3(self):
        self.assertEqual(sum13([1, 2, 13, 1, 13, 1]), 3)

