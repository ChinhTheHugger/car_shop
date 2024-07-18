from django.contrib import admin
from django.urls import path,re_path

from shop.views.home import homepage
from shop.views.carinfo import get_car
from shop.views.brandinfo import get_brand
from shop.views.category import category
from shop.views.search import search
from shop.views.login import Login, logout
from shop.views.signup import Signup
from shop.views.cart import view_cart
from shop.views.makerequest import add_to_cart
from shop.views.editrequest import UpdateDeleteRequest
from shop.views.editcar import get_car_info_for_edit
from shop.views.updatedeletecar import UpdateDeleteCar
from shop.views.newcar import AddNewCar
from shop.views.editbrand import get_brand_info_for_edit
from shop.views.updatedeletebrand import UpdateDeleteBrand
from shop.views.newbrand import AddNewBrand
from shop.views.editcategory import get_category_info_for_edit
from shop.views.updatedeletecategory import UpdateDeleteCategory
from shop.views.newcategory import AddNewCategory
from shop.views.newcontract import get_info_for_contract
from shop.views.contractinfo import get_contract
from shop.views.setupcontract import SetUpContract
from shop.views.editcontract import get_contract_info_for_edit
from shop.views.updatedeletecontract import UpdateDeleteContract
from .middlewares.auth import auth_middleware
from shop.views.accountinfo import get_account

from .views_api.carlistapi import CarListApiView
from .views_api.cardetailapi import CarDetailApiView
from .views_api.brandlistapi import BrandListApiView
from .views_api.branddetailapi import BrandDetailApiView
from .views_api.categorylistapi import CategoryListApiView
from .views_api.categorydetailapi import CategoryDetailApiView

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
    
    path('account', get_account, name='account'),
    
    # cart
    path('cart', view_cart, name='view-cart'),
    
    path('addtocart/<slug:brand>_<slug:model>_<slug:year>', add_to_cart, name='add-to-cart'),
    
    path('editrequest', UpdateDeleteRequest.as_view(), name='edit-request'),
    
    # contract
    path('contractinfo/<slug:info_str>', get_contract, name='get-contract'),
    
    path('addcontract/<slug:customerusername>_<slug:brand>_<slug:model>_<slug:year>_<slug:unixtimestamp>', get_info_for_contract, name='add-contract'),
    
    path('newcontractprocessing', SetUpContract.as_view(), name='setup-contract'),
    
    path('editcontract/<slug:info_str>', get_contract_info_for_edit, name='edit-contract'),
    
    path('updatedeletecontract', UpdateDeleteContract.as_view(), name='update-delete-contract'),
    
    # api
    
    # path('api_test/car', CarListApiView.as_view()),
    # path('api_test/car/<slug:brand>_<slug:model>_<slug:year>', CarDetailApiView.as_view()),
    
    # path('api_test/brand', BrandListApiView.as_view()),
    # path('api_test/brand/<slug:brand>', BrandDetailApiView.as_view()),
    
    # path('api_test/category', CategoryListApiView.as_view()),
    # path('api_test/category/<slug:category>', CategoryDetailApiView.as_view()),
    
    
]
