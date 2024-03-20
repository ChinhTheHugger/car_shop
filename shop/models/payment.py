from django.db import models
import datetime
from datetime import date

from models.contract import Contract
from models.customer import Customer

class Payment(models.Model):
    contract = models.IntegerField(default=1)
    customer = models.IntegerField(default=1)
    manager = models.IntegerField(default=1)
    basecost = models.IntegerField(default=0)
    additionalcost = models.IntegerField(default=0)
    totalcost = models.IntegerField(default=0)
    paymentamount = models.IntegerField(default=0)
    change = models.IntegerField(default=0)
    paymentmethod = models.IntegerField(default=1)
    # for online transaction
    bank = models.IntegerField(default=1)
    account = models.IntegerField(default=1)
    
    @staticmethod
    def get_payments_by_customer(customer_id):
        return Payment.objects.filter(customer=customer_id)
    
    @staticmethod
    def get_payments_by_manager(manager_id):
        return Payment.objects.filter(manager=manager_id)
    
    @staticmethod
    def get_payments_by_contract(contract_id):
        return Payment.objects.filter(contract=contract_id)
    
    def __str__(self):
        customer = Customer.objects.filter(id=self.customer)
        return customer.firstname + " " + customer.lastname + ", payment for contract ID " + self.contract
    
    class Meta:
        db_table = 'payment'