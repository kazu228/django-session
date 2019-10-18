from django.shortcuts import render
from django.http import HttpResponse
from .forms import kakikomiForm
# Create your views here.

def kakikomi(request):
    f = kakikomiForm()
    return render(request, 'djapp/index.html', {'form1': f})

