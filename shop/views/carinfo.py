from django.shortcuts import render, redirect, HttpResponseRedirect
from shop.models.car import Car
from shop.models.category import Category
from shop.models.brand import Brand
from django.views import View

def get_car(request,brand,model,year):

    carinfo = Car.get_car_info(brand,model,year)
    for c in carinfo:
        carbrand = Car.get_cars_similar_brand(c.brand)
        carcategory = Car.get_cars_similar_category(c.category)
    context = {'carinfo': carinfo,'carbrand': carbrand,'carcategory': carcategory}
    return render(request,'carinfo.html',context)