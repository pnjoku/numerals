from django import forms

from .constants import ROMAN_NUMERAL_MAP


class NumeralForm(forms.Form):
    n = forms.IntegerField(min_value=1, max_value=3999)

    def to_roman(self):
        """convert integer to Roman numeral"""

        n = self.cleaned_data.get('n')

        result = ""
        for numeral, integer in ROMAN_NUMERAL_MAP:
            while n >= integer:
                result += numeral
                n -= integer
        return result
