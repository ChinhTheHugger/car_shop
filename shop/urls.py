from django.contrib import admin
from django.urls import path

from .views.home import homepage
from .views.carinfo import get_car
from .views.brandinfo import get_brand
from .views.category import category

urlpatterns = [
    path('', homepage, name='homepage'),
    path('homepage', homepage, name='homepage'),
    
    path('carinfo/<slug:brand>_<slug:model>_<slug:year>', get_car, name='get-car'),
    
    path('brandinfo/<slug:name>', get_brand, name='get-brand'),
    
    path('category/<slug:name>', category , name='category'),
]
