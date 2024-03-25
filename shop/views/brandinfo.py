from django.shortcuts import render, redirect
from shop.models.brand import Brand
from shop.models.car import Car

# Create your views here.

def get_brand(request,name):
    brand = Brand.get_brand_by_name(name)
    car = Car.get_cars_similar_brand(name)
    context = {'brand': brand, 'car': car}
    return render(request,'brandinfo.html',context)