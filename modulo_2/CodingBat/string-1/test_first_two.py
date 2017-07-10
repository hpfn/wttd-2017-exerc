# coding=utf-8
from unittest import TestCase
from first_two import first_two


class FirstTwoTest(TestCase):
    def test_first_two_none(self):
        self.assertEqual(first_two(''), '')

    def test_first_two_single(self):
        self.assertEqual(first_two('X'), 'X')

    def test_first_two(self):
        self.assertEqual(first_two('Hello'), 'He')

