# coding=utf-8
import unittest
from array123 import array123


class Array123Test(unittest.TestCase):
    def test_array123_small(self):
        self.assertTrue(array123([1, 2, 3]))

    def test_array123(self):
        self.assertTrue(array123([1, 1, 2, 3, 1]))

    def test_array123_at_the_end(self):
        self.assertTrue(array123([1, 1, 2, 1, 2, 3]))

    def test_array123_fail(self):
        self.assertFalse(array123([1, 1, 2, 4, 1]))

    def test_array123_fail_small(self):
        self.assertFalse(array123([1, 1]))