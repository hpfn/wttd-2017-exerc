import unittest
from not_string import not_string


class NotStringTest(unittest.TestCase):
    def test_begin_not(self):
        self.assertRegex(not_string('not bad'), '^not')

    def test_begin_without_not(self):
        self.assertRegex(not_string('candy'), '^not')