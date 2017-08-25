# coding=utf-8
from unittest import TestCase
from make_readable import make_readable


class MakeReadableTest(TestCase):
    def test_makereadable(self):
        self.assertEqual(make_readable(0), "00:00:00")

    def test_makereadable_1(self):
        self.assertEqual(make_readable(5), "00:00:05")

    def test_makereadable_2(self):
        self.assertEqual(make_readable(25), "00:00:25")

    def test_makereadable_3(self):
        self.assertEqual(make_readable(200), "00:03:20")

    def test_makereadable_4(self):
        self.assertEqual(make_readable(500), "00:08:20")

    def test_makereadable_5(self):
        self.assertEqual(make_readable(86399), "23:59:59")

    def test_makereadable_4(self):
        self.assertEqual(make_readable(359999), "99:59:59")