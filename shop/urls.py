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
from .views.newcar import AddNewCar
from .views.editbrand import get_brand_info_for_edit
from .views.updatedeletebrand import UpdateDeleteBrand
from .views.newbrand import AddNewBrand
from .views.editcategory import get_category_info_for_edit
from .views.updatedeletecategory import UpdateDeleteCategory
from .views.newcategory import AddNewCategory
from .views.newcontract import AddNewContract

urlpatterns = [
    path('', homepage, name='homepage'),
    
    path('homepage', homepage, name='homepage'),
    
    # car
    path('carinfo/<slug:brand>_<slug:model>_<slug:year>', get_car, name='get-car'),
    
    path('editcar/<slug:brand>_<slug:model>_<slug:year>', get_car_info_for_edit, name='edit-car'), # manager only
    
    path('updatedeletecar', UpdateDeleteCar.as_view(), name='update-delete-car'), # manager only
    
    path('addcar', AddNewCar.as_view(), name='add-car'), # manager only
    
    # brand
    path('brandinfo/<slug:name>', get_brand, name='get-brand'),
    
    path('editbrand/<slug:brand>', get_brand_info_for_edit, name='edit-brand'), # manager only
    
    path('updatedeletebrand', UpdateDeleteBrand.as_view(), name='update-delete-brand'), # manager only
    
    path('addbrand', AddNewBrand.as_view(), name='add-brand'), # manager only
    
    # category
    path('category/<slug:name>', category , name='category'),
    
    path('editcategory/<slug:category>', get_category_info_for_edit, name='edit-category'), # manager only
    
    path('updatedeletecategory', UpdateDeleteCategory.as_view(), name='update-delete-category'), # manager only
    
    path('addcategory', AddNewCategory.as_view(), name='add-category'), # manager only
    
    # search
    path('search', search, name='search'),
    
    # account
    path('signup', Signup.as_view(), name='signup'),
    
    path('login', Login.as_view(), name='login'),
    
    path('logout', logout , name='logout'),
    
    # cart
    path('cart', view_cart, name='view-cart'),
    
    path('addtocart/<slug:brand>_<slug:model>_<slug:year>', add_to_cart, name='add-to-cart'),
    
    path('editrequest', UpdateDeleteRequest.as_view(), name='edit-request'),
    
    # contract
    path('addcontract/request?=<slug:customerusername>_<slug:brand>_<slug:model>_<slug:year>_<slug:unixtimestamp>', AddNewContract.as_view(), name='add-contract')
    
    
]
