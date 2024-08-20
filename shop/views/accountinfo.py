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
def get_account(request, type):
    username = request.session.get('account')
    account = Account.get_account_by_username(username)
    
    if type == 'info':
        data = {
            'account': account
        }
        return render(request, 'account_info.html', data)
    
    if account.check_account_type():
        if type == 'requests':
            requests = Request.total_cart_customer(username)
            data = {
                'type': account.check_account_type(),
                'request': requests
            }
            return render(request, 'account_request.html', data)
        if type == 'contracts':
            contracts = Contract.get_contract_by_customer(username)
            data = {
                'type': account.check_account_type(),
                'contract': contracts
            }
            return render(request, 'account_contract.html', data)
        if type == 'payments':
            data = {}
            return render(request, 'account_payment.html', data)
    else:
        if type == 'customers':
            customers = Account.get_all_customer()
            data = {
                'type': account.check_account_type(),
                'customer': customers
            }
            return render(request, 'account_customer.html', data)
        if type == 'requests':
            requests = Request.total_cart_manager()
            data = {
                'type': account.check_account_type(),
                'request': requests
            }
            return render(request, 'account_request.html', data)
        if type == 'contracts':
            contracts = Contract.get_all_contracts()
            data = {
                'type': account.check_account_type(),
                'contract': contracts
            }
            return render(request, 'account_contract.html', data)
        if type == 'payments':
            data = {}
            return render(request, 'account_payment.html', data)
        if type == 'statistics':
            data = {}
            return render(request, 'account_statistic.html', data)