from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shop.models.category import Category
from shop.models.account import Account
from django.views import View
import codecs
from django.utils.encoding import force_bytes
from django.core.files.storage import FileSystemStorage
from upload_validator import FileTypeValidator
from django.core.files.uploadedfile import TemporaryUploadedFile
import mimetypes

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
                'category': category_new,
                'image': logo_new
            }
        
        edited_category = Category.set_up_edited_category(category_new,logo_new)
        
        error_message = self.validateCategory(edited_category)
        
        if error_message:
            data = {
                'values': values,
                'account': customerinfo,
                'error': error_message
            }
            return render(request, 'addcategory.html', data)
        else:
            if logo_new != False:
                save_new_logo =  FileSystemStorage(location='uploads/fronts/',base_url='uploads/fronts/').save(logo_new.name,logo_new)
                new_logo_url = FileSystemStorage(location='uploads/fronts/',base_url='uploads/fronts/').url(save_new_logo)
            else:
                new_logo_url = ""
            
            category_new = str(category_new).upper()
            
            Category.add_new_category(category_new,new_logo_url)
            return redirect('category',name=category_new)
    
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