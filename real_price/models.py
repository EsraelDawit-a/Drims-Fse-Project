from django.db import models
from main.models import *
from management.models import *

class ProductPrice(models.Model):
    user = models.ForeignKey(CustomUser,null=True,on_delete=models.PROTECT,related_name ='price_user')
    product_name = models.CharField(max_length=250)
    catagory = models.ForeignKey(ProductCatagory,on_delete = models.PROTECT)
    description = models.TextField()
    product_image = models.ImageField(upload_to = 'media/images/')
    post_date = models.DateTimeField(auto_now_add =True)
    price = models.FloatField(default =1.0)
    is_accepted = models.BooleanField(default = False)

    class Meta:
        ordering = ('-post_date',)

    def get_absloute_url(self):
        return reverse('product_detail', args=(str(self.pk),))
    
    def __str__(self):
        return self.product_name

class AddProductCatagory(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
