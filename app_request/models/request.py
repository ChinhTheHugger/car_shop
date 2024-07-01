from django.db import models
import datetime
from datetime import date
import time

from app_car.models.car import Car
from app_account.models.account import Account

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
    
    def get_all_requests(self):
        return Request.objects.all()
    
    def __str__(self):
        customer = Account.get_account_by_username(self.customer)
        return customer.__str__() + ", renting request for " + self.car + ", made on " + str(self.date)
    
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
    
    def update_customer_username(old_username,new_username):
        requests_to_update = Request.objects.filter(customer=old_username)
        for i in range(requests_to_update.count()):
            requests_to_update[i].customer=new_username
        Request.objects.bulk_update(requests_to_update,["customer"])
        return
    
    def update_car_name(old_name,new_name):
        requests_to_update = Request.objects.filter(car=old_name)
        for i in range(requests_to_update.count()):
            requests_to_update[i].car=new_name
        Request.objects.bulk_update(requests_to_update,["car"])
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
    
    def search_requests_by_keywords(keywords): # car search for manager
        customerlist = Account.get_account_by_keywords(keywords)
        list = []
        for cus in customerlist:
            list.append(cus.get_username())
        cart_items =  Request.objects.filter(customer__in=list).order_by('date')
        cart_items.annotate(frontimg=Value('', output_field=ImageField(upload_to='uploads/fronts/')))
        cart_items.annotate(carprice=Value('', output_field=IntegerField()))
        cart_items.annotate(totalprice=Value('', output_field=IntegerField()))
        cart_items.annotate(customername=Value('', output_field=CharField()))
        for item in cart_items:
            car_kw = str(item.car).split()
            carinfo = Car.get_car_info_for_cart(car_kw[0],car_kw[1],car_kw[2])
            item.frontimg = carinfo.get_front_img()
            item.carprice = carinfo.get_price()
            item.totalprice = item.quantity * carinfo.price
            customerinfo = Account.get_account_by_username(item.customer)
            item.customername = customerinfo.__str__()
            item.save()
        return cart_items
    
    def get_all_requests_for_cart_display(): # cart display for manager
        cart_items =  Request.objects.filter(status=False).order_by('date')
        cart_items.annotate(frontimg=Value('', output_field=ImageField(upload_to='uploads/fronts/')))
        cart_items.annotate(carprice=Value('', output_field=IntegerField()))
        cart_items.annotate(totalprice=Value('', output_field=IntegerField()))
        cart_items.annotate(customername=Value('', output_field=CharField()))
        cart_items.annotate(carbrand=Value('', output_field=CharField()))
        cart_items.annotate(carmodel=Value('', output_field=CharField()))
        cart_items.annotate(caryear=Value('', output_field=CharField()))
        cart_items.annotate(unixtimestamp=Value('', output_field=IntegerField()))
        for item in cart_items:
            car_kw = str(item.car).split()
            carinfo = Car.get_car_info_for_cart(car_kw[0],car_kw[1],car_kw[2])
            item.carbrand = carinfo.get_brand()
            item.carmodel = carinfo.get_model()
            item.caryear = carinfo.get_year()
            item.frontimg = carinfo.get_front_img()
            item.carprice = carinfo.get_price()
            item.totalprice = item.quantity * carinfo.get_price()
            customerinfo = Account.get_account_by_username(item.customer)
            item.customername = customerinfo.__str__()
            item.unixtimestamp = int(time.mktime(item.date.timetuple()))
            item.save()
        return cart_items
    
    def cart_display(customer_username): # car display for customer
        cart_items =  Request.objects.filter(customer=customer_username,status=False)
        cart_items.annotate(frontimg=Value('', output_field=ImageField(upload_to='uploads/fronts/')))
        cart_items.annotate(carprice=Value('', output_field=IntegerField()))
        cart_items.annotate(totalprice=Value('', output_field=IntegerField()))
        cart_items.annotate(carbrand=Value('', output_field=CharField()))
        cart_items.annotate(carmodel=Value('', output_field=CharField()))
        cart_items.annotate(caryear=Value('', output_field=CharField()))
        for item in cart_items:
            car_kw = str(item.car).split()
            carinfo = Car.get_car_info_for_cart(car_kw[0],car_kw[1],car_kw[2])
            item.carbrand = carinfo.get_brand()
            item.carmodel = carinfo.get_model()
            item.caryear = carinfo.get_year()
            item.frontimg = carinfo.get_front_img()
            item.carprice = carinfo.get_price()
            item.totalprice = item.quantity * carinfo.get_price()
            item.save()
        return cart_items
    
    def total_cart_manager(): # cart display for manager
        cart_items =  Request.objects.all().order_by('date')
        cart_items.annotate(frontimg=Value('', output_field=ImageField(upload_to='uploads/fronts/')))
        cart_items.annotate(carprice=Value('', output_field=IntegerField()))
        cart_items.annotate(totalprice=Value('', output_field=IntegerField()))
        cart_items.annotate(customername=Value('', output_field=CharField()))
        cart_items.annotate(carbrand=Value('', output_field=CharField()))
        cart_items.annotate(carmodel=Value('', output_field=CharField()))
        cart_items.annotate(caryear=Value('', output_field=CharField()))
        cart_items.annotate(unixtimestamp=Value('', output_field=IntegerField()))
        for item in cart_items:
            car_kw = str(item.car).split()
            carinfo = Car.get_car_info_for_cart(car_kw[0],car_kw[1],car_kw[2])
            item.carbrand = carinfo.get_brand()
            item.carmodel = carinfo.get_model()
            item.caryear = carinfo.get_year()
            item.frontimg = carinfo.get_front_img()
            item.carprice = carinfo.get_price()
            item.totalprice = item.quantity * carinfo.get_price()
            customerinfo = Account.get_account_by_username(item.customer)
            item.customername = customerinfo.__str__()
            item.unixtimestamp = int(time.mktime(item.date.timetuple()))
            item.save()
        return cart_items
    
    def total_cart_customer(customer_username): # car display for customer
        cart_items =  Request.objects.filter(customer=customer_username)
        cart_items.annotate(frontimg=Value('', output_field=ImageField(upload_to='uploads/fronts/')))
        cart_items.annotate(carprice=Value('', output_field=IntegerField()))
        cart_items.annotate(totalprice=Value('', output_field=IntegerField()))
        for item in cart_items:
            car_kw = str(item.car).split()
            carinfo = Car.get_car_info_for_cart(car_kw[0],car_kw[1],car_kw[2])
            item.frontimg = carinfo.get_front_img()
            item.carprice = carinfo.get_price()
            item.totalprice = item.quantity * carinfo.get_price()
            item.save()
        return cart_items
    
    def request_custom_id(self):
        car_kw = str(self.car).split()
        carinfo = Car.get_car_info_for_cart(car_kw[0],car_kw[1],car_kw[2])
        return self.customer + "_" + carinfo.get_brand() + "_" + carinfo.get_model() + "_" + str(carinfo.get_year()) + "_" + str(self.date)
    
    def get_request(customer_in,brand_in,model_in,year_in,date):
        car_str = brand_in + " " + model_in + " " + str(year_in)
        return Request.objects.get(customer=customer_in,car=car_str,date=date,status=False)
    
    def get_quantity(self):
        return self.quantity
    
    def get_date(self):
        return self.date
    
    def current_status(self):
        if self.status == False:
            return False
        
        return True
    
    class Meta:
        db_table = 'request'
        constraints = [
            models.UniqueConstraint(fields=['customer','car','date'], name='unique_customer_car_date')
        ]