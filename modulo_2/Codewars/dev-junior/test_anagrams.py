# coding=utf-8
from unittest import TestCase
from anagrams import anagrams


class AnagramsTest(TestCase):
    def test_anagrams(self):
        self.assertEqual(
            anagrams('abba',
                     ['aabb', 'abcd', 'bbaa', 'dada']),
            ['aabb', 'bbaa'])

    def test_anagrams_1(self):
        self.assertEqual(
            anagrams('racer',
                     ['crazer', 'carer', 'racar', 'caers', 'racer']),
            ['carer', 'racer'])

    def test_anagrams_2(self):
        self.assertEqual(
            anagrams('laser',
                     ['lazing', 'lazy',  'lacer']),
            [])
