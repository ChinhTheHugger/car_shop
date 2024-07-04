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
    
    def set_up_edited_brand(brnd,wb,des,logo):
        return Brand(brandname=brnd,website=wb,desintext=des,brandlogo=logo)
    
    def update_brand(self,brnd,wb,des,logo):
        if brnd != "":
            self.brandname = brnd
        if wb != "":
            self.website = wb
        if des != "":
            self.desintext = des
        if logo != "":
            self.brandlogo = logo
        self.save()
        
        return
    
    def add_new_brand(brnd,wb,des,logo):
        brand = Brand()
        brand.brandname = brnd
        brand.website = wb
        brand.desintext = des
        brand.brandlogo = logo
        brand.save()
        
        return
    
    def remove_brand(brnd):
        brand = Brand.get_brand_by_name(brnd)
        brand.delete()
        return
    
    def isExist(self):
        brand = Brand.objects.filter(brandname=self.brandname)
        if brand:
            return True
        
        return False
    
    def get_brand_by_name(name):
        return Brand.objects.get(brandname=name)
    
    def get_brand_info(name):
        return Brand.objects.filter(brandname=name)
    
    def get_brand(self):
        return self.brandname
    
    def get_website(self):
        return self.website
    
    def get_desintext(self):
        return self.desintext
    
    def get_logo(self):
        return self.brandlogo

    def __str__(self):
        return self.brandname
    
    class Meta:
        db_table = 'brand'
        constraints = [
            models.UniqueConstraint(fields=['brandname'], name='unique_brand')
        ]