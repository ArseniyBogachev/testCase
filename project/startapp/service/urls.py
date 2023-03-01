from django.urls import path, re_path
from .views import *


urlpatterns = [
    # path(r'<slug:url>/', home, name='base'),
    path(r'', home, name='base'),
    path(r'<slug:url>/<slug:btn>/', home, name='btn')
]