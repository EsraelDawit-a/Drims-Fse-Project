from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.real_price,name = 'real_price'),
    path('add_product_price/',views.add_product_price,name = 'add_product_price'),
    path('add_catagory_price/',views.add_catagory_price,name = 'add_catagory_price'),
    path('search_product_price/',views.search_product_price,name = 'search_product_price'),
    # path('send_email/',views.send_email,name = 'send_email'),
    # path('request_email/',views.request_email,name = 'request_email'),
]