# coding=utf-8
from unittest import TestCase
from centered_average import centered_average



class CenteredAverageTest(TestCase):
    def test_centeredaverage(self):
        self.assertEqual(centered_average([1, 2, 3, 4, 100]), 3)

    def test_centeredaverage_1(self):
        self.assertEqual(centered_average([1, 1, 5, 5, 10, 8, 7]), 5)

    def test_centeredaverage_2(self):
        self.assertEqual(centered_average([-10, -4, -2, -4, -2, 0]), -3)