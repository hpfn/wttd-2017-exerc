# coding=utf-8
from unittest import TestCase
from sum3 import sum3


class Sum3Test(TestCase):
    def test_sum3(self):
        self.assertEqual(sum3([1, 2, 3]), 6)

    def test_sum3_1(self):
        self.assertEqual(sum3([5, 11, 2]), 18)

    def test_sum3_2(self):
        self.assertEqual(sum3([7, 0, 0]), 7)