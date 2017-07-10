# coding=utf-8
from unittest import TestCase
from left2 import left2


class Left2Test(TestCase):
    def test_left2(self):
        self.assertEqual(left2('Hello'), 'lloHe')

    def test_left2_1(self):
        self.assertEqual(left2('java'), 'vaja')

    def test_left2_2(self):
        self.assertEqual(left2('Hi'), 'Hi')