from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from app_category.models.category import Category
from app_account.models.account import Account
from django.views import View
import codecs
from django.utils.encoding import force_bytes
from django.core.files.storage import FileSystemStorage
from upload_validator import FileTypeValidator
from django.core.files.uploadedfile import TemporaryUploadedFile
import mimetypes
import requests

class AddNewCategory(View):
    def get(self, request):
        customerusername = request.session.get('account')
        values = {
                'category': "",
                'image': ""
        }
        customerinfo = Account.get_account_by_username_for_iterate(customerusername)
        return render(request, 'addcategory.html', {'account': customerinfo, 'values': values})
    
    def post(self,request):
        customerusername = request.session.get('account')
        customerinfo = Account.get_account_by_username_for_iterate(customerusername)
    
        category_new = request.POST.get('category')
        
        logo_new = request.FILES.get('image', False)
        
        values = {
                'categoryname': category_new
            }
        
        files = {
            'categoryimage': logo_new
        }
        
        response = requests.post('http://127.0.0.1:8000/api/category/new', data=data, files=files)
        
        if response.status_code == 201:
            return redirect('category',name=category_new)
        elif response.status_code == 400:
            values = {
                'categoryname': category_new,
                'categoryimage': logo_new
            }
            
            data = {
                'values': values,
                'account': customerinfo,
                'error': response.json()
            }
            
            return render(request, 'addcategory.html', data)
    
    def validateCategory(self,edited_category):
        error_message = None
        if (not edited_category.categoryname):
            error_message = "Category name can't be blank!!"
        if edited_category.isExist():
            error_message = "Category already exists!! (matching name)"
        if (not edited_category.categoryimage):
            error_message = "Brand should have a logo!!"
        if edited_category.categoryimage:
            type_logo, decoding = mimetypes.guess_type(str(edited_category.categoryimage))
            if 'image' not in type_logo:
                error_message = "The input file for logo is invalid!!"
        
        return error_message