from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as A
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username','phone','Adress','optional_adress','first_name','last_name','Email_Adress','role' ]
    # add_form = A.add_form
    # add_form_template = A.add_form_template
    # add_fieldsets = A.add_fieldsets
class ProfileAdmin(admin.ModelAdmin):
   list_display =  ['user','pic','bio']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile,ProfileAdmin)
# admin.site.register(Buyer, UA)
# admin.site.register(Seller, UA)
# admin.site.register(Transporter)
# admin.site.register(BranchAdminRegistration)