# coding=utf-8
import unittest
from last2 import last2


class Last2Test(unittest.TestCase):
    def test_last2_0(self):
        self.assertEqual(last2('ixx'), 0)

    def test_last2_0_again(self):
        self.assertEqual(last2('iab'), 0)

    def test_last2_1(self):
        self.assertEqual(last2('hixxhi'), 1)

    def test_last2_1_again(self):
        self.assertEqual(last2('xaxxaxaxx'), 1)

    def test_last2_2(self):
        self.assertEqual(last2('axxxaaxx'), 2)

    def test_last2_2_again(self):
        self.assertEqual(last2('abxxabaab'), 2)

    def test_last2_2_missing(self):
        self.assertEqual(last2('xxxx'), 2)

    def test_last2_3(self):
        self.assertEqual(last2('xabxxabxabxab'), 3)

