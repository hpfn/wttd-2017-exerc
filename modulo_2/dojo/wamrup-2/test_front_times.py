# coding=utf-8
import unittest
from front_times import front_times


class FrontTimeTest(unittest.TestCase):
    def test_front_times_0(self):
        self.assertEqual(front_times('Java', 0), '')

    def test_front_times_1(self):
        self.assertEqual(front_times('Chocolate', 1), 'Cho')

    def test_front_times_2(self):
        self.assertEqual(front_times('abc', 2), 'abcabc')

    def test_front_times_less_then_3(self):
        self.assertEqual(front_times('xy', 3), 'xyxyxy')

    def test_front_times_less_then_0(self):
        self.assertEqual(front_times('a', -1), 'not a valid number')
