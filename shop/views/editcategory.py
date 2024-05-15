from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from app_category.models.category import Category
from app_account.models.account import Account
from django.views import View

def get_category_info_for_edit(request,category):
    customerusername = request.session.get('account')
    customerinfo = Account.get_account_by_username_for_iterate(customerusername)
    categoryinfo = Category.get_category_info(category)
    for category in categoryinfo:
        values = {
            'category': category.get_name,
            'image': category.get_image
        }
    values_new = {
            'category': "",
            'image': ""
        }
    context = {'categoryinfo': categoryinfo, 'account': customerinfo, 'values': values, 'values_new': values_new}
    return render(request,'editcategory.html',context)