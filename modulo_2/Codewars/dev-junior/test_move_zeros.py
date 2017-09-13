# coding=utf-8
from unittest import TestCase
from move_zeros import move_zeros


class MoveZerosTest(TestCase):
    def test_movezeros(self):
        self.assertEqual(move_zeros([]), [])

    def test_movezeros_1(self):
        self.assertEqual(move_zeros([0]), [0])

    def test_movezeros_2(self):
        self.assertEqual(move_zeros([0, 0]), [0, 0])

    def test_movezeros_3(self):
        self.assertEqual(move_zeros(['a']), ['a'])

    def test_movezeros_4(self):
        self.assertEqual(move_zeros(['a', 'b']), ['a', 'b'])

    def test_movezeros_5(self):
        self.assertEqual(move_zeros([0, 1, None, 2, False, 1, 0]),
                         [1, None, 2, False, 1, 0, 0])

    def test_movezeros_6(self):
        self.assertEqual(move_zeros(
            ["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]),
            ["a", "b", None, "c", "d", 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


    def test_movezeros_7(self):
        self.assertEqual(move_zeros(
            [9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])