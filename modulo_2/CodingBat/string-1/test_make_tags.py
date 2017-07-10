# coding=utf-8
import unittest
from make_tags import make_tags


class MakeTagsTest(unittest.TestCase):
    def test_make_tags(self):
        self.assertEqual(make_tags('i', 'Yay'), '<i>Yay</i>')

    def test_make_tags_1(self):
        self.assertEqual(make_tags('i', 'Hello'), '<i>Hello</i>')

    def test_make_tags2(self):
        self.assertEqual(make_tags('cite', 'Yay'), '<cite>Yay</cite>')