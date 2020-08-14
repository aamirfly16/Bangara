from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.videocategory import videocategory
from .models.home import Home
from embed_video.admin import AdminVideoMixin
from .models.video import Item

class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'image', 'description']

class AdminCategory(admin.ModelAdmin):
     list_display = ['name']

class AdminHome(admin.ModelAdmin):
    list_display = ['name', 'description', 'category']

class AdminItem(admin.ModelAdmin):
    list_display = ['video', 'Name']

class AdminVideocategory(admin.ModelAdmin):
     list_display = ['name']

    # Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(videocategory, AdminVideocategory)
admin.site.register(Home, AdminHome)
admin.site.register(Item, AdminItem)
