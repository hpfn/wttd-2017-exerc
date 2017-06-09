import unittest
from string_times import string_times


class StringTimesTest(unittest.TestCase):
    def test_string_times_0(self):
        self.assertEqual(string_times('Hi', 0), '')

    def test_string_times_1(self):
        self.assertEqual(string_times('Hi', 1), 'Hi')

    def test_string_times_2(self):
        self.assertEqual(string_times('Hi', 2), 'HiHi')

    def test_string_times_3(self):
        self.assertEqual(string_times('Hi', 3), 'HiHiHi')

    def test_string_times_neg(self):
        self.assertEqual(string_times('Hi', -1), 'not a valid number')

    def test_string_times_null(self):
        self.assertEqual(string_times('', 4), '')


