# coding=utf-8
from unittest import TestCase
from lucky_sum import lucky_sum


class LuckySumTest(TestCase):
    def test_lucky_sum(self):
        self.assertEqual(lucky_sum(1, 2, 3), 6)

    def test_lucky_sum_1(self):
        self.assertEqual(lucky_sum(1, 2, 13), 3)

    def test_lucky_sum_2(self):
        self.assertEqual(lucky_sum(1, 13, 3), 1)

    def test_lucky_sum_3(self):
        self.assertEqual(lucky_sum(13, 2, 3), 0)

    def test_lucky_sum_4(self):
        self.assertEqual(lucky_sum(1, 13, 13), 1)

    def test_lucky_sum_3(self):
        self.assertEqual(lucky_sum(13, 2, 13), 0)