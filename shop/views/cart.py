from django.shortcuts import render, redirect

from shop.models.car import Car
from shop.models.request import Request
from shop.models.account import Account

def view_cart(request):
    customerusername = request.session.get('account')
    cart_items = Request.get_requests_by_customer(customerusername)
    context = {'cart_items': cart_items}
    return render(request,'cart.html',context)
    