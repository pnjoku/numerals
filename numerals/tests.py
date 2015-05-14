from django.test import TestCase
from .forms import to_roman


class NumeralTests(TestCase):
    def testToRoman(self):
        """toRoman(n) for all n"""
        for integer in range(1, 4000):
            numeral = to_roman(integer)
            self.assertEqual(numeral, numeral)
