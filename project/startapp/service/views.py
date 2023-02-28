from django.http import Http404
from django.shortcuts import render
from .models import *


def home(request, pk):
    model = ParentMenu.objects.filter(children=pk)

    if not model:
        raise Http404
    return render(request, 'home.html', {'menu': model})
# Create your views here.
