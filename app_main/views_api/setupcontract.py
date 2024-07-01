from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from app_car.models.car import Car
from app_contract.models.contract import Contract
from app_account.models.account import Account
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

class SetUpContract(View):
    def post(self, request):
        accountusername = request.session.get('account')
        accountinfo = Account.get_account_by_username_for_iterate(accountusername)
        
        req = request.POST.get('request')
        customer = request.POST.get('customer')
        manager = request.POST.get('manager')
        car = request.POST.get('car')
        quantity = request.POST.get('quantity')
        purpose = request.POST.get('purpose')
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        carodometerbefore = request.POST.get('carodometerbefore')
        carsystemstatusbefore = request.POST.get('carsystemstatusbefore')
        
        residence = request.FILES.get('residence', False)
        idcard = request.FILES.get('idcard', False)
        driverlicense = request.FILES.get('driverlicense', False)
        carfrontbefore = request.FILES.get('carfrontbefore', False)
        carbackbefore = request.FILES.get('carbackbefore', False)
        carinteriorbefore = request.FILES.get('carinteriorbefore', False)
        
        carinfo = Car.get_car_by_str(car)
        cost = carinfo.get_price() * quantity * self.numOfDays(startdate,enddate)
        createdate = datetime.datetime.today
        
        data = {
            'request': req,
            'customer': customer,
            'manager': manager,
            'car': car,
            'quantity': quantity,
            'purpose': purpose,
            'startdate': startdate,
            'enddate': enddate,
            'carodometerbefore': carodometerbefore,
            'carsystemstatusbefore': carsystemstatusbefore,
            'cost': cost
        }
        
        files = {
            'carfrontbefore': carfrontbefore,
            'carbackbefore': carbackbefore,
            'carinteriorbefore': carinteriorbefore
        }
        
        response = requests.post('http://127.0.0.1:8000/api/contract/new', data=data, files=files)
        
        if response.status_code == 201:
            infostr = str(customer) + "_" + str(car).replace(' ',"_") + "_" + str(datetime.datetime.timestamp(createdate)*1000)
            
            return redirect('get-contract',info_str=infostr)
        elif response.status_code == 400:
            customerlist = Account.get_all_customer()
            managerlist = Account.get_all_manager()
    
            data = {
                'request': req,
                'customer': customer,
                'manager': manager,
                'car': car,
                'quantity': quantity,
                'purpose': purpose,
                'startdate': startdate,
                'enddate': enddate,
                'carodometerbefore': carodometerbefore,
                'carsystemstatusbefore': carsystemstatusbefore,
                'cost': cost,
                'carfrontbefore': carfrontbefore,
                'carbackbefore': carbackbefore,
                'carinteriorbefore': carinteriorbefore
            }
            return render(request, 'addcontract.html', data)
        
    
    
    def validateContract(self,contract): 
        error_message = None
        if contract.carodometerbefor <= 0:
            error_message = "Invalid carodometer value!!"
        if contract.startdate > contract.enddate:
            error_message = "Start date can't be after end date!!"
        if contract.quantity < 1:
            error_message = "Quantity can't be zero or negative!!"
        if contract.residence:
            type_front, decoding = mimetypes.guess_type(str(contract.residence))
            if 'image' not in type_front:
                error_message = "The input file for residence is invalid!!"
        if contract.idcard:
            type_back, decoding = mimetypes.guess_type(str(contract.idcard))
            if 'image' not in type_back:
                error_message = "The input file for id card is invalid!!"
        if contract.driverlicense:
            type_interior, decoding = mimetypes.guess_type(str(contract.driverlicense))
            if 'image' not in type_interior:
                error_message = "The input file for driver license is invalid!!"
        if contract.carfrontbefore:
            type_front, decoding = mimetypes.guess_type(str(contract.carfrontbefore))
            if 'image' not in type_front:
                error_message = "The input file for front view is invalid!!"
        if contract.carbackbefore:
            type_back, decoding = mimetypes.guess_type(str(contract.carbackbefore))
            if 'image' not in type_back:
                error_message = "The input file for back view is invalid!!"
        if contract.carinteriorbefore:
            type_interior, decoding = mimetypes.guess_type(str(contract.carinteriorbefore))
            if 'image' not in type_interior:
                error_message = "The input file for interior view is invalid!!"
        
        return error_message
    
    def numOfDays(date1, date2):
        if date2 > date1:   
            return (date2-date1).days
        else:
            return (date1-date2).days
        
        