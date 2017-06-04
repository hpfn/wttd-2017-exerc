# coding=utf-8
import unittest
from .parrot_trouble import parrot_trouble


class ParrotTroubleTest(unittest.TestCase):
    def test_trouble_in_6_talk(self):
        self.assertTrue(parrot_trouble(True, 6))

    def test_trouble_in_6_not_talk(self):
        self.assertFalse(parrot_trouble(False, 6))

    def test_trouble_in_7_talk(self):
        self.assertFalse(parrot_trouble(True, 7))

    def test_trouble_in_7_not_talk(self):
        self.assertFalse(parrot_trouble(False, 7))

    def test_trouble_in_20_talk(self):
        self.assertFalse(parrot_trouble(True, 20))

    def test_trouble_in_20_not_talk(self):
        self.assertFalse(parrot_trouble(False, 20))

    def test_trouble_in_21_talk(self):
        self.assertTrue(parrot_trouble(True, 21))

    def test_trouble_in_21_not_talk(self):
        self.assertFalse(parrot_trouble(False, 21))
