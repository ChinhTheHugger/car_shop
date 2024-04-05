from django.shortcuts import render, redirect

from shop.models.car import Car
from shop.models.request import Request
from shop.models.account import Account

def view_cart(request):
    customerid = request.session.get('account')
    print(customerid)
    customerinfo = Account.get_account_by_username(customerid)
    cart_items = Request.get_requests_by_customer(customerinfo.username)
    context = {'cart_items': cart_items}
    return render(request,'cart.html',context)
    