# coding=utf-8
from unittest import TestCase
from no_teen_sum import no_teen_sum


# my tests did not cover the whole picture
class NoTeenSumTest(TestCase):
    def test_noteensum(self):
        self.assertEqual(no_teen_sum(1, 2, 3), 6)

    def test_noteensum_1(self):
        self.assertEqual(no_teen_sum(2, 13, 1), 3)

    def test_noteensum_2(self):
        self.assertEqual(no_teen_sum(15, 13, 1), 16)

    def test_noteensum_3(self):
        self.assertEqual(no_teen_sum(2, 1, 14), 3)

    def test_noteensum_4(self):
        self.assertEqual(no_teen_sum(17, 18, 19), 0)

    def test_noteensum_5(self):
        self.assertEqual(no_teen_sum(5, 17, 18), 5)