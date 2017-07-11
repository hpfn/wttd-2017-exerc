# coding=utf-8
from unittest import TestCase
from reverse3 import reverse3


class Reverse3Test(TestCase):
    def test_reverse3(self):
        self.assertEqual(reverse3([1, 2, 3]), [3, 2, 1])

    def test_reverse3_1(self):
        self.assertEqual(reverse3([5, 11, 9]), [9, 11, 5])

    def test_reverse3_2(self):
        self.assertEqual(reverse3([7, 0, 0]), [0, 0, 7])