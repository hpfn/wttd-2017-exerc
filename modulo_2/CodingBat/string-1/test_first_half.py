# coding=utf-8
from unittest import TestCase
from first_half import first_half


class FirstHalfTest(TestCase):
    def test_firsthalf_even(self):
        self.assertEqual(first_half('WooHoo'), 'Woo')

    def test_firsthalf_odd(self):
        self.assertEqual(first_half('WooHooT'), 'Woo')

    def test_first_half_too_short(self):
        self.assertFalse(first_half('X'))

    def test_first_half_space(self):
        self.assertEqual(first_half(' H'), ' ')

    def test_first_half_sinlge(self):
        self.assertEqual(first_half('H '), 'H')