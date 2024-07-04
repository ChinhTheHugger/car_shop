from django.shortcuts import render, redirect
from shop.models.brand import Brand
from shop.models.car import Car
from shop.models.account import Account
import requests

# Create your views here.

def get_brand(request,name):
    customerusername = request.session.get('account')
    customerinfo = Account.get_account_by_username_for_iterate(customerusername)
    
    response = requests.get('http://127.0.0.1:8000/api/brand/all')
    brand_list = response.json()
    
    response = requests.get('http://127.0.0.1:8000/api/car/all')
    car_list = response.json()
    
    arr_brand = [brnd for brnd in brand_list if brnd['brandname'] == name]
    arr_car = [c for c in car_list if c['brand'] == name]
    
    context = {'brand': arr_brand, 'car': arr_car, 'account': customerinfo}
    return render(request,'brandinfo.html',context)