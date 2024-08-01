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
    if request.session.get('account') != '':
        # # print(request.session.items())
        # username = request.session.get('account')
        # accountinfo = Account.get_account_by_username_for_iterate(username)    
        # requests = Request.total_cart_manager()
        # contracts = Contract.get_all_contracts()
        
        # for acc in accountinfo:
        #     data = {
        #         'accounts': accountinfo,
        #         'request': requests,
        #         'contract': contracts,
        #         'status': acc.check_account_type()
        #     }
        username = request.session.get('account')
        
        account = Account.get_account_by_username(username)
        data = {'account': account}
        
        return render(request, 'account_test.html', data)
    else:
        username = request.session.get('account')
        
        account = Account.get_account_by_username(username)
        data = {'account': account}
        
        return render(request, 'account_test.html', data)