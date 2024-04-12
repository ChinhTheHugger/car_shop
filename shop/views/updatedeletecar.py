from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shop.models.car import Car
from shop.models.account import Account
from django.views import View

class UpdateDeleteCar(View):
    def post(self, request):
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        year = request.POST.get('year')
        category = request.POST.get('category')
        desintext = request.POST.get('desintext')
        instock = request.POST.get('instock')
        price = request.POST.get('price')
        
        front = request.POST.get('front')
        back = request.POST.get('back')
        interior = request.POST.get('interior')
        
        return redirect('edit-car-parameters',brnd=brand,mdl=model,yr=year)