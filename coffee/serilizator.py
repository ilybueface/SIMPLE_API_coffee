from .models import Drink, Category, Order, Review
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


class Reviewserializers(serializers.ModelSerializer):
    drink = Drinkserializers(read_only=True)
    drink_id = serializers.IntegerField(write_only=True)
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = [
            'id',
            'drink',
            'drink_id',
            'author',
            'text',
            'rating',
            'created_at'
        ]
