from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from app_car.models.car import Car
from app_brand.models.brand import Brand
from app_account.models.account import Account
from app_request.models.request import Request
from django.views import View
import codecs
from django.utils.encoding import force_bytes
from django.core.files.storage import FileSystemStorage
from upload_validator import FileTypeValidator
from django.core.files.uploadedfile import TemporaryUploadedFile
import mimetypes
from datetime import date
import datetime
import time

def get_info_for_contract(request,customerusername,brand,model,year,unixtimestamp):
    accountusername = request.session.get('account')
    customerinfo = Account.get_account_by_username_for_iterate(accountusername)
    
    carinfo = Car.get_car(brand,model,year)
    requestinfo = Request.get_request(customerusername,brand,model,year,unixtimestamp)
    
    customerlist = Account.get_all_customer()
    managerlist = Account.get_all_manager()
    
    customername = Account.get_account_by_username(customerusername)
    managername = Account.get_account_by_username(accountusername)
    
    values = {
        'request': requestinfo.request_custom_id(),
        'customer': customerusername,
        'manager': accountusername,
        'car': carinfo.__str__(),
        'quantity': requestinfo.get_quantity(),
        'purpose': '',
        'startdate': '',
        'enddate': '',
        'carodometerbefore': '',
        'carsystemstatusbefore': '',
        'cost': carinfo.get_price() * requestinfo.get_quantity()
    }
    context = {
        'account': customerinfo, 
        'values': values, 
        'customerlist': customerlist, 
        'managerlist': managerlist,
        'customername': customername.__str__(),
        'managername': managername.__str__()
    }
    return render(request, 'addcontract.html', context)

