# coding=utf-8
from unittest import TestCase
from common_end import common_end


class CommonEndTest(TestCase):
    def test_commonend(self):
        self.assertTrue(common_end([1, 2, 3], [7, 3]))

    def test_commonend_1(self):
        self.assertFalse(common_end([1, 2, 3], [7, 3, 2]))

    def test_commonend_2(self):
        self.assertTrue(common_end([1, 2, 3], [1, 3]))