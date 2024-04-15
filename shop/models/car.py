from django.db import models
from django.db.models import Q
from django.core.validators import FileExtensionValidator
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

class Car(models.Model):
    brand= models.CharField(max_length=50,null=True)
    model= models.CharField(max_length=50,null=True)
    year= models.IntegerField(default=0)
    category= models.CharField(max_length=50,null=True)
    desintext= models.TextField(default='No description')
    front= models.ImageField(upload_to='uploads/fronts/',validators=[FileExtensionValidator(['apng','png','gif','svg','ico','cur','jpg','jpeg','jfif','pjpeg','pjp','webp'])])
    back= models.ImageField(upload_to='uploads/backs/',validators=[FileExtensionValidator(['apng','png','gif','svg','ico','cur','jpg','jpeg','jfif','pjpeg','pjp','webp'])])
    interior= models.ImageField(upload_to='uploads/interiors/',validators=[FileExtensionValidator(['apng','png','gif','svg','ico','cur','jpg','jpeg','jfif','pjpeg','pjp','webp'])])
    instock= models.IntegerField(default=0)
    price= models.IntegerField(default=0)

    @staticmethod
    def get_car_by_id(car_id):
        return Car.objects.get(id=car_id)
    
    @staticmethod
    def get_all_cars():
        return Car.objects.all()
    
    def homepage_three_car():
        return Car.objects.all().order_by('?')[:3]
    
    def homepage_popular_car():
        return Car.objects.all().order_by('?')[:10]
    
    def get_cars_similar_category(category_name):
        return Car.objects.filter(category=category_name).order_by('?')[:10]
    
    def get_cars_similar_brand(brand_name):
        return Car.objects.filter(brand=brand_name).order_by('?')[:10]
    
    def get_car_by_parameters(brand_search,model_search,year_search,category_search,keyword_search):
        result = Car.objects.all()
        if brand_search != 'all':
            result = result.filter(brand=brand_search)
        if model_search != 'all':
            result = result.filter(model=model_search)
        if year_search != 'all':
            result = result.filter(year=year_search)
        if category_search != 'all':
            result = result.filter(category=category_search)
        for keyword in keyword_search:
            result = result.filter(Q(brand__icontains=keyword)|Q(model__icontains=keyword)|Q(year__icontains=keyword)|Q(category__icontains=keyword)|Q(desintext__icontains=keyword))
        return result
    
    def get_car_model_distinct():
        # distinct = Car.objects.values('model').distinct().order_by('model')
        # return Car.objects.filter(model__in=[item['model'] for item in distinct]).order_by('model')
        return Car.objects.values('model').distinct().order_by('model')
    
    def get_car_year_distinct():
        # distinct = Car.objects.values('year').distinct().order_by('year')
        # return Car.objects.filter(year__in=[item['year'] for item in distinct]).order_by('year')
        return Car.objects.values('year').distinct().order_by('year')
    
    def get_car_info(brand_in,model_in,year_in):
        return Car.objects.filter(brand=brand_in,model=model_in,year=year_in)
    
    def get_car_info_for_cart(brand_in,model_in,year_in):
        return Car.objects.get(brand=brand_in,model=model_in,year=year_in)
    
    def set_up_edited_car(brnd,mdl,yr,ctgr,des,frnt,bck,intr,stock,prc):
        return Car(brand=brnd,model=mdl,year=yr,category=ctgr,desintext=des,front=frnt,back=bck,interior=intr,instock=stock,price=prc)
    
    def update_car(brnd,mdl,yr,ctgr,des,frnt,bck,intr,stock,prc,old_brand,old_model,old_year):
        edited_car = Car.get_car_info(old_brand,old_model,old_year)
        for car in edited_car:
            car.brand = brnd
            car.model = mdl
            car.year = yr
            car.category = ctgr
            car.desintext = des
            car.instock = stock
            car.price = prc
            
            car.front.open('wb')
            new_front = open(frnt,'rb')
            car.front.write(new_front.read())
            new_front.close()
            car.front.close()
            
            car.back.open('wb')
            new_back = open(frnt,'rb')
            car.back.write(new_back.read())
            new_back.close()
            car.back.close()
            
            car.interior.open('wb')
            new_interior = open(frnt,'rb')
            car.interior.write(new_interior.read())
            new_interior.close()
            car.interior.close()
            
            car.save()
        
        return
    
    def isExist(self):
        car = Car.objects.filter(brand=self.brand,model=self.model,year=self.year)
        if car:
            return True
        
        return False
    
    def remove_car(brand_in,model_in,year_in):
        car = Car.objects.get(brand=brand_in,model=model_in,year=year_in)
        car.delete()
        return
    
    def get_brand(self):
        return self.brand
    
    def get_model(self):
        return self.model
    
    def get_year(self):
        return self.year
    
    def get_front_img(self):
        return self.front
    
    def get_price(self):
        return self.price
    
    def __str__(self):
        return self.brand + " " + self.model + " " + str(self.year)
    
    class Meta:
        db_table = 'car'