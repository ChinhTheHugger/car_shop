from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shop.models.car import Car
from shop.models.account import Account
from django.views import View
import codecs
from django.utils.encoding import force_bytes
from django.core.files.storage import FileSystemStorage
from upload_validator import FileTypeValidator

class UpdateDeleteCar(View):
    def post(self, request):
        customerusername = request.session.get('account')
        customerinfo = Account.get_account_by_username_for_iterate(customerusername)
    
        brand_original = request.POST.get('brand-original')
        model_original = request.POST.get('model-original')
        year_original = request.POST.get('year-original')
        
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
        
        button_action = request.POST.get('action_button')

        original_car = Car.get_car_info_for_cart(brand_original,model_original,year_original)
        
        if brand_new:
            brand_new = str(brand_new).upper()
        else:
            brand_new = brand_original
            
        if model_new:
            model_new = str(model_new).upper()
        else:
            model_new = model_original
            
        if year_new:
            category_new = str(category_new).upper()
        else:
            year_new = year_original
        
        if front_new != False:
            save_new_front =  FileSystemStorage(location='uploads/fronts/').save(front_new.name,front_new)
            new_front_url = FileSystemStorage(location='uploads/fronts/').url(save_new_front)
        else:
            new_front_url = "no new image uploaded"
        
        if back_new != False:
            save_new_back =  FileSystemStorage(location='uploads/backs/').save(back_new.name,back_new)
            new_back_url = FileSystemStorage(location='uploads/backs/').url(save_new_back)
        else:
            new_back_url = "no new image uploaded"
        
        if interior_new != False:
            save_new_interior =  FileSystemStorage(location='uploads/interiors/').save(interior_new.name,interior_new)
            new_interior_url = FileSystemStorage(location='uploads/interiors/').url(save_new_interior)
        else:
            new_interior_url = "no new image uploaded"
        
        error_message = None
        
        carinfo = Car.get_car_info(brand_original,model_original,year_original)
        for car in carinfo:
            values = {
                'brand': car.get_brand,
                'model': car.get_model,
                'year': car.get_year,
                'category': car.get_category,
                'desintext': car.get_desintext,
                'instock': car.get_stock,
                'price': car.get_price,
                'front': car.get_front_img,
                'back': car.get_back_img,
                'interior': car.get_interior_img
            }
        
        
        original_car = Car.get_car_info_for_cart(brand_original,model_original,year_original)
        edited_car = Car.set_up_edited_car(brand_new,model_new,year_new,category_new,desintext_new,new_front_url,new_back_url,new_interior_url,instock_new,price_new)
        
        error_message = self.validateCar(edited_car,brand_original,model_original,year_original)
        
        if button_action == "update":
            if not error_message:
                Car.update_car(brand_new,model_new,year_new,category_new,desintext_new,front_new,back_new,interior_new,instock_new,price_new,brand_original,model_original,year_original)
                return redirect('edit-car',brand=brand_new,model=model_new,year=year_new)
            else:
                values_new = {
                    'brand': brand_new,
                    'model':model_new,
                    'year': year_new,
                    'category': category_new,
                    'desintext': desintext_new,
                    'instock': instock_new,
                    'price': price_new
                }
                data = {
                    'error': error_message,
                    'values': values,
                    'values_new': values_new,
                    'account': customerinfo
                }
                return render(request,'editcar.html',data)
        if button_action == "delete":
            Car.remove_car(brand_original,model_original,year_original)
            return redirect('homepage')
            
    
    # def validateCar(self,edited_car):
    #     error_message = None
    #     if (not edited_car.brand):
    #         error_message = "Brand name can't be blank!!"
    #     if (not edited_car.model):
    #         error_message = "Model name can't be blank!!"
    #     if (not edited_car.year):
    #         error_message = "Manufacture year can't be blank!!"
    #     if edited_car.isExist():
    #         error_message = "Car already exists!! (matching brand, model and manufacture year)"
    #     if (not edited_car.category):
    #         error_message = "Category can't be blank!!"
    #     if (not edited_car.desintext):
    #         error_message = "Car should have a description!!"
    #     if (not edited_car.instock):
    #         error_message = "Number of cars in stock can't be blank!!"
    #     if (not edited_car.price):
    #         error_message = "Car renting price can't be blank!!"
    #     if (not edited_car.front):
    #         error_message = "Invalid file type for car's front view!!"
    #     if (not edited_car.back):
    #         error_message = "Invalid file type for car's rear view!!"
    #     if (not edited_car.interior):
    #         error_message = "Invalid file type for car's interior view!!"
        
    #     return error_message
    
    def validateCar(self,edited_car,brnd,mdl,yr):
        validator = FileTypeValidator(allowed_types=['images/*'])
        error_message = None
        if edited_car.isExist() and edited_car.brand != brnd and edited_car.model != mdl and edited_car.year != yr:
            error_message = "The brand, model, year combination already belongs to another car!!"
        
        return error_message