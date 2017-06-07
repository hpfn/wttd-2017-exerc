import unittest
from front_back import front_back


class FrontBackTest(unittest.TestCase):
    def test_front_back_0(self):
        self.assertEqual(front_back('code'), 'eodc')

    def test_front_back_1(self):
        self.assertEqual(front_back('a'), 'a')

    def test_front_back_2(self):
        self.assertEqual(front_back('od'), 'do')

    def test_front_back_empty(self):
        self.assertEqual(front_back(''), '')