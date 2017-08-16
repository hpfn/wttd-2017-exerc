# coding=utf-8
from unittest import TestCase
from end_other import end_other


class EndOtherTest(TestCase):
    def test_endother(self):
        self.assertTrue(end_other('Hiabc', 'abc'))

    def test_endother_1(self):
        self.assertTrue(end_other('AbC', 'HiaBc'))

    def test_endother_2(self):
        self.assertTrue(end_other('abc', 'abXabc'))

    def test_endother_3(self):
        self.assertFalse(end_other('Hiabx', 'abc'))

    # CondingBat
    def test_endother_4(self):
        self.assertTrue(end_other('Hiabc', 'bc'))

    def test_endother_5(self):
        self.assertTrue(end_other('Z', '12xz'))