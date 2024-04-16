from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shop.models.car import Car
from shop.models.account import Account
from django.views import View
import codecs
from django.utils.encoding import force_bytes

class UpdateDeleteCar(View):
    def post(self, request):
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

        brand_new = str(brand_new).upper()
        model_new = str(model_new).upper()
        category_new = str(category_new).upper()
        front_new = force_bytes(front_new)
        back_new = force_bytes(back_new)
        interior_new = force_bytes(interior_new)
        error_message = None
        values = {
            'brand_input': brand_new,
            'model_input': model_new,
            'year_input': year_new,
            'category_input': category_new,
            'desintext_input': desintext_new,
            'instock_input': instock_new,
            'price_input': price_new,
        }
        print(front_new)
        original_car = Car.get_car_info_for_cart(brand_original,model_original,year_original)
        edited_car = Car.set_up_edited_car(brand_new,model_new,year_new,category_new,desintext_new,front_new,back_new,interior_new,instock_new,price_new)
        
        self.setupCar(original_car,edited_car)
        error_message = self.validateCar(edited_car)
        
        if button_action == "update":
            if not error_message:
                Car.update_car(brand_new,model_new,year_new,category_new,desintext_new,front_new,back_new,interior_new,instock_new,price_new,brand_original,model_original,year_original)
                return redirect('edit-car',brand=brand_new,model=model_new,year=year_new)
            else:
                data = {
                    'error': error_message,
                    'values': values
                }
                return redirect('edit-car',brand=brand_new,model=model_new,year=year_new)
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
    
    def validateCar(self,edited_car):
        error_message = None
        if (not edited_car.front):
            error_message = "Invalid file type for car's front view!!"
        if (not edited_car.back):
            error_message = "Invalid file type for car's rear view!!"
        if (not edited_car.interior):
            error_message = "Invalid file type for car's interior view!!"
        
        return error_message
    
    def setupCar(self,original_car,edited_car):
        if edited_car.brand == None:
            edited_car.brand = original_car.brand
        if edited_car.model == None:
            edited_car.model = original_car.model
        if edited_car.year == None:
            edited_car.year = original_car.year
        if edited_car.category == None:
            edited_car.category = original_car.category
        if edited_car.desintext == None:
            edited_car.desintext = original_car.desintext
        if edited_car.instock == None:
            edited_car.instock = original_car.instock
        if edited_car.price == None:
            edited_car.price = original_car.price
        if edited_car.front == None:
            edited_car.front = original_car.front
        if edited_car.back == None:
            edited_car.back = original_car.back
        if edited_car.interior == None:
            edited_car.interior = original_car.interior
            
        return