# coding=utf-8
import unittest
from array_count9 import array_count9


class ArrayCount9Test(unittest.TestCase):
    def test_array_count9_1(self):
        self.assertEqual(array_count9([1, 2, 9]), 1)

    def test_array_count9_2(self):
        self.assertEqual(array_count9([1, 9, 9]), 2)

    def test_array_count9_3(self):
        self.assertEqual(array_count9([1, 9, 2, 9, 9]), 3)