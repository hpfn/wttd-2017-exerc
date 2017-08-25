# coding=utf-8
from unittest import TestCase
from divisors import divisors


class DivisorsTest(TestCase):
    def test_divisors(self):
        self.assertEqual(divisors(15), [3, 5])

    def test_divisors_1(self):
        self.assertEqual(divisors(12), [2, 3, 4, 6])

    def test_divisors_2(self):
        self.assertEqual(divisors(13), "13 is prime")

    def test_divisors_3(self):
        self.assertEqual(divisors(25), [5])
