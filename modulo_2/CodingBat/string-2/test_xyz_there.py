# coding=utf-8
from unittest import TestCase
from xyz_there import xyz_there


class XyzThereTest(TestCase):
    def test_xyzthere(self):
        self.assertTrue(xyz_there('abcxyz'))

    def test_xyzthere_1(self):
        self.assertFalse(xyz_there('abc.xyz'))

    def test_xyzthere_2(self):
        self.assertTrue(xyz_there('xyz.abc'))

    def test_xyzthere_3(self):
        self.assertTrue(xyz_there('xyz.xyz'))

