# coding=utf-8
from unittest import TestCase
from caught_speeding import caught_speeding


class CaughtSpeedingTest(TestCase):
    def test_caught_speeding(self):
        self.assertEqual(caught_speeding(60, False), 0)

    def test_caught_speeding_1(self):
        self.assertEqual(caught_speeding(65, False), 1)

    def test_caught_speeding_2(self):
        self.assertEqual(caught_speeding(81, False), 2)

    def test_caught_speeding_birth(self):
        self.assertEqual(caught_speeding(65, True), 0)

    def test_caught_speeding_birth_1(self):
        self.assertEqual(caught_speeding(81, True), 1)

    def test_caught_speeding_birth_2(self):
        self.assertEqual(caught_speeding(86, True), 2)