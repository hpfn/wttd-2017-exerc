# coding=utf-8
from unittest import TestCase
from lone_sum import lone_sum



class LoneSumTest(TestCase):
    def test_lone_sum(self):
        self.assertEqual(lone_sum(1, 2, 3), 6)

    def test_lone_sum_1(self):
        self.assertEqual(lone_sum(3, 3, 3), 0)

    def test_lone_sum_2(self):
        self.assertEqual(lone_sum(2, 3, 3), 2)

    def test_lone_sum_2(self):
        self.assertEqual(lone_sum(3, 2, 3), 2)

    def test_lone_sum_3(self):
        self.assertEqual(lone_sum(3, 3, 2), 2)