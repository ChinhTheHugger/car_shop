from django.db import models

class Category(models.Model):
    categoryname= models.CharField(max_length=50)
    categoryimage= models.ImageField(upload_to='uploads/categories/')

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def homepage_popular_category():
        return Category.objects.all().order_by('?')[:10]

    def __str__(self):
        return self.categoryname
    
    class Meta:
        db_table = 'category'