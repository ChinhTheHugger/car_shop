from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from app_category.models.category import Category
from app_account.models.account import Account
from django.views import View
import requests

def get_category_info_for_edit(request,category):
    customerusername = request.session.get('account')
    customerinfo = Account.get_account_by_username_for_iterate(customerusername)
    
    response = requests.get(f'http://127.0.0.1:8000/api/category/info/{category}')
    categoryinfo = response.json()
    
    for category in categoryinfo:
        values = {
            'category': category['categoryname'],
            'image': category['categoryimage']
        }
    values_new = {
            'category': "",
            'image': ""
        }
    context = {'categoryinfo': categoryinfo, 'account': customerinfo, 'values': values, 'values_new': values_new}
    return render(request,'editcategory.html',context)