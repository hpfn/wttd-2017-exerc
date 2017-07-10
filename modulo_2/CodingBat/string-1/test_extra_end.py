# coding=utf-8
from unittest import TestCase
from extra_end import extra_end


class ExtraEndTest(TestCase):
    def test_extra_end(self):
        self.assertEqual(extra_end('Hello'), 'lololo')

    def test_extra_end_1(self):
        self.assertEqual(extra_end('ab'), 'ababab')

    def test_extra_end_fail(self):
        self.assertFalse(extra_end('H'))