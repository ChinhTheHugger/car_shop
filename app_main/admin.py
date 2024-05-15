from django.contrib import admin

from app_car.models.car import Car
from app_brand.models.brand import Brand
from app_category.models.category import Category
from app_account.models.account import Account
from app_request.models.request import Request
from app_contract.models.contract import Contract

# Register your models here.

class AdminCar(admin.ModelAdmin):
    list_display = ['__str__']
    
class AdminBrand(admin.ModelAdmin):
    list_display = ['__str__']

class AdminCategory(admin.ModelAdmin):
    list_display = ['__str__']

class AdminAccount(admin.ModelAdmin):
    list_display = ['__str__']

class AdminManager(admin.ModelAdmin):
    list_display = ['__str__']
    
class AdminRequest(admin.ModelAdmin):
    list_display = ['__str__']

class AdminContract(admin.ModelAdmin):
    list_display = ['__str__']

class AdminPayment(admin.ModelAdmin):
    list_display = ['__str__']
    
admin.site.register(Car,AdminCar)
admin.site.register(Brand,AdminBrand)
admin.site.register(Category,AdminCategory)
admin.site.register(Account,AdminAccount)
admin.site.register(Request,AdminRequest)
admin.site.register(Contract,AdminContract)
