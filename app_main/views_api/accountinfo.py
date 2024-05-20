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
import requests

class AccountView(View):
    def get(self, request):
        username = request.session.get('account')
        accountinfo = Account.get_account_by_username(username)
        
        if accountinfo.check_account_type:
            response = requests.get('http://127.0.0.1:8000/api/request/all')
            request_list = response.json()
            
            response = requests.get('http://127.0.0.1:8000/api/contract/all')
            contract_list = response.json()
            
            arr_request = [req for req in request_list if req['customer'] == username]
            arr_contract = [con for con in contract_list if con['customer'] == username]
            
            data = {
                'account': accountinfo,
                'request': arr_request,
                'contract': arr_contract
            }
            
            return render(request, 'account.html', data)
        else:
            response = requests.get('http://127.0.0.1:8000/api/request/all')
            request_list = response.json()
            
            response = requests.get('http://127.0.0.1:8000/api/contract/all')
            contract_list = response.json()
            
            arr_request = [req for req in request_list if req['manager'] == username]
            arr_contract = [con for con in contract_list if con['manager'] == username]
            
            data = {
                'account': accountinfo,
                'request': arr_request,
                'contract': arr_contract
            }
            
            return render(request, 'account.html', data)