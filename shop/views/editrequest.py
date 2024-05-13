from django.shortcuts import render, redirect

from shop.models.car import Car
from shop.models.request import Request
from shop.models.account import Account

from django.views import View
from datetime import datetime
import datetime

class UpdateDeleteRequest(View):
    def post(self, request):
        accountusername = request.session.get('account')
        accountinfo = Account.get_account_by_username(accountusername)
        
        quantity = request.POST.get('quantity')
        car_name = request.POST.get('car_name')
        customer_name = request.POST.get('customer_name')
        unixtimestamp = request.POST.get('date')
        button_action = request.POST.get('action_button')
        
        if accountinfo.check_account_type():
            if button_action == "update" and quantity != 0:
                Request.update_quantity(str(car_name),accountusername,quantity)
            if button_action == "delete" or quantity == 0:
                Request.remove_request(str(car_name),accountusername)
        else:
            if button_action == "update" and quantity != 0:
                arr = str(car_name).split()
                return redirect('add-contract',customerusername=customer_name,brand=arr[0],model=arr[1],year=int(arr[2]),unixtimestamp=int(unixtimestamp))
            if button_action == "delete" or quantity == 0:
                Request.remove_request(str(car_name),customer_name)
            
        return redirect('view-cart')