from django.contrib import admin
from shop.models import Category
from shop.models import Product


# Register your models here.
admin.site.register(Category)
admin.site.register(Product)