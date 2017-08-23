# coding=utf-8
from unittest import TestCase
from thue_morse import thue_morse


class ThueMorseTest(TestCase):
    def test_thuemorse(self):
        self.assertEqual(thue_morse(1), '0')

    def test_thuemorse_1(self):
        self.assertEqual(thue_morse(2), '01')

    def test_thuemorse_2(self):
        self.assertEqual(thue_morse(5), '01101')

    def test_thuemorse_3(self):
        self.assertEqual(thue_morse(10),
                         "0110100110")

    def test_thuemorse_4(self):
        self.assertEqual(thue_morse(100),
                         "0110100110010110100101100110100110010110011010010110100110010110100101100110100101101001100101100110")

