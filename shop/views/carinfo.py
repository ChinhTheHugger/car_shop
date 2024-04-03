from django.shortcuts import render, redirect, HttpResponseRedirect
import datetime
from datetime import date
from shop.models.car import Car
from shop.models.category import Category
from shop.models.brand import Brand
from shop.models.contract import Contract
from django.views import View

def get_car(request,brand,model,year):

    carinfo = Car.get_car_info(brand,model,year)
    for c in carinfo:
        carbrand = Car.get_cars_similar_brand(c.brand)
        carcategory = Car.get_cars_similar_category(c.category)
    for i in range(carinfo.count()):
        carinfo[i].instock = carinfo[i].instock - Contract.get_active_contract_number(carinfo[i].__str__,date.today())
    context = {'carinfo': carinfo,'carbrand': carbrand,'carcategory': carcategory}
    return render(request,'carinfo.html',context)