# coding=utf-8
from unittest import TestCase
from middle_way import middle_way


class MiddleWayTest(TestCase):
    def test_middleway(self):
        self.assertEqual(middle_way([1, 2, 3], [4, 5, 6]), [2, 5])