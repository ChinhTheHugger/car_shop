from django.db import models
import datetime
from datetime import date

from .car import Car
from .account import Account

class Request(models.Model): # similar to "cart"
    customer = models.CharField(max_length=50) # use customerusername
    car = models.CharField(max_length=50) # use Car.__str__
    quantity = models.IntegerField(default=1)
    date = models.DateField(default=datetime.datetime.today)
    status = models.CharField(max_length=50)
    
    def placeOrder(self):
        self.save()

    @staticmethod
    def get_requests_by_customer(customer_username):
        return Request.objects.filter(customer=customer_username)
    
    def __str__(self):
        customer = Account.get_account_by_username(customer)
        return customer.__str__ + ", renting request made on" + str(self.date)
    
    class Meta:
        db_table = 'request'