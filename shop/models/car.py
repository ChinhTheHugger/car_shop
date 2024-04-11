from django.db import models
from django.db.models import Q

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
    
    def __str__(self):
        return self.brand + " " + self.model + " " + str(self.year)
    
    class Meta:
        db_table = 'car'