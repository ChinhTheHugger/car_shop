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

def get_contract(request,customerusername,brand,model,year,unixtimestamp):
    accountusername = request.session.get('account')
    customerinfo = Account.get_account_by_username_for_iterate(accountusername)
    carinfo = Car.get_car(brand,model,year)
    contract = Contract.get_contract_by_parameters(customerusername,carinfo.__str__(),unixtimestamp)
    values = {
        'request': contract.get_request(),
        'customer': customerusername,
        'manager': accountusername,
        'car': carinfo.__str__(),
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
    return render(request, 'addcontract.html', {'account': customerinfo, 'values': values})