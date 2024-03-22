from django.db import models
import datetime
from datetime import date

from .car import Car
from .customer import Customer

class Request(models.Model):
    customer = models.IntegerField(default=1)
    car = models.IntegerField(default=1)
    quantity = models.IntegerField(default=1)
    purpose = models.CharField(max_length=50)
    date = models.DateField(default=datetime.datetime.today)
    startdate = models.DateField(default=datetime.datetime.today)
    enddate = models.DateField(default=datetime.datetime.today)
    status = models.CharField(max_length=50)
    
    def placeOrder(self):
        self.save()

    @staticmethod
    def get_contracts_by_customer(customer_id):
        return Request.objects.filter(customer=customer_id)
    
    @property
    def car_name(self):
        car = Car.objects.filter(id=self.car)
        return car.__str__
    
    def __str__(self):
        customer = Customer.objects.filter(id=self.customer)
        return customer.__str__ + ", renting request made on" + str(self.date)
    
    class Meta:
        db_table = 'request'