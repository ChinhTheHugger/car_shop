from django.shortcuts import render, redirect

from shop.models.car import Car
from shop.models.request import Request
from shop.models.account import Account

from itertools import chain

def view_cart(request):
    keyword_in = request.POST.get('keyword')
    customerusername = request.session.get('account')
    
    keyword_list = str(keyword_in).split()
    
    requestsearch = Request.search_requests_by_keywords(keyword_list)
    cart_items = Request.cart_display(customerusername)
    cart_items_manager = Request.get_all_requests_for_cart_display()
    accountinfo = Account.get_account_by_username_for_iterate(customerusername)
    
    context = {'cart_items': cart_items, 'cart_items_manager': cart_items_manager,'cart_items_manager_search': requestsearch, 'account_info': accountinfo}
    return render(request,'cart.html',context)
    