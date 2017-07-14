# coding=utf-8
from unittest import TestCase
from sorta_sum import sorta_sum


class SortaSumTest(TestCase):
    def test_sorta_sum_low(self):
        self.assertEqual(sorta_sum(3, 4), 7)

    def test_sorta_sum_in_range(self):
        self.assertEqual(sorta_sum(9, 4), 20)

    def test_sorta_sum_up(self):
        self.assertEqual(sorta_sum(10, 11), 21)

    def test_sorta_sum_in_low_limit(self):
        self.assertEqual(sorta_sum(5, 5), 20)

    def test_sorta_sum_in_up_limit(self):
        self.assertEqual(sorta_sum(9, 10), 20)