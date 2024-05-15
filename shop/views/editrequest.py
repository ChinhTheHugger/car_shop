from django.shortcuts import render, redirect

from app_car.models.car import Car
from app_request.models.request import Request
from app_account.models.account import Account

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
                return redirect('add-contract',customerusername=customer_name,brand=arr[0],model=arr[1],year=int(arr[2]),unixtimestamp=self.clean_date(unixtimestamp))
            if button_action == "delete" or quantity == 0:
                Request.remove_request(str(car_name),customer_name)
            
        return redirect('view-cart')
    
    def clean_date(self,dt):
        dt = str(dt).replace(',','')
        arr = dt.split(' ')
        if arr[0] == 'January':
            arr[0] = '01'
        if arr[0] == 'february':
            arr[0] = '02'
        if arr[0] == 'March':
            arr[0] = '03'
        if arr[0] == 'April':
            arr[0] = '04'
        if arr[0] == 'May':
            arr[0] = '05'
        if arr[0] == 'June':
            arr[0] = '06'
        if arr[0] == 'July':
            arr[0] = '07'
        if arr[0] == 'August':
            arr[0] = '08'
        if arr[0] == 'September':
            arr[0] = '09'
        if arr[0] == 'October':
            arr[0] = '10'
        if arr[0] == 'November':
            arr[0] = '11'
        if arr[0] == 'December':
            arr[0] = '12'
        return str(arr[2] + "-" + arr[0] + "-" + arr[1])