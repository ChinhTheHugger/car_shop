from django.contrib import admin
from django.urls import path

from .views.home import homepage
from .views.carinfo import get_car
from .views.brandinfo import get_brand
from .views.category import category
from .views.search import search
from .views.login import Login, logout
from .views.signup import Signup
from .views.cart import view_cart
from .views.makerequest import add_to_cart
from .views.editrequest import UpdateDeleteRequest

urlpatterns = [
    path('', homepage, name='homepage'),
    path('homepage', homepage, name='homepage'),
    
    path('carinfo/<slug:brand>_<slug:model>_<slug:year>', get_car, name='get-car'),
    
    path('brandinfo/<slug:name>', get_brand, name='get-brand'),
    
    path('category/<slug:name>', category , name='category'),
    
    path('search', search, name='search'),
    
    # account
    path('signup', Signup.as_view(), name='signup'),
    
    path('login', Login.as_view(), name='login'),
    
    path('logout', logout , name='logout'),
    
    # cart
    path('cart', view_cart, name='view-cart'),
    
    path('addtocart/<slug:brand>_<slug:model>_<slug:year>', add_to_cart, name='add-to-cart'),
    
    path('editrequest', UpdateDeleteRequest.as_view(), name='edit-request'),
    
    
]
