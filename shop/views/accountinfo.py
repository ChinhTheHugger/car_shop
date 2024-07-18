from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shop.models.car import Car
from shop.models.contract import Contract
from shop.models.account import Account
from shop.models.request import Request
from django.views import View
import codecs
from django.utils.encoding import force_bytes
from django.core.files.storage import FileSystemStorage
from upload_validator import FileTypeValidator
from django.core.files.uploadedfile import TemporaryUploadedFile
import mimetypes
from datetime import date
import datetime

def get_account(request):
    username = request.session.get('account')
    accountinfo = Account.get_account_by_username(username)
        
    if accountinfo.check_account_type:
        requests = Request.total_cart_customer(username)
        contracts = Contract.get_contract_by_customer(username)
        data = {
            'account': accountinfo,
            'request': requests,
            'contract': contracts
        }
            
        return render(request, 'account.html', data)
    else:
        requests = Request.total_cart_manager()
        contracts = Contract.get_all_contracts()
        data = {
            'account': accountinfo,
            'request': requests,
            'contract': contracts
        }
            
        return render(request, 'account.html', data)