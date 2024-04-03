from django.shortcuts import render, redirect

from shop.models.car import Car
from shop.models.request import Request
from shop.models.account import Account

def view_cart(request,brand,model,year):
    customerid = request.session.get('account')
    customerinfo = Account.get_account_by_id(customerid)
    for customer in customerinfo:
        cart_items = Request.get_requests_by_customer(customer.username)
        context = {'cart_items': cart_items}
        return render(request,'cart.html',context)
    
def add_to_cart(request)