from django.shortcuts import render, redirect

from app_car.models.car import Car
from app_request.models.request import Request
from app_account.models.account import Account
    
def add_to_cart(request,brand,model,year):
    customerid = request.session.get('account')
    customerinfo = Account.get_account_by_username(customerid)
    carinfo = Car.get_car_info(brand,model,year)
    for car in carinfo:
        carname = car.__str__()
    print(carname)
    Request.update_or_create(carname,customerinfo.username)
    return redirect('view-cart')