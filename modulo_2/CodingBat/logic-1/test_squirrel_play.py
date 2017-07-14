# coding=utf-8
from unittest import TestCase
from squirrel_play import squirrel_play


class SquirrelPlayTest(TestCase):
    def test_squirrelplay_no_sun(self):
        self.assertTrue(squirrel_play(70, False))

    def test_squirrelplay_sun(self):
        self.assertTrue(squirrel_play(95, True))

    def test_squirrelplay_no_sun_up(self):
        self.assertFalse(squirrel_play(95, False))

    def test_squirrelplay_no_sun_low(self):
        self.assertFalse(squirrel_play(55, False))