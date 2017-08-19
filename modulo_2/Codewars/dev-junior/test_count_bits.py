# coding=utf-8
from unittest import TestCase
from count_bits import count_bits


class CountBitsTest(TestCase):
    def test_count_bits(self):
        self.assertEqual(count_bits(1234), 5)

    def test_count_bits_1(self):
        self.assertEqual(count_bits(4), 1)

    def test_count_bits_2(self):
        self.assertEqual(count_bits(0), 0)

    def test_count_bits_3(self):
        self.assertEqual(count_bits(7), 3)