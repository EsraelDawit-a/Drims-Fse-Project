from django.contrib import admin
from .models import *

class ProductsAdmin(admin.ModelAdmin):
        list_display = ('user','product_name','description','product_image','amount','specific_adress','price')
# Register your models here.

class WantedProductsAdmin(admin.ModelAdmin):
        list_display =['product_name','description','product_image','amount_need','specific_adress','price_range']

class CommentReviewAdmin(admin.ModelAdmin):
        list_display = ('commetned_by','comment','product_id')

class  MessageAdmin(admin.ModelAdmin):
        list_display = ('user','full_name','email','subject')


class ProductOrdersAdmin(admin.ModelAdmin):
        list_display = ('ordered_by','ordered_item','prouct_owner','order_date','order_destination','order_source_adress','orderer_optional_adress')

class TransportOrdersAdmin(admin.ModelAdmin):
        list_display = ('ordered_by','transport_owner','order_date','order_source_adress','orderer_optional_adress')

class TransportAdmin(admin.ModelAdmin):
        list_display = ('user','transport_name','post_date','specific_adress','price')

admin.site.register(Products,ProductsAdmin)
admin.site.register(ProductCatagory)
admin.site.register(CommentReview,CommentReviewAdmin)
admin.site.register(Message,MessageAdmin)
admin.site.register(ProductOrders,ProductOrdersAdmin)
admin.site.register(TransportOrders,TransportOrdersAdmin)
admin.site.register(WantedProducts,WantedProductsAdmin)
admin.site.register(Transports,TransportAdmin)