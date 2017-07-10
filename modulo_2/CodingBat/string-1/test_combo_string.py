# coding=utf-8
from unittest import TestCase
from combo_string import combo_string


class ComboStringTest(TestCase):
    def test_combo_string_same_size(self):
        self.assertFalse(combo_string('Hello', 'Hello'))

    def test_combo_string(self):
        self.assertEqual(combo_string('Hello', 'hi'), 'hiHellohi')

    def test_combo_string_1(self):
        self.assertEqual(combo_string('hi', 'Hello'), 'hiHellohi')

    def test_combo_string_2(self):
        self.assertEqual(combo_string('aaa', 'b'), 'baaab')

    def test_combo_string_3(self):
        self.assertEqual(combo_string(' ', 'hi'), ' hi ')

    def test_combo_string_4(self):
        self.assertEqual(combo_string('', 'hi'), 'hi')