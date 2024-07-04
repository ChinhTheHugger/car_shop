from django.contrib import admin

from shop.models.car import Car
from shop.models.brand import Brand
from shop.models.category import Category
from shop.models.account import Account
from shop.models.request import Request
from shop.models.contract import Contract

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
