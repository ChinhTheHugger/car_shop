from django.shortcuts import render, redirect
from shop.models.car import Car
from shop.models.category import Category
from shop.models.brand import Brand

def homepage(request):
    
    carTop3 = Car.homepage_three_car
    carMostPopular = Car.homepage_popular_car
    brandMostPopular = Brand.homepage_popular_brand
    carCategory = Category.homepage_popular_category
    context = {'cartopthree': carTop3,'carMostPopular': carMostPopular,'brandMostPopular': brandMostPopular,'carCategory': carCategory}
    return render(request,'homepage.html',context)