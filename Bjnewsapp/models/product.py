from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='uploads/products/')
    description = models.CharField(max_length=500, default='1', null=True, blank=True)

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()