from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('create_product/', views.add_product,name='create_product'),
    path('user_products/',views.user_products,name = 'user_products'),
    path('product_detail/<int:pk>/',views.product_detail,name='product_detail'),
    path('contact/',views.contactus,name='contactus'),
    path('order_product/<int:pk>/',views.order_product,name='order_product'),
    path('update_product/<int:pk>/',views.update_product,name='update_product'),
    path('delete/<int:pk>/',views.delete_product,name='delete'),
    path('add_wanted_product/',views.add_wanted_product,name = 'add_wanted_product'),
    path('wantedproductlist/',views.wantedproductlist,name = 'wantedproductlist'),
    path('wanted_product_detail/<int:pk>/',views.wanted_product_detail,name= 'wanted_product_detail'),
    path('change_status/<int:pk>/',views.change_status,name = 'change_status'),
    path('delete_orders/<int:pk>/',views.delete_orders,name ='delete_orders'),
    path('add_catagory/',views.add_catagory,name = 'add_catagory'),
    path('transport_add/',views.transport_add,name = 'transport_add'),
    path('display_transports/',views.display_transports,name ='display_transports'),
    path('transport_product_detail/<int:pk>/',views.transport_product_detail,name = 'transport_product_detail'),
    path('order_Transport/<int:pk>/',views.order_Transport, name = 'order_Transport'),
    path('change_status_transport/<int:pk>/',views.change_status_transport,name = 'change_status_transport'),
    path('search_transport/',views.search_transport,name = 'search_transport'),
    path('update_transport/<int:pk>/',views.update_transport,name = 'update_transport'),
    path('delete_transports/<int:pk>',views.delete_transports,name = 'delete_transports')
   # path('commentreview/',views.commentreview,name='commentreview')
    # path('product_detail2/<int:pk>/',views.ProductDetail.as_view(), name='product_detail')
]