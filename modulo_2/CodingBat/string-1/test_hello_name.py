# coding=utf-8
import unittest
from hello_name import hello_name


class HelloNameTest(unittest.TestCase):
    def test_hello_name(self):
        self.assertEqual(hello_name('Bob'), 'Hello Bob!')
