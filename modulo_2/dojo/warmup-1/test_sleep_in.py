import unittest
from sleep_in import sleep_in

class SleepInTest(unittest.TestCase):
    def test_both_false(self):
        self.assertTrue(sleep_in(False, False))

    def test_both_true(self):
        self.assertTrue(sleep_in(True, True))

    def test_true_false(self):
        self.assertFalse(sleep_in(True, False))

    def test_false_true(self):
        self.assertTrue(sleep_in(False, True))
