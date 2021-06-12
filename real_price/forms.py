from .models import *
from management.models import ProductCatagory
from django.forms import ModelForm
from django.forms import *
class AddProductPrice(ModelForm):
    class Meta:
        model = ProductPrice
        fields = ['user','product_name','description','product_image','catagory','price']


class AddCatagorypr(ModelForm):
    class Meta:
        model = AddProductCatagory
        fields = '__all__'


class VertifyUserEmail(forms.Form):
    for_m = CharField(max_length = 8)

class getUserEmail(forms.Form):
    for_m = CharField(max_length = 100)