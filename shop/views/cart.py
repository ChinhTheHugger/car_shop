from django.shortcuts import render, redirect

from shop.models.car import Car
from shop.models.request import Request
from shop.models.account import Account

def view_cart(request):
    customerid = request.session.get('account')
    customerinfo = Account.get_account_by_id(customerid)
    cart_items = Request.get_requests_by_customer(customerinfo.username)
    context = {'cart_items': cart_items}
    return render(request,'cart.html',context)
    
def add_to_cart(request,brand,model,year):
    customerid = request.session.get('account')
    customerinfo = Account.get_account_by_id(customerid)
    carinfo = Car.get_car_info(brand,model,year)
    cart_item = Request.get_or_create(carinfo.__str__,customerinfo.username)
    Request.placeOrder(cart_item)
    return redirect('view-cart')