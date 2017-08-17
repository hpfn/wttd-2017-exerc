# coding=utf-8
from unittest import TestCase
from has22 import has22

# CodingBat
class Has22Test(TestCase):
    def test_has22(self):
        self.assertTrue(has22([1, 2, 2]))

    def test_has22_1(self):
        self.assertFalse(has22([1, 2, 1, 2]))

    def test_has22_2(self):
        self.assertFalse(has22([2, 1, 2]))

    def test_has22_3(self):
        self.assertTrue(has22([2, 1, 2, 2]))

    def test_has22_3(self):
        self.assertTrue(has22([2, 2, 1, 2]))

    def test_has22_3(self):
        self.assertFalse(has22([2]))