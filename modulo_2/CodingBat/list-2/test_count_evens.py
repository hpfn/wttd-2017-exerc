# coding=utf-8
from unittest import TestCase
from count_evens import count_evens



class CountEvensTest(TestCase):
    def test_countevens(self):
        self.assertEqual(count_evens([2, 1, 2, 3, 4]), 3)

    def test_countevens_1(self):
        self.assertEqual(count_evens([2, 2, 0]), 3)

    def test_countevens_2(self):
        self.assertEqual(count_evens([1, 3, 5]), 0)