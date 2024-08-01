from django.shortcuts import render, redirect, HttpResponseRedirect
from shop.models.car import Car
from shop.models.brand import Brand
from shop.models.category import Category
from django.views import View

def search(request):
    keyword_in = request.POST.get('keyword')
    model_in = request.POST.get('model')
    brand_in = request.POST.get('brand')
    category_in = request.POST.get('category')
    year_in = request.POST.get('year')
    
    car_model_opt = Car.get_car_model_distinct
    car_year_opt = Car.get_car_year_distinct
    brand_opt = Brand.get_all_brands
    category_opt = Category.get_all_categories
    
    keyword_list = str(keyword_in).split()
    
    if keyword_in is None and model_in is None and brand_in is None and category_in is None and year_in is None:
        carsearch = Car.get_all_cars()
    else:
        carsearch = Car.get_car_by_parameters(brand_in,model_in,year_in,category_in,keyword_list)

    context = {'carsearch': carsearch,'brand_opt': brand_opt,'category_opt': category_opt,'car_model_opt': car_model_opt,'car_year_opt': car_year_opt}
    return render(request,'search.html',context)