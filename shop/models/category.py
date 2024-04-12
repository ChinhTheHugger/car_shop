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

    def __str__(self):
        return self.categoryname
    
    class Meta:
        db_table = 'category'