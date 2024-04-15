from django.contrib import admin
from django.urls import path,re_path

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
from .views.editcar import get_car_info_for_edit
from .views.updatedeletecar import UpdateDeleteCar

urlpatterns = [
    path('', homepage, name='homepage'),
    
    path('homepage', homepage, name='homepage'),
    
    # car
    path('carinfo/<slug:brand>_<slug:model>_<slug:year>', get_car, name='get-car'),
    
    path('editcar/<slug:brand>_<slug:model>_<slug:year>', get_car_info_for_edit, name='edit-car'),
    
    re_path(r'^editcar/(?P<brnd>\d+)_(?P<mdl>\d+)_(?P<yr>\d+)/$', get_car_info_for_edit, name='edit-car-parameters'),
    
    path('updatedeletecar', UpdateDeleteCar.as_view(), name='update-delete-car'),
    
    # brand
    path('brandinfo/<slug:name>', get_brand, name='get-brand'),
    
    # category
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
