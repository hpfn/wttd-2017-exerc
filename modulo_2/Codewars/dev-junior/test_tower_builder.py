# coding=utf-8
from unittest import TestCase
from tower_builder import tower_builder



class TowerBuilderTest(TestCase):
    def test_towerbuilder(self):
        self.assertEqual(tower_builder(1), ['*', ])

    def test_towerbuilder_2(self):
        self.assertEqual(tower_builder(2), [' * ', '***'])

    def test_towerbuilder_3(self):
        self.assertEqual(tower_builder(3), ['  *  ', ' *** ', '*****'])

    def test_towerbuilder_4(self):
        self.assertEqual(tower_builder(6),
                         [
                             '     *     ',
                             '    ***    ',
                             '   *****   ',
                             '  *******  ',
                             ' ********* ',
                             '***********'
                         ])