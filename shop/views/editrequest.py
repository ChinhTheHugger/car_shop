from django.shortcuts import render, redirect

from shop.models.car import Car
from shop.models.request import Request
from shop.models.account import Account

from django.views import View

class UpdateRequest(View):
    def post(self, request):
        quantity = request.POST.get('quantity')
        car_name = request.POST.get('car_name')
        customerid = request.session.get('account')
        customerinfo = Account.get_account_by_username(customerid)
        print(str(car_name)+" "+str(customerinfo.username)+" "+str(quantity))
        Request.update_quantity(str(car_name),customerinfo.username,quantity)
        return redirect('view-cart')