from django.shortcuts import render, redirect

from shop.models.car import Car
from shop.models.request import Request
from shop.models.account import Account

from itertools import chain

def view_cart(request):
    customerusername = request.session.get('account')
    cart_items = Request.cart_display(customerusername)
    context = {'cart_items': cart_items}
    return render(request,'cart.html',context)
    