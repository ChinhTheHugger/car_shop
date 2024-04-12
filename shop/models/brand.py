from django.db import models
from django.core.validators import FileExtensionValidator

class Brand(models.Model):
    brandname= models.CharField(max_length=50)
    website= models.CharField(max_length=50)
    desintext= models.CharField(max_length=250, default='', blank=True, null= True)
    brandlogo= models.ImageField(upload_to='uploads/brands/',validators=[FileExtensionValidator(['apng','png','gif','svg','ico','cur','jpg','jpeg','jfif','pjpeg','pjp','webp'])])

    @staticmethod
    def get_all_brands():
        return Brand.objects.all().order_by('brandname')
    
    def homepage_popular_brand():
        return Brand.objects.all().order_by('?')[:10]
    
    def get_brand_by_name(name):
        return Brand.objects.get(brandname=name)

    def __str__(self):
        return self.brandname
    
    class Meta:
        db_table = 'brand'