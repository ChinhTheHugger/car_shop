from django.shortcuts import render, redirect
from shop.models.brand import Brand
from shop.models.car import Car
from shop.models.account import Account

# Create your views here.

def get_brand(request,name):
    customerusername = request.session.get('account')
    customerinfo = Account.get_account_by_username_for_iterate(customerusername)
    brand = Brand.get_brand_by_name(name)
    car = Car.get_cars_similar_brand(name)
    context = {'brand': brand, 'car': car, 'account': customerinfo}
    return render(request,'brandinfo.html',context)