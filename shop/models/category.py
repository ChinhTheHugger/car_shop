from django.db import models
from django.core.validators import FileExtensionValidator

class Category(models.Model):
    categoryname= models.CharField(max_length=50)
    categoryimage= models.ImageField(upload_to='uploads/categories/',validators=[FileExtensionValidator(['apng','png','gif','svg','ico','cur','jpg','jpeg','jfif','pjpeg','pjp','webp'])])

    @staticmethod
    def get_all_categories():
        return Category.objects.all().order_by('categoryname')
    
    def homepage_popular_category():
        return Category.objects.all().order_by('?')[:10]
    
    def get_category_info(name):
        return Category.objects.filter(categoryname=name)
    
    def get_category_by_name(name):
        return Category.objects.get(categoryname=name)
    
    def set_up_edited_category(ctgr,img):
        return Category(categoryname=ctgr,categoryimage=img)
    
    def update_category(ctgr,img,ctgr_ori):
        category = Category.objects.get(categoryname=ctgr_ori)
        category.categoryname = ctgr
        category.categoryimage = img
        category.save()
        
        return
    
    def add_new_category(ctgr,img):
        category = Category()
        category.categoryname = ctgr
        category.categoryimage = img
        category.save()
        
        return
    
    def remove_category(ctgr):
        category = Category.objects.get(categoryname=ctgr)
        category.delete()
        
        return
    
    def isExist(self):
        ctgr = Category.objects.filter(categoryname=self.categoryname)
        if ctgr:
            return True
        
        return False
    
    def get_name(self):
        return self.categoryname
    
    def get_image(self):
        return self.categoryimage

    def __str__(self):
        return self.categoryname
    
    class Meta:
        db_table = 'category'
        constraints = [
            models.UniqueConstraint(fields=['categoryname'], name='unique_category')
        ]