from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView


urlpatterns = [
    path('',views.homepage,name = 'indexpage'),
    path('update_profile/', views.update_profile,name='update_profile'),
    path('start/loginuser/',views.login_view,name='loginuser'),
    path('logoutuser/',views.logoutuser,name='logoutuser'),
    path('start/registercustomer/',views.registercustomer,name = 'registercustomer'),
    path('update/', views.CustomUserView.as_view(), name='update_customer'),
    path('profile_detail/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('start/homepage/',views.homepage,name='homepage'),
    path('start/productlist',views.productlist,name = 'productlist'),
    path('vertifyaccount/',views.vertifyaccount,name = 'vertifyaccount'),
    path('resetoptions/',views.resetoptions,name = 'resetoptions'),

    path('password_reset/',PasswordResetView.as_view(template_name = 'reset_password.html'),name='password_reset'),
    path('password_reset/done',PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'),name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/' ,PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html'),name = 'password_reset_confirm'),

    path('password_reset_complete/',PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'),name='password_reset_complete'),
    path('search_item/',views.search_item,name = 'search_item'),
    path('about_us/',views.about_us,name = 'about_us')
    
    # path('registerSeller/',views.registerSeller,name='regiseter_seller'),
    # path('registerTransporter/',views.registerTransporter,name='register_transplorter'),
    # path('workers_registration/',views.BranchAdmin,name='workers_registration')
  
 
]
