# coding=utf-8
from unittest import TestCase
from make_out_word import make_out_word


class MakeOutWordTest(TestCase):
    def test_make_out_word(self):
        self.assertEqual(make_out_word('<<>>', 'Yay'), '<<Yay>>')

    def test_make_out_word_1(self):
        self.assertEqual(make_out_word('<<>>', 'WooHoo'), '<<WooHoo>>')

    def test_make_out_word_2(self):
        self.assertEqual(make_out_word('[[]]', 'word'), '[[word]]')

    def test_donot_make_out_word(self):
        self.assertFalse(make_out_word('<<<>>', 'Bad'))