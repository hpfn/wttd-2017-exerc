# coding=utf-8
from unittest import TestCase
from title_case import title_case

# from Codewars
class TitleCaseTest(TestCase):
    def test_titlecase(self):
        self.assertEqual(title_case('the quick brown fox'), 'The Quick Brown Fox')

    def test_titlecase_1(self):
        self.assertEqual(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')

    def test_titlecase_2(self):
        self.assertEqual(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')

    def test_titlecase_3(self):
        self.assertEqual(title_case(''), '')

    def test_titlecase_4(self):
        self.assertEqual(title_case('First a of in', 'an often into'), 'First A Of In')
