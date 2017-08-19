# coding=utf-8
from unittest import TestCase
from find_short import find_short


class FindShortTest(TestCase):
    def test_find_short(self):
        self.assertEqual(find_short("bitcoin take over the world maybe who knows perhaps"), 3)