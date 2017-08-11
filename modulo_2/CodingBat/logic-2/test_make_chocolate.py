# coding=utf-8
from unittest import TestCase
from make_chocolate import make_chocolate


class MakeChocolateTest(TestCase):
    def test_makechocolate(self):
        self.assertEqual(make_chocolate(4, 1, 9), 4)

    def test_makechocolate_1(self):
        self.assertEqual(make_chocolate(4, 1, 10), -1)

    def test_makechocolate_2(self):
        self.assertEqual(make_chocolate(4, 1, 7), 2)

    def test_makechocolate_3(self):
        self.assertEqual(make_chocolate(4, 2, 17), -1)

    def test_makechocolate_4(self):
        self.assertEqual(make_chocolate(2, 2, 11), 1)

    def test_makechocolate_5(self):
        self.assertEqual(make_chocolate(2, 2, 13), -1)

    # from CodingBat
    def test_makechocolate_6(self):
        self.assertEqual(make_chocolate(6, 2, 7), 2)

    def test_makechocolate_7(self):
        self.assertEqual(make_chocolate(60, 100, 550), 50)

    def test_makechocolate_8(self):
        self.assertEqual(make_chocolate(1, 2, 6), 1)

    def test_makechocolate_9(self):
        self.assertEqual(make_chocolate(1, 2, 5), 0)