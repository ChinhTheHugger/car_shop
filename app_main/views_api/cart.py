from django.shortcuts import render, redirect

from shop.models.car import Car
from shop.models.request import Request
from shop.models.account import Account

from itertools import chain
import requests

def view_cart(request):
    keyword_in = request.POST.get('keyword')
    customerusername = request.session.get('account')
    
    keyword_list = str(keyword_in).split()
    
    requestsearch = Request.search_requests_by_keywords(keyword_list)
    accountinfo = Account.get_account_by_username_for_iterate(customerusername)
    
    response = requests.get('http://127.0.0.1:8000/api/request/all')
    cart_items = response.json()
    
    arr_customer = [req for req in cart_items if req['customer'] == customerusername]
    arr_manager = [req for req in cart_items]
    
    context = {'cart_items': arr_customer, 'cart_items_manager': arr_manager,'cart_items_manager_search': requestsearch, 'account_info': accountinfo}
    return render(request,'cart.html',context)
    