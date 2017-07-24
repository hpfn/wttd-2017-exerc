# coding=utf-8
from unittest import TestCase
from love6 import love6


class Love6Test(TestCase):
    def test_love6(self):
        self.assertTrue(love6(6, 4))

    def test_love6_1(self):
        self.assertTrue(love6(1, 5))

    def test_love6_2(self):
        self.assertFalse(love6(4, 5))

    def test_love6_3(self):
        self.assertTrue(love6(7, 13))

    def test_love6_4(self):
        self.assertFalse(love6(-7, 1))