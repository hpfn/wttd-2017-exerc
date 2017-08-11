# coding=utf-8
from unittest import TestCase
from close_far import close_far


class CloseFarTest(TestCase):
    def test_closefar_a(self):
        self.assertTrue(close_far(1, 4, 3))

    def test_closefar_b(self):
        self.assertTrue(close_far(1, 4, 2))

    def test_closefar_c(self):
        self.assertTrue(close_far(1, 2, 10))

    def test_closefar(self):
        self.assertFalse(close_far(1, 2, 3))

    def test_closefar(self):
        self.assertTrue(close_far(1, 1, 3))