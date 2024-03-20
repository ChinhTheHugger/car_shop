from django.contrib import admin
from django.urls import path

from views.home import homepage

urlpatterns = [
    path('', homepage, name='homepage'),
    path('homepage', homepage, name='homepage'),
]
