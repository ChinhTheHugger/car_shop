from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shop.models.car import Car
from shop.models.account import Account
from django.views import View

class UpdateDeleteCar(View):
    def get(request,brand,model,year):
        customerusername = request.session.get('account')
        customerinfo = Account.get_account_by_username_for_iterate(customerusername)
        carinfo = Car.get_car_info(brand,model,year)
        context = {'carinfo': carinfo, 'account': customerinfo}
        return render(request,'carinfo.html',context)
    
    def post(self,request):
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        year = request.POST.get('year')
        category = request.POST.get('category')
        desintext = request.POST.get('desintext')
        price = request.POST.get('price')