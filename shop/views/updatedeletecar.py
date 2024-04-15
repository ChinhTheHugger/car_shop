from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from shop.models.car import Car
from shop.models.account import Account
from django.views import View

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
        
        front_new = request.FILE('front')
        back_new = request.FILE('front')
        interior_new = request.FILE('front')

        brand_new = str(brand_new).upper()
        model_new = str(model_new).upper()
        category_new = str(category_new).upper()
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
        edited_car = Car.set_up_edited_car(brand_new,model_new,year_new,category_new,desintext_new,front_new,back_new,interior_new,instock_new,price_new)
        
        error_message = self.validateCar(edited_car)
        
        if not error_message:
            Car.update_car(brand_new,model_new,year_new,category_new,desintext_new,front_new,back_new,interior_new,instock_new,price_new,brand_original,model_original,year_original)
            return redirect('edit-car-parameters',brnd=brand_new,mdl=model_new,yr=year_new)
        else:
            data = {
                'error': error_message,
                'values': values
            }
            return render(request,'editcar.html',data)
            
    
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
        if edited_car.isExist():
            error_message = "Car already exists!! (matching brand, model and manufacture year)"
        if (not edited_car.front):
            error_message = "Invalid file type for car's front view!!"
        if (not edited_car.back):
            error_message = "Invalid file type for car's rear view!!"
        if (not edited_car.interior):
            error_message = "Invalid file type for car's interior view!!"
        
        return error_message