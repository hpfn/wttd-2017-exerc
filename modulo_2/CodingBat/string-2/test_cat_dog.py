# coding=utf-8
from unittest import TestCase
from cat_dog import cat_dog


class CatDogTest(TestCase):
    def test_cat_dog(self):
        self.assertTrue(cat_dog('catdog'))

    def test_cat_dog_1(self):
        self.assertFalse(cat_dog('catcat'))

    def test_cat_dog_2(self):
        self.assertTrue(cat_dog('1cat1cadodog'))

    def test_cat_dog_3(self):
        self.assertTrue(cat_dog('dogdogcacatcat cat dog'))
