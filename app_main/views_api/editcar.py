from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shop.models.car import Car
from shop.models.account import Account
from django.views import View
import requests

def get_car_info_for_edit(request,brand,model,year):
    customerusername = request.session.get('account')
    customerinfo = Account.get_account_by_username_for_iterate(customerusername)
    
    response = requests.get(f'http://127.0.0.1:8000/api/car/info/{brand}_{model}_{year}')
    carinfo = response.json()
    
    for car in carinfo:
        values = {
            'brand': car['brand'],
            'model': car['model'],
            'year': car['year'],
            'category': car['category'],
            'desintext': car['desintext'],
            'instock': car['instock'],
            'price': car['price'],
            'front': car['front'],
            'back': car['back'],
            'interior': car['interior']
        }
    values_new = {
            'brand': "",
            'model': "",
            'year': "",
            'category': "",
            'desintext': "",
            'instock': "",
            'price': ""
        }
    context = {'carinfo': carinfo, 'account': customerinfo, 'values': values, 'values_new': values_new}
    return render(request,'editcar.html',context)