from rest_framework.relations import PrimaryKeyRelatedField

from .models import (
    Drink,
    Category,
    Order,
    OrderItem,
    Review,
    Promotion,
    Favorite,
    Ingredient,
)
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


class OrderItemserializers(serializers.ModelSerializer):
    drink = Drinkserializers(read_only=True)
    drink_id = serializers.IntegerField(write_only=True)
    quantity = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = [
            'drink',
            'drink_id',
            'quantity',
        ]


class Orderserializers(serializers.ModelSerializer):
    items = OrderItemserializers(many=True, read_only=True)
    items_data = OrderItemserializers(write_only=True, many=True)

    class Meta:
        model = Order
        fields = [
            'created_at',
            'items_data',
            'details',
            'items',
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


class Promotionserializers(serializers.ModelSerializer):
    drinks = Drinkserializers(read_only=True, many=True)
    drinks_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Drink.objects.all()
    )

    class Meta:
        model = Promotion
        fields = [
            'id',
            'drinks',
            'drinks_ids',
            'title',
            'discount_percent',
            'active_until',
        ]


class Favoriteserializer(serializers.ModelSerializer):
    drink = Drinkserializers(read_only=True)
    drink_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Favorite
        fields = [
            'drink',
            'drink_id',
            'added_at',
        ]


class Ingredientserializer(serializers.ModelSerializer):
    drinks = Drinkserializers(read_only=True, many=True)
    drinks_ids = serializers.PrimaryKeyRelatedField(
        write_only=True,
        many=True,
        queryset=Drink.objects.all()
    )

    class Meta:
        model = Ingredient
        fields = [
            'drinks',
            'drinks_ids',
            'is_allergen',
            'name',
            'extra_price',
        ]