from forms import NumeralForm
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext


def index(request):
    if request.method == 'POST':
        form = NumeralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('questions')
    else:
        form = NumeralForm()
    return render_to_response('template/index.html', {'form': form}, context_instance=RequestContext(request))
