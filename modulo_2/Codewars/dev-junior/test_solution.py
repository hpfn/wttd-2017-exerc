# coding=utf-8
from unittest import TestCase
from solution import solution


class SolutionTest(TestCase):
    def test_solution(self):
        self.assertEqual(
            solution("asdfadsf"),
            ['as', 'df', 'ad', 'sf'])

    def test_solution_1(self):
        self.assertEqual(
            solution("asdfads"),
            ['as', 'df', 'ad', 's_'])

    def test_solution_2(self):
        self.assertEqual(
            solution(""),
            [])

    def test_solution_3(self):
        self.assertEqual(
            solution("x"),
            ["x_"])
