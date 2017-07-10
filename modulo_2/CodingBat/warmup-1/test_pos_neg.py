import unittest
from pos_neg import pos_neg

# not enough tests
class PosNegTest(unittest.TestCase):
    def test_pos_first_false(self):
        self.assertTrue(pos_neg(1, -1, False))

    def test_neg_first_false(self):
        self.assertTrue(pos_neg(-1, 1, False))

    def test_neg_pos_true(self):
        self.assertFalse(pos_neg(-1, 1, True))

    def test_pos_neg_true(self):
        self.assertFalse(pos_neg(1, -1, True))

    def test_neg_neg_true(self):
        self.assertTrue(pos_neg(-1, -1, True))

    def test_neg_neg_false(self):
        self.assertFalse(pos_neg(-1, -1, False))

    def test_pos_pos_true(self):
        self.assertFalse(pos_neg(1, 1, True))

    def test_pos_pos_false(self):
        self.assertFalse(pos_neg(1, 1, False))