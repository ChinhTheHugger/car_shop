from django.db import models
import datetime
from datetime import date

from .car import Car
from .account import Account
from .request import Request

class Contract(models.Model):
    request = models.IntegerField(default=1)
    customer = models.CharField(max_length=50) # use customer username
    manager = models.CharField(max_length=50) # use manager username
    car = models.CharField(max_length=50) # use Car.__str__
    quantity = models.IntegerField(default=1)
    purpose = models.CharField(max_length=50)
    startdate = models.DateField(default=datetime.datetime.today)
    enddate = models.DateField(default=datetime.datetime.today)
    residence = models.ImageField(upload_to='uploads/contracts/residences/')
    idcard = models.ImageField(upload_to='uploads/contracts/idcards/')
    driverlicense = models.ImageField(upload_to='uploads/contracts/driverlicences/')
    carodometerbefore = models.IntegerField(default=1)
    carsystemstatusbefore = models.TextField(default='Functional')
    carfrontbefore = models.ImageField(upload_to='uploads/contracts/frontstatusbefore/')
    carbackbefore = models.ImageField(upload_to='uploads/contracts/backstatusbefore/')
    carinteriorbefore = models.ImageField(upload_to='uploads/contracts/interiorstatusbefore/')
    cost = models.IntegerField(default=0)
    
    #to save the data
    def register(self):
        self.save()
        
    @staticmethod
    def get_contract_by_customer(customer_username):
        return Contract.objects.filter(customer=customer_username)
    
    def __str__(self):
        customer = Account.get_account_by_username(customer)
        return customer.__str__ + ", from " + str(self.startdate) + " to " + str(self.enddate)
    
    class Meta:
        db_table = 'contract'