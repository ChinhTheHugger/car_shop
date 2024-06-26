from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from app_car.models.car import Car
from app_contract.models.contract import Contract
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

class AccountView(View):
    def get(self, request):
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