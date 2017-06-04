import unittest
from near_hundred import near_hundred


class NearHundredTest(unittest.TestCase):
    def test_nearhundred_100_1(self):
        self.assertTrue(near_hundred(93))

    def test_nearhundred_100_2(self):
        self.assertTrue(near_hundred(90))

    def test_nearhundred_100_3(self):
        self.assertTrue(near_hundred(110))

    def test_nearhundred_100_4(self):
        self.assertFalse(near_hundred(89))

    def test_nearhundred_100_5(self):
        self.assertFalse(near_hundred(111))

    def test_nearhundred_200_1(self):
        self.assertTrue(near_hundred(193))

    def test_nearhundred_200_2(self):
        self.assertTrue(near_hundred(209))

    def test_nearhundred_200_3(self):
        self.assertFalse(near_hundred(189))

    def test_nearhundred_200_4(self):
        self.assertFalse(near_hundred(211))
