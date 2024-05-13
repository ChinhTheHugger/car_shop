from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shop.models.car import Car
from shop.models.brand import Brand
from shop.models.account import Account
from shop.models.request import Request
from shop.models.contract import Contract
from django.views import View
import codecs
from django.utils.encoding import force_bytes
from django.core.files.storage import FileSystemStorage
from upload_validator import FileTypeValidator
from django.core.files.uploadedfile import TemporaryUploadedFile
import mimetypes
from datetime import date

def get_contract(request,info_str):
    accountusername = request.session.get('account')
    customerinfo = Account.get_account_by_username_for_iterate(accountusername)
    
    arr = str(info_str).split('_')
    car_str = str(arr[1]) + " " + str(arr[2]) + " " + str(arr[3])
    
    contract = Contract.get_contract_by_parameters(arr[0],car_str,arr[4])
    customer = Account.get_customer(contract.get_customer())
    manager = Account.get_manager(contract.get_manager())
    values = {
        'request': contract.get_request(),
        'customer': customer.__str__(),
        'manager': manager.__str__(),
        'car': contract.get_car(),
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
        'carfrontbefore': contract.get_front(),
        'carbackbefore': contract.get_back(),
        'carinteriorbefore': contract.get_interior()
    }
    context = {
        'account': customerinfo, 
        'values': values, 
        'info_str': info_str
    }
    return render(request, 'contractinfo.html', context)