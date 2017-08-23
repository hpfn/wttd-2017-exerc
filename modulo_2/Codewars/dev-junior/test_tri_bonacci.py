# coding=utf-8
from unittest import TestCase
from tri_bonacci import tri_bonacci



class TriBonacciTest(TestCase):
    def test_tribonicci(self):
        self.assertEqual(tri_bonacci([1, 1, 1], 10),
                         [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])

    def test_tribonacci_1(self):
        self.assertEqual(tri_bonacci([0, 0, 1],10),
                         [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])

    def test_tribonacci_2(self):
        self.assertEqual(tri_bonacci([0, 1, 1], 10),
                         [0, 1, 1, 2, 4, 7, 13, 24, 44, 81])

    def test_tribonacci_3(self):
        self.assertEqual(tri_bonacci([1, 1, 1], 1),
                         [1])

    def test_tribonacci_4(self):
        self.assertEqual(tri_bonacci([300, 200, 100], 0),
                         [])
