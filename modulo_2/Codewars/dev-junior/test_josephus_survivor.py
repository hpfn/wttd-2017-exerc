# coding=utf-8
from unittest import TestCase
from josephus_survivor import josephus_survivor



class JosephusSurvivorTest(TestCase):
    def test_josephussurvivor(self):
        self.assertEqual(josephus_survivor(7, 3), 4)

    def test_josephussurvivor_1(self):
        self.assertEqual(josephus_survivor(11, 19), 10)

    def test_josephussurvivor_2(self):
        self.assertEqual(josephus_survivor(1, 300), 1)

    def test_josephussurvivor_3(self):
        self.assertEqual(josephus_survivor(14, 2), 13)

    def test_josephussurvivor_4(self):
        self.assertEqual(josephus_survivor(100, 1), 100)