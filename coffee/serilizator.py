from .models import Drink, Category, Order
from rest_framework import serializers


class Categoryserializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name'
        ]


class Drinkserializers(serializers.ModelSerializer):
    category = Categoryserializers(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Drink
        fields = [
            'id',
            'name',
            'price',
            'category',
            'category_id'
        ]



class Orderserializers(serializers.ModelSerializer):
    drink = Drinkserializers(read_only=True)
    drink_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Order
        fields = [
            'id',
            'date',
            'drink',
            'drink_id'
        ]
