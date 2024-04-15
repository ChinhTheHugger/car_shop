from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shop.models.car import Car
from shop.models.account import Account
from django.views import View

def get_car_info_for_edit(request,brand,model,year):
    customerusername = request.session.get('account')
    customerinfo = Account.get_account_by_username_for_iterate(customerusername)
    carinfo = Car.get_car_info(brand,model,year)
    for car in carinfo:
        values = {
            'brand_input': car.brand,
            'model_input': car.model,
            'year_input': car.year,
            'category_input': car.category,
            'desintext_input': car.desintext,
            'instock_input': car.instock,
            'price_input': car.price,
        }
    context = {'carinfo': carinfo, 'account': customerinfo, 'values': values}
    return render(request,'editcar.html',context)