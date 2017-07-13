# coding=utf-8
from unittest import TestCase
from date_fashion import date_fashion

# two tests were missing
class DateFashionTest(TestCase):
    def test_df(self):
        self.assertEqual(date_fashion(5, 10), 2)

    def test_df_limit(self):
        self.assertEqual(date_fashion(8, 5), 2)

    def test_df_no(self):
        self.assertEqual(date_fashion(5, 2), 0)

    def test_df_maybe(self):
        self.assertEqual(date_fashion(5, 5), 1)

    def test_df_extrems(self):
        self.assertEqual(date_fashion(2, 10), 0)

    def test_df_extrems_1(self):
        self.assertEqual(date_fashion(10, 2), 0)