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

class UpdateDeleteContract(View):
    def post(self, request):
        accountusername = request.session.get('account')
        accountinfo = Account.get_account_by_username_for_iterate(accountusername)
        
        info_str = request.POST.get('info_str')
        
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
        
        values = {
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
        
        arr = str(info_str).split('_')
        car_str = str(arr[1]) + " " + str(arr[2]) + " " + str(arr[3])
    
        contract_original = Contract.get_contract_by_parameters(arr[0],car_str,arr[4])
        
        error_message = None
        
        contract = Contract.set_up_contract(request,customer,manager,car,quantity,purpose,startdate,enddate,residence,idcard,driverlicense,carodometerbefore,carsystemstatusbefore,carfrontbefore,carbackbefore,carinteriorbefore,cost,createdate)
        error_message = self.validateContract(contract)
        
        button_action = request.POST.get('action_button')
        
        if button_action == 'update':
            if not error_message:
                if residence != False:
                    save_new_residence =  FileSystemStorage(location='uploads/residences/',base_url='uploads/residences/').save(residence.name,residence)
                    new_residence_url = FileSystemStorage(location='uploads/residences/',base_url='uploads/residences/').url(save_new_residence)
                else:
                    new_front_url = ""
                
                if idcard != False:
                    save_new_idcard =  FileSystemStorage(location='uploads/idcards/',base_url='uploads/idcards/').save(idcard.name,idcard)
                    new_idcard_url = FileSystemStorage(location='uploads/idcards/',base_url='uploads/idcards/').url(save_new_idcard)
                else:
                    new_back_url = ""
                
                if driverlicense != False:
                    save_new_driverlicense =  FileSystemStorage(location='uploads/driverlicenses/',base_url='uploads/driverlicenses/').save(driverlicense.name,driverlicense)
                    new_driverlicense_url = FileSystemStorage(location='uploads/driverlicenses/',base_url='uploads/driverlicenses/').url(save_new_driverlicense)
                else:
                    new_interior_url = ""
                
                if carfrontbefore != False:
                    save_new_front =  FileSystemStorage(location='uploads/fronts/',base_url='uploads/fronts/').save(carfrontbefore.name,carfrontbefore)
                    new_front_url = FileSystemStorage(location='uploads/fronts/',base_url='uploads/fronts/').url(save_new_front)
                else:
                    new_front_url = ""
                
                if carbackbefore != False:
                    save_new_back =  FileSystemStorage(location='uploads/backs/',base_url='uploads/backs/').save(carbackbefore.name,carbackbefore)
                    new_back_url = FileSystemStorage(location='uploads/backs/',base_url='uploads/backs/').url(save_new_back)
                else:
                    new_back_url = ""
                
                if carinteriorbefore != False:
                    save_new_interior =  FileSystemStorage(location='uploads/interiors/',base_url='uploads/interiors/').save(carinteriorbefore.name,carinteriorbefore)
                    new_interior_url = FileSystemStorage(location='uploads/interiors/',base_url='uploads/interiors/').url(save_new_interior)
                else:
                    new_interior_url = ""
                    
                contract_original.update_contract(request,customer,manager,car,quantity,purpose,startdate,enddate,new_residence_url,new_idcard_url,new_driverlicense_url,carodometerbefore,carsystemstatusbefore,new_front_url,new_back_url,new_interior_url,cost,createdate)
                
                return redirect('get-contract',info_str=info_str)
            else:
                customerlist = Account.get_all_customer()
                managerlist = Account.get_all_manager()
                
                data = {
                        'error': error_message,
                        'values': values,
                        'account': accountinfo,
                        'customerlist': customerlist, 
                        'managerlist': managerlist
                    }
                return render(request, 'editcontract.html', data)
        else:
            Contract.delete_contract(arr[0],car_str,arr[4])
            return redirect('homepage')
        
        
        
    def validateContract(self,contract,info_str): 
        error_message = None
        arr = str(info_str).split('_')
        car_str = str(arr[1]) + " " + str(arr[2]) + " " + str(arr[3])
        contract_info = Contract.get_contract_by_parameters(arr[0],car_str,arr[4])
        
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