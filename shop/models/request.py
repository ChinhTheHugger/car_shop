from django.db import models
import datetime
from datetime import date

from .car import Car
from .account import Account

from django.db.models import Value, CharField, ImageField, IntegerField

class Request(models.Model): # similar to "cart"
    customer = models.CharField(max_length=50) # use customerusername
    car = models.CharField(max_length=255) # use Car.__str__
    quantity = models.IntegerField(default=1)
    date = models.DateField(default=datetime.datetime.today)
    status = models.CharField(max_length=50, default=False) # "True" for having a contract, "False" for not having any contract
    
    def placeOrder(self):
        self.save()

    @staticmethod
    def get_requests_by_customer(customer_username):
        return Request.objects.filter(customer=customer_username).annotate(mycolumn=Value('xxx', output_field=CharField()))
    
    def __str__(self):
        customer = Account.get_account_by_username(customer)
        return customer.__str__ + ", renting request made on" + str(self.date)
    
    def update_or_create(car_name,customer_username):
        check_request = Request.objects.filter(customer=customer_username,car=car_name,status='False')
        if check_request.exists():
            for req in check_request:
                req.quantity += 1
                req.save()
        else:
            new_request = Request(customer=customer_username,car=car_name,quantity='1',date=date.today(),status='False')
            new_request.placeOrder()
        return
    
    def update_quantity(car_name,customer_username,quantity):
        request = Request.objects.get(customer=customer_username,car=car_name,status='False')
        request.quantity = quantity
        request.save()
        return
        
    def remove_request(car_name,customer_username):
        request = Request.objects.get(customer=customer_username,car=car_name,status='False')
        request.delete()
        return
    
    def cart_display(customer_username):
        cart_items =  Request.objects.filter(customer=customer_username)
        cart_items.annotate(frontimg=Value('', output_field=ImageField(upload_to='uploads/fronts/')))
        cart_items.annotate(carprice=Value('', output_field=IntegerField()))
        cart_items.annotate(totalprice=Value('', output_field=IntegerField()))
        for item in cart_items:
            car_kw = str(item.car).split()
            carinfo = Car.get_car_info_for_cart(car_kw[0],car_kw[1],car_kw[2])
            item.frontimg = carinfo.front
            item.carprice = carinfo.price
            item.totalprice = item.quantity * carinfo.price
            item.save()
        return cart_items
    
    class Meta:
        db_table = 'request'