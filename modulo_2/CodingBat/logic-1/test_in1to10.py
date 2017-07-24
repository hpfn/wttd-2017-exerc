# coding=utf-8
from unittest import TestCase
from in1to10 import in1to10


class In1to10Test(TestCase):
    def test_in1to10(self):
        self.assertTrue(in1to10(5, False))

    def test_in1to10_1(self):
        self.assertTrue(in1to10(11, True))

    def test_in1to10_2(self):
        self.assertFalse(in1to10(11, False))

    def test_in1to10_3(self):
        self.assertFalse(in1to10(5, True))

