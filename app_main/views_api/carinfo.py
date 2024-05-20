from django.shortcuts import render, redirect, HttpResponseRedirect
import datetime
from datetime import date
from app_car.models.car import Car
from app_account.models.account import Account
from app_category.models.category import Category
from app_brand.models.brand import Brand
from app_contract.models.contract import Contract
from django.views import View
import requests

def get_car(request,brand,model,year):
    customerusername = request.session.get('account')
    customerinfo = Account.get_account_by_username_for_iterate(customerusername)
    
    response = requests.get('http://127.0.0.1:8000/api/car/all')
    carinfo = response.json()
    
    response = requests.get('http://127.0.0.1:8000/api/brand/all')
    brand_list = response.json()
    
    response = requests.get('http://127.0.0.1:8000/api/category/all')
    category_list = response.json()
    
    arr_brand = [brnd for brnd in brand_list if brnd['brandname'] == carinfo['brand']]
    arr_category = [cat for cat in category_list if cat['categoryname'] == carinfo['category']]
    
    context = {'carinfo': carinfo,'carbrand': arr_brand,'carcategory': arr_category, 'account': customerinfo}
    return render(request,'carinfo.html',context)