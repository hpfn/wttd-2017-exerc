# coding=utf-8
from unittest import TestCase
from is_merge import is_merge


class IsMergeTest(TestCase):
    def test_ismerge(self):
        self.assertFalse(is_merge('codewars', 'cod', 'wars'))

    def test_ismerge_1(self):
        self.assertTrue(is_merge('codewars', 'code', 'wars'))

    def test_ismerge_2(self):
        self.assertTrue(is_merge('codewars', 'cdw', 'oears'))

    def test_ismerge_3(self):
        self.assertFalse(is_merge('codewars', 'cwd', 'oears'))

    def test_ismerge_4(self):
        self.assertFalse(is_merge('codewars', 'code', 'code'))

    def test_ismerge_5(self):
        self.assertFalse(is_merge('bananas', 'bah', 'amas'))

    def test_ismerge_6(self):
        self.assertFalse(is_merge('bahamas', 'ban', 'anas'))

    def test_ismerge_7(self):
        self.assertTrue(is_merge('bananas', 'bnns', 'aaa'))

    def test_ismerge_8(self):
        self.assertFalse(is_merge('bananas', 'bms', 'aha'))

    def test_ismerge_9(self):
        self.assertFalse(is_merge('codewars', 'code', 'wasr'))