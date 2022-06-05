from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description', 'price', 'group', 'available')


admin.site.register(Product, ProductAdmin)