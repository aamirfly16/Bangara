from django.db import models
from .category import Category

# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=500, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/home/')

    @staticmethod
    def get_all_homes_by_categoryid(category_id):
        if category_id:
            return Home.objects.filter(category = category_id)
        else:
            return Home.get_all_homes();

    @staticmethod
    def get_all_homes():
        return Home.objects.all()