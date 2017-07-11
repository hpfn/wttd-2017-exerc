# coding=utf-8
from unittest import TestCase
from has23 import has23


class Has23Test(TestCase):
    def test_has23(self):
        self.assertTrue(has23([2, 5]))

    def test_has23_1(self):
        self.assertTrue(has23([4, 3]))

    def test_has23_2(self):
        self.assertFalse(has23([4, 5]))