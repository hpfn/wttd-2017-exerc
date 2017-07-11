# coding=utf-8
from unittest import TestCase
from sum2 import sum2



class Sum2Test(TestCase):
    def test_sum2(self):
        self.assertEqual(sum2([1, 2, 3]), 3)

    def test_sum2_1(self):
        self.assertEqual(sum2([1, 1]), 2)

    def test_sum2_2(self):
        self.assertEqual(sum2([1, 1, 1, 1]), 2)

    def test_sum2_3(self):
        self.assertEqual(sum2([]), 0)

    def test_sum2_4(self):
        self.assertEqual(sum2([1]), 1)