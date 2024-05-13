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
        
        edited_car = Car.set_up_edited_car(brand_new,model_new,year_new,category_new,desintext_new,front_new,back_new,interior_new,instock_new,price_new)
        
        error_message = self.validateCar(edited_car)
        
        if error_message:
            data = {
                'values': values,
                'account': customerinfo,
                'error': error_message
            }
            return render(request, 'addcar.html', data)
        else:
            if front_new != False:
                save_new_front =  FileSystemStorage(location='uploads/fronts/',base_url='uploads/fronts/').save(front_new.name,front_new)
                new_front_url = FileSystemStorage(location='uploads/fronts/',base_url='uploads/fronts/').url(save_new_front)
            
            if back_new != False:
                save_new_back =  FileSystemStorage(location='uploads/backs/',base_url='uploads/backs/').save(back_new.name,back_new)
                new_back_url = FileSystemStorage(location='uploads/backs/',base_url='uploads/backs/').url(save_new_back)
            
            if interior_new != False:
                save_new_interior =  FileSystemStorage(location='uploads/interiors/',base_url='uploads/interiors/').save(interior_new.name,interior_new)
                new_interior_url = FileSystemStorage(location='uploads/interiors/',base_url='uploads/interiors/').url(save_new_interior)
            
            brand_new = str(brand_new).upper()
            model_new = str(model_new).upper()
            year_new = str(year_new).upper()
            category_new = str(category_new).upper()
            
            Car.add_new_car(brand_new,model_new,year_new,category_new,desintext_new,new_front_url,new_back_url,new_interior_url,instock_new,price_new)
            return redirect('get-car',brand=brand_new,model=model_new,year=year_new)
    
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