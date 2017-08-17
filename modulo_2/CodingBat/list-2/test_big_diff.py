# coding=utf-8
from unittest import TestCase
from big_diff import big_diff



class BigDiffTest(TestCase):
    def test_bigdiff(self):
        self.assertEqual(big_diff([10, 3, 5, 6]), 7)

    def test_bigdiff_1(self):
        self.assertEqual(big_diff([7, 2, 10, 9]), 8)

    def test_bigdiff_2(self):
        self.assertEqual(big_diff([2 , 10, 7, 2]), 8)