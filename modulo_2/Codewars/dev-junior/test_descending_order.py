# coding=utf-8
from unittest import TestCase
from .descending_order import descending_order


class DescendingOrderTest(TestCase):
    def test_descending_order(self):
        self.assertEqual(descending_order(21445), 54421)

    def test_descending_order_1(self):
        self.assertEqual(descending_order(145263), 654321)

    def test_descending_order_2(self):
        self.assertEqual(descending_order(1254859723), 9875543221)



