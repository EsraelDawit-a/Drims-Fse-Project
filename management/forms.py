from .models import *
from django.forms import ModelForm


class AddProducts(ModelForm):
    class Meta:
        model = Products
        fields = ['user','product_name','description','product_image','amount','specific_adress','catagory','price']
    

class AddCatagory(ModelForm):
    class Meta:
        model = ProductCatagory
        fields = '__all__'

class AddWantedProducts(ModelForm):
    class Meta:
        model = WantedProducts
        fields = ['user','product_name','description','product_image','amount_need','specific_adress','price_range']

class CommentRev(ModelForm):
    class Meta:
        model = CommentReview
        fields = ['commetned_by','comment','product_id']

class MessageSend(ModelForm):
    class Meta:
        model = Message
        fields = ['user','full_name','subject','message','email']

class OrderUserProduct(ModelForm):
    class Meta:
        model = ProductOrders
        fields = ['ordered_item','ordered_by','prouct_owner','order_destination','order_source_adress','orderer_optional_adress']

class TransportOrdersAdd(ModelForm):
    class Meta:
        model = TransportOrders
        fields = ['ordered_by','transport_owner','message','orderer_optional_adress']

class AddTransports(ModelForm):
    class Meta:
        model = Transports
        fields = ('user','transport_name','description','transport_image','specific_adress','price')