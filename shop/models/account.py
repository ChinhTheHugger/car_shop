from django.db import models

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
    
    def get_account_by_username(acc_username):
        try:
            return Account.objects.get(username=acc_username)
        except:
            return False


    def isExistEmail(self):
        if Account.objects.get(email = self.email):
            return True

        return False
    
    def isExistUsername(self):
        if Account.objects.get(username = self.username):
            return True

        return False
    
    def check_pwd(acc_username):
        result = Account.objects.get(username = acc_username)
        return result
    
    def __str__(self):
        return self.firstname +" "+ self.lastname +" ("+ self.type +")"
    
    class Meta:
        db_table = 'account'