from django.shortcuts import render, redirect

from shop.models.car import Car
from shop.models.request import Request
from shop.models.account import Account
    
def add_to_cart(request,id):
    customerid = request.session.get('account')
    customerinfo = Account.get_account_by_id(customerid)
    carinfo = Car.get_car_by_id(id)
    cart_item = Request.get_or_create(carinfo.__str__,customerinfo.username)
    Request.placeOrder(cart_item)
    return render(request,'makerequest.html')