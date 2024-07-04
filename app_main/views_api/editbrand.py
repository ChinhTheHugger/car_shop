from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shop.models.brand import Brand
from shop.models.account import Account
from django.views import View
import requests

def get_brand_info_for_edit(request,brand):
    customerusername = request.session.get('account')
    customerinfo = Account.get_account_by_username_for_iterate(customerusername)
    
    response = requests.get(f'http://127.0.0.1:8000/api/brand/info/{brand}')
    brandinfo = response.json()
    
    for brand in brandinfo:
        values = {
            'brand': brand['brandname'],
            'website': brand['website'],
            'desintext': brand['desintext'],
            'logo': brand['brandlogo']
        }
    values_new = {
            'brand': "",
            'website': "",
            'desintext': "",
        }
    context = {'brandinfo': brandinfo, 'account': customerinfo, 'values': values, 'values_new': values_new}
    return render(request,'editbrand.html',context)