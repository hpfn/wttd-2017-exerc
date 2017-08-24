# coding=utf-8
from unittest import TestCase
from find_even_array import find_even_index


class FindEvenArrayTest(TestCase):
    def test_findevenarray(self):
        self.assertEqual(find_even_index(
            [1, 2, 3, 4, 3, 2, 1]), 3)

    def test_findevenarray_1(self):
        self.assertEqual(find_even_index(
            [1, 100, 50, -51, 1, 1]), 1)

    def test_findevenarray_2(self):
        self.assertEqual(find_even_index(
            [1, 2, 3, 4, 5, 6]), -1)

    def test_findevenarray_3(self):
        self.assertEqual(find_even_index(
            [20, 10, -80, 10, 10, 15, 35]), 0)

    def test_findevenarray_4(self):
        self.assertEqual(find_even_index(
            [0, 0, 0, 0, 0]), 0)

