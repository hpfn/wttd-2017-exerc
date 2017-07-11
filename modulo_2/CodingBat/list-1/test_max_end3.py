# coding=utf-8
from unittest import TestCase
from max_end3 import max_end3


class MaxEnd3Test(TestCase):
    def test_maxend3(self):
        self.assertEqual(max_end3([1, 2, 3]), [3, 3, 3])

    def test_maxend3_1(self):
        self.assertEqual(max_end3([11, 5, 9]), [11, 11, 11])

    def test_maxend3_2(self):
        self.assertEqual(max_end3([2, 11, 3]), [3, 3, 3])