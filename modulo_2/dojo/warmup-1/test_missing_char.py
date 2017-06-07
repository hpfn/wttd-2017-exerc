import unittest
from missing_char import missing_char


class MissingCharTest(unittest.TestCase):
    def test_missing_char_0(self):
        self.assertEqual(missing_char('kitten', 0),'itten')

    def test_missing_char_1(self):
        self.assertEqual(missing_char('kitten', 1),'ktten')

    def test_missing_char_4(self):
        self.assertEqual(missing_char('kitten', 4),'kittn')