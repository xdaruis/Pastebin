from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import textForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def add(request):
    submitted = False
    if request.method == 'POST':
        form = textForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect('/add?submitted=True')
            return HttpResponseRedirect('/history')
    else:
        form = textForm
        if submitted in request.GET:
            submitted = True
    # context = {'form': form, 'submitted': submitted}
    return render(request, 'add.html', {'form': form, 'submitted': submitted})

def history(request):
    pastebins = text.objects.all()
    return render(request, 'history.html', {'pastebins': pastebins})