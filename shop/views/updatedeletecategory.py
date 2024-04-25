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

class UpdateDeleteCategory(View):
    def post(self, request):
        customerusername = request.session.get('account')
        customerinfo = Account.get_account_by_username_for_iterate(customerusername)
    
        category_original = request.POST.get('category-original')
        
        category_new = request.POST.get('category')
        
        logo_new = request.FILES.get('image', False)
        
        button_action = request.POST.get('action_button')
        
        if category_new:
            category_new = str(category_new).upper()
        else:
            category_new = category_original
        
        if logo_new != False:
            save_new_logo =  FileSystemStorage(location='uploads/categories/',base_url='uploads/categories/').save(logo_new.name,logo_new)
            new_logo_url = FileSystemStorage(location='uploads/categories/',base_url='uploads/categories/').url(save_new_logo)
        else:
            new_logo_url = ""
        
        error_message = None
        
        categoryinfo = Category.get_category_info(category_original)
        for category in categoryinfo:
            values = {
                'category': category.get_name,
                'image': category.get_image
            }
        
        edited_category = Category.set_up_edited_category(category_new,new_logo_url)
        
        error_message = self.validateCategory(edited_category,category_original)
        
        if button_action == "update":
            if not error_message:
                original_category = Category.get_category_by_name(category_original)
                original_category.update_category(category_new,new_logo_url,category_original)
                return redirect('edit-category',category=category_new)
            else:
                values_new = {
                    'category': category_new,
                    'image': logo_new
                }
                data = {
                    'error': error_message,
                    'values': values,
                    'values_new': values_new,
                    'account': customerinfo
                }
                return render(request,'editcategory.html',data)
        if button_action == "delete":
            Category.remove_category(category_original)
            return redirect('homepage')
    
    def validateCategory(self,edited_category,ctgr): 
        error_message = None
        if edited_category.isExist() and edited_category.categoryname != ctgr:
            error_message = "The category name already belongs to another category!!"
        if edited_category.categoryimage:
            type_logo, decoding = mimetypes.guess_type(str(edited_category.categoryimage))
            if 'image' not in type_logo:
                error_message = "The input file for logo is invalid!!"
        
        return error_message