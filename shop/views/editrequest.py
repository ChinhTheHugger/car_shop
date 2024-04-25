from django.shortcuts import render, redirect

from shop.models.car import Car
from shop.models.request import Request
from shop.models.account import Account

from django.views import View

class UpdateDeleteRequest(View):
    def post(self, request):
        quantity = request.POST.get('quantity')
        car_name = request.POST.get('car_name')
        button_action = request.POST.get('action_button')
        customerid = request.session.get('account')
        # customerinfo = Account.get_account_by_username(customerid)
        # print(str(car_name)+" "+str(customerinfo.username)+" "+str(quantity))
        if button_action == "update" and quantity != 0:
            Request.update_quantity(str(car_name),customerid,quantity)
        if button_action == "delete" or quantity == 0:
            Request.remove_request(str(car_name),customerid)
        return redirect('view-cart')