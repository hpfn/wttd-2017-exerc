# coding=utf-8
import unittest
from string_splosion import string_splosion


class StringSplosionTest(unittest.TestCase):
    def test_string_splosion_5(self):
        self.assertEqual(string_splosion('Codare'), 'CCoCodCodaCodarCodare')

    def test_string_splosion_4(self):
        self.assertEqual(string_splosion('Code'), 'CCoCodCode')

    def test_string_splosion_3(self):
        self.assertEqual(string_splosion('abc'), 'aababc')

    def test_string_splosion_2(self):
        self.assertEqual(string_splosion('ab'), 'aab')

    def test_string_splosion_1(self):
        self.assertEqual(string_splosion('a'), 'a')