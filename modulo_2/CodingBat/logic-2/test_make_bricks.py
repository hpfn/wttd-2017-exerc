# coding=utf-8
from unittest import TestCase
from make_bricks import make_bricks


class MakeBricksTest(TestCase):
    def test_make_bricks(self):
        self.assertTrue(make_bricks(3, 1, 8))

    def test_make_bricks_1(self):
        self.assertFalse(make_bricks(3, 1, 9))

    def test_make_bricks_2(self):
        self.assertTrue(make_bricks(3, 2, 10))

    def test_make_bricks_3(self):
        self.assertTrue(make_bricks(10, 0, 10))

    def test_make_bricks_4(self):
        self.assertTrue(make_bricks(4, 5, 18))

    def test_make_bricks_5(self):
        self.assertTrue(make_bricks(3, 2, 8))

    def test_make_bricks_6(self):
        self.assertTrue(make_bricks(1, 4, 11))

    def test_make_bricks_7(self):
        self.assertTrue(make_bricks(7, 1, 8))

    def test_make_bricks_8(self):
        self.assertFalse(make_bricks(40, 2, 52))

    def test_make_bricks_9(self):
        self.assertTrue(make_bricks(0, 2, 10))

    def test_make_bricks_10(self):
        self.assertTrue(make_bricks(40, 2, 47))