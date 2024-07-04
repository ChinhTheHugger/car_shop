from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shop.models.car import Car
from shop.models.contract import Contract
from shop.models.account import Account
from django.views import View
import requests

def get_contract_info_for_edit(request,info_str):
    accountusername = request.session.get('account')
    accountinfo = Account.get_account_by_username_for_iterate(accountusername)
    
    arr = str(info_str).split('_')
    car_str = str(arr[1]) + " " + str(arr[2]) + " " + str(arr[3])
    
    response = requests.get('http://127.0.0.1:8000/api/contract/all')
    contract_list = response.json()
    
    contracts = [con for con in contract_list if con['customer'] == arr[1] and con['car'] == car_str and con['createdate'] == arr[4]]
    
    customerlist = Account.get_all_customer()
    managerlist = Account.get_all_manager()
    
    for contract in contracts:
        values = {
            'request': contract['request'],
            'customer': contract['customer'],
            'manager': contract['manager'],
            'car': contract['car'],
            'quantity': contract['quantity'],
            'purpose': contract['purpose'],
            'startdate': contract['startdate'],
            'enddate': contract['enddate'],
            'carodometerbefore': contract['carodometerbefore'],
            'carsystemstatusbefore': contract['carsystemstatusbefore'],
            'cost': contract['cost'],
            'residence': contract['residence'],
            'idcard': contract['idcard'],
            'driverlicense': contract['driverlicense'],
            'front': contract['carfrontbefore'],
            'back': contract['carbackbefore'],
            'interior': contract['carinteriorbefore']
        }
    
    data = {
        'contract': values,
        'account': accountinfo,
        'info_str': info_str,
        'customerlist': customerlist,
        'managerlist': managerlist
    }
    
    return render(request,'editcontract.html',data)