# coding=utf-8
from unittest import TestCase
from make_pi import make_pi



class MakePiTest(TestCase):
    def test_make_pi(self):
        self.assertEqual(make_pi(), [3, 1, 4])