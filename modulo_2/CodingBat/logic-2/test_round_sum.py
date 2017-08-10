# coding=utf-8
from unittest import TestCase
from round_sum import round_sum


class RoundSumTest(TestCase):
    def test_roundsum(self):
        self.assertEqual(round_sum(16, 17, 18), 60)

    def test_roundsum_1(self):
        self.assertEqual(round_sum(12, 13, 14), 30)

    def test_roundsum_2(self):
        self.assertEqual(round_sum(6, 4, 4), 10)

    def test_roundsum_3(self):
        self.assertEqual(round_sum(55, 14, 23), 90)


