from django.db.models import fields
from rest_framework import serializers
from management.models import *
from real_price.models import *

class ProductSeliazers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class WantedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = WantedProducts
        fields = '__all__'

class  TransportSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Transports
        fields = '__all__'

class TransportOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportOrders
        fields = '__all__'

class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = '__all__'