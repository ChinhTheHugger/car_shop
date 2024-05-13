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
            'brand': car.get_brand,
            'model': car.get_model,
            'year': car.get_year,
            'category': car.get_category,
            'desintext': car.get_desintext,
            'instock': car.get_stock,
            'price': car.get_price,
            'front': car.get_front_img,
            'back': car.get_back_img,
            'interior': car.get_interior_img
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