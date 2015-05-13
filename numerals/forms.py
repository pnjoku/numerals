from django import forms


class NumeralForm(forms.Form):
    n = forms.IntegerField(min_value=1, max_value=3999)

    ROMAN_NUMERAL_MAP = (
        ('M',  1000),
        ('CM', 900),
        ('D',  500),
        ('CD', 400),
        ('C',  100),
        ('XC', 90),
        ('L',  50),
        ('XL', 40),
        ('X',  10),
        ('IX', 9),
        ('V',  5),
        ('IV', 4),
        ('I',  1)
    )

    def to_roman(self):
        """convert integer to Roman numeral"""

        n = self.cleaned_data.get('n')

        result = ""
        for numeral, integer in self.ROMAN_NUMERAL_MAP:
            while n >= integer:
                result += numeral
                n -= integer
        return result
