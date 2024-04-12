from django.db import models
from django.db.models import Q

class Account(models.Model):
    username = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=50, default='customer')

    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_account_by_email(email):
        try:
            return Account.objects.get(email= email)
        except:
            return False
    
    @staticmethod
    def get_account_by_id(acc_id):
        return Account.objects.get(id=acc_id)
    
    def get_username(self):
        return self.username
    
    def get_account_by_username(acc_username):
        try:
            return Account.objects.get(username=acc_username)
        except:
            return False
        
    def get_account_by_username_for_iterate(acc_username):
         return Account.objects.filter(username=acc_username)

    def get_account_by_keywords(keywords):
        result = Account.objects.all()
        for keyword in keywords:
            result.filter(Q(username__icontains=keyword)|Q(firstname__icontains=keyword)|Q(lastname__icontains=keyword)|Q(email__icontains=keyword))
        return result

    def isExistEmail(self):
        acc_list = Account.objects.filter(email = self.email)
        if acc_list.count() != 0:
            return True
        else:
            return False
    
    def isExistUsername(self):
        acc_list = Account.objects.filter(username = self.username)
        if acc_list.count() != 0:
            return True
        else:
            return False
    
    def check_pwd(acc_username):
        result = Account.objects.get(username = acc_username)
        return result
    
    def check_account_type(self):
        if self.type == "customer":
            return True
        
        return False
    
    def __str__(self):
        return self.firstname +" "+ self.lastname +" ("+ self.type +")"
    
    class Meta:
        db_table = 'account'