from Bonus import*
from unittest import TestCase

class TestSyracuse(TestCase):
    """We test some / all the functions in the Bonus.py file"""

    def test_tempsdevol(self):
        """Does entering 14 as arg gve me 52 as expected ?"""
        test_value = tempsdevol(14)
        self.assertEqual(test_value, 52)
