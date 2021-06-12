from django.contrib import admin
from .models import *

class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ['user','product_name','catagory','post_date','price','is_accepted']

class ProductCatagoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(AddProductCatagory,ProductCatagoryAdmin)
admin.site.register(ProductPrice,ProductPriceAdmin)
