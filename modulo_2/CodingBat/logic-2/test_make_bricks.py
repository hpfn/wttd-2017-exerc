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

    def test_make_bricks_11(self):
        self.assertTrue(make_bricks(3, 2, 8))

    def test_make_bricks_12(self):
        self.assertFalse(make_bricks(3, 2, 9))

    def test_makebricks(self):
        self.assertTrue(make_bricks(3, 1, 8))

    def test_makebricks_1(self):
        self.assertFalse(make_bricks(3, 1, 9))

    def test_makebricks_2(self):
        self.assertTrue(make_bricks(3, 2, 10))

    def test_makebricks_3(self):
        self.assertTrue(make_bricks(3, 2, 8))

    def test_makebricks_4(self):
        self.assertFalse(make_bricks(3, 2, 9))

    def test_makebricks_5(self):
        self.assertTrue(make_bricks(6, 1, 11))

    def test_makebricks_6(self):
        self.assertFalse(make_bricks(6, 0, 11))

    def test_makebricks_7(self):
        self.assertTrue(make_bricks(1, 4, 11))

    def test_makebricks_8(self):
        self.assertTrue(make_bricks(0, 3, 10))

    def test_makebricks_9(self):
        self.assertFalse(make_bricks(1, 4, 12))

    def test_makebricks_10(self):
        self.assertTrue(make_bricks(3, 1, 7))

    def test_makebricks_11(self):
        self.assertFalse(make_bricks(1, 1, 7))

    def test_makebricks_12(self):
        self.assertTrue(make_bricks(2, 1, 7))

    def test_makebricks_13(self):
        self.assertTrue(make_bricks(7, 1, 11))

    def test_makebricks_14(self):
        self.assertTrue(make_bricks(7, 1, 8))

    def test_makebricks_15(self):
        self.assertFalse(make_bricks(7, 1, 13))

    def test_makebricks_16(self):
        self.assertTrue(make_bricks(43, 1, 46))

    def test_makebricks_17(self):
        self.assertFalse(make_bricks(40, 1, 46))

    def test_makebricks_18(self):
        self.assertTrue(make_bricks(40, 2, 47))

    def test_makebricks_19(self):
        self.assertTrue(make_bricks(40, 2, 50))

    def test_makebricks_20(self):
        self.assertFalse(make_bricks(40, 2, 52))

    def test_makebricks_21(self):
        self.assertFalse(make_bricks(22, 2, 33))

    def test_makebricks_22(self):
        self.assertTrue(make_bricks(0, 2, 10))

    def test_makebricks_23(self):
        self.assertTrue(make_bricks(1000000, 1000, 1000100))

    def test_makebricks_24(self):
        self.assertFalse(make_bricks(2, 1000000, 100003))

    def test_makebricks_25(self):
        self.assertTrue(make_bricks(20, 0, 19))

    def test_makebricks_26(self):
        self.assertFalse(make_bricks(20, 0, 21))

    def test_makebricks_27(self):
        self.assertFalse(make_bricks(20, 4, 51))

    def test_makebricks_28(self):
        self.assertTrue(make_bricks(20, 4, 39))

