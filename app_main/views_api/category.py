from django.shortcuts import render, redirect, HttpResponseRedirect
from app_car.models.car import Car
from app_category.models.category import Category
from django.views import View
import requests

def category(request,name):
    response = requests.get('http://127.0.0.1:8000/api/category/all')
    category_list = response.json()
    arr_category = [cat for cat in category_list]
    
    if name != 'all':
        response = requests.get('http://127.0.0.1:8000/api/car/all')
        car_list = response.json()
        
        arr_car = [car for car in car_list if car['category'] == name]
    else:
        response = requests.get('http://127.0.0.1:8000/api/car/all')
        car_list = response.json()
        
        arr_car = [car for car in car_list]
        
    context = {'category': arr_category,'car': arr_car}
    return render(request,'category.html', context)