from django.contrib import admin
from django.urls import path,re_path

from app_main.views.home import homepage
from app_main.views.search import search

from app_main.views.carinfo import get_car
from app_main.views.editcar import get_car_info_for_edit
from app_main.views.updatedeletecar import UpdateDeleteCar
from app_main.views.newcar import AddNewCar

from app_main.views.brandinfo import get_brand
from app_main.views.editbrand import get_brand_info_for_edit
from app_main.views.updatedeletebrand import UpdateDeleteBrand
from app_main.views.newbrand import AddNewBrand

from app_main.views.category import category
from app_main.views.editcategory import get_category_info_for_edit
from app_main.views.updatedeletecategory import UpdateDeleteCategory
from app_main.views.newcategory import AddNewCategory

from app_main.views.login import Login, logout
from app_main.views.signup import Signup
from app_main.middlewares.auth import auth_middleware
from app_main.views.accountinfo import AccountView

from app_main.views.cart import view_cart
from app_main.views.makerequest import add_to_cart
from app_main.views.editrequest import UpdateDeleteRequest

from app_main.views.newcontract import get_info_for_contract
from app_main.views.contractinfo import get_contract
from app_main.views.setupcontract import SetUpContract
from app_main.views.editcontract import get_contract_info_for_edit
from app_main.views.updatedeletecontract import UpdateDeleteContract

urlpatterns = [
    # homepage
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
    
    path('account', auth_middleware(AccountView.as_view()), name='account'),
    
    # cart
    path('cart', view_cart, name='view-cart'),
    
    path('addtocart/<slug:brand>_<slug:model>_<slug:year>', add_to_cart, name='add-to-cart'),
    
    path('editrequest', UpdateDeleteRequest.as_view(), name='edit-request'),
    
    # contract
    path('contractinfo/<slug:info_str>', get_contract, name='get-contract'),
    
    path('addcontract/<slug:customerusername>_<slug:brand>_<slug:model>_<slug:year>_<slug:unixtimestamp>', get_info_for_contract, name='add-contract'),
    
    path('newcontractprocessing', SetUpContract.as_view(), name='setup-contract'),
    
    path('editcontract/<slug:info_str>', get_contract_info_for_edit, name='edit-contract'),
    
    path('updatedeletecontract', UpdateDeleteContract.as_view(), name='update-delete-contract')
    
    
]
