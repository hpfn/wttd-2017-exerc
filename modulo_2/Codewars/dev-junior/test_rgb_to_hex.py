# coding=utf-8
from unittest import TestCase
from rgb_to_hex import rgb_to_hex


class RgbToHexTest(TestCase):
    def test_rgb_to_hex(self):
        self.assertEqual(rgb_to_hex(255, 255, 255), 'FFFFFF')

    def test_rgb_to_hex_1(self):
        self.assertEqual(rgb_to_hex(0, 0, 0), "000000")

    def test_rgb_to_hex_2(self):
        self.assertEqual(rgb_to_hex(1, 2, 3), "010203")

    def test_rgb_to_hex_3(self):
        self.assertEqual(rgb_to_hex(254, 253, 252), "FEFDFC")

    def test_rgb_to_hex_4(self):
        self.assertEqual(rgb_to_hex(-20,275,125), "00FF7D")