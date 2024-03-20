from django.db import models

class Brand(models.Model):
    brandname= models.CharField(max_length=50)
    website= models.CharField(max_length=50)
    desintext= models.CharField(max_length=250, default='', blank=True, null= True)
    brandlogo= models.ImageField(upload_to='uploads/brands/')

    @staticmethod
    def get_all_brands():
        return Brand.objects.all()
    
    def homepage_popular_brand():
        return Brand.objects.all().order_by('?')[:10]

    def __str__(self):
        return self.brandname
    
    class Meta:
        db_table = 'brand'