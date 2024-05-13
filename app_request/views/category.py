from django.shortcuts import render, redirect, HttpResponseRedirect
from shop.models.car import Car
from shop.models.category import Category
from django.views import View

def category(request,name):
    category = Category.get_all_categories
    if name != 'all':
        car = Car.get_cars_similar_category(name)
    else:
        car = Car.get_all_cars
        
    context = {'category': category,'car': car}
    return render(request,'category.html', context)