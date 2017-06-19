# coding=utf-8
import unittest
from array_front9 import array_front9


class ArrayFront9Test(unittest.TestCase):
    def test_array_front9_yes(self):
        self.assertTrue(array_front9([1, 2, 9, 3, 4]))

    def test_array_front9_yes_with_3(self):
        self.assertTrue(array_front9([1, 2, 9]))

    def test_array_front9_no(self):
        self.assertFalse(array_front9([1, 2, 3, 4, 9]))

    def test_array_front9_no_with_3(self):
        self.assertFalse(array_front9([1, 2, 3]))

    def test_array_front9_no_with_2(self):
        self.assertFalse(array_front9([1, 2]))

    def test_array_front9_no_without(self):
        self.assertFalse(array_front9([1, 2, 3, 4, 5]))



