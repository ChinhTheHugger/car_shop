from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from app_car.models.car import Car
from app_contract.models.contract import Contract
from app_account.models.account import Account
from django.views import View

def get_contract_info_for_edit(request,info_str):
    accountusername = request.session.get('account')
    accountinfo = Account.get_account_by_username_for_iterate(accountusername)
    
    arr = str(info_str).split('_')
    car_str = str(arr[1]) + " " + str(arr[2]) + " " + str(arr[3])
    
    contract = Contract.get_contract_by_parameters(arr[0],car_str,arr[4])
    
    customerlist = Account.get_all_customer()
    managerlist = Account.get_all_manager()
    
    values = {
        'request': contract.get_request(),
        'customer': contract.get_customer(),
        'manager': contract.get_manager(),
        'car': contract.get_car,
        'quantity': contract.get_quantity(),
        'purpose': contract.get_purpose(),
        'startdate': contract.get_startdate(),
        'enddate': contract.get_enddate(),
        'carodometerbefore': contract.get_odometer(),
        'carsystemstatusbefore': contract.get_systemstatus(),
        'cost': contract.get_cost(),
        'residence': contract.get_residence(),
        'idcard': contract.get_id(),
        'driverlicense': contract.get_driverlicense(),
        'front': contract.get_front(),
        'back': contract.get_back(),
        'interior': contract.get_interior()
    }
    
    data = {
        'contract': values,
        'account': accountinfo,
        'info_str': info_str,
        'customerlist': customerlist,
        'managerlist': managerlist
    }
    
    return render(request,'editcontract.html',data)