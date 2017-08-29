# coding=utf-8
from unittest import TestCase
from scramblies import scramblies


class ScrambliesTest(TestCase):
    def test_scramblies(self):
        self.assertTrue(scramblies('rkqodlw', 'world'))

    def test_scramblies_1(self):
        self.assertTrue(scramblies('cedewaraaossoqqyt','codewars'))

    def test_scramblies_2(self):
        self.assertFalse(scramblies('katas', 'steak'))

    def test_scramblies_3(self):
        self.assertTrue(scramblies('scriptjava','javascript'))

    def test_scramblies_4(self):
        self.assertTrue(scramblies('scriptingjava','javascript'))

    def test_scramblies_5(self):
        self.assertFalse(scramblies('scriptingjava','blablabla'))