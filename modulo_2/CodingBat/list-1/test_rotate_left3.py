# coding=utf-8
from unittest import TestCase
from rotate_left3 import rotate_left3


class RotateLeft3Test(TestCase):
    def test_rotateleft3(self):
        self.assertEqual(rotate_left3([1, 2, 3]), [2, 3, 1])

    def test_rotateleft3_1(self):
        self.assertEqual(rotate_left3([5, 11, 9]), [11, 9, 5])

    def test_rotateleft3_2(self):
        self.assertEqual(rotate_left3([7, 0, 0]), [0, 0, 7])