from django.db import models
import datetime
from datetime import date

from models.car import Car
from models.customer import Customer
from models.request import Request

class Contract(models.Model):
    request = models.IntegerField(default=1)
    customer = models.IntegerField(default=1)
    manager = models.IntegerField(default=1)
    car = models.IntegerField(default=1)
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
    def get_contract_by_customer(contract_id):
        return Contract.objects.filter(id=contract_id)
    
    def __str__(self):
        customer = Customer.objects.filter(id=self.customer)
        return customer.firstname + " " + customer.lastname + ", from " + str(self.startdate) + " to " + str(self.enddate)
    
    class Meta:
        db_table = 'contract'