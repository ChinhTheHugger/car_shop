from django.db import models
import datetime
from datetime import date
import datetime
from django.core.validators import FileExtensionValidator

from shop.models.car import Car
from shop.models.account import Account
from shop.models.request import Request

class Contract(models.Model): # similar to "order"
    request = models.CharField(max_length=50) # use Request custom id
    customer = models.CharField(max_length=50) # use customer username
    manager = models.CharField(max_length=50) # use manager username
    car = models.CharField(max_length=255) # use Car.__str__
    quantity = models.IntegerField(default=1)
    purpose = models.TextField(max_length=50)
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
    cost = models.FloatField(default=0)
    createdate = models.DateField(default=datetime.datetime.today)
    createdate_timestamp = models.CharField(max_length=50,default=str(int(datetime.datetime.now().timestamp()*1000000)))
    
    #to save the data
    def register(self):
        self.save()
        
    @staticmethod
    def get_contract_by_customer(customer_username):
        return Contract.objects.filter(customer=customer_username)
    
    def get_contract_by_parameters(customer,car_str,timestamp):
        return Contract.objects.get(customer=customer,car=car_str,createdate_timestamp=timestamp)
    
    def set_up_contract(request,customer,manager,car,quantity,purpose,startdate,enddate,residence,idcard,driverlicense,carodometerbefore,carsystemstatusbefore,carfrontbefore,carbackbefore,carinteriorbefore,cost,createdate):
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
                        cost=cost,
                        createdate=createdate,
                        createdate_timestamp='temp create date timestamp string')
        
    def add_new_contract(request,customer,manager,car,quantity,purpose,startdate,enddate,residence,idcard,driverlicense,carodometerbefore,carsystemstatusbefore,carfrontbefore,carbackbefore,carinteriorbefore,cost,createdate,createdate_timestamp):
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
        contract.createdate = createdate
        contract.createdate_timestamp = createdate_timestamp
        contract.save()
        
    def update_contract(self,request,customer,manager,car,quantity,purpose,startdate,enddate,residence,idcard,driverlicense,carodometerbefore,carsystemstatusbefore,carfrontbefore,carbackbefore,carinteriorbefore,cost):
        if request != "":
            self.request = request
        if customer != "":
            self.customer = customer
        if manager != "":
            self.manager = manager
        if car != "":
            self.car = car
        if quantity != "":
            self.quantity = quantity
        if purpose != "":
            self.purpose = purpose
        if startdate != "":
            self.startdate = startdate
        if enddate != "":
            self.enddate = enddate
        if residence != "":
            self.residence = residence
        if idcard != "":
            self.idcard = idcard
        if driverlicense != "":
            self.driverlicense = driverlicense
        if carodometerbefore != "":
            self.carodometerbefore = carodometerbefore
        if carsystemstatusbefore != "":
            self.carsystemstatusbefore = carsystemstatusbefore
        if carfrontbefore != "":
            self.carfrontbefore = carfrontbefore
        if carbackbefore != "":
            self.carbackbefore = carbackbefore
        if carinteriorbefore != "":
            self.carinteriorbefore = carinteriorbefore
        if cost != "":
            self.cost = cost
        self.save()
        
        return
    
    def delete_contract(customer,car_str,date):
        contract = Contract.objects.get(customer=customer,car=car_str,createdate=date)
        contract.delete()
        return
    
    def get_active_contract_number(car_name,date):
        return Contract.objects.filter(car=car_name,enddate__gt=date).count()
    
    def get_all_contracts():
        return Contract.objects.all()
    
    def is_past_due(self):
        if date.today() <= self.enddate:
            return True
        
        return False
    
    def has_started(self):
        if date.today() >= self.startdate:
            return True
        
        return False
    
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
    
    def get_request(self):
        return self.request
    
    def get_customer(self):
        return self.customer
    
    def get_manager(self):
        return self.manager
    
    def get_car(self):
        return self.car
    
    def get_quantity(self):
        return self.quantity
    
    def get_purpose(self):
        return self.purpose
    
    def get_startdate(self):
        return self.startdate
    
    def get_enddate(self):
        return self.enddate
    
    def get_odometer(self):
        return self.carodometerbefore
    
    def get_systemstatus(self):
        return self.carsystemstatusbefore
    
    def get_cost(self):
        return self.cost
    
    def get_residence(self):
        return self.residence
    
    def get_id(self):
        return self.idcard
    
    def get_driverlicense(self):
        return self.driverlicense
    
    def get_front(self):
        return self.carfrontbefore
    
    def get_back(self):
        return self.carbackbefore
    
    def get_interior(self):
        return self. carinteriorbefore
    
    def info_string(self):
        return self.customer + "_" + str(self.car).replace(" ","_") + "_" + str(self.createdate_timestamp)
    
    def __str__(self):
        customer = Account.get_account_by_username(customer)
        return customer.__str__ + ", from " + str(self.startdate) + " to " + str(self.enddate)
    
    class Meta:
        db_table = 'contract'
        constraints = [
            models.UniqueConstraint(fields=['request'], name='unique_request')
        ]