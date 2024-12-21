from django.contrib import admin
from .models import Product
# signup your models here

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','category','price','image','stock')
    prepopulated_fields = {"slug": ('product_name',)}

admin.site.register(Product,ProductAdmin)
