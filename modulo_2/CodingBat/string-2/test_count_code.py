# coding=utf-8
from unittest import TestCase
from count_code import count_code



class CountCodeTest(TestCase):
    def test_countcode(self):
        self.assertEqual(count_code('aaacodebbb'), 1)

    def test_countcode_1(self):
        self.assertEqual(count_code('codexxcode'), 2)

    def test_countcode_2(self):
        self.assertEqual(count_code('cozexxcope'), 2)

    def test_countcode_3(self):
        self.assertEqual(count_code('cddexxcpde'), 0)

    def test_countcode_4(self):
        self.assertEqual(count_code('cppexxco'), 0)

    def test_countcode_5(self):
        self.assertEqual(count_code('codexxcod'), 1)

    def test_countcode_6(self):
        self.assertEqual(count_code('codecopecode'), 3)

    # CodingBat
    def test_countcode_7(self):
        self.assertEqual(count_code('xxcozeyycop'), 1)