# coding=utf-8
from unittest import TestCase
from without_end import without_end


class WithoutEndTest(TestCase):
    def test_without_end(self):
        self.assertEqual(without_end('Hello'), 'ell')

    def test_without_end_1(self):
        self.assertEqual(without_end('Java'), 'av')

    def test_without_end_2(self):
        self.assertEqual(without_end('coding'), 'odin')

    def test_without_end_too_short(self):
        self.assertFalse(without_end('X'))