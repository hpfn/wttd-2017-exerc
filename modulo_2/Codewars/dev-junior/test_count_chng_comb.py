# coding=utf-8
from unittest import TestCase
from count_chng_comb import count_chng_comb


class CountChngCombTest(TestCase):
    def test_count_chng_comb(self):
        self.assertEqual(count_chng_comb(4, [1, 2]), 3)

    def test_count_chng_comb_1(self):
        self.assertEqual(count_chng_comb(10, [5, 2, 3]), 4)

    def test_count_chng_comb_2(self):
        self.assertEqual(count_chng_comb(11, [5, 7]), 0)

