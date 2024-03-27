from django.db import models

class Customer(models.Model):
    customerusername = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)

    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.filter(email= email)
        except:
            return False
    
    @staticmethod
    def get_customer_by_id(customer_id):
        return Customer.objects.filter(id=customer_id)
    
    def get_customer_by_username(customer_username):
        return Customer.objects.filter(customerusername=customer_username)


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False
    
    def __str__(self):
        return self.firstname +" "+ self.lastname
    
    class Meta:
        db_table = 'customer'