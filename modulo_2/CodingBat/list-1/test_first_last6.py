# coding=utf-8
from unittest import TestCase
from first_last6 import first_last6


class FirstLast6Test(TestCase):
    def test_firstlast6(self):
        self.assertTrue(first_last6([1, 2, 6]))

    def test_firstlast6_1(self):
        self.assertTrue(first_last6([6, 1, 2, 3]))

    def test_firstlast6_2(self):
        self.assertFalse(first_last6([13, 6, 1, 2, 3]))