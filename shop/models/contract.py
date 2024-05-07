from django.db import models
import datetime
from datetime import date
from django.core.validators import FileExtensionValidator

from .car import Car
from .account import Account
from .request import Request

class Contract(models.Model): # similar to "order"
    request = models.CharField(max_length=50) # use Request custom id
    customer = models.CharField(max_length=50) # use customer username
    manager = models.CharField(max_length=50) # use manager username
    car = models.CharField(max_length=255) # use Car.__str__
    quantity = models.IntegerField(default=1)
    purpose = models.CharField(max_length=50)
    startdate = models.DateField(default=datetime.datetime.today)
    enddate = models.DateField(default=datetime.datetime.today)
    residence = models.ImageField(upload_to='uploads/contracts/residences/',validators=[FileExtensionValidator(['apng','png','gif','svg','ico','cur','jpg','jpeg','jfif','pjpeg','pjp','webp'])])
    idcard = models.ImageField(upload_to='uploads/contracts/idcards/',validators=[FileExtensionValidator(['apng','png','gif','svg','ico','cur','jpg','jpeg','jfif','pjpeg','pjp','webp'])])
    driverlicense = models.ImageField(upload_to='uploads/contracts/driverlicences/',validators=[FileExtensionValidator(['apng','png','gif','svg','ico','cur','jpg','jpeg','jfif','pjpeg','pjp','webp'])])
    carodometerbefore = models.IntegerField(default=1)
    carsystemstatusbefore = models.TextField(default='Functional')
    carfrontbefore = models.ImageField(upload_to='uploads/contracts/frontstatusbefore/',validators=[FileExtensionValidator(['apng','png','gif','svg','ico','cur','jpg','jpeg','jfif','pjpeg','pjp','webp'])])
    carbackbefore = models.ImageField(upload_to='uploads/contracts/backstatusbefore/',validators=[FileExtensionValidator(['apng','png','gif','svg','ico','cur','jpg','jpeg','jfif','pjpeg','pjp','webp'])])
    carinteriorbefore = models.ImageField(upload_to='uploads/contracts/interiorstatusbefore/',validators=[FileExtensionValidator(['apng','png','gif','svg','ico','cur','jpg','jpeg','jfif','pjpeg','pjp','webp'])])
    cost = models.IntegerField(default=0)
    
    #to save the data
    def register(self):
        self.save()
        
    @staticmethod
    def get_contract_by_customer(customer_username):
        return Contract.objects.filter(customer=customer_username)
    
    def get_contract_by_parameters(customer,car_str)
    
    def set_up_contract(request,customer,manager,car,quantity,purpose,startdate,enddate,residence,idcard,driverlicense,carodometerbefore,carsystemstatusbefore,carfrontbefore,carbackbefore,carinteriorbefore,cost):
        return Contract(request=request,
                        customer=customer,
                        manager=manager,
                        car=car,
                        quantity=quantity,
                        purpose=purpose,
                        startdate=startdate,
                        enddate=enddate,
                        residence=residence,
                        idcard=idcard,
                        driverlicense=driverlicense,
                        carodometerbefore=carodometerbefore,
                        carsystemstatusbefore=carsystemstatusbefore,
                        carfrontbefore=carfrontbefore,
                        carbackbefore=carbackbefore,
                        carinteriorbefore=carinteriorbefore,
                        cost=cost)
        
    def add_new_contract(request,customer,manager,car,quantity,purpose,startdate,enddate,residence,idcard,driverlicense,carodometerbefore,carsystemstatusbefore,carfrontbefore,carbackbefore,carinteriorbefore,cost):
        contract = Contract()
        contract.request = request
        contract.customer = customer
        contract.manager = manager
        contract.car = car
        contract.quantity = quantity
        contract.purpose = purpose
        contract.startdate = startdate
        contract.enddate = enddate
        contract.residence = residence
        contract.idcard = idcard
        contract.driverlicense = driverlicense
        contract.carodometerbefore = carodometerbefore
        contract.carsystemstatusbefore = carsystemstatusbefore
        contract.carfrontbefore = carfrontbefore
        contract.carbackbefore = carbackbefore
        contract.carinteriorbefore = carinteriorbefore
        contract.cost = cost
        contract.save()
    
    def get_active_contract_number(car_name,date):
        return Contract.objects.filter(car=car_name,enddate__gt=date).count()
    
    def is_past_due(self):
        return date.today() <= self.enddate
    
    def customer_update(old_username,new_username):
        contracts_to_update = Contract.objects.filter(customer=old_username)
        for contract in contracts_to_update:
            contract.customer = new_username
        Contract.objects.bulk_update(contracts_to_update,["customer"])
        return
    
    def manager_update(old_username,new_username):
        contracts_to_update = Contract.objects.filter(manager=old_username)
        for contract in contracts_to_update:
            contract.customer = new_username
        Contract.objects.bulk_update(contracts_to_update,["manager"])
        return
    
    def car_update(old_name,new_name):
        contracts_to_update = Contract.objects.filter(car=old_name)
        for contract in contracts_to_update:
            contract.car = new_name
        Contract.objects.bulk_update(contracts_to_update,["car"])
        return
    
    def __str__(self):
        customer = Account.get_account_by_username(customer)
        return customer.__str__ + ", from " + str(self.startdate) + " to " + str(self.enddate)
    
    class Meta:
        db_table = 'contract'