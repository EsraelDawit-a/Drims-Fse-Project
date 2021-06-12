from django.db import models
from main.models import CustomUser
from django.urls import reverse

# Create your models here.
sell_type = (
    ('per single','persingle'),
    ('per pack','perpack')
)


class Products(models.Model):
    user = models.ForeignKey(CustomUser,null=True,on_delete=models.PROTECT,related_name ='product_user')
    product_name = models.CharField(max_length=250)
    catagory = models.ForeignKey('ProductCatagory',on_delete = models.PROTECT)
    description = models.TextField()
    product_image = models.ImageField(upload_to = 'media/images/')
    post_date = models.DateTimeField(auto_now_add =True)
    amount = models.CharField(max_length=100,choices = sell_type)
    specific_adress = models.CharField(max_length=250,null=True,blank=True)
    price = models.FloatField(default =1.0)

    class Meta:
        ordering = ('-post_date',)

    def get_absloute_url(self):
        return reverse('product_detail', args=(str(self.pk),))
    
    def __str__(self):
        return self.product_name

need = (
    ('single','single'),
    ('many','many'),
    ('unknown','unknown')
)
class WantedProducts(models.Model):
    user = models.ForeignKey(CustomUser,null=True,on_delete=models.PROTECT,related_name ='wanted_product_user')
    product_name = models.CharField(max_length=250)
    #catagory = models.ForeignKey('ProductCatagory',on_delete = models.PROTECT)
    description = models.TextField()
    product_image = models.ImageField(upload_to = 'media/images/')
    post_date = models.DateTimeField(auto_now_add =True)
    amount_need = models.CharField(max_length=100,choices = need)
    specific_adress = models.CharField(max_length=250,null=True,blank=True)
    price_range = models.CharField(max_length=100)
    found = models.BooleanField(default = False)

    class Meta:
        ordering = ('-post_date',)

    def get_absloute_url(self):
        return reverse('wanted_product_detail', args=(str(self.pk),))
    
    def __str__(self):
        return self.product_name


class ProductCatagory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CommentReview(models.Model):
    commetned_by = models.ForeignKey(CustomUser,on_delete=models.PROTECT,related_name ='commenter',null=True)
    comment = models.TextField()
    product_id = models.IntegerField()
    commented_date = models.DateTimeField(auto_now_add =True)


    class Meta:
        ordering = ('-commented_date',)

    def __str__(self):
        return self.comment

class Message(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.PROTECT,related_name ='messenger',null=True)
    full_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return (f'Message Sent From {self.user.username}')

class ProductOrders(models.Model):
     ordered_item = models.ForeignKey(Products,on_delete = models.PROTECT,related_name = 'ordered_product')
     ordered_by = models.ForeignKey(CustomUser,null=True,on_delete=models.PROTECT,related_name ='product_ordered_by')
     prouct_owner = models.ForeignKey(CustomUser,null= True,on_delete = models.PROTECT,related_name = 'product_owner')
     order_date = models.DateTimeField(auto_now_add = True)
     order_destination = models.CharField(max_length = 250,null=True,blank =True)
    #  message = models.TextField(null=True,blank = True)
     order_source_adress = models.CharField(max_length = 250,null=True,blank=True)
     orderer_optional_adress = models.CharField(max_length = 250,null=True,blank=True)
     accecpted = models.BooleanField(default = False)
     
     class Meta:
         ordering = ('-order_date',)

     def __str__(self):
         return self.ordered_item.product_name
    
class Transports(models.Model):
    user = models.ForeignKey(CustomUser,null=True,on_delete=models.PROTECT,related_name ='transport_user')
    transport_name = models.CharField(max_length=250)
    description = models.TextField()
    transport_image = models.ImageField(upload_to = 'media/images/')
    post_date = models.DateTimeField(auto_now_add =True)
    specific_adress = models.CharField(max_length=250,null=True,blank=True)
    price = models.FloatField(default =1.0)

    class Meta:
        ordering = ('-post_date',)

    def get_absloute_url(self):
        return reverse('transport_product_detail', args=(str(self.pk),))
    
    def __str__(self):
        return self.transport_name



class TransportOrders(models.Model):
     transport = models.ForeignKey(Transports,null=True,on_delete = models.PROTECT,related_name = 'transport')
     ordered_by = models.ForeignKey(CustomUser,null=True,on_delete=models.PROTECT,related_name ='transport_ordered_by')
     transport_owner = models.ForeignKey(CustomUser,null= True,on_delete = models.PROTECT,related_name = 'transport_owner')
     order_date = models.DateTimeField(auto_now_add = True)
     message = models.TextField(null=True,blank = True)
     order_source_adress = models.CharField(max_length = 250,null=True,blank=True)
     orderer_optional_adress = models.CharField(max_length = 250,null=True,blank=True)
     status = models.BooleanField(default = False)
     
     class Meta:
         ordering = ('-order_date',)

     def __str__(self):
         return self.transport_owner.username
    



    





