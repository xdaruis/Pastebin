from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import textForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def add(request):
    form = textForm
    if request.method == 'POST':
        form = textForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/history')
    return render(request, 'add.html', {'form': form})

def history(request):
    pastebins = text.objects.all()
    return render(request, 'history.html', {'pastebins': pastebins})

def displayContent(request, text_id):
    actPastebin = text.objects.get(pk=text_id)
    return render(request, 'displayContent.html', {'actPastebin': actPastebin}) 
