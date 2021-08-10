from rest_framework import serializers

from .models import Product

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fileds = ['user']
        #TODO: add product and quantity