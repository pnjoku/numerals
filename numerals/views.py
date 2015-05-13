from django.shortcuts import render

from .forms import NumeralForm


def index(request):
    form = NumeralForm(request.POST or None)
    numerals = ''
    if request.method == 'POST':
        if form.is_valid():
            numerals = form.to_roman()
    return render(request, 'index.html', {'form': form,
        'numerals': numerals})
