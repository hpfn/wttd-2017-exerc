# coding=utf-8
from unittest import TestCase
from count_hi import count_hi


class CountHiTest(TestCase):
    def test_count_hi(self):
        self.assertEqual(count_hi('abc hi ho'), 1)

    def test_count_hi_1(self):
        self.assertEqual(count_hi('ABChi hi'), 2)

    def test_count_hi_2(self):
        self.assertEqual(count_hi('hihi'), 2)