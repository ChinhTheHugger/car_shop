from django.db import models

class Car(models.Model):
    brand= models.CharField(max_length=50,null=True)
    model= models.CharField(max_length=50,null=True)
    year= models.IntegerField(default=0)
    category= models.CharField(max_length=50,null=True)
    desintext= models.CharField(max_length=250, default='', blank=True, null= True)
    front= models.ImageField(upload_to='uploads/fronts/')
    back= models.ImageField(upload_to='uploads/backs/')
    interior= models.ImageField(upload_to='uploads/interiors/')
    instock= models.IntegerField(default=0)
    price= models.IntegerField(default=0)

    @staticmethod
    def get_car_by_id(car_id):
        return Car.objects.filter(id=car_id)
    
    @staticmethod
    def get_all_cars():
        return Car.objects.all()
    
    def homepage_three_car():
        return Car.objects.all().order_by('?')[:3]
    
    def homepage_popular_car():
        return Car.objects.all().order_by('?')[:10]
    
    def __str__(self):
        return self.brand + " " + self.model + " " + str(self.year)
    
    class Meta:
        db_table = 'car'