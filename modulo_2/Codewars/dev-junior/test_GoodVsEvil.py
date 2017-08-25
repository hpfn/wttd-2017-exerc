# coding=utf-8
from unittest import TestCase
from GoodVsEvil import GoodVsEvil


class GoodVsEvilTest(TestCase):
    def test_goodvsevil(self):
        self.assertEqual(
            GoodVsEvil(
                '1 1 1 1 1 1', '1 1 1 1 1 1 1'),
        "Battle Result: Evil eradicates all trace of Good" )

    def test_goodvsevil_1(self):
        self.assertEqual(
            GoodVsEvil(
                '0 0 0 0 0 10', '0 1 1 1 1 0 0'),
            "Battle Result: Good triumphs over Evil")

    def test_goodvsevil_2(self):
        self.assertEqual(
            GoodVsEvil(
                '1 0 0 0 0 0', '1 0 0 0 0 0'),
            "Battle Result: No victor on this battle field")
