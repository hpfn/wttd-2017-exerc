# coding=utf-8
from unittest import TestCase
from comp import comp


class CompTest(TestCase):
    def test_comp(self):
        array1 = [121, 144, 19, 161, 19, 144, 19, 11]
        array2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
        self.assertTrue(comp(array1, array2))

    def test_comp_1(self):
        array1 = [121, 144, 19, 161, 19, 144, 19, 11]
        array2 = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
        self.assertFalse(comp(array1, array2))

    def test_comp_2(self):
        array1 = 1
        array2 = [1, 2, 3]
        self.assertFalse(comp(array1, array2))
