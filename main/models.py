from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse



role = (
     ('Producer','Producer'),
     ('Buyer','Buyer'),
     ('Transport-Provider','Transport-Provider'),
     ('empty','empty'),
     ('Price_teller','Price_teller')
)
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=100)
    registerddate = models.DateTimeField(auto_now_add = True)
    is_banned = models.BooleanField(default=False)
    Email_Adress = models.CharField(max_length=1000)
    role = models.CharField(choices = role,max_length=100,default='empty',null=True,blank=True)
    phone_vertified = models.BooleanField(default=False)
    email_vertified = models.BooleanField(default=False)
    is_premium_account = models.BooleanField(default=False)
    Adress =models.CharField(max_length=200,null=True,blank =True)
    optional_adress = models.CharField(max_length=200)



    


    

class Profile(models.Model):
     user = models.OneToOneField(CustomUser,null=True,on_delete=models.CASCADE,related_name ='profile')
     # product = models.CharField(max_length =100)
     pic = models.ImageField(upload_to = 'images', default='media/images/app4.jpg', blank =True,null = True)
     bio = models.TextField(null=True,blank=True)
     licencecopy = models.FileField(upload_to='media/documents',null=True,blank=True)
     idimg = models.ImageField(upload_to = 'media/docimages',blank =True,null = True)
     #role = models.CharField(max_length=100,choices=choices)

     def __str__(self):
          return self.user.username
     
         
     





