import unittest
from same_first_last import same_first_last

class MyTestCase(unittest.TestCase):
    def test_same_first_last(self):
        self.assertFalse(same_first_last([1, 2, 3]))

    def test_same_first_last_1(self):
        self.assertTrue(same_first_last([1, 2, 3, 1]))

    def test_same_first_last_2(self):
        self.assertTrue(same_first_last([1, 2, 1]))

