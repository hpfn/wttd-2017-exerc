# coding=utf-8
from unittest import TestCase
from make_ends import make_ends


class MakeEndsTest(TestCase):
    def test_makeends(self):
        self.assertEqual(make_ends([1, 2, 3]), [1, 3])

    def test_makeends_1(self):
        self.assertEqual(make_ends([1, 2, 3, 4]), [1, 4])

    def test_makeends_2(self):
        self.assertEqual(make_ends([7, 4, 6, 2]), [7, 2])

    def test_makeends_3(self):
        self.assertEqual(make_ends([1]), [1, 1])