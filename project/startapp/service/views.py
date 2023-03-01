from django.db.models import Count
from django.http import Http404
from django.shortcuts import render
from .models import *


def home(request, url=None, btn=None):
    return render(request, 'home.html', {'url': url, 'btn': btn})
# Create your views here.
