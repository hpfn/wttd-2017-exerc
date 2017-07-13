# coding=utf-8
from unittest import TestCase
from cigar_party import cigar_party

# two tests were missing
class CigarPartyTest(TestCase):
    def test_cigarparty_no_wk_default(self):
        self.assertTrue(cigar_party(60, False))

    def test_cigarparty_no_wk_default_1(self):
        self.assertTrue(cigar_party(40, False))

    def test_cigarparty_wk_ok(self):
        self.assertTrue(cigar_party(50, True))

    def test_cigarparty_no_wk(self):
        self.assertTrue(cigar_party(50, False))

    def test_cigarparty_wk_ok_1(self):
        self.assertTrue(cigar_party(70, True))

    def test_cigarparty_wk_fail(self):
        self.assertFalse(cigar_party(30, True))

    def test_cigarparty_no_wk_1(self):
        self.assertFalse(cigar_party(30, False))

    def test_cigarparty_no_wk_fail_1(self):
        self.assertFalse(cigar_party(65, False))