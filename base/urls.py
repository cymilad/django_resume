from django.urls import path
from base.views import *

urlpatterns = [
    path('', index, name='index'),
]