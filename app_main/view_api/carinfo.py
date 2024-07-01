from django.shortcuts import render, redirect, HttpResponseRedirect
import datetime
from datetime import date
from app_car.models.car import Car
from app_account.models.account import Account
from app_category.models.category import Category
from app_brand.models.brand import Brand
from app_contract.models.contract import Contract
from django.views import View

def get_car(request,brand,model,year):
    customerusername = request.session.get('account')
    customerinfo = Account.get_account_by_username_for_iterate(customerusername)
    carinfo = Car.get_car_info(brand,model,year)
    for c in carinfo:
        carbrand = Car.get_cars_similar_brand(c.brand)
        carcategory = Car.get_cars_similar_category(c.category)
    for i in range(carinfo.count()):
        carinfo[i].instock = carinfo[i].instock - Contract.get_active_contract_number(str(carinfo[i].__str__),date.today())
    context = {'carinfo': carinfo,'carbrand': carbrand,'carcategory': carcategory, 'account': customerinfo}
    return render(request,'carinfo.html',context)