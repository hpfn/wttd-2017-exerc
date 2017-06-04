# coding=utf-8
import unittest
from .makes10 import makes10


class Makes10Test(unittest.TestCase):
    def test_10_true(self):
        self.assertTrue(makes10(9, 10))

    def test_sum_10_false(self):
        self.assertFalse(makes10(9, 9))

    def test_sum_10_true(self):
        self.assertTrue(makes10(1, 9))
