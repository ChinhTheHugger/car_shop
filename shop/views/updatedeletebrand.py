from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shop.models.brand import Brand
from shop.models.account import Account
from django.views import View
import codecs
from django.utils.encoding import force_bytes
from django.core.files.storage import FileSystemStorage
from upload_validator import FileTypeValidator
from django.core.files.uploadedfile import TemporaryUploadedFile
import mimetypes

class UpdateDeleteBrand(View):
    def post(self, request):
        customerusername = request.session.get('account')
        customerinfo = Account.get_account_by_username_for_iterate(customerusername)
    
        brand_original = request.POST.get('brand-original')
        
        brand_new = request.POST.get('brand')
        website_new = request.POST.get('website')
        desintext_new = request.POST.get('desintext')
        
        logo_new = request.FILES.get('logo', False)
        
        button_action = request.POST.get('action_button')
        
        if brand_new:
            brand_new = str(brand_new).upper()
        else:
            brand_new = brand_original
        
        if logo_new != False:
            save_new_logo =  FileSystemStorage(location='uploads/brands/',base_url='uploads/brands/').save(logo_new.name,logo_new)
            new_logo_url = FileSystemStorage(location='uploads/brands/',base_url='uploads/brands/').url(save_new_logo)
        else:
            new_logo_url = ""
        
        error_message = None
        
        brandinfo = Brand.get_brand_info(brand_original)
        for brand in brandinfo:
            values = {
                'brand': brand.get_brand,
                'website': brand.get_website,
                'desintext': brand.get_desintext,
                'logo': brand.get_logo
            }
        
        edited_brand = Brand.set_up_edited_brand(brand_new,website_new,desintext_new,new_logo_url)
        
        error_message = self.validateBrand(edited_brand,brand_original)
        
        if button_action == "update":
            if not error_message:
                original_brand = Brand.get_brand_by_name(brand_original)
                original_brand.update_brand(brand_new,website_new,desintext_new,new_logo_url)
                return redirect('edit-brand',brand=brand_new)
            else:
                values_new = {
                    'brand': brand_new,
                    'website': website_new,
                    'desintext': desintext_new
                }
                data = {
                    'error': error_message,
                    'values': values,
                    'values_new': values_new,
                    'account': customerinfo
                }
                return render(request,'editbrand.html',data)
        if button_action == "delete":
            Brand.remove_brand(brand_original)
            return redirect('homepage')
    
    def validateBrand(self,edited_brand,brnd): 
        error_message = None
        if edited_brand.isExist() and edited_brand.brandname != brnd:
            error_message = "The brand name already belongs to another brand!!"
        if edited_brand.brandlogo:
            type_logo, decoding = mimetypes.guess_type(str(edited_brand.brandlogo))
            if 'image' not in type_logo:
                error_message = "The input file for logo is invalid!!"
        
        return error_message