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
                'brand': brand_new,
                'website': website_new,
                'desintext': desintext_new,
                'logo': logo_new
            }
        
        edited_brand = Brand.set_up_edited_brand(brand_new,website_new,desintext_new,logo_new)
        
        error_message = self.validateBrand(edited_brand)
        
        if error_message:
            data = {
                'values': values,
                'account': customerinfo,
                'error': error_message
            }
            return render(request, 'addbrand.html', data)
        else:
            if logo_new != False:
                save_new_logo =  FileSystemStorage(location='uploads/fronts/',base_url='uploads/fronts/').save(logo_new.name,logo_new)
                new_logo_url = FileSystemStorage(location='uploads/fronts/',base_url='uploads/fronts/').url(save_new_logo)
            else:
                new_logo_url = ""
            
            brand_new = str(brand_new).upper()
            
            Brand.add_new_brand(brand_new,website_new,desintext_new,new_logo_url)
            return redirect('get-brand',brand=brand_new)
    
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