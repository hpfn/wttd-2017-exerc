# coding=utf-8
from unittest import TestCase
from .small_int import small_int



class SmallIntTest(TestCase):
    def test_small_int(self):
        self.assertEqual(small_int([78,56,232,12,11,43]), 11)

    def test_small_int_1(self):
        self.assertEqual(small_int([78,56,-2,12,8,-33]), -33)