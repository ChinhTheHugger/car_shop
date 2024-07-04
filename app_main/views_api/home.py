from django.shortcuts import render, redirect
from shop.models.car import Car
from shop.models.category import Category
from shop.models.brand import Brand
import requests
from random import sample

def homepage(request):
    response = requests.get('http://127.0.0.1:8000/api/car/all')
    car_list = response.json()
    
    carTop3 = sample(car_list,3)
    carMostPopular = sample(car_list,10)
    
    response = requests.get('http://127.0.0.1:8000/api/brand/all')
    brand_list = response.json()
    
    brandMostPopular = sample(brand_list,5)
    
    response = requests.get('http://127.0.0.1:8000/api/category/all')
    category_list = response.json()
    
    categoryMostPopular = sample(category_list,5)
    
    context = {'cartopthree': carTop3,'carMostPopular': carMostPopular,'brandMostPopular': brandMostPopular,'carCategory': categoryMostPopular}
    return render(request,'homepage.html',context)