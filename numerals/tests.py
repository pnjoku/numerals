from django.test import TestCase

from .constants import ROMAN_NUMERAL_MAP
from .forms import NumeralForm


class NumeralTests(TestCase):

    def test_to_roman(self):

        for item in ROMAN_NUMERAL_MAP:
            form = NumeralForm({'n': item[1]})
            form.is_valid()
            numeral = form.to_roman()
            self.assertEqual(numeral, item[0],
                "Integer was not converted correctly. "
                "{} was expected to be {}. Instead "
                "was {}".format(
                    item[1], item[0], numeral))
