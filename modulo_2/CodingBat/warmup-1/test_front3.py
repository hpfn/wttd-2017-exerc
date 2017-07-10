import unittest
from front3 import front3


class Front3Test(unittest.TestCase):
    def test_front3_0(self):
        self.assertEqual(front3('Java'), 'JavJavJav')

    def test_front3_1(self):
        self.assertEqual(front3('Chocolate'), 'ChoChoCho')

    def test_front3_2(self):
        self.assertEqual(front3('abc'), 'abcabcabc')

    def test_front3_less_then_3(self):
        self.assertEqual(front3('xy'), 'xyxyxy')

    def test_front3_less_the_2(self):
        self.assertEqual(front3('a'), 'aaa')

    def test_front3_less_then_1(self):
        self.assertEqual(front3(''), '')
