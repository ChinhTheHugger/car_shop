from django.db import models
import datetime
from datetime import date

from .contract import Contract
from .account import Account

class Payment(models.Model):
    contract = models.CharField(max_length=50) # use Contract.__str__
    customer = models.CharField(max_length=50) # use customer username
    manager = models.CharField(max_length=50) # use manager username
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
    def get_payments_by_customer(customer_username):
        return Payment.objects.filter(customer=customer_username)
    
    @staticmethod
    def get_payments_by_manager(manager_username):
        return Payment.objects.filter(manager=manager_username)
    
    @staticmethod
    def get_payments_by_contract(contract_str):
        return Payment.objects.filter(contract=contract_str)
    
    def __str__(self):
        customer = Account.get_account_by_username(customer)
        return customer.__str__ + ", payment for contract: " + self.contract
    
    class Meta:
        db_table = 'payment'