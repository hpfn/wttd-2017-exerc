# coding=utf-8
from unittest import TestCase
from non_start import non_start


class NonStartTest(TestCase):
    def test_non_start(self):
        self.assertEqual(non_start('Hello', 'There'), 'ellohere')