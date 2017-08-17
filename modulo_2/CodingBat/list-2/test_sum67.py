# coding=utf-8
from unittest import TestCase
from sum67 import sum67


class Sum67Test(TestCase):
    def test_sum67(self):
        self.assertEqual(sum67([1, 2, 2]), 5)

    def test_sum67_1(self):
        self.assertEqual(sum67([1, 2, 2, 6, 99, 99, 7]), 5)

    def test_sum67_2(self):
        self.assertEqual(sum67([1, 1, 6, 7, 2]), 4)

    # CondingBat
    def test_sum67_3(self):
        self.assertEqual(sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]), 2)

    def test_sum67_4(self):
        self.assertEqual(sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]), 2)

    def test_sum67_5(self):
        self.assertEqual(sum67([2, 7, 6, 2, 6, 7, 2, 7]), 18)

    def test_sum67_5(self):
        self.assertEqual(sum67([2, 7, 6, 2, 6, 2, 7]), 9)