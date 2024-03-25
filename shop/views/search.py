from django.shortcuts import render, redirect, HttpResponseRedirect
from shop.models.car import Car
from shop.models.brand import Brand
from shop.models.category import Category
from django.views import View

def search(request):
    model_in = request.POST.get('model')
    brand_in = request.POST.get('brand')
    category_in = request.POST.get('category')
    year_in = request.POST.get('year')

    carsearch = Car.objects.select_related('brand').all()
    
    car_opt = Car.get_all_cars
    brand_opt = Brand.get_all_brands
    category_opt = Category.get_all_categories
    
    if model_in != "All":
        carsearch = carsearch.filter(model=model_in)
    if brand_in != "0":
        carsearch = carsearch.filter(brand=brand_in)
    if category_in != "0":
        carsearch = carsearch.filter(category=category_in)
    if year_in != "All":
        carsearch = carsearch.filter(year=year_in)

    context = {'carsearch': carsearch,'brand_opt': brand_opt,'category_opt': category_opt,'car_opt': car_opt}
    return render(request,'search.html',context)