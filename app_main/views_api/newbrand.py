from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from app_brand.models.brand import Brand
from app_account.models.account import Account
from django.views import View
import codecs
from django.utils.encoding import force_bytes
from django.core.files.storage import FileSystemStorage
from upload_validator import FileTypeValidator
from django.core.files.uploadedfile import TemporaryUploadedFile
import mimetypes
import requests

class AddNewBrand(View):
    def get(self, request):
        customerusername = request.session.get('account')
        values = {
                'brand': "",
                'website': "",
                'desintext': "",
                'logo': ""
        }
        customerinfo = Account.get_account_by_username_for_iterate(customerusername)
        return render(request, 'addbrand.html', {'account': customerinfo, 'values': values})
    
    def post(self,request):
        customerusername = request.session.get('account')
        customerinfo = Account.get_account_by_username_for_iterate(customerusername)
    
        brand_new = request.POST.get('brand')
        website_new = request.POST.get('website')
        desintext_new = request.POST.get('desintext')
        
        logo_new = request.FILES.get('logo', False)
        
        values = {
                'brandname': brand_new,
                'website': website_new,
                'desintext': desintext_new
            }
        files = {
            'brandlogo': logo_new
        }
        
        response = requests.post('http://127.0.0.1:8000/api/brand/new', data=data, files=files)
        
        if response.status_code == 201:
            response_new = requests.get(f'http:127.0.0.1:8000/api/brand/info/{brand_new}')
            car_list_response = requests.get('http://127.0.0.1:8000/api/car/all')
            
            brandinfo = response_new.json()
            car_list = car_list_response.json()
            
            arr_car = [car for car in car_list if car['brand'] == brand_new]
            
            data = {'brand': brandinfo, 'car': arr_car, 'account': customerinfo}
            return render(request, 'addbrand.html', data)
        elif response.status_code == 400:
            values = {
                'brandname': brand_new,
                'website': website_new,
                'desintext': desintext_new,
                'brandlogo': logo_new
            }
            
            data = {
                'values': values,
                'account': customerinfo,
                'error': response.json()
            }
            
            return render(request, 'addbrand.html', data)
    
    def validateBrand(self,edited_brand):
        error_message = None
        if (not edited_brand.brandname):
            error_message = "Brand name can't be blank!!"
        if (not edited_brand.website):
            error_message = "Website can't be blank!!"
        if edited_brand.isExist():
            error_message = "Brand already exists!! (matching name)"
        if (not edited_brand.desintext):
            error_message = "Brand should have a description!!"
        if (not edited_brand.brandlogo):
            error_message = "Brand should have a logo!!"
        if edited_brand.brandlogo:
            type_logo, decoding = mimetypes.guess_type(str(edited_brand.brandlogo))
            if 'image' not in type_logo:
                error_message = "The input file for logo is invalid!!"
        
        return error_message