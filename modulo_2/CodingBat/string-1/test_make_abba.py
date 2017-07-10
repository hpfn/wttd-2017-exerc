# coding=utf-8
import unittest
from make_abba import make_abba


class MakeAbbaTest(unittest.TestCase):
    def test_make_abba(self):
        self.assertEqual(make_abba('Hi', 'Bye'), 'HiByeByeHi')

    def test_make_abba_1(self):
        self.assertEqual(make_abba('Yo', 'Alice'), 'YoAliceAliceYo')