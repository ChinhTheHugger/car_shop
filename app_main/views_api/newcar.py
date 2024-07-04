from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shop.models.car import Car
from shop.models.account import Account
from django.views import View
import codecs
from django.utils.encoding import force_bytes
from django.core.files.storage import FileSystemStorage
from upload_validator import FileTypeValidator
from django.core.files.uploadedfile import TemporaryUploadedFile
import mimetypes
import requests

class AddNewCar(View):
    def get(self, request):
        customerusername = request.session.get('account')
        values = {
                'brand': "",
                'model': "",
                'year': "",
                'category': "",
                'desintext': "",
                'instock': "",
                'price': "",
                'front': "",
                'back': "",
                'interior': ""
        }
        customerinfo = Account.get_account_by_username_for_iterate(customerusername)
        return render(request, 'addcar.html', {'account': customerinfo, 'values': values})
    
    def post(self,request):
        customerusername = request.session.get('account')
        customerinfo = Account.get_account_by_username_for_iterate(customerusername)
    
        brand_new = request.POST.get('brand')
        model_new = request.POST.get('model')
        year_new = request.POST.get('year')
        category_new = request.POST.get('category')
        desintext_new = request.POST.get('desintext')
        instock_new = request.POST.get('instock')
        price_new = request.POST.get('price')
        
        front_new = request.FILES.get('front', False)
        back_new = request.FILES.get('back', False)
        interior_new = request.FILES.get('interior', False)
        
        data = {
            'brand': brand_new,
            'model': model_new,
            'year': year_new,
            'category': category_new,
            'desintext': desintext_new,
            'instock': instock_new,
            'price': price_new
        }
        
        files = {
            'front': front_new,
            'back': back_new,
            'interior': interior_new
        }
        
        response = requests.post('http://127.0.0.1:8000/api/car/new',data=data,files=files)
        
        if response.status_code == 201:
            # Success
            response_new = requests.get(f'http://127.0.0.1:8000/api/car/info/{brand_new}_{model_new}_{year_new}')
            car_list_response = requests.get('http://127.0.0.1:8000/api/car/all')
            
            carinfo = response_new.json()
            car_list = car_list_response.json()
            
            arr_brand = [car for car in car_list if car['brand'] == brand_new]
            arr_category = [car for car in car_list if car['category'] == category_new]
            
            data = {
                'carinfo': carinfo,
                'carbrand': arr_brand,
                'carcategory': arr_category,
                'account': customerinfo
            }
            return render(request, 'carinfo.html', data)
        elif response.status_code == 400:
            # Error handling
            values = {
                'brand': brand_new,
                'model': model_new,
                'year': year_new,
                'category': category_new,
                'desintext': desintext_new,
                'instock': instock_new,
                'price': price_new,
                'front': front_new,
                'back': back_new,
                'interior': interior_new
            }
            
            data = {
                'values': values,
                'account': customerinfo,
                'error': response.json()
            }
            return render(request, 'addcar.html', data)
        
        
    def validateCar(self,edited_car):
        error_message = None
        if (not edited_car.brand):
            error_message = "Brand name can't be blank!!"
        if (not edited_car.model):
            error_message = "Model name can't be blank!!"
        if (not edited_car.year):
            error_message = "Manufacture year can't be blank!!"
        if edited_car.isExist():
            error_message = "Car already exists!! (matching brand, model and manufacture year)"
        if (not edited_car.category):
            error_message = "Category can't be blank!!"
        if (not edited_car.desintext):
            error_message = "Car should have a description!!"
        if (not edited_car.instock):
            error_message = "Number of cars in stock can't be blank!!"
        if (not edited_car.price):
            error_message = "Car's renting price can't be blank!!"
        if (not edited_car.front):
            error_message = "Car should have a front view!!"
        if edited_car.front:
            type_front, decoding = mimetypes.guess_type(str(edited_car.front))
            if 'image' not in type_front:
                error_message = "The input file for front view is invalid!!"
        if (not edited_car.back):
            error_message = "Car should have a back view!!"
        if edited_car.back:
            type_back, decoding = mimetypes.guess_type(str(edited_car.back))
            if 'image' not in type_back:
                error_message = "The input file for back view is invalid!!"
        if (not edited_car.interior):
            error_message = "Car should have an interior view!!"
        if edited_car.interior:
            type_interior, decoding = mimetypes.guess_type(str(edited_car.interior))
            if 'image' not in type_interior:
                error_message = "The input file for interior view is invalid!!"
        
        return error_message