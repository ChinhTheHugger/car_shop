from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from app_brand.models.brand import Brand
from app_account.models.account import Account
from django.views import View

def get_brand_info_for_edit(request,brand):
    customerusername = request.session.get('account')
    customerinfo = Account.get_account_by_username_for_iterate(customerusername)
    brandinfo = Brand.get_brand_info(brand)
    for brand in brandinfo:
        values = {
            'brand': brand.get_brand,
            'website': brand.get_website,
            'desintext': brand.get_desintext,
            'logo': brand.get_logo
        }
    values_new = {
            'brand': "",
            'website': "",
            'desintext': "",
        }
    context = {'brandinfo': brandinfo, 'account': customerinfo, 'values': values, 'values_new': values_new}
    return render(request,'editbrand.html',context)